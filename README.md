# Yearly Budget Generator
#### Video Demo:  https://youtu.be/vOFMicHV2bM
#### Description:
This program allows the user to generate a budget for the entire year. The user is able to input information regarding their expenses and their income and the program will lay out the entire year and show them when their account balance will get low and or go negative. The user is also able to create multiple budgets to try different scenarios out as well as delete budgets they no longer need. The program is written in python as per the requirements and is ran in the terminal. Below is an explanation of what each portion of the programs code does and how they work together to accomplish the desired outcome.


**Imports**

#### *import sys* - Used to have access to sys.exit().

*import os* - Used to be able to make new files based on user input.

*import csv* - Used to handle the manipulation of csv files that store the users budgets.

*from tabulate import tabulate* - Used to style the users budget in a manner more easily readable.

*from datetime import datetime, date, timedelta* - Used to get date information and generate when budget items are due.


#### **project.py Functions**

*def main():*\
This is the main function that calls on the other functions needed to produce the desired outcome. It presents the main menu that the user can use to navigate the program. Based on what option the user chooses form the main menu, it will call on the function that executes that choice’s functionality.

*def view_budget():*\
This function is called by main and will generate a list of budgets available for viewing. It does this by getting the names of all the files stored in the folder which stores the user’s created budgets. Once a user selects a file to view this function calls on render_budget to actually display the chosen budget on the screen.

*def render_budget(budget, starting_balance):*\
This function is called by view_budget. The main job of this function is to format the budget to be easy to read by the user. This is accomplished with the help of three other functions that each help prepare the budget for displaying. Those functions are find_balance_col, calc_balance_values, and color_code. After these three functions have done their job the tabulate module is used to display the budget in a grid format.

*def make_new_budget():*\
This function is used when a user would like to generate a new budget. It will ask the user for all the information needed to generate a new budget and store it in the budget folder along with the user’s other budgets.

*def delete_budget():*\
Simple function that asked a user to choose an item to delete and then deletes the chosen item.

*def exit_program():*\
Simple function to print an exit message and then exit the program with exit code 0.

*def enter_pause():*\
Simple function used to pause the program to allow the used to read information. The user may then press ENTER once they are ready to proceed.

*def find_balance_col(headers) -> int:*\
One of the functions called by render_budget used to find which colon contains the balance information. This will then be passed to the calc_balance_values for further processing.

*def calc_balance_values(rows, balance_col, starting_balance):*\
Another one of the functions called by render_budget used to fill out the balance column information.

*def color_code(rows, balance_col):*\
The last functions called by render_budget used to color code the balance column information to indicate low and negative balances.


#### **Testing Functions**
*def test_find_balance_col():*\
Tests the find_balance_col function to make sure it correctly locates which column contains the balance information.

*def test_calc_balance_values():*\
Tests the calc_balance_values function to make sure it correctly calculates balance values based on expenses and income.

*def test_color_code():*\
Tests the color_code function to make sure the correct color coding is applied to the balance column.
