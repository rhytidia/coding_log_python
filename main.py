import constants
from get_filepath import get_filepath_curr_month
from read_write import read_write

''' 
Open a file with the current month and add an entry for today's date (or update with current time) and write user-inputted 
answers to provided questions in that file. 

This program takes in a directory path from the user (see get_filepath.py) and, if that file can be opened, 
it asks the uswer questions and writes their answers to that file under an h2 heading with today's date, then returns the 
file path. If there is already a header in the file with today's date, it writes "Update at <current_time> under an h3 heading.
If the user skips some questions or exits early, the questions without answers are not written to the file.
'''


def main():
    print(constants.welcome_msg) 
    file_path = get_filepath_curr_month()
    if file_path is None: # get_filepath will return None if max number of attempts reached
        return
    read_write(file_path)
    
if __name__ == "__main__":
    main()

