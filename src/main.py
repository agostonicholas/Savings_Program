# Function Definitions #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import json


def load_bills(filename="bills.json"):  # finished
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


def save_bills(bills, filename="bills.json"):  # finished
    with open(filename, "w") as file:
        json.dump(bills, file, indent=4)


def track_bills():  # FIX_ME: Add a total of bills feature, central tendencies, Bill loading is broken
    bills = load_bills()

    # load the bills and print them # Adds total
    if bills:
        print("* * * Existing Bills * * *\n")
        total = 0
        for bill_name, bill_amount in bills:
            print(f"* {bill_name}: ${bill_amount:.2f} *\n")
            total += bill_amount
            print(f"Total of all bills: ${total:.2f}\n")
    else:
        print("No saved bills")

    choice = input("Add new bills? (y/n) ").strip().lower()

    # add new bills #
    if choice == "y":
        while True:
            name = input("What is the name: ").strip()
            amount = float(input(f"What is the amount for {name}").strip())
            bills[name] = amount

            another = input("Add another bill? (y/n)").strip().lower()

            if another != "y":
                break
    save_bills(bills)

    print("Bills Updated!")

    total = sum(bills.values())


def track_savings():
    pass


def save():
    pass


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
    print("3: Create monthly goal")
    print("4: Create year goal")
    print("5: Save")
    print("6: Save and quit")
    # # options for the menu
    options = {
        "1": track_bills,
        "2": track_savings,
        "3": create_goal_month,
        "4": create_goal_year,
        "5": save,
        "6": save_and_quit
    }
    # # handles the choices
    if choice in options:
        options[choice]()
    else:
        print("Invalid option. Choose a number 1-6.")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # Main # # # # # # # # # # # # # #
def main():
    while True:
        menu_options("")
        choice = input().strip()
        menu_options(choice)


main()

