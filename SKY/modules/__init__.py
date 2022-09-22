"""
Copyright (c) 2022 Yash-Sharma-1807

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
   """

import glob
import importlib
import sys
from os.path import basename, dirname, isfile

LOAD = []
MOD_LOAD = []
MOD_NOLOAD = []

def __list_all_modules():
    # This generates a list of modules in this
    # folder for the * in __main__ to work.
    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    all_modules = [
        basename(f)[:-3]
        for f in mod_paths
        if isfile(f)
           and f.endswith(".py")
           and not f.endswith("__init__.py")
           and not f.endswith("__main__.py")
    ]

    if MOD_LOAD or MOD_NOLOAD:
        to_load = MOD_LOAD
        if to_load:
            if not all(
                    any(mod == module_name for module_name in all_modules)
                    for mod in to_load
            ):
                sys.exit()

        else:
            to_load = all_modules

        if MOD_NOLOAD:
            return [item for item in to_load if item not in MOD_NOLOAD]

        return to_load

    return all_modules


print("[INFO]: IMPORTING MODULES")
importlib.import_module("SKY.modules.__main__")
x = sorted(__list_all_modules())
__all__ = x + ["ALL_MODULES"]