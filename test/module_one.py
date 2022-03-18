"""A testmodule docstring"""
__version__ = "1.1.1"

import time


def foo(x=42):
    time.sleep(0.1)
    return x
