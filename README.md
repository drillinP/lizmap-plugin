[![logo](icon.png "3Liz")][3liz]Lizmap 2.4.3
==============================================

**WARNING** the master branch is compatible only with QGIS 3.x from August 23rd 2018. The branch *qgis2* targets QGIS 2.x compatibiliy.

Publication plugin for Lizmap Web Application, by 3LIZ.

    begin       : 2011-11-01
    copyright   : (C) 2011 by 3liz
    authors     : René-Luc D'Hont and Michaël Douchin
    email       : info@3liz.com
    website     : http://www.3liz.com

Lizmap Qgis plugin aims to be used to configure a web application dynamically generated by Lizmap (php/html/css/js) with the help of Qgis Server ( [QGIS Server Tutorial] ) With this plugin, you can configure one web map per Qgis project. The Lizmap web application must be installed on the server.

The Original Code is 3liz code.

Authors
-------

The Initial Developer of the Original Code are René-Luc D'Hont <rldhont@3liz.com> and Michael Douchin <mdouchin@3liz.com>. Portions created by the Initial Developer are Copyright (C) 2011 the Initial Developer. All Rights Reserved.

Contributors
--------------

* Salvatore Larosa  @slarosa
* Paolo Cavallini @pcav
* Arnaud Deleurme
* @ewsterrenburg
* Sławomir Bienias @SaekBinko
* Petr Tsymbarovich @mentaljam
* Víctor Herreros @vherreros
* João Gaspar
* Felix Kuehne
* Kari Salovaara
* Xan Vieiro
* Etienne Trimaille @Gustry

*Please propose a PR to add yourself if you are missing*

Installation
-----------

from github repository:

1. Clone the repo: `git clone git@github.com:3liz/lizmap-plugin.git`
2. `cp lizmap-plugin ~/.qgis2/python/plugins`
3. `cd ~/.qgis2/python/plugins`
4. `mv lizmap-plugin lizmap`

or from QGIS application:

1. Plugins menu -> Manage and Install Plugins...
2. Select LizMap plugin from Not installed list
3. Install plugin

Documentation
--------------

[French doc]: http://docs.3liz.com/
[English doc translated via Google Translate]: http://translate.google.fr/translate?sl=fr&tl=en&js=n&prev=_t&hl=fr&ie=UTF-8&eotf=1&u=http%3A%2F%2Fdocs.3liz.Com

Translation
-----------

You can use the Makefile to update and compile the strings for translation.

```
# Update strings
make transup

# Compile
make transcompile

```

License
-------
Version: MPL 2.0/GPL 2.0/LGPL 2.1

The contents of this file are subject to the Mozilla Public License Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.mozilla.org/MPL/

Alternatively, the contents of this file may be used under the terms of either of the GNU General Public License Version 2 or later (the "GPL"), or the GNU Lesser General Public License Version 2.1 or later (the "LGPL"), in which case the provisions of the GPL or the LGPL are applicable instead of those above. If you wish to allow use of your version of this file only under the terms of either the GPL or the LGPL, and not to allow others to use your version of this file under the terms of the MPL, indicate your decision by deleting the provisions above and replace them with the notice and other provisions required by the GPL or the LGPL. If you do not delete the provisions above, a recipient may use your version of this file under the terms of any one of the MPL, the GPL or the LGPL.

Software distributed under the License is distributed on an "AS IS" basis, WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License for the specific language governing rights and limitations under the License.


  [QGIS Server Tutorial]: http://www.qgis.org/wiki/QGIS_Server_Tutorial
  [3liz]:http://www.3liz.com
