import unittest

from functions.get_files_info import get_files_info

from functions.get_file_content import get_file_content

from functions.write_file import write_file

from functions.run_python import run_python_file


class TestGetInfo(unittest.TestCase):

    def test_getCalulator(self):
        result = get_files_info("calculator", ".")

        expected = "Result for current directory:\n- main.py: file_size=575 bytes, is_dir=False\n- tests.py: file_size=1342 bytes, is_dir=False\n- pkg: file_size=4096 bytes, is_dir=True\n- lorem.txt: file_size=20066 bytes, is_dir=False\n"

        # self.assertEqual(result, expected)
        print(result)

    def test_getCalulatorPkg(self):
        result = get_files_info("calculator", "pkg")
        expected = (
            "Result for 'pkg' directory:\n- render.py: file_size=766 bytes, is_dir=False\n- calculator.py: file_size=1737 bytes, is_dir=False\n- __pycache__: file_size=4096 bytes, is_dir=True\n"
            ""
        )

        # self.assertEqual(result, expected)
        print(result)

    def test_getCalulatorBin(self):
        result = get_files_info("calculator", "/bin")
        expected = """Result for '/bin' directory:
Error: Cannot list "/bin" as it is outside the permitted working directory"""

        # self.assertEqual(result, expected)
        print(result)

    def test_getCalulatorOutside(self):
        result = get_files_info("calculator", "../")
        expected = """Result for '../' directory:
Error: Cannot list "../" as it is outside the permitted working directory"""

        # self.assertEqual(result, expected)
        print(result)


class TestGetContent(unittest.TestCase):

    def test_calc_main(self):
        result = get_file_content("calculator", "main.py")
        print(result)

    def test_pkg_calc(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        print(result)

    def test_bin_cat(self):
        result = get_file_content("calculator", "/bin/cat")
        print(result)

    def test_bin_exists(self):
        result = get_file_content("calculator", "pkg/does_not_exist.py")
        print(result)


class TestWriteFile(unittest.TestCase):
    def test_write_lorem(self):
        results = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print(results)

    def test_write_morelorem(self):
        results = write_file(
            "calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"
        )
        print(results)

    def test_temp_test(self):
        results = write_file(
            "calculator", "/tmp/temp.txt", "this should not be allowed"
        )
        print(results)


class TestRunPython(unittest.TestCase):
    def test_calc_one(self):
        result = run_python_file("calculator", "main.py")
        print(result)

    def test_calc_two(self):
        result = run_python_file("calculator", "main.py", ["3 + 5"])
        print(result)

    def test_get_file_info(self):
        result = run_python_file("functions", "get_files_info.py", ["calculator", "."])
        print(result)

    def test_calc_tests(self):
        result = run_python_file("calculator", "tests.py")
        print(result)

    def test_outside_main(self):
        result = run_python_file("calculator", "../main.py")
        print(result)

    def test_non_existent(self):
        result = run_python_file("calculator", "nonexistent.py")
        print(result)


if __name__ == "__main__":
    unittest.main()
