import os

def get_running_path():
    path = os.path.abspath(__file__)
    path = path.split("\\")
    path = path[:-1]
    path = "\\".join(path)
    return path

# step one, check if venv exists

def is_venv(venv_path:str)->bool:
    return os.path.exists(get_running_path()+f"\\{venv_path}")
    