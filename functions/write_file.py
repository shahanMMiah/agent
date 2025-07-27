import os
import locale
import sys

def write_file(working_directory, file_path, content):
    
    full_path = os.path.abspath(os.path.join(working_directory, file_path))
    output_str = str()
    if working_directory not in full_path:
        output_str = f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        return output_str
    
    try:
        par_dir = os.path.dirname(full_path)
        if not os.path.exists(par_dir):
            os.makedirs(os.path.dirname(par_dir))

        with open(full_path, "w", encoding=locale.getpreferredencoding()) as writer:
            writer.write(content)
            output_str = str().join([output_str, f'Successfully wrote to "{file_path}" ({len(content)} characters written)'])

    except Exception as err:
        output_str = str().join([output_str, f"Error: {err}"])

    return output_str

if __name__ == "__main__":
    script, *args = sys.argv
    print(write_file(*args))

