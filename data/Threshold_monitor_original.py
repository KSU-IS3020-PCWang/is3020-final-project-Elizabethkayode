investments = {
    "1":
}

"""
Investment Threshold Tracker
IS 3020 - Introduction to Business Programming
Author: [Your Name]

A console application that lets a user build a watchlist of investments,
set an upper and lower price threshold for each one, record current prices,
and receive alerts when a price crosses a threshold.
"""

import csv
import os

DATA_FILE = "watchlist.csv"


def get_float_input(prompt):
    """Ask the user for a number and keep asking until a valid one is entered."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than zero.")
            else:
                return value
        except ValueError:
            print("That is not a valid number. Please try again.")


def load_watchlist(filename):
    """Read the CSV file and return the investments as a list of dictionaries."""
    watchlist = []
    if not os.path.exists(filename):
        print("No saved watchlist found. Starting with an empty list.")
        return watchlist

    try:
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                investment = {
                    "symbol": row["symbol"],
                    "current_price": float(row["current_price"]),
                    "lower_limit": float(row["lower_limit"]),
                    "upper_limit": float(row["upper_limit"])
                }
                watchlist.append(investment)
        print("Loaded " + str(len(watchlist)) + " investment(s) from " + filename + ".")
    except (KeyError, ValueError):
        print("The saved file is damaged. Starting with an empty list.")
        watchlist = []

    return watchlist


def save_watchlist(filename, watchlist):
    """Write the current watchlist to the CSV file."""
    try:
        with open(filename, "w", newline="") as file:
            fieldnames = ["symbol", "current_price", "lower_limit", "upper_limit"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for investment in watchlist:
                writer.writerow(investment)
        print("Watchlist saved to " + filename + ".")
    except IOError:
        print("The watchlist could not be saved.")


def find_investment(watchlist, symbol):
    """Return the dictionary for a symbol, or None if it is not in the watchlist."""
    for investment in watchlist:
        if investment["symbol"] == symbol.upper():
            return investment
    return None


def add_investment(watchlist):
    """Collect information from the user and add one investment to the watchlist."""
    symbol = input("Enter the ticker symbol: ").upper().strip()

    if symbol == "":
        print("The symbol cannot be blank.")
        return

    if find_investment(watchlist, symbol) is not None:
        print(symbol + " is already on the watchlist.")
        return

    current_price = get_float_input("Enter the current price: $")
    lower_limit = get_float_input("Enter the LOWER threshold: $")
    upper_limit = get_float_input("Enter the UPPER threshold: $")

    if lower_limit >= upper_limit:
        print("The lower threshold must be less than the upper threshold.")
        print(symbol + " was not added.")
        return

    investment = {
        "symbol": symbol,
        "current_price": current_price,
        "lower_limit": lower_limit,
        "upper_limit": upper_limit
    }
    watchlist.append(investment)
    print(symbol + " was added to the watchlist.")


def remove_investment(watchlist):
    """Delete one investment from the watchlist."""
    symbol = input("Enter the symbol to remove: ").upper().strip()
    investment = find_investment(watchlist, symbol)

    if investment is None:
        print(symbol + " is not on the watchlist.")
    else:
        watchlist.remove(investment)
        print(symbol + " was removed.")


def update_price(watchlist):
    """Record a new current price for one investment and report any alert."""
    symbol = input("Enter the symbol to update: ").upper().strip()
    investment = find_investment(watchlist, symbol)

    if investment is None:
        print(symbol + " is not on the watchlist.")
        return

    new_price = get_float_input("Enter the new price for " + symbol + ": $")
    investment["current_price"] = new_price
    print(symbol + " is now $" + format(new_price, ".2f") + ".")

    status = check_threshold(investment)
    if status != "OK":
        print(build_alert_message(investment, status))


def check_threshold(investment):
    """Compare one price to its limits. Return 'ABOVE', 'BELOW', or 'OK'."""
    if investment["current_price"] >= investment["upper_limit"]:
        return "ABOVE"
    elif investment["current_price"] <= investment["lower_limit"]:
        return "BELOW"
    else:
        return "OK"


def build_alert_message(investment, status):
    """Create the sentence that is shown to the user for one alert."""
    price = format(investment["current_price"], ".2f")

    if status == "ABOVE":
        limit = format(investment["upper_limit"], ".2f")
        return ("ALERT: " + investment["symbol"] + " reached $" + price
                + ", at or above the upper limit of $" + limit + ".")
    else:
        limit = format(investment["lower_limit"], ".2f")
        return ("ALERT: " + investment["symbol"] + " fell to $" + price
                + ", at or below the lower limit of $" + limit + ".")


def check_all_alerts(watchlist):
    """Check every investment and display all triggered alerts."""
    if len(watchlist) == 0:
        print("The watchlist is empty.")
        return

    alert_count = 0
    print("\n--- Alerts ---")
    for investment in watchlist:
        status = check_threshold(investment)
        if status != "OK":
            print(build_alert_message(investment, status))
            alert_count = alert_count + 1

    if alert_count == 0:
        print("No thresholds have been reached.")
    else:
        print("Total alerts: " + str(alert_count))


def display_watchlist(watchlist):
    """Show every investment in a formatted table."""
    if len(watchlist) == 0:
        print("The watchlist is empty.")
        return

    print("\n--- Watchlist ---")
    print("SYMBOL     PRICE      LOWER      UPPER      STATUS")
    for investment in watchlist:
        symbol = investment["symbol"].ljust(10)
        price = ("$" + format(investment["current_price"], ".2f")).ljust(10)
        lower = ("$" + format(investment["lower_limit"], ".2f")).ljust(10)
        upper = ("$" + format(investment["upper_limit"], ".2f")).ljust(10)
        status = check_threshold(investment)
        print(symbol + " " + price + " " + lower + " " + upper + " " + status)


def display_menu():
    """Print the list of choices."""
    print("\n=========================================")
    print("   INVESTMENT THRESHOLD TRACKER")
    print("=========================================")
    print("1. View watchlist")
    print("2. Add an investment")
    print("3. Update a price")
    print("4. Remove an investment")
    print("5. Check all alerts")
    print("6. Save and exit")


def main():
    """Run the program until the user chooses to exit."""
    watchlist = load_watchlist(DATA_FILE)
    running = True

    while running:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            display_watchlist(watchlist)
        elif choice == "2":
            add_investment(watchlist)
        elif choice == "3":
            update_price(watchlist)
        elif choice == "4":
            remove_investment(watchlist)
        elif choice == "5":
            check_all_alerts(watchlist)
        elif choice == "6":
            save_watchlist(DATA_FILE, watchlist)
            print("Goodbye.")
            running = False
        else:
            print("Please enter a number from 1 to 6.")


main()