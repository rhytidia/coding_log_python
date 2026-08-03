import inputs
from get_filepath import get_filepath_curr_month
from date_time_funcs import get_curr_time_mins, get_today_date

def open_curr_month_file(file_path: str) -> None:
    today_date = get_today_date()
    now_time = get_curr_time_mins()
    try:
        with open(file_path, "a+", encoding="utf-8") as f: 
            f.seek(0)
            content = f.read()
            if today_date not in content:
                f.write(f"## {today_date}\n\n")
                print("\nFile successfully opened; ready to write your coding log for today.")
            else:
                f.write(f"### Update at {now_time}\n\n")
                print("\nFile successfully opened; ready to update your coding log for today.")
    except PermissionError as e:
        print(f"A permission error occurred: {e}. Please try again or type Ctrl-C to exit")
        get_filepath_curr_month()
    except OSError as e:
        print(f"An OS error occurred: {e}. Please try again or type Ctrl-C to exit")
        get_filepath_curr_month()

def write_answers(file_path: str) -> None:
    questions = inputs.questions
    answers_list = []
    for question in questions:
        answer = input(f"\n{question}\n")
        if answer == "end":
            print(f"Closing the log. If you wrote any answers so far, they have been saved at {file_path}\n")
            return
        elif answer == "":
            continue
        else: 
            with open(file_path, "a") as f:
                f.write(f"\n**{question}**\n\n")
                f.write(f"{answer}\n\n")
            answers_list.append(answer)
    print(answers_list)
    if len(answers_list) == 0:
        print("Closing the log. No answers were provided or saved.")
    print(f"Closing the log. Your answers have been saved in a markdown file at {file_path}\n")
    

