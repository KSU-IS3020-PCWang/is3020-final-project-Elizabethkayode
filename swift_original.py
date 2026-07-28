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


    #elizabeth
