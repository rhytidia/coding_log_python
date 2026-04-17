from datetime import datetime
import inputs
import os

''' 
Open a file with today's date (or update with current time) and write user-inputted answers to provided questions.

This program takes in a directory path from the user (see get_filepath()) and, if that file can be opened, 
it asks the uswer questions and writes their answers to that file under an h2 heading with today's date, then returns the file path. If there is already 
a header in the file with today's date, it writes "Update at <current_time> under an h3 heading.
If the user skips some questions, those questions are not written to the file.
'''


def main():
    questions = inputs.questions
    today_date = get_today_date()
    now_time = get_curr_time_mins()
    print(inputs.welcome_msg)
    file_path = get_filepath()
    if file_path is not None: # Needed because get_filepath() will return None if max number of attempts reached
        try:
            with open(file_path, "a+", encoding="utf-8") as f: 
                f.seek(0)
                content = f.read()
                if today_date not in content:
                    f.write(f"## {today_date}\n\n")
                else:
                    f.write(f"### Update at {now_time}\n\n")
        except PermissionError as e:
            print(f"A permission error occurred: {e}. Please try again or type Ctrl-C to exit")
            get_filepath()
        except OSError as e:
            print(f"An OS error occurred: {e}. Please try again or type Ctrl-C to exit")
            get_filepath()
        print(inputs.questions_msg) # instructions for answering or skipping questions, or ending earlh
        for question in questions:
            answer = input(f"\n{question}\n")
            if answer == "end":
                return
            elif answer == "":
                continue
            else: 
                with open(file_path, "a") as f:
                    f.write(f"\n**{question}**\n\n")
                    f.write(f"{answer}\n\n")
        print(f"Your answers have been saved in a markdown file at {file_path}\n")
   
'''
Get a user-inputted directory path and combine with a filename with today's date

Asks for a directory path from the user, and if valid, joins that directory path with a filename
that has today's date plus a markdown extension: e.g., '2026-04-10.md'. User has up to a max of
three tries to provide a valid directoy path.
'''

def get_filepath():
    for i in range(3):
        directory = input("Please provide a path to a directory where you want the file to be saved.\n")
        if not directory:
            print("Please try again.\n")
            continue
        elif not os.path.isdir(directory):
            print("Directory path does not exist or is not a full path, please try again.\n")
            continue
        break
    else: 
        print("Maximum number of attempts reached; exiting program.\n")
        return None
    today = get_today_date()
    filename = f"{today}.md"
    full_filepath = os.path.join(directory, filename)
    return full_filepath

# Helper functions for date and time
def get_today_date():
    now = datetime.now()
    today_ymd = now.strftime("%Y-%m-%d")
    return today_ymd

def get_curr_time_mins():
    now = datetime.now()
    current_time_mins = now.strftime("%H:%M")
    return current_time_mins

if __name__ == "__main__":
    main()

