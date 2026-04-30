import inputs
from get_filepath import get_filepath_curr_month
from date_time_funcs import get_curr_time_mins, get_today_date

''' 
Open a file with today's date (or update with current time) and write user-inputted answers to provided questions.

This program takes in a directory path from the user (see get_filepath.py) and, if that file can be opened, 
it asks the uswer questions and writes their answers to that file under an h2 heading with today's date, then returns the file path. If there is already 
a header in the file with today's date, it writes "Update at <current_time> under an h3 heading.
If the user skips some questions, those questions are not written to the file.
'''


def main():
    questions = inputs.questions
    today_date = get_today_date()
    now_time = get_curr_time_mins()
    print(inputs.welcome_msg)
    file_path = get_filepath_curr_month()
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
            get_filepath_curr_month()
        except OSError as e:
            print(f"An OS error occurred: {e}. Please try again or type Ctrl-C to exit")
            get_filepath_curr_month()
        print(inputs.questions_msg) # instructions for answering or skipping questions, or ending early
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

if __name__ == "__main__":
    main()

