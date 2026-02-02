import os


def write_file(working_directory, file, content):
    try:
        abs_path = os.path.abspath(working_directory)
        file_path = os.path.normpath(os.path.join(abs_path, file))
        is_valid_path = os.path.commonpath([abs_path, file_path]) == abs_path
        is_dir = os.path.isdir(file_path)

        if not is_valid_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        elif is_dir:
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        else:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, "w") as f:
                f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
