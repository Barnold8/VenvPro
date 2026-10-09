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

def enter_venv(venv_path:str,py_file:str) -> None:
    try:
        subprocess.Popen([f"{venv_path}/bin/python", py_file])
    except FileNotFoundError as FNFE:
        print("Error while starting VENV. Possible cause is venv doesnt exist or path to venv is wrong. Less possible cause is main file doesnt exist or path to main file is wrong")
        exit(-1)

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def parse_packages(packages:str)->None:
    return [x.split(" ")[0] for x in packages.stdout.split("\n")[2:]]

def is_venv(venv_path:str)->bool:
    return os.path.exists(get_running_path()+f"\\{venv_path}")

def get_requirements(requirements_path:str)-> List[str]:
    requirements = []

    try:
        with open(requirements_path,"r") as file:
            
            lines = file.readlines()
            for line in lines:
                if "=" in line:
                    l = line.split("=")[0]
                    requirements.append(l.lower())
                else:
                    requirements.append(line.lower())
        
    except FileNotFoundError as FNFE:
        eprint(f"Error: could not find requirements file at path \"{requirements_path}\"")
        exit(-1)

    return requirements

def clean_array(arr:List[str])-> List[str]:
    return [(x.strip()).lower() for x in arr]

# step two, check if libs are installed
def is_requirements(requirements_path:str,venv_path:str)->bool:

    requirements = get_requirements(requirements_path)    
    
    packages = parse_packages(subprocess.run(["pip ","list"],encoding="utf-8",capture_output=True))
    packages = clean_array(packages)
    requirements = clean_array(requirements)

    for requirement in requirements:
        if requirement not in packages:
            print(f"Warning: module {requirement.strip("\n")} not installed") 
            print(f"lines: {requirements}\n{"="*128}\npackages: {packages}")
            print(len(requirements),len(packages))
            
            return False
    return True

def install_requirements():
    subprocess.run("pip install -r requirements.txt".split(" "))


def get_running_file() -> str:
    return sys.argv[0]

def venv(venv_path:str,args: List[str] = [], requirements_path:str = "requirements.txt") -> None:

    if is_venv(venv_path):
        print("IN VENV")
        if is_requirements(requirements_path):
            print("REQUIREMENTS")
        else:
            install_requirements()
            print("INSTALL REQUIREMENTS")
    else:
        venv_call = ["python","-m","venv",venv_path]
        venv_call = venv_call + args

        subprocess.run(venv_call)   
    
        enter_venv(venv_path,get_running_file())
        
        print(get_running_file())



