import unittest
from unittest import mock
from unittest.mock import patch, mock_open
from read_write import open_curr_month_file, q_and_a
from date_time_funcs import get_today_date, get_curr_time_mins


'''for open_curr_month_file'''

class TestReadWrite(unittest.TestCase):

    # test search for today's date in file content and write the date in the file if not found

    def test_write_today_date(self):
        today_date = get_today_date()
        # mocked content for a mocked file
        mock_file_content = 'some test content with no date'
        # stacking patches to test both open and print
        with patch('read_write.open', mock_open(read_data=mock_file_content)) as mock_file, \
            patch('read_write.print') as mock_print:
            # fake file path; doesn't matter what this is b/c mocked
            file_path = 'test/path/file.md'
            open_curr_month_file(file_path)
            # mock a call to f.write with the string in parentheses (just that the call was made, not that this was actually written)
            mock_file.return_value.write.assert_any_call(f'## {today_date}\n\n')
            # mock printingi the string to the console (just that the call was made, not checking the actual stdout)
            mock_print.assert_any_call(f'\nFile successfully opened at {file_path}; ready to write your coding log for {today_date}.')

    # test search for today's date in file content and if found, write an update with current time

    def test_write_curr_time(self):
        today_date = get_today_date()
        mock_file_content = f'## {today_date}'
        with patch('read_write.open', mock_open(read_data=mock_file_content)) as mock_file, \
            patch('read_write.print') as mock_print:
            file_path = 'test/path/file.md'
            now_time = get_curr_time_mins()
            open_curr_month_file(file_path)
            mock_file.return_value.write.assert_any_call(f'### Update at {now_time}\n\n')
            mock_print.assert_any_call(f'\nFile successfully opened at {file_path}; ready to update your log for {today_date}, at {now_time}.')

    # test raising a Permission Error
    def test_perm_error(self):
         # stacking patches, including calling a function within the read_write module
         with patch('read_write.open', mock_open()) as mock_file, \
            patch('read_write.print') as mock_print, \
            patch('read_write.get_filepath_curr_month') as mock_func:
            mock_file.side_effect = PermissionError("test Permission Error message")
            file_path = 'test/path/file.md'
            open_curr_month_file(file_path)
            mock_print.assert_any_call(f'A permission error occurred: test Permission Error message. Please try again or type Ctrl-C to exit')
            mock_func.assert_called()

'''Test Q&A actions'''

# to be implemented...
class TestQA(unittest.TestCase):
    pass