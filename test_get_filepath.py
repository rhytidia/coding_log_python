from unittest import mock
from unittest.mock import patch
from get_filepath import get_filepath_curr_month
from date_time_funcs import get_curr_year_month
import unittest

class TestGetFilepath(unittest.TestCase):

    '''Testing if the provided path is not a directory, returning None & printing the right thing'''

    # patch decorator will mock just the things in the named module rather than, e.g. *all* inputs in your project
    
    @patch('get_filepath.print')# first part here is module name, then what you're testing
    @patch('get_filepath.os.path.isdir') 
    @patch('get_filepath.input')
    # when you stack 2 or more decorators they get passed into the function as args but in reverse order
    # so put them into the arg list in reverse order; here: input, isdir, and print
    def test_not_a_directory(self, mock_input, mock_isdir, mock_print): 
        # mock inputted data
        mock_input.return_value = '/some/fake/path'
        # mock whether inputted data ('/some/fake/path') is a directory or not
        mock_isdir.return_value = False
        actual = get_filepath_curr_month()
        expected = None
        # check that function returns None if the input is not a directory
        self.assertEqual(actual, expected)
        # check if a specific print call was called at any time in the function call 
        # this function tries three times; last one would be max attempts; want to also check print on earlier attempts
        mock_print.assert_any_call("Directory path does not exist or is not a full path, please try again.\n")
        mock_print.assert_called_with("Maximum number of attempts reached; exiting program.\n")

    '''Testing returning None if no input is given (for max number of times in the loop), 
    and also print statement'''

    @patch('get_filepath.print')
    @patch('get_filepath.input')
    def test_no_dir_path_input(self, mock_input, mock_print):
        mock_input.return_value = ""
        # condensing actual & expected into one self.assertEqual line
        self.assertEqual(get_filepath_curr_month(), None)
        mock_print.assert_any_call("Please try again to input a directory path.\n")
        mock_print.assert_called_with("Maximum number of attempts reached; exiting program.\n")

    '''Testing successful path: filename with current month is joined to inputted dirctory'''

    @patch('get_filepath.os.path.isdir') 
    @patch('get_filepath.input')
    def test_valid_directory(self, mock_input, mock_isdir):
        mock_input.return_value = '/valid/directory/'
        mock_isdir.return_value = True
        curr_month = get_curr_year_month()
        actual = get_filepath_curr_month()
        expected = f'/valid/directory/{curr_month}.md' 
        self.assertEqual(actual, expected)

