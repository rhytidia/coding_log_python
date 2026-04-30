from date_time_funcs import get_curr_year_month
import os

'''The following produces a filepath with the current year and month as a filename, and
joins it to a user-provided directory.'''

def get_filepath_curr_month():
    for i in range(3):
        directory = input("Please provide a path to a directory where you want the file to be saved\n")
        if not directory:
            print("Please try again to input a directory path")
            continue
        elif not os.path.isdir(directory):
            print("Directory path does not exist or is not a full path, please try again.")
            continue
        break
    else: 
        print("Maximum number of attempts reached; exiting program")
        return None
    curr_month = get_curr_year_month()
    filename = f"{curr_month}.md"
    full_filepath = os.path.join(directory, filename)
    return full_filepath
