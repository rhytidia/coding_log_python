# Project title

Coding Log

# Overview

A CLI program written mostly in python that generates a daily log to record what one did that day in terms of coding work. It asks the user a series of questions about their coding activities that day and writes the answers to a markdown file at a path provided by the user.

This program could easily be modified to prompt the user to make logs on any topic by adjusting the questions in `constants.py`. The rest of the program is content-agnostic.

## Motivation

As part of a learning path on [Boot.dev](https://boot.dev), we needed to create a personal project. I know python best so decided to create something in python. Though I know one could easily just generate a template for a markdown note and fill it out whenever one wants, I wanted to do this for learning, and also to create something I might actually use.

This is the first coding project I have created without a guided tutorial.

## Dependencies

Nothing beyond python. The project uses modules that are already built into python such as datetime, os, and unittest.

## Status

Main functionality completed, unit testing completed (though may fiddle with that a bit more for the sake of learning). 

Progress over time can be found on the [progress page](https://github.com/rhytidia/coding_log_python/wiki/Progress) for this project. I worked on this project off and on for several months; going weeks here and there without touching it. See the commit history for specific activity.

# Functionality details

The rogram runs in a CLI and saves inputs written into the console to a markdown file in a user-provided directory.

## Creating/updating a markdown file for the log

The user provides a filepath to a directory to save a markdown file with the log. The program checks that it's a valid directory, and then joins that directory path with a markdown file with the current month as a filename (e.g., 2026-05.md). It creates the md file if it doesn't exist already, or opens it if it does.

The program searches the markdown file to see if today's date is already there. If not, it writes today's date as a heading 2 (e.g. ## 2026-05-15). 

If today's date is already there it means that there is already a log entry for today. In that case, a heading 3 is provided in the form: `### Updated at {current_time}` (e.g. "Updated at 17:32).

## Writing the log
The program prints a series of questions to the console, prompting the user to answer each one. The questions are stored in `constants.py`, so can easily be changed. In the current functionality, the program does not accept multi-line inputs, so the log is limited to short updates.

The user can :
- skip questions by pressing `return`
- exit early by typing `exit`
- go back to the previous question and replace the earlier answer (or add an answer if the previous question was skipped) by typing `back`; then the question they were originally on when they typed `back` is asked again

In all cases, nothing is written to the markdown file (including no headings) unless there is at least one answer to a question, and only the questions that have answers are written. I.e., if a question is skipped, or if the user exits early, only those questions with answers are written to the log, not the questions skipped.

The questions are written to the markdown file in bold, and the answers in regular weight type.

## Possible future functionality

See the [functionality overview](https://github.com/rhytidia/coding_log_python/wiki/Functionality-overview) page on the project wiki for ideas for extending the project (not sure if I will end up doing any of these).

I had originally wanted to add a GUI to this program, but decided to just focus on learning more about unit testing with mock and testing most of the program's functionality that way. The GUI would add a lot more time and need for refactoring, and I'd like to call this one finished for now and possibly do more with it later (or not).

# Other

## Sample documentation

As part of the freeCodeCamp Responsive Web Design Certification path, we needed to create a technical documentation page. I decided to create one for this project. You can find it on Code Pen: [Coding log technical documentation (fCC)](https://codepen.io/Rhytidia/pen/JoENVVQ).

## Use of AI

All of the code in this program and the tests is my own. I learned how to do things mostly by referring to notes from learning python, by doing hours of web searches, and by trial and error. I sometimes asked an LLM (free version of Claude) to help with questions when I got stuck.

I have custom instructions for Claude to only ask me questions or suggest things to search on the internet, not to write code. It mostly complies. I used Claude as a support for learning, not for writing any of the code here.