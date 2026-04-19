import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
    
        # Gibt den absoluten Path von working directory an bspw. /user/lepucp/agent_project/functions
        working_directory_abs = os.path.abspath(working_directory)

        target_file = os.path.normpath(os.path.join(working_directory_abs, file_path))

        if not os.path.commonpath([working_directory_abs, target_file]) == working_directory_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not target_file[-3:] ==".py":
            return f'Error: "{file_path}" is not a Python file'
        if file_path not in os.listdir(os.path.dirname(target_file)):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        

        command = ["python", target_file]
        if args:
            command.extend(args)
        
        results = subprocess.run(command, text=True, cwd=working_directory_abs, capture_output=True, timeout=30)
        
        output_string = ""
        if results.returncode != 0:
            output_string += "Process exited with code X"
        if results.stdout is None and results.stderr is None:
            output_string += "No output produced"
        elif results.stdout:
            output_string += f"STDOUT: {results.stdout}"
        elif results.stderr:
            output_string += f"STDERR: {results.stderr}"
        
        return output_string
    except:
        return f"ERROR: python file ({file_path}) konnte nicht gesatrtet werden"

    




