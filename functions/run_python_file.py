import os
import subprocess

def run_python_file(working_directory, file, args=None):
    try:
        abs_path = os.path.abspath(working_directory)
        file_path = os.path.normpath(os.path.join(abs_path, file))
        is_valid_path = os.path.commonpath([abs_path, file_path]) == abs_path
        is_dir = os.path.isdir(file_path)

        if not is_valid_path:
            return f'Error: Cannot execute "{file}" as it is outside the permitted working directory'
        elif not os.path.isfile(file_path):
            return f'Error: "{file}" does not exist or is not a regular file'
        elif not file_path.endswith(".py"):
            return f'Error: "{file}" is not a Python file'
        else:
            command = ["python", file_path]
            if args != None:
                command.extend(args)
            output = subprocess.run(
                command,
                stdin=None,
                input=None,
                capture_output=True,
                shell=False,
                cwd=working_directory,
                timeout=30,
                text=True,
            )
            output_string = ""
            if output.returncode != 0:
                output_string += f"Process exited with code {output.returncode}\n"
            output_string += f"STDOUT: {'No output produced' if output.stdout == "" else output.stdout}\n"
            output_string += f"STDERR: {'No output produced' if output.stderr == "" else output.stderr}\n"
            return output_string
    except Exception as e:
        return f"Error: executing python file: {e}"
