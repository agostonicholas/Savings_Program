# Function Definitions #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import json


# # # # # # #
# Save/Load # Finished 2/3/2025 Working
# # # # # # # # # # # # # # # # # # # # # # # # # # #

def load_data(filename):  # finished
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):  # Handles both errors together
        return {}


def save_data(data, filename):  # finished
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
    except PermissionError:
        print(f"Error: Cannot write to {filename}. Check file permissions.")


# # # # #
# Bills # Finished 2/3/2025 Working
# # # # # # # # # # # # # # # # # # # # # # # # # # #

def edit_bill():
    bills = load_data("bills.json") or {}  # Ensure bills is a Dictionary
    bills_lower = {key.lower(): key for key in bills}  # lowercase the dictionary for case insensitivity

    print("\n* * * Edit Bills * * *\n")
    try:
        while True:
            bill_to_edit = input("What bill would you like to edit? (press ctrl+c to cancel)").strip().lower()
            if not bill_to_edit:  # if there's no input
                print("Enter a bill:")
                continue

            if bill_to_edit not in bills_lower:  # if the input doesn't match a bill
                print("Bill not found...")
                continue

            if bill_to_edit in bills_lower:  # bill matches
                edit_or_remove = input("Edit or Remove?").strip().lower()  # choice for edit
                original_name = bills_lower[bill_to_edit]  # removes the lowercase

                if edit_or_remove == "edit":  # Editing
                    while True:
                        try:
                            new_amount = float(input("Enter the new amount in dollars:"))  # takes new amount
                            break
                        except ValueError:  # catches invalid inputs
                            print("Enter a number")
                    bills[original_name] = new_amount  # finds the bill in bills.json and changes the amount
                    save_data(bills, "bills.json")  # save
                    print(f'{original_name} bill changed to ${new_amount}')
                    break

                if edit_or_remove == "remove":  # Removing
                    del bills[original_name]
                    save_data(bills, "bills.json")
                    print(f'{original_name} bill removed.')
                    break

                else:  # input validation
                    print('Enter edit or remove to continue.')

    except KeyboardInterrupt:
        track_bills()


def list_bills():  # Finished Working 2/3/2025
    bills = load_data("bills.json") or {}  # Ensure bills is a dictionary

    # Load and display existing bills
    if bills:
        print("\n* * * Existing Bills * * *\n")
        total = 0
        for bill_name, bill_amount in bills.items():
            print(f"{bill_name}: ${bill_amount:.2f}")
            total += bill_amount
        print(f"\nTotal of all bills: ${total:.2f}\n")
    else:
        print("No saved bills.")

    # Ask if user wants to add new bills
    choice = input("Add new bills? (y/n): ").strip().lower()

    # Add new bills
    if choice in ("y", "yes"):
        while True:
            name = input("What is the name: ").strip()

            # Validate numeric input
            while True:
                try:
                    amount = float(input(f"What is the amount for {name}: ").strip())
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            bills[name] = amount

            another = input("Add another bill? (y/n): ").strip().lower()
            if another not in ("y", "yes"):
                break  # Exit the loop

        save_data(bills, "bills.json")
        print("Bills Updated!")


def track_bills():  # Working 2/3/2025 Finished for now
    while True:

        print("1: List bills and their total")
        print("2: Edit/Remove an existing bill")
        print("3: Return to Main Menu")
        try:
            bills_option = int(input("Enter a number 1-3:"))

            bills_menu = {
                1: list_bills,
                2: edit_bill,
                3: main
            }

            if bills_option in bills_menu:
                bills_menu[bills_option]()
            else:
                print("Choose a number 1-3.")
        except ValueError:
            print("Choose a number 1-3.")


# # # # # #
# Income  #
# # # # # # # # # # # # # # # # # # # # # # # # # # #
def track_income():
    print('1: Total Income')
    print('2: Income Breakdown')
    print('3: Income Minus Bills')
    print('4: Main Menu')

    income_options = {
        1: total_income,
        2: income_breakdown,
        3: income_minus_bills,
        4: main
    }
    try:
        choice = int(input())
        if choice in income_options:
            income_options[choice]()
        else:
            print('Invalid input choose a number 1-4')
    except ValueError:
        print('Invalid input choose a number 1-4')


def list_income():
    income = load_data("income.json") or {}
    print('* * * Sources of Income * * *')
    for name, amount in income.items():
        print(f'* {name}: ${amount} *')


def total_income():
    income = load_data("income.json") or {}
    print('* * * Income * * *')
    while True:
        if not income:
            print('No income :(')
            monthly_amount = float(input('Add your monthly income.'))
            income["Monthly Income"] = monthly_amount
            weekly_amount = float(input('Add a weekly income.'))
            income["Weekly Income"] = weekly_amount
            save_data(income, "income.json")
            list_income()
        list_income()

        choice = input('Edit your income sources?').lower().strip()

        if choice == 'yes' or "y":
            print('Weekly or monthly?')
            income_type = input().lower().strip()
            if income_type == 'weekly':
                new_amount = float(input('Enter the new weekly income amount:'))
                income["Weekly Income"] = new_amount
                save_data(income, "income.json")
            if income_type == 'monthly':
                new_amount = float(input('Enter the new monthly income amount:'))
                income["Monthly Income"] = new_amount
                save_data(income, "income.json")
            else:
                print('Please enter weekly or monthly.')

        list_income()

        if choice == 'no' or "n":
            track_income()
        else:
            print('Please choose yes or no.')


def income_breakdown():
    pass


def income_minus_bills():
    pass


# # # # # #
# Savings # More functions in the future?? 2/3/2025
# # # # # # # # # # # # # # # # # # # # # # # # # # #
def track_savings():
    savings = load_data("savings.json") or {}  # Ensure savings is a Dictionary
    print('* * * Savings * * *')
    while True:
        if not savings:
            print('No savings >:(')
            amount = float(input('Enter an amount to start saving.'))
            savings["Total Savings"] = amount
            save_data(savings, "savings.json")
        for money, saved in savings.items():
            print(f'${saved} in savings')

        choice = input('Add to savings...').lower().split()
        if choice == 'yes' or 'y':
            amount = float(input('Enter an amount to save.'))
            savings["Total Savings"] += amount
            for money, saved in savings.items():
                print(f'${saved} in savings')
            save_data(savings, "savings.json")
        if choice == 'no' or 'n':
            for money, saved in savings.items():
                print(f'${saved} in savings')
            main()


# # # # # # # # # # # # # # # # # # # # # # # # # # #

def create_goal_month():
    pass


def create_goal_year():
    pass


def save_and_quit():
    pass


# # menu function. displays menu options and references functions
def menu_options(choice):
    print("1: Track bills")
    print("2: Track savings")
    print("3: Track income")
    print("4: Create monthly goal")
    print("5: Create year goal")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # Main # # # # # # # # # # # # # # #
def main():
    while True:
        options = {
            "1": track_bills,
            "2": track_savings,
            "3": track_income,
            "4": create_goal_month,
            "5": create_goal_year
        }

        menu_options("")  # Only needed if it prints the menu

        choice = input("Enter a choice: ").strip()  # Prompts user for input

        if choice == "6":  # Exit condition
            print("Exiting program...")
            break

        if choice in options:  # Ensure valid input
            options[choice]()  # Call the function
        else:
            print("Invalid option. Choose a number 1-5.")


main()
