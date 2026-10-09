# VenvPro

VenvPro is a painless approach to the python virtual envrionment system. You can think of it like a build system for Python built entirely in python in one file!

# Usage

When writing a project, you will need to place VenvPro before any module dependant code and call the "venv" function. A clean way of achieving this would be as follows

Imagine you have a project like:

```
my_app/
├─ src/
│  ├─ main.py
│  ├─ venvpro.py
│  ├─ setup.py
```
You could put your call to "venv" in setup.py and import setup.py before any module dependant code.

An example would look like

```py
#main.py
import setup # <-- all checks and setup is done at the start of the program
from flask import Flask

app = Flask(__name__)

@app.route("/")
def helloworld():
    return "<h1> VenvPro helped build this app! </h1>"

if __name__ == "__main__":
    app.run()
```


# Example

When using venvpro you will only need the venv function. The venv function requires 1 argument but comes with 2 optional arguments too

1. venv_path | Mandatory argument for the path of your venv relative to your main file 
2. args | Optional argument comprised of strings that are the direct arguments you can pass to pythons venv system
3. requirements_path | Optional argument to say where the requirements.txt file is for the project. If left empty, the directory of the main python file is assumed for the location of requirements.txt

an example in code

```py
import venvpro as vp

vp.venv("my_virtual_env",[],"config/requirements.txt")
```

To see a real usage example of venvpro check https://github.com/Barnold8/VenvPro/tree/testing for a hello world flask app that uses venvpro as its build tool