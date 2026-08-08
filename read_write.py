import inputs
from get_filepath import get_filepath_curr_month
from date_time_funcs import get_curr_time_mins, get_today_date

'''This module tries to open a file at the user-provided file_path, and if successful, it
searches for today's date in the file. If today's date is not there, then it goes down the 
"new log for today path." It asks the uswer questions and gathers answers into a dictionary 
of questions: answers. It then prints today's date as a heading 2 in the file only if there 
are user-provided answers, and prints the questions and answers below that.

If today's date is found in the file, then the read_write() function goes down the "update" path. 
It writes "Updated at <current_time> as a heading 3 on the file only if the user has provided some answers 
to the questions. It also writes questions and the user's answers to the file.'''

def read_write(file_path: str) -> None:
    today_date = get_today_date()
    now_time = get_curr_time_mins()
    try:
        with open(file_path, "a+", encoding="utf-8") as f: 
            f.seek(0)
            content = f.read()
            if today_date not in content:
                print(f"\nFile successfully opened at {file_path}; ready to write your coding log for {today_date}.")
                print(inputs.questions_msg) # instructions for answering or skipping questions, or ending early
                write_new_today_log(file_path)
            else:
                print(f"\nFile successfully opened at {file_path}; ready to update your log for {today_date}, at {now_time}.")
                print(inputs.questions_msg) 
                write_updated_today_log(file_path)
    except PermissionError as e:
        print(f"A permission error occurred: {e}. Please try again or type Ctrl-C to exit")
        get_filepath_curr_month()
    except OSError as e:
        print(f"An OS error occurred: {e}. Please try again or type Ctrl-C to exit")
        get_filepath_curr_month()

def q_and_a() -> dict:
    questions = inputs.questions
    qa_dict = {}
    for question in questions:
        answer = input(f"\n{question}\n")
        if answer == "end":
            break
        elif answer == "":
            continue
        else: 
            qa_dict[question] = answer
    return qa_dict

def write_new_today_log(file_path: str) -> None:
    today_date = get_today_date()
    qa_dict = q_and_a()
    if not qa_dict:
        print("Closing the log. No answers were provided or saved.")
    else: 
        with open(file_path, "a") as f:
            f.write(f"## {today_date}\n\n")
            for question, answer in qa_dict.items():
                f.write(f"\n**{question}**\n\n")
                f.write(f"{answer}\n\n")
        print(f"Closing the log. Your answers have been saved in a markdown file at {file_path}\n")

def write_updated_today_log(file_path: str) -> None:
    now_time = get_curr_time_mins()
    qa_dict = q_and_a()
    if not qa_dict:
        print("Closing the log. No answers were provided or saved.")
    else: 
        with open(file_path, "a") as f:
            f.write(f"### Update at {now_time}\n\n")
            for question, answer in qa_dict.items():
                f.write(f"\n**{question}**\n\n")
                f.write(f"{answer}\n\n")
        print(f"Closing the log. Your answers have been saved in a markdown file at {file_path}\n")