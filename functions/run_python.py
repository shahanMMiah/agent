import os
import subprocess

from functions import config

def run_python_file(working_directory, file_path, args=[]):
   
    full_path = os.path.abspath(os.path.join(working_directory, file_path))
    info_str = str()

    if working_directory not in full_path:
        info_str = f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        return info_str

    if not os.path.exists(full_path):
        info_str = f'Error: File "{file_path}" not found.'
        return info_str

    if not str(file_path).endswith(".py"):
        info_str = f'Error: "{file_path}" is not a Python file.'
        return info_str
    
    try:
       
        proccess = subprocess.run(["python3", full_path, *args], cwd=os.path.dirname(os.path.abspath(working_directory)), timeout=config.TIMEOUT_AMOUNT,check=False,capture_output=True)
        info_str = str().join([info_str, f"STDOUT: {proccess.stdout}\n", f"STDERR: {proccess.stderr}\n"])

        if proccess.returncode != 0:
            info_str = str().join([info_str, f"Process exited with code {proccess.returncode}\n"])
        if not proccess.stdout:
            info_str = str().join([info_str, "No output produced."])
    
    except Exception as err:
        info_str = str().join([info_str, f"Error: executing Python file: {err}"])

    return info_str