import sys

from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
        name = "Marc Thomas",
        version = "0.10.0",
        description = "Clan HBS Communicator App",
        options = {"build_exe" : {"includes" : "atexit" }},
        executables = [Executable("communicator.py", base = base)]
)

