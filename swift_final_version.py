"""
Swift Alert
IS 3020 - Introduction to Business Programming
Author: [Your Name]

A beginner console application that tracks five investments. The user sets a
lower price limit and an upper price limit for any investment, and the program
alerts the user when the market price reaches or passes one of those limits.
"""

# The five investments the program tracks.
# Each investment is a dictionary stored inside one main dictionary.
# The keys "1" through "5" are the numbers the user types to pick one.
investments = {
    "1": {"name": "Tesla", "symbol": "TSLA", "price": 330.50,
         "lower": 0.0, "upper": 0.0, "limits_set": False},
    "2": {"name": "Apple", "symbol": "AAPL", "price": 212.75,
          "lower": 0.0, "upper": 0.0, "limits_set": False},
    "3": {"name": "Nvidia", "symbol": "NVDA", "price": 168.20,
          "lower": 0.0, "upper": 0.0, "limits_set": False},
    "4": {"name": "Intel", "symbol": "INTC", "price": 23.45,
          "lower": 0.0, "upper": 0.0, "limits_set": False},
    "5": {"name": "Google", "symbol": "GOOGL", "price": 185.90,
          "lower": 0.0, "upper": 0.0, "limits_set": False}
}


def show_welcome():
    """Display the welcome message when the program starts."""
    print("=" * 50)
    print("           WELCOME TO SWIFT ALERT")
    print("=" * 50)
    print("Swift Alert helps you watch five popular investments.")
    print("Choose an investment, set your own lower and upper")
    print("price limits, and Swift Alert will tell you when the")
    print("market price reaches one of them.")
    print("=" * 50)


def show_menu():
    """Display the main menu options."""
    print("\n----------- MAIN MENU -----------")
    print("1. View investments")
    print("2. Set my price limits")
    print("3. Check for alerts")
    print("4. Change a market price")
    print("5. Exit")
    print("---------------------------------")


def get_price(prompt):
    """Ask for a price and keep asking until the user types a valid one."""
    while True:
        try:
            price = float(input(prompt))
            if price <= 0:
                print("The price must be greater than zero.")
            else:
                return price
        except ValueError:
            print("That is not a number. Please try again.")


def choose_investment():
    """Show the five investments and return the one the user picks."""
    print("\nWhich investment?")
    for number in investments:
        print(number + ". " + investments[number]["name"])

    while True:
        choice = input("Enter 1 - 5: ")
        if choice in investments:
            return investments[choice]
        else:
            print("Please enter a number from 1 to 5.")


def display_investments():
    """Show every investment, its price, and the limits the user has set."""
    print("\n--------------- MY INVESTMENTS ---------------")
    print("NAME       PRICE      LOWER      UPPER")

    for number in investments:
        stock = investments[number]
        name = stock["name"].ljust(10)
        price = ("$" + format(stock["price"], ".2f")).ljust(10)

        if stock["limits_set"]:
            lower = ("$" + format(stock["lower"], ".2f")).ljust(10)
            upper = ("$" + format(stock["upper"], ".2f")).ljust(10)
        else:
            lower = "not set".ljust(10)
            upper = "not set".ljust(10)

        print(name + " " + price + " " + lower + " " + upper)


def set_limits():
    """Let the user enter a lower limit and an upper limit for one investment."""
    stock = choose_investment()

    print("\nSetting limits for " + stock["name"] + ".")
    print("The market price right now is $" + format(stock["price"], ".2f") + ".")

    while True:
        lower = get_price("Enter your LOWER limit: $")
        upper = get_price("Enter your UPPER limit: $")

        if lower < upper:
            stock["lower"] = lower
            stock["upper"] = upper
            stock["limits_set"] = True
            print("Limits saved for " + stock["name"] + ".")
            break
        else:
            print("The lower limit must be smaller than the upper limit.")
            print("Please enter both limits again.")


def check_investment(stock):
    """Compare one price to its limits and return LOW, HIGH, SAFE, or NONE."""
    if not stock["limits_set"]:
        return "NONE"
    elif stock["price"] <= stock["lower"]:
        return "LOW"
    elif stock["price"] >= stock["upper"]:
        return "HIGH"
    else:
        return "SAFE"


def check_alerts():
    """Look at all five investments and display every alert that is triggered."""
    print("\n---------------- ALERTS ----------------")
    alerts = 0
    no_limits = 0

    for number in investments:
        stock = investments[number]
        result = check_investment(stock)
        price = format(stock["price"], ".2f")

        if result == "LOW":
            limit = format(stock["lower"], ".2f")
            print("ALERT! " + stock["name"] + " dropped to $" + price
                  + ". That is at or below your lower limit of $" + limit + ".")
            alerts = alerts + 1
        elif result == "HIGH":
            limit = format(stock["upper"], ".2f")
            print("ALERT! " + stock["name"] + " rose to $" + price
                  + ". That is at or above your upper limit of $" + limit + ".")
            alerts = alerts + 1
        elif result == "NONE":
            no_limits = no_limits + 1

    if alerts == 0:
        print("No alerts. Every price with limits is in a safe range.")
    else:
        print("Total alerts: " + str(alerts))

    if no_limits > 0:
        print("(" + str(no_limits) + " investment(s) still have no limits set.)")


def change_price():
    """Let the user type a new market price to see how the alerts change."""
    stock = choose_investment()
    print("\n" + stock["name"] + " is currently $" + format(stock["price"], ".2f") + ".")

    new_price = get_price("Enter the new market price: $")
    stock["price"] = new_price
    print(stock["name"] + " is now $" + format(new_price, ".2f") + ".")

    result = check_investment(stock)
    if result == "LOW":
        print("ALERT! That is at or below your lower limit.")
    elif result == "HIGH":
        print("ALERT! That is at or above your upper limit.")
    elif result == "SAFE":
        print("That price is still in your safe range.")
    else:
        print("You have not set limits for " + stock["name"] + " yet.")


def main():
    """Run the program until the user chooses to exit."""
    show_welcome()

    print("\nLet's get started!")
    print("First, choose an investment and set your price limits.")
    set_limits()

    running = True

    while running:
        show_menu()
        choice = input("What would you like to do? (1 - 5): ")

        if choice == "1":
            display_investments()
        elif choice == "2":
            set_limits()
        elif choice == "3":
            check_alerts()
        elif choice == "4":
            change_price()
        elif choice == "5":
            print("\nThank you for using Swift Alert. Goodbye!")
            running = False
        else:
            print("That is not a valid choice. Please enter 1 through 5.")


main()
def check_investment(stock):
    """Compare one price to its limits and return LOW, HIGH, SAFE, or NONE."""
    if not stock["limits_set"]:
        return "NONE"
    elif stock["price"] <= stock["lower"]:
        return "LOW"
    elif stock["price"] >= stock["upper"]:
        return "HIGH"
    else:
        return "SAFE"


def check_alerts():
    """Look at all five investments and display every alert that is triggered."""
    print("\n---------------- ALERTS ----------------")
    alerts = 0
    no_limits = 0

    for number in investments:
        stock = investments[number]
        result = check_investment(stock)
        price = format(stock["price"], ".2f")

        if result == "LOW":
            limit = format(stock["lower"], ".2f")
            print("ALERT! " + stock["name"] + " dropped to $" + price
                  + ". That is at or below your lower limit of $" + limit + ".")
            alerts = alerts + 1
        elif result == "HIGH":
            limit = format(stock["upper"], ".2f")
            print("ALERT! " + stock["name"] + " rose to $" + price
                  + ". That is at or above your upper limit of $" + limit + ".")
            alerts = alerts + 1
        elif result == "NONE":
            no_limits = no_limits + 1

    if alerts == 0:
        print("No alerts. Every price with limits is in a safe range.")
    else:
        print("Total alerts: " + str(alerts))

    if no_limits > 0:
        print("(" + str(no_limits) + " investment(s) still have no limits set.)")


def change_price():
    """Let the user type a new market price to see how the alerts change."""
    stock = choose_investment()
    print("\n" + stock["name"] + " is currently $" + format(stock["price"], ".2f") + ".")

    new_price = get_price("Enter the new market price: $")
    stock["price"] = new_price
    print(stock["name"] + " is now $" + format(new_price, ".2f") + ".")

    result = check_investment(stock)
    if result == "LOW":
        print("ALERT! That is at or below your lower limit.")
    elif result == "HIGH":
        print("ALERT! That is at or above your upper limit.")
    elif result == "SAFE":
        print("That price is still in your safe range.")
    else:
        print("You have not set limits for " + stock["name"] + " yet.")


def main():
    """Run the program until the user chooses to exit."""
    show_welcome()
    running = True

    while running:
        show_menu()
        choice = input("What would you like to do? (1 - 5): ")

        if choice == "1":
            display_investments()
        elif choice == "2":
            set_limits()
        elif choice == "3":
            check_alerts()
        elif choice == "4":
            change_price()
        elif choice == "5":
            print("\nThank you for using Swift Alert. Goodbye!")
            running = False
        else:
            print("That is not a valid choice. Please enter 1 through 5.")


main()