# This will be the main calling function to run the application
from classes.TerminalInterface import TerminalInterface


TerminalInterface().run()

# prompt = "Enter a number"
# error_msg = "That was not a number!"

# def get_integer_input(prompt, error_msg):
#     while True:
#         try:
#             user_input = int(input(prompt))
#             return user_input
#         except ValueError:
#             print(error_msg)

# get_integer_input(prompt, error_msg)