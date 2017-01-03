from sanic import Blueprint
import pkgutil
import inspect

class Blueprints(object):
    pass

for loader, name, is_pkg in pkgutil.walk_packages(__path__):
    module = loader.find_module(name).load_module(name)
    if hasattr(module, 'bp') and isinstance(module.bp, Blueprint):
        setattr(Blueprints, name, module.bp)
