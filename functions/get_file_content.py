import os
from google.genai import types
from config import MAX_CHARACTERS as MAX_CHARS

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read the content of a given file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file": types.Schema(
                type=types.Type.STRING,
                description="Path of the file to read, relative to the working directory",
            ),
        },
    ),
)


def get_file_content(working_directory, file):
    try:
        abs_path = os.path.abspath(working_directory)
        file_path = os.path.normpath(os.path.join(abs_path, file))
        is_valid_path = os.path.commonpath([abs_path, file_path]) == abs_path
        path_exists = os.path.isfile(file_path)

        if not is_valid_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        elif not path_exists:
            return f'Error: File not found or is not a regular file: "{file_path}"'
        else:
            with open(file_path, "r") as f:
                file_content_string = f.read(MAX_CHARS)
                if f.read(1):
                    file_content_string += (
                        f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                    )
                return file_content_string
    except Exception as e:
        return f"Error: {e}"
