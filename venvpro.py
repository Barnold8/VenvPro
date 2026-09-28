import os
import subprocess
from typing import List

def get_running_path():
    path = os.path.abspath(__file__)
    path = path.split("\\")
    path = path[:-1]
    path = "\\".join(path)
    return path


# step one, check if venv exists
def is_venv(venv_path:str)->bool:
    return os.path.exists(get_running_path()+f"\\{venv_path}")

# step two, check if libs are installed
def is_requirements(requirements_path:str)->bool:

    try:
        with open(requirements_path) as file:
            pass
    except FileNotFoundError as FNFE:
        print()

    l = subprocess.run(["pip ","list"],encoding="utf-8",capture_output=True)
    print(f"fffff {l.stdout}")


def venv(venv_name:str,args: List[str] = []) -> None:
    #Note for developers: venv_name is going to be the relative directory to your running python script. 
        # For example passing "venv" as the venv_name param will make a folder called venv in the same directory as your python script

    if is_venv(venv_name):
        pass
    else:

        venv_call = ["python","-m","venv",venv_name]
        venv_call = venv_call + args

        subprocess.run(venv_call)


    