# pyru_importer.py

import subprocess

def import_python_module(module_name):
    # Use subprocess to run Python code to import module
    result = subprocess.run(['python', '-c', f'import {module_name}'], capture_output=True)
    if result.returncode == 0:
        print(f"Python module '{module_name}' imported successfully.")
    else:
        print(f"Failed to import Python module '{module_name}'.")

def import_ruby_module(module_name):
    # Use subprocess to run Ruby code to import module
    result = subprocess.run(['ruby', '-e', f'require "{module_name}"'], capture_output=True)
    if result.returncode == 0:
        print(f"Ruby module '{module_name}' imported successfully.")
    else:
        print(f"Failed to import Ruby module '{module_name}'.")
