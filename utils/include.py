import fnmatch
import importlib
import inspect
import os
import re


class T:
    pass


def include(cls, dir="./", ignore=[], isObject=False, all_path=True):
    ##################################################
    #        Recursive all files under dir           #
    ##################################################
    files = []
    if dir[-1] != "/":
        dir += "/"
    if dir[0:2] == "./":
        dir = dir[2:]
    for root, dirnames, filenames in os.walk(dir):
        for filename in fnmatch.filter(filenames, '*.py'):
            if filename in ignore:
                continue
            files.append(os.path.join(root, filename))
    for file in files:
        ##################################################
        #       trans normal path to import path       ###
        #       ex: abc/def.py => abc.def              ###
        ##################################################
        packagepath = file[:-3]
        packagepath = packagepath.replace("/", ".")
        classbuildpath = packagepath[len(dir):]
        now = cls
        if all_path:
            for attr in classbuildpath.split("."):
                if not hasattr(now, attr):
                    setattr(now, attr, T())
                now = getattr(now, attr)
        else:
            for attr in classbuildpath.split(".")[:-1]:
                if not hasattr(now, attr):
                    setattr(now, attr, T())
                now = getattr(now, attr)
        package = importlib.import_module(packagepath)
        classes = inspect.getmembers(package, inspect.isclass)
        reg_exp = "^.*" + packagepath + "\..*$"
        for classname, classpath in classes:
            if re.match(reg_exp, str(classpath)):
                if isObject:
                    setattr(now, classname, getattr(package, classname)())
                else:
                    setattr(now, classname, getattr(package, classname))
                if all_path:
                    setattr(getattr(now, classname), 'path',
                            packagepath.split(".") + [classname])
                else:
                    setattr(getattr(now, classname), 'path',
                            packagepath.split(".")[:-1] + [classname])
