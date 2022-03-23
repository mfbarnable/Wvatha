import os
import sys
import subprocess
import platform

TOOLS_DIR = "{}\\tools".format(os.getcwd())
PLATFORM_TOOL = ""

def GenerateProject():
    platform = sys.platform.lower()
    if "win32" == platform or "windows" == platform:
        PLATFORM_TOOL="gensln"
    elif platform.startswith("linux"):
        PLATFORM_TOOL="genlinux"
    elif "darwin" == platform:
        PLATFORM_TOOL="genmac"
    else:
        print("Error unknown platform")
        exit(-1)
    RunCommand(PLATFORM_TOOL)

def RunCommand(cmd):
    subprocess.call("py {}/{}.py".format(TOOLS_DIR, cmd))

for i in range(1, len(sys.argv)):
    cmd = sys.argv[i]
    print("\n---------------------------------")
    print("Executing: ", cmd)
    if cmd.lower() == "genproj":
        GenerateProject()
    else:
        RunCommand(cmd)
