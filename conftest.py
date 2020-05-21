"""Pytest config file."""

from importlib import import_module
from typing import Any, List

import os
import pytest





def get_sol_instances() -> List[Any]:
    """Returns a list of Solution instances found in the solutions package."""
    solutions = []
    for i in os.scandir(SOLUTIONS_DIR):
        if i.is_dir() and i.name != "__pycache__":
            module_name = f"{SOLUTIONS_DIR}.{i.name}.{SOLUTION_MODULE_NAME}"
            try:
                module = import_module(module_name)
            except ModuleNotFoundError:
                pytest.fail(f"failed loading {module_name}")
            try:
                cls = getattr(module, SOLUTION_CLASS_NAME)
            except AttributeError:
                pytest.fail(f"failed getting solution class {SOLUTION_CLASS_NAME}")
            solutions.append(cls)
    return solutions


def pytest_generate_tests(metafunc):
    """Generate the funcarg values used for the test cases."""
    if 'sol_cls' in metafunc.fixturenames:
        metafunc.parametrize('sol_cls', get_sol_instances())
  