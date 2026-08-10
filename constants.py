'''
These are constants used in various fumctions. The questions are used in q_and_a() in read_write.py.
The welcome_message is used in main.py, and the questions_msg is used in read_write.py.
'''

q1 = "Q1: What are you working on?"
q2 = "Q2: What have you completed or accomplished?"
q3 = "Q3: Any questions or challenges coming up?"
q4 = "Q4: What are your next steps?"
questions = [q1, q2, q3, q4]

welcome_msg = '''\nWelcome to your coding log. 
First, you will choose a path for a markdown file where your log will be saved.
Then you will answer questions and your answers will be saved to the log under today's date.\n'''

questions_msg = '''\nNow, please answer the questions as they come up.
If you want to skip to the next question just hit 'return.'
If you want to go back to the previous question & replace your previous answer, type 'back'.
If you want to exit early, type 'exit'. 
If you skip questions or exit early, only the answers you've provided so far (if any) will be saved to the log.\n'''