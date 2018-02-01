from distutils.core import setup, Extension


module1 = Extension('polaris',
                    sources = [
'ndicapi.cxx',
'ndicapi_math.cxx',
'ndicapi_serial.cxx',
'ndicapi_thread.cxx',
'polarismodule.c',
])

setup (name = 'polaris',
       version = '3.2',
       description = 'This is a demo package',
       ext_modules = [module1])
