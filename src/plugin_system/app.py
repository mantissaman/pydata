#from plugins import one, two
# import sys
# print(sys.path)
# sys.path.append("./plugins")
import importlib

PLUGIN_NAME ="plugins.two"


plugin_module = importlib.import_module(PLUGIN_NAME, '.')
print(plugin_module)
# print(two)

# one.Plugin("hello one", key =1)
# two.Plugin("hello two", key=2)

plugin_module.Plugin("hello one", key =1)