"""Test file for testing the functions in main.py file"""

import unittest  # for creating the test case
import sys  # for adding the parent directory to the path
from pathlib import Path  # for getting the path of the main.py file
# add the parent directory to the path in order to run it from the run command in vscode
MAIN_FILE_FOLDER = Path(__file__).parents[1].as_posix()
sys.path.insert(1, MAIN_FILE_FOLDER)
from main import list_prime_factors  # nopep8 pylint: disable=wrong-import-position


class TestFunction(unittest.TestCase):
    """Class for testing the main.py file"""

    def setUp(self):
        self.nums: dict[int, list[int]] = {1: [], 2: [2], 3: [3], 4: [2, 2], 21: [
            3, 7], 56: [2, 2, 2, 7], 83: [83], 97: [97], 120: [2, 2, 2, 3, 5]}

    def test_list_prime_factors(self):
        """Test the list_prime_factors function"""
        for key, value in self.nums.items():
            self.assertEqual(list_prime_factors(key), value)


if __name__ == "__main__":
    unittest.main()
