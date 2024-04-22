# pyru_module.py

from pyru.pyru_python_bridge import PythonBridge

def add(a, b):
    return PythonBridge.add(a, b)

def call_python_function():
    return PythonBridge.call_python_function()

def pyru_to_python_list(pyru_list):
    return PythonBridge.pyru_to_python_list(pyru_list)

def python_to_pyru_list(python_list):
    return PythonBridge.python_to_pyru_list(python_list)
