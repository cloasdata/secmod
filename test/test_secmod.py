import pytest
from pathlib import Path
from types import ModuleType
from secmod import ModuleProxy

@pytest.fixture()
def path_to_pytest():
    return Path(__file__).parent / "module_one.py"


def test_secmod(path_to_pytest):
    module_proxy = ModuleProxy(path_to_pytest)

    import module_one

    assert module_one.__name__ == module_proxy.__name__
    assert module_one.__doc__ == module_proxy.__doc__
    assert module_one.__spec__ == module_proxy.__spec__
    assert module_one.__loader__ == module_proxy.__loader__


