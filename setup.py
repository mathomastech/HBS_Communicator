from cx_Freeze import setup, Executable
import os, site, sys

## Get the site-package folder, not everybody will install
## Python into C:\PythonXX
site_dir = site.getsitepackages()[1]
include_dll_path = os.path.join(site_dir, "gtk")

## Collect the list of missing dll when cx_freeze builds the app
missing_dll = ['libatk-1.0-0.dll',
                'libcairo-2.dll',
                'libcairo-gobject-2.dll',
                'libcairo-script-interpreter-2.dll',
                'libcroco-0.6-3.dll',
                'libffi-6.dll',
                'libfontconfig-1.dll',
                'libfreetype-6.dll',
                'libgailutil-3-0.dll',
                'libgcrypt-11.dll',
                'libgdk-3-0.dll',
                'libgio-2.0-0.dll',
                'libglib-2.0-0.dll',
                'libgmodule-2.0-0.dll',
                'libgnutls-26.dll',
                'libgobject-2.0-0.dll',
                'libgthread-2.0-0.dll',
                'libgtk-3-0.dll',
                'libiconv-2.dll',
                'libintl-8.dll',
                'libjasper-1.dll',
                'libjpeg-9.dll',
                'liblzma-5.dll',
                'libp11-kit-0.dll',
                'libpango-1.0-0.dll',
                'libpangocairo-1.0-0.dll',
                'libpangoft2-1.0-0.dll',
                'libpangowin32-1.0-0.dll',
                'libpixman-1-0.dll',
                'libpng15-15.dll',
                'librsvg-2-2.dll',
                'libtiff-5.dll',
                'libxml2-2.dll',
                'pthreadGC2.dll',
                'zlib1.dll']

## We also need to add the glade folder, cx_freeze will walk
## into it and copy all the necessary files
glade_folder = 'glade'

## We need to add all the libraries too (for themes, etc..)
gtk_libs = ['etc', 'lib', 'share']

## Create the list of includes as cx_freeze likes
include_files = []
for dll in missing_dll:
    include_files.append((os.path.join(include_dll_path, dll), dll))

## Let's add glade folder and files
include_files.append((glade_folder, glade_folder))

## Let's add gtk libraries folders and files
for lib in gtk_libs:
    include_files.append((os.path.join(include_dll_path, lib), lib))

base = None

## Lets not open the console while running the app
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable("main.py",
               base=base
    )
]

buildOptions = dict(
    compressed = False,
    includes = ["gi"],
    packages = ["gi"],
    include_files = include_files
    )

setup(
    name = "Communicator",
    author = "Marc Thomas",
    version = "1.0",
    description = "HBS Communicator App",
    options = dict(build_exe = buildOptions),
    executables = executables
)
