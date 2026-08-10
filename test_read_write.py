import unittest
from unittest.mock import patch, mock_open
from read_write import read_write, write_new_today_log, write_updated_today_log, q_and_a
from date_time_funcs import get_today_date, get_curr_time_mins
from constants import questions_msg

'''Test cases for various functions in read_write.py'''

class TestWriteDayTime(unittest.TestCase):

    # test search for today's date in file content and pursue the "new log for today" path in read_write()

    def test_no_today_date_in_file(self):
        # fake file path; doesn't matter what this is b/c mocked
        file_path = 'test/path/file.md'
        today_date = get_today_date()
        # mocked content for a mocked file
        mock_file_content = 'some test content with no date'
        # stacking patches to test open, print, and calling a function
        with patch('read_write.open', mock_open(read_data=mock_file_content)) as mock_file, \
            patch('read_write.print') as mock_print, \
            patch('read_write.write_new_today_log') as mock_func:
            read_write(file_path)
            # check that file was opened to read
            mock_file.assert_called_once_with(file_path, "a+", encoding="utf-8")
             # mock printing the string to the console (just that the call was made, not checking the actual stdout)
            mock_print.assert_any_call(f'\nFile successfully opened at {file_path}; ready to write your coding log for {today_date}.')
            # mock printing the qa_message to the console as the last print call 
            mock_print.assert_called_with(questions_msg)
            # mock calling write_new_today_log() without actually doing so
            mock_func.assert_called()

    # test search for today's date in file content and if found, pursue the "updated log for today" path

    def test_today_date_in_file(self):
        file_path = 'test/path/file.md'
        today_date = get_today_date()
        now_time = get_curr_time_mins()
        mock_file_content = f'## {today_date}'
        with patch('read_write.open', mock_open(read_data=mock_file_content)) as mock_file, \
            patch('read_write.print') as mock_print, \
            patch('read_write.write_updated_today_log') as mock_func:
            read_write(file_path)
            mock_file.assert_called_once_with(file_path, "a+", encoding="utf-8")
            mock_print.assert_any_call(f'\nFile successfully opened at {file_path}; ready to update your log for {today_date}, at {now_time}.')
            mock_print.assert_called_with(questions_msg)
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

    # test what happens if the input reads 'exit' and there is no other input so returns empty dictionary

    def test_input_exit_no_answers(self):
        questions = ['question 1']
        with patch('read_write.input') as mock_input:
            mock_input.return_value = 'exit'
            self.assertEqual(q_and_a(questions), {})

    # test input as 'exit' but earlier questions have been answered so returns a dictionary with those answers (only)
    
    def test_input_exit_with_answers(self):
        questions = ['question 1', 'question 2', 'question 3']
        with patch('read_write.input') as mock_input:
            mock_input.side_effect = ['answer 1', 'answer 2', 'exit']
            self.assertEqual(q_and_a(questions), {'question 1': 'answer 1', 'question 2': 'answer 2'})

    # test skipping a question and the function still adds other questions & answers to the returned dictionary

    def test_skip_qs(self):
        questions = ['question 1', 'question 2', 'question 3', 'question 4']
        with patch('read_write.input') as mock_input:
            mock_input.side_effect = ['answer 1', 'answer 2', '', 'answer 4']
            self.assertEqual(q_and_a(questions), {'question 1': 'answer 1', 'question 2': 'answer 2', 'question 4': 'answer 4'})

    # test write a new log for today with today's date (tests just writing one q and one a)"

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

    # test writing an updated log for today with the current time (just tests writing one q and one a)

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
    
