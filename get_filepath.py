from date_time_funcs import get_curr_year_month
import os

'''
Asks the user for a filepath to a directory, and checks if it is a directory. The user has
three chances to provide a valid directory path. If successful, the function joins the user-
provided filepath with a filename of <current_year_month>.md: e.g., file/path/2026-05.md. 
This is then the full filepath that read_write.py will use.
'''

def get_filepath_curr_month() -> str | None:
    print("Start by specifying a file path for a log file; a file with the current month as title will be opened at that path.\n")
    for i in range(3):
        directory = input("Please provide a path to a directory where you want the file to be saved:\n")
        if not directory:
            print("Please try again to input a directory path.\n")
            continue
        elif not os.path.isdir(directory):
            print("Directory path does not exist or is not a full path, please try again.\n")
            continue
        break
    else: 
        print("Maximum number of attempts reached; exiting program.\n")
        return None
    curr_month = get_curr_year_month()
    filename = f"{curr_month}.md"
    full_filepath = os.path.join(directory, filename)
    return full_filepath
