import unittest
from unittest.mock import patch
from get_filepath import get_filepath_curr_month
from date_time_funcs import get_curr_year_month

class TestGetFilepath(unittest.TestCase):

    '''Testing if the provided path is not a directory, returning None & printing the right thing'''

    # patch decorator will mock just the things in the named module rather than, e.g. *all* inputs in your project
    @patch('get_filepath.print')# first part here is module name, then what you're testing
    @patch('get_filepath.os.path.isdir') 
    @patch('get_filepath.input')
    # when you stack 2 or more decorators they get passed into the function as args but in reverse order
    # so put them into the arg list in reverse order; here: input, isdir, and print
    def test_not_a_directory(self, mock_input, mock_isdir, mock_print): 
        # mock inputted directory path that is not a directory
        mock_input.return_value = '/some/fake/dir'
        # mock that the inputted path is not a directory
        mock_isdir.return_value = False
        actual = get_filepath_curr_month()
        expected = None # the function should return None if the input is not a directory
        self.assertEqual(actual, expected)
        # assert_any_call checks that print was called at any time 
        # assert_called_with checks that the print statement was the last one (here, last one is max attempts)
        mock_print.assert_any_call("Directory path does not exist or is not a full path, please try again.\n")
        mock_print.assert_called_with("Maximum number of attempts reached; exiting program.\n")

    '''Testing returning None if no input is given (for max number of times in the loop), 
    and also print statement'''

    @patch('get_filepath.print')
    @patch('get_filepath.input')
    def test_no_dir_path_input(self, mock_input, mock_print):
        mock_input.return_value = ""
        self.assertEqual(get_filepath_curr_month(), None) # should return none if no valid filepath provided
        mock_print.assert_any_call("Please try again to input a directory path.\n")
        mock_print.assert_called_with("Maximum number of attempts reached; exiting program.\n")

    '''Testing successful path: filename with current month is joined to inputted dirctory'''

    @patch('get_filepath.print')
    @patch('get_filepath.os.path.isdir') 
    @patch('get_filepath.input')
    def test_valid_directory(self, mock_input, mock_isdir, mock_print):
        mock_input.return_value = '/valid/directory/'
        mock_isdir.return_value = True
        curr_month = get_curr_year_month()
        actual = get_filepath_curr_month()
        # the function should return a joined user-inputted the directory with the filename of curr_month.md 
        expected = f'/valid/directory/{curr_month}.md' 
        self.assertEqual(actual, expected)
        mock_print.assert_called_with("Start by specifying a file path for a log file; a file with the current month as title will be opened at that path.\n")

    '''Testing empty path, then invalid directory path, then valid one'''
    @patch('get_filepath.print')
    @patch('get_filepath.os.path.isdir') 
    @patch('get_filepath.input')
    def test_valid_directory(self, mock_input, mock_isdir, mock_print):
        # side_effect allows you to test different inputs and return values on different iterations; 
        # this function allows 3 tries
        mock_input.side_effect = ['', 'invalid/directory', '/valid/directory/']
        # if input is empty, os.path.isdir() is not called, so only the 2nd and 3rd options above are checked
        mock_isdir.side_effect = [False, True]
        curr_month = get_curr_year_month()
        actual = get_filepath_curr_month()
        # the function should return a joined user-inputted the directory with the filename of curr_month.md 
        expected = f'/valid/directory/{curr_month}.md' 
        self.assertEqual(actual, expected)
        mock_print.assert_any_call("Please try again to input a directory path.\n")
        mock_print.assert_any_call("Directory path does not exist or is not a full path, please try again.\n")
       