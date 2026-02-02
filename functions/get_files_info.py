from ntpath import abspath
import os


def get_files_info(working_directory, directory="."):
    results = []
    try:
        abs_path = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(abs_path, directory))
        is_valid_path = os.path.commonpath([abs_path, target_path]) == abs_path
        path_exists = os.path.isdir(target_path)

        if not is_valid_path:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        elif not path_exists:
            return f'Error: "{directory}" is not a directory'
        else:
            dir_content = os.listdir(target_path)
            for item in dir_content:
                item_path = os.path.normpath(os.path.join(target_path, item))
                results.append(
                    f"- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}"
                )
        return "\n".join(results)
    except Exception as e:

        return f"Error: {e}"


if __name__ == "__main__":
    print(get_files_info("calculator", "."))
