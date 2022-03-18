"""A simple python module proxy/fake imitating the ModuleType interface"""
__version__ = "0.1.0"
import ast
import importlib
import importlib.util
from types import ModuleType
from typing import  Any
from pathlib import Path


class ModuleVisitor(ast.NodeVisitor):
    __version__ = ""

    def visit_Assign(self, node: ast.Assign) -> Any:
        for target in node.targets:
            if getattr(target, 'id', None) == '__version__':
                self.__version__ = getattr(node.value, "value", None)


class ModuleProxy:
    """
    A module proxy. Emulating the ModuleType Interface without executing it.
    This can be useful to inspect module without executing it and falling into namespace troubles at given time.
    """
    def __init__(self, path_to_module: Path):
        self.path = path_to_module
        self.name = self.path.stem
        self.__code__ = self.path.read_text()
        self._node = ast.parse(self.__code__)

        self.__name__ = self.name
        self.__spec__ = importlib.util.spec_from_file_location(self.name, self.path)
        self.__loader__ = self.__spec__.loader
        self.__package__ = "" # todo ???
        self.__doc__ = ast.get_docstring(self._node)

        mv = ModuleVisitor()
        mv.visit(self._node)
        self.__version__ = mv.__version__

    def _execute(self) -> ModuleType:
        self._module = importlib.util.module_from_spec(self.__spec__)
        self.__spec__.loader.exec_module(self._module)
        return self._module


def _make_module(filepath: Path):
    """
    The hard way. Executing it. Will always be problematic, as it will be executed in the current
    namespace.
    :param filepath:
    :return:
    """
    module_name = "module." + filepath.stem
    spec = importlib.util.spec_from_file_location(module_name, filepath)
    module = importlib.util.module_from_spec(spec)
    return module
