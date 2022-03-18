# secmod

A simple module proxy for python.
Avoids importing the module but gives an interface like ModuleType.

This useful when you want to examine the contents of the module without executing it.
For example so safe the docstring or code in a database. 


## Install

    pip install secmod

or install it from github
    
    pip install git+https://github.com/cloasdata/secmod.git

or just clone it

## usage
```python
from pathlib import Path
from secmod import ModuleProxy

fp_module = Path("some_module.py")
module = ModuleProxy(fp_module)

print(module.__doc__)

```