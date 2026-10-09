# Welcome

Welcome to the testing branch for VenvPro. This branch is not unit tests like you may expect but more of a way to show how I tested this library. It also serves as a branch to provide an example app using venvpro as its build system.

# Usage

To try this branch, try ``python reset.py``

# Known issues

When testing I noticed a lot of permission errors when venvpro tries to access ``venv\\bin\\python.exe`` after the first intial setup. To get around this, you will need to kill any parent processes of venvpro. My reasoning of this error comes down to some abandoned proccess spawned by the subprocess model which is shoddy programming on my behalf. However, this is a testing branch and I don't aim to fix it.  