from unittest import mock
from unittest.mock import patch
from get_filepath import get_filepath_curr_month
import unittest

class TestGetFilepath(unittest.TestCase):

    '''Testing if the provided path is not a directory, returning None & printing the right thing'''

    @patch('get_filepath_practice.print')# first part here is module name, then what you're testing
    @patch('get_filepath_practice.os.path.isdir') 
    @patch('get_filepath_practice.input')
    # when you stack 2 or more decorators they get passed into the function as args but in reverse order
    def test_not_a_directory(self, mock_input, mock_isdir, mock_print): 
        mock_input.return_value = '/some/fake/path'
        mock_isdir.return_value = False
        actual = get_filepath_curr_month()
        expected = None
        self.assertEqual (actual, expected)
        mock_print.assert_any_call("Directory path does not exist or is not a full path, please try again.")
        mock_print.assert_any_call("Maximum number of attempts reached; exiting program")

    '''Testing returning None if no input is given (for max number of times in the loop), and also print statement'''

    @patch('get_filepath_practice.print')
    @patch('get_filepath_practice.input')
    def test_no_dir_path_input(self, mock_input, mock_print):
        mock_input.return_value = ""
        self.assertEqual(get_filepath_curr_month(), None)
        mock_print.assert_any_call("Please try again to input a directory path")
