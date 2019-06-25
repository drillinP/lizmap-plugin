
import glob
import subprocess
from pytransifex.api import Transifex
from qgispluginbooster.parameters import Parameters
from qgispluginbooster.exceptions import TranslationFailed, TransifexNoResource, TransifexManyResources
from qgispluginbooster.utils import touch_file


class Translation():
    def __init__(self, parameters: Parameters, create_project: bool = True):
        """
        Parameters
        ----------
        parameters:

        create_project:
            if True, it will create the project, resource and language on Transifex

        """
        self.parameters = parameters
        self._t = Transifex(parameters.transifex_token, parameters.transifex_organization, i18n_type='QT')
        assert self._t.ping()
        self.ts_file = '{dir}/i18n/{res}_{lan}.ts'.format(dir=self.parameters.src_dir,
                                                          res=self.parameters.project_slug,
                                                          lan=self.parameters.translation_source_language)

        if self._t.project_exists(parameters.project_slug):
            print('Project {o}/{p} exists on Transifex'.format(o=self.parameters.transifex_organization,
                                                               p=self.parameters.project_slug))
        elif create_project:
            print('project does not exists on Transifex, creating one as {o}/{p}'.format(o=self.parameters.transifex_organization,
                                                                                         p=self.parameters.project_slug))
            self._t.new_project(slug=parameters.project_slug,
                                repository_url=self.parameters.repository_url,
                                source_language_code=parameters.translation_source_language)
            self.update_strings()
            print('creating resource in {o}/{p} with {f}'.format(o=self.parameters.transifex_organization,
                                                                 p=self.parameters.project_slug,
                                                                 f=self.ts_file))
            self._t.new_resource(project_slug=self.parameters.project_slug,
                                 path_to_file=self.ts_file,
                                 resource_slug=self.parameters.project_slug)
            print('OK')
        else:
            raise TranslationFailed('Project {o}/{p} does notexists on Transifex'.format(
                o=self.parameters.transifex_organization, p=self.parameters.project_slug))

    def update_strings(self):
        cmd = ['pylupdate5', '-noobsolete']
        for ext in ('py', 'ui'):
            for file in glob.glob('{dir}/**/*.{ext}'.format(dir=self.parameters.src_dir, ext=ext), recursive=True):
                cmd.append(file)
        touch_file(self.ts_file)
        cmd.append('-ts')
        cmd.append(self.ts_file)
        output = subprocess.run(cmd, capture_output=True, text=True)
        if output.returncode != 0:
            raise TranslationFailed(output.stderr)
        else:
            print('Successfuly run pylupdate5: {}'.format(output.stdout))

    def compile_string(self):
        pass


    def pull(self):
        resource = self.__get_resource()
        existing_langs = self._t.list_languages(project_slug=self.parameters.project_slug, resource_slug=resource['slug'])
        existing_langs.remove(self.parameters.translation_source_language)
        print('{c} languages found for resource ''{s}'' ({langs})'.format(s=resource['slug'], c=len(existing_langs), langs=existing_langs))
        for lang in self.parameters.translation_languages:
            if lang not in existing_langs:
                print('creating missing language: {}'.format(lang))
                self._t.new_language(self.parameters.project_slug, lang, [self.parameters.transifex_coordinator])
                existing_langs.append(lang)
        for lang in existing_langs:
            ts_file = '{dir}/i18n/{res}_{lan}.ts'.format(dir=self.parameters.src_dir,
                                                         res=self.parameters.project_slug,
                                                         lan=lang)
            print('downloading translation file: {}'.format(ts_file))
            self._t.get_translation(self.parameters.project_slug, resource['slug'], lang, ts_file)

    def push(self):
        pass

    def __get_resource(self) -> dict:
        resources = self._t.list_resources(self.parameters.project_slug)
        if len(resources) == 0:
            raise TransifexNoResource("project '{}' has no resource on Transifex".format(self.parameters.project_slug))
        if len(resources) > 1:
            raise TransifexManyResources("project '{p}' has several resources on Transifex. Will use first one ({r})"
                                         .format(p=self.parameters.project_slug,
                                                 r=resources[0]['slug']))
        return resources[0]