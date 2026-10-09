import subprocess
import shutil
from os import listdir    
from os.path import isfile, join

def delete():

    paths = [
        "venv",
        "__pycache__"
    ]

    for path in paths:
        try:
            print(f"RESET: Removing {path}")
            shutil.rmtree(path)
        except FileNotFoundError as FNFE:
            print(f"RESET: Could not find path {path} to delete, skipping...")


def reset():

    print("RESET: Deleting venv and cache")
    delete()
    print("RESET: Running venv test")
    subprocess.run(["python","main.py"])


reset()