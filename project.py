# CS50P Final Project
# Name: Personal Finance Application
# Usage: project.py
# Summary: This program can be used to track users monthly expenses and income.
import sys
import os
import csv

from tabulate import tabulate
from datetime import datetime, date, timedelta

def main():
    # Start Program that will stay active until user ends it.
    while True:
        # Present action menu
        os.system('clear')

        print("Choose an action")
        menu_options = [['1. View Budget'], ['2. Make New Budget'], ['3. Delete Budget'], ['4. EXIT']]  # List of lists for the tabulate function
        print(tabulate(menu_options))

        # Execute choice
        choice = int(input("Enter Choice: "))
        match choice:

            case 1:
                view_budget()

            case 2:
                make_new_budget()

            case 3:
                delete_budget()

            case 4:
                exit_program()

            case _:
                print("Not a valid choice")
                enter_pause()
                continue


def view_budget():
    '''
    Shows a list of all available budgets and allows
    the user to select one to view
    '''
    while True:
        # Shows budgets created
        os.system('clear')
        budgets = []
        rowIDs = []
        for i, name in enumerate(os.listdir('budgets/')):
            budgets.append([name.rstrip('.csv')])
            rowIDs.append(i + 1)
        print(tabulate(budgets, showindex=rowIDs))

        choice = int(input("Choose budget to view: "))

        if choice in rowIDs:
            # Open csv containing chosen file and display it
            chosen_budget = os.listdir('budgets/')[choice - 1]
            current_balance = int(input("Enter Starting Balance: "))
            render_budget(chosen_budget, current_balance)
            break
        else:
            print("Not a valid choice.\nPlease choose from the list provided")
            enter_pause()


def render_budget(budget, starting_balance):
    '''
    Called from function view_budget.
    Chosen budget is passed as arg to be redered to console.
    '''
    os.system('clear')
    path = 'budgets/' + budget
    rows = []
    headers = []



    # Load csv
    with open(path, 'r') as budget_file:
        reader = csv.reader(budget_file)
        for i, row in enumerate(reader):
            if i == 0:
                headers = row
            else:
                rows.append(row)

    # Find what row contains the balance.
    balance_col = -1
    balance_col = find_balance_col(headers)  # TEST FUNCTION

    # Calculate Balance values
    rows = calc_balance_values(rows, balance_col, starting_balance)  # TEST FUNCTION

    # for i in range(len(rows)):
    #     if i == 0:
    #         rows[0][balance_col] = starting_balance
    #     else:
    #         try:
    #             int1 = int(rows[i - 1][balance_col])
    #         except ValueError:
    #             int1 = 0

    #         try:
    #             int2 = int(rows[i][balance_col - 1])
    #         except ValueError:
    #             int2 = 0

    #         rows[i][balance_col] = str(int1 + int2)



    # Color code Balance values
    rows = color_code(rows, balance_col)  # TEST FUNCTION

    # for row in rows:
    #     if row[0] == 'New Month':
    #         continue
    #     else:
    #         bal = int(row[balance_col])
    #         if bal <= 100 and bal > 0:
    #             row[balance_col] = f'{BLACK_TXT}{YELLOW_BG}{row[balance_col]}{RESET}'
    #         elif bal <= 0:
    #             row[balance_col] = f'{WHITE_TXT}{RED_BG}{row[balance_col]}{RESET}'
    #         else:
    #             continue

    print(tabulate(rows, headers=headers, tablefmt="grid"))
    enter_pause()


def make_new_budget():
    '''Creates file needed to store new budget'''
    os.system('clear')

    while True:
        name = input("Enter budget name: ")
        name_csv = name + '.csv'
        budget_folder_path = f'budgets/{name_csv}'

        if not os.path.exists(budget_folder_path):
            with open(budget_folder_path, 'w') as file:
                print(f"Budget named {name} has been created!\nFile name is {name_csv}")
            enter_pause()
            break
        else:
            print(f"Budget named {name} already exists.\nPlease choose a different name.")
            enter_pause()

    # Loads newly created file with needed items
    # Enter column names
    col_names = ['Month', 'Day', 'Item', 'Amount', 'Balance', 'Notes']
    c_num = 6
    # Custom column names to be added later
    # while True:
    #     c_name = input(f"Enter Column #{c_num + 1}'s name or 'D' if done: ")
    #     if c_name == 'D':
    #         break
    #     else:
    #         col_names.append(c_name)
    #         c_num += 1

    # Enter items
    os.system('clear')
    items = []
    print("Enter budget items\nEnter 'D' when done")
    while True:
        item_name = input("Item Name: ")
        if item_name == 'D':
            break
        day_due = input("Day Due: ")
        amount_due = input("Amount Due: ")
        items.append([day_due, item_name, amount_due])
        print()

    os.system('clear')
    pay_items = []
    print("Enter pay infomration\nEnter 'D' when done")
    while True:
        pay_name = input("Name: ")
        if pay_name == 'D':
            break
        pay_amount = input("Amount: ")
        print("Choose pay frequency:\n1. Monthly\n2. Bi-Weekly\n3. Weekly")
        pay_frequency = int(input("Frequency: "))
        pay_items.append([pay_name, pay_amount, pay_frequency])
        print()

    os.system('clear')
    pay_dates = []
    for pay in pay_items:
        match pay[2]:
            case 1:  # Monthly
                day = input("Enter pay day: ")

                for j in range(12):
                    pay_dates.append([j + 1, day, f'{pay[0]} Pay Day', pay[1]])
            case 2:  # Bi-Weekly
                s_mth, s_day, s_year = input(f"Enter date of first pay check recived this year by {pay[0]} (MM/DD/YYYY): ").split("/")
                start_date = datetime.strptime(s_year + "-" + s_mth + "-" + s_day, "%Y-%m-%d")

                for j in range(26):
                    date_to_add = start_date + timedelta(days=(14 * j))
                    date_to_add = str(date_to_add.date())

                    _, m_to_add, d_to_add = date_to_add.split("-")
                    pay_dates.append([m_to_add, d_to_add, f'{pay[0]} Pay Day', pay[1]])

            case 3:  # Weekly
                s_mth, s_day, s_year = input(f"Enter date of first pay check recived this year by {pay[0]} (MM/DD/YYYY): ").split("/")
                start_date = datetime.strptime(s_year + "-" + s_mth + "-" + s_day, "%Y-%m-%d")

                for j in range(52):
                    date_to_add = start_date + timedelta(days=(7 * j))
                    date_to_add = str(date_to_add.date())

                    _, m_to_add, d_to_add = date_to_add.split("-")
                    pay_dates.append([m_to_add, d_to_add, f'{pay[0]} Pay Day', pay[1]])

    # Add all items due and paychecks
    with open(budget_folder_path, 'w', newline='') as budget_file:
        writer = csv.writer(budget_file, quotechar='|')
        writer.writerow(col_names)
        for i in range(12):
            for j in range(30):
                for item in items:
                    if j + 1 == int(item[0]):
                        new_row = [0] * c_num
                        new_row[0] = i + 1
                        new_row[1] = item[0]
                        new_row[2] = item[1]
                        new_row[3] = str(int(item[2]) * -1)
                        writer.writerow(new_row)
                for pay_day in pay_dates:
                    if i + 1 == int(pay_day[0]) and j + 1 == int(pay_day[1]):
                        new_row = [0] * c_num
                        new_row[0] = i + 1
                        new_row[1] = pay_day[1]
                        new_row[2] = pay_day[2]
                        new_row[3] = pay_day[3]
                        writer.writerow(new_row)

            new_month = ['---'] * c_num
            new_month[0] = 'New Month'
            writer.writerow(new_month)


def delete_budget():
    while True:
        # Shows budgets created
        os.system('clear')
        budgets = []
        rowIDs = []
        for i, name in enumerate(os.listdir('budgets/')):
            budgets.append([name.rstrip('.csv')])
            rowIDs.append(i + 1)
        print(tabulate(budgets, showindex=rowIDs))

        choice = int(input("Choose budget to DELETE: "))

        if choice in rowIDs:
            # Open csv containing chosen file and display it
            chosen_budget = os.listdir('budgets/')[choice - 1]
            os.remove(f"budgets/{chosen_budget}")
            print("Selected budget has been deleted")
            enter_pause()
            break
        else:
            print("Not a valid choice.\nPlease choose from the list provided")
            enter_pause()


def exit_program():
    '''Used to exit the program and clear screen'''
    os.system('clear')
    print("Program Exited Successfully")
    sys.exit(0)


def enter_pause():
    '''Used to pause program and wait for user to press ENTER'''
    print("Press ENTER to continue.")
    input()
    return


# Functions to test
def find_balance_col(headers) -> int:
    for i, field in enumerate(headers):
        if field == 'Balance':
            return i

def calc_balance_values(rows, balance_col, starting_balance):

    for i in range(len(rows)):
        if i == 0:
            rows[0][balance_col] = starting_balance
        else:
            try:
                int1 = int(rows[i - 1][balance_col])
            except ValueError:
                int1 = 0

            try:
                int2 = int(rows[i][balance_col - 1])
            except ValueError:
                int2 = 0

            rows[i][balance_col] = str(int1 + int2)

    return rows


def color_code(rows, balance_col):

    # ANSI Color codes
    BLACK_TXT = "\033[30m"
    WHITE_TXT = "\033[37m"

    YELLOW_BG = "\033[43m"
    RED_BG ="\033[41m"

    RESET = "\033[0m"
    for row in rows:
        if row[0] == 'New Month':
            continue
        else:
            bal = int(row[balance_col])
            if bal <= 100 and bal > 0:
                row[balance_col] = f'{BLACK_TXT}{YELLOW_BG}{row[balance_col]}{RESET}'
            elif bal <= 0:
                row[balance_col] = f'{WHITE_TXT}{RED_BG}{row[balance_col]}{RESET}'
            else:
                continue

    return rows


if __name__ == "__main__":
    main()
