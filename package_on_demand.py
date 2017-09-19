
import pkgutil
import importlib
import sys
import copy
import imp
import inspect
import site
import os
import pprint

site_package_paths = map(os.path.realpath, site.getsitepackages())

def main():
    before_module = set([str(i) for i in sys.modules])
    relative_path = sys.argv[1] if len(sys.argv) > 1 else 'tests/test.py'
    name = relative_path[:-3].replace("/", ".")

    mod = importlib.import_module(name)

    extra = set()
    for i, j in sys.modules.iteritems():
        if i not in before_module and j is not None:
            extra.add(j)
    to_export = []
    for i in extra:
        if hasattr(i, '__file__') and any(map(lambda r: i.__file__.startswith(r), site_package_paths)):
            to_export.append(i.__file__)
    pprint.pprint(sorted(filter(lambda r: '__init__.py' in r, to_export)))

if __name__ == "__main__":
    main()
