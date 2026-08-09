import unittest
from unittest import mock
from unittest.mock import patch, mock_open
from read_write import read_write, write_new_today_log, write_updated_today_log, q_and_a
from date_time_funcs import get_today_date, get_curr_time_mins

# testing open_curr_month_file()

class TestWriteDayTime(unittest.TestCase):

    # test search for today's date in file content and write the date in the file if not found

    def test_write_today_date(self):
        file_path = 'test/path/file.md'
        today_date = get_today_date()
        # mocked content for a mocked file
        mock_file_content = 'some test content with no date'
        # stacking patches to test both open and print
        with patch('read_write.open', mock_open(read_data=mock_file_content)) as mock_file, \
            patch('read_write.print') as mock_print, \
            patch('read_write.write_new_today_log') as mock_func:
            # fake file path; doesn't matter what this is b/c mocked
            read_write(file_path)
            # mock printingi the string to the console (just that the call was made, not checking the actual stdout)
            mock_print.assert_any_call(f'\nFile successfully opened at {file_path}; ready to write your coding log for {today_date}.')
            # mock calling write_new_today_log() without actually doing so
            mock_func.assert_called()

    # test search for today's date in file content and if found, write an update with current time

    def test_write_curr_time(self):
        file_path = 'test/path/file.md'
        today_date = get_today_date()
        now_time = get_curr_time_mins()
        mock_file_content = f'## {today_date}'
        with patch('read_write.open', mock_open(read_data=mock_file_content)) as mock_file, \
            patch('read_write.print') as mock_print, \
            patch('read_write.write_updated_today_log') as mock_func:
            read_write(file_path)
            mock_print.assert_any_call(f'\nFile successfully opened at {file_path}; ready to update your log for {today_date}, at {now_time}.')
            mock_func.assert_called()
            
    # test raising an OS Error

    def test_os_error(self):
         # stacking patches, including calling a function within the read_write module
         with patch('read_write.open', mock_open()) as mock_file, \
            patch('read_write.print') as mock_print, \
            patch('read_write.get_filepath_curr_month') as mock_func:
            # what is in parentheses is the message that would be in `e` in the original fuction
            mock_file.side_effect = OSError("test OS message")
            file_path = 'test/path/file.md'
            read_write(file_path)
            mock_print.assert_any_call(f'An OS error occurred: test OS message. Please try again or type Ctrl-C to exit')
            # testing that the get_filepath_curr_month() mock function is called
            mock_func.assert_called()

# Test Q&A actions

class TestQA(unittest.TestCase):

    # test what happens if the input reads 'end' and there is no other input so returns empty dictionary

    def test_input_end_no_answers(self):
        questions = ['question 1']
        with patch('read_write.input') as mock_input:
            mock_input.return_value = 'exit'
            self.assertEqual(q_and_a(questions), {})

    # test input as 'end' but other questions have been answered so returns a dictionary with those answers (only)
    def test_input_end_with_answers(self):
        questions = ['question 1', 'question 2', 'question 3']
        pass
        # TO BE IMPLEMENTED
        # need to mock providing answers to one or two questions, then not the last one, 
        # and returning a dictionary with, e.g, {q1: a1, q2: a2}
        # how to mock input more than once?

    # test functionality if the user inputs answers to questions without typing "end"

    def test_write_new_log(self):
        qa_dict = {'question 1': 'answer 1', 'question 2': 'answer 2'}
        file_path = 'test/path/file.md'
        today_date = get_today_date()
        with patch('read_write.open', mock_open()) as mock_file,\
            patch('read_write.print') as mock_print,\
            patch('read_write.q_and_a') as mock_q_a:
            mock_q_a.return_value = qa_dict
            write_new_today_log(file_path)
            mock_print.assert_any_call(f'Closing the log. Your answers have been saved in a markdown file at {file_path}\n')
            mock_file.return_value.write.assert_any_call(f'## {today_date}\n\n')
            mock_file.return_value.write.assert_any_call(f'\n**question 1**\n\n')
            mock_file.return_value.write.assert_any_call(f'answer 1\n\n')


    def test_write_updated_log(self):
        qa_dict = {'question 1': 'answer 1', 'question 2': 'answer 2'}
        file_path = 'test/path/file.md'
        now_time = get_curr_time_mins()
        with patch('read_write.open', mock_open()) as mock_file,\
            patch('read_write.print') as mock_print,\
            patch('read_write.q_and_a') as mock_q_a:
            mock_q_a.return_value = qa_dict
            write_updated_today_log(file_path)
            mock_print.assert_any_call(f'Closing the log. Your answers have been saved in a markdown file at {file_path}\n')
            mock_file.return_value.write.assert_any_call(f'### Update at {now_time}\n\n')
            mock_file.return_value.write.assert_any_call(f'\n**question 2**\n\n')
            mock_file.return_value.write.assert_any_call(f'answer 2\n\n')
    
