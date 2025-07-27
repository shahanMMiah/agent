import os
import sys
import locale
from functions import config


def get_file_content(working_directory, file_path):

    full_path = os.path.abspath(os.path.join(working_directory, file_path))

    info_str = str()

    if working_directory not in full_path or not os.path.exists(full_path):
        info_str = f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        return info_str

    if not os.path.isfile(full_path):
        info_str = f'Error: File not found or is not a regular file: "{file_path}"'
        return info_str

    try:
        with open(full_path, "r", encoding=locale.getpreferredencoding()) as file:
            read_file = file.read()
            if len(read_file) > config.MAX_READ_CHARS:

                info_str = str().join([info_str, read_file[: config.MAX_READ_CHARS]])
                info_str = str().join(
                    [info_str, '...File "{file_path}" truncated at 10000 characters']
                )

            else:
                info_str += read_file

    except Exception as err:
        info_str = str().join([info_str, f"Error: {err}"])

    return info_str


if __name__ == "__main__":
    script, *args = sys.argv
    print(get_file_content(*args))