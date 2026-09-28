import os
import subprocess
import sys
from typing import List

def get_running_path():
    path = os.path.abspath(__file__)
    path = path.split("\\")
    path = path[:-1]
    path = "\\".join(path)
    return path

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# step one, check if venv exists
def is_venv(venv_path:str)->bool:
    return os.path.exists(get_running_path()+f"\\{venv_path}")

# step two, check if libs are installed
def is_requirements(requirements_path:str)->bool:

    requirements = []

    try:
        with open(requirements_path,"r") as file:
            pass
    except FileNotFoundError as FNFE:
        print()

    l = subprocess.run(["pip ","list"],encoding="utf-8",capture_output=True)
    print(f"fffff {l.stdout}")


def venv(venv_path:str,args: List[str] = [], requirements_path:str = "requirements.txt") -> None:

    if is_venv(venv_path):
        is_requirements(requirements_path)
    else:

        venv_call = ["python","-m","venv",venv_path]
        venv_call = venv_call + args

        subprocess.run(venv_call)


    