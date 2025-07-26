import os


def get_files_info(working_directory, directory="."):

    full_path = os.path.abspath(os.path.join(working_directory, directory))
    info_str = str()

    if directory == ".":
        info_str = "Result for current directory:\n"

    else:
        info_str = f"Result for '{directory}' directory:\n"

        if working_directory not in full_path or not os.path.exists(full_path):
            info_str = str().join(
                [
                    info_str,
                    f'Error: Cannot list "{directory}" as it is outside the permitted working directory',
                ]
            )
            return info_str

        if not os.path.isdir(full_path):
            info_str = str().join(
                [info_str, f'Error: "{directory}" is not a directory']
            )
            return info_str

    try:
        files = os.listdir(full_path)
        files = sorted(
            files, key=lambda file: os.path.getsize(os.path.join(full_path, file))
        )

        for items in files:
            full_item = os.path.join(full_path, items)
            isdir = os.path.isdir(full_item)
            info_str = str().join(
                [
                    info_str,
                    f"- {items}: file_size={os.path.getsize(full_item)} bytes, is_dir={isdir}\n",
                ]
            )

    except Exception as err:
        info_str = str().join([info_str, f"Error: {err}\n"])

    return info_str
