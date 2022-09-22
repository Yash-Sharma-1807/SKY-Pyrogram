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

from os.path import dirname , isfile
import glob

def all_mod():
    x = dirname(__file__)
    y = glob.glob(x + "/*.py")
    
    all_mods = [
        (((f.replace(x, "")).replace("\\", "."))[:-3])
        for f in y
        if isfile(f)
        and f.endswith(".py")
        and not f.endswith("__init__.py")]
    return all_mods

z = sorted(all_mod())

__all__ = z + ["ALL_MODULES"]
