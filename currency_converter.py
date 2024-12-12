import requests


def currency_converter():
    # Fetch real-time exchange rates
    url = "https://v6.exchangerate-api.com/v6/your_api_key_here/latest/USD"  # Replace with your API key
    response = requests.get(url)

    # Check if the response was successful
    if response.status_code != 200:
        print(f"Error fetching exchange rates: {response.status_code}")
        return

    try:
        # Attempt to decode JSON response
        data = response.json()
        if data["result"] != "success":
            print("Error: Unable to fetch valid exchange rates.")
            return
    except Exception as e:
        print(f"Error decoding JSON response: {e}")
        return

    currencies = data["conversion_rates"]

    # Show the list of currencies in a compact 7-column grid
    currency_codes = list(currencies.keys())
    print("Available currencies:")

    for i in range(0, len(currency_codes), 7):
        # Print 7 codes per row, aligning them to the left
        print("  ".join(f"{currency_codes[i + j]:<5}" for j in range(7) if i + j < len(currency_codes)))

    # Choose base currency
    base_currency = input("Enter the base currency code (e.g., USD): ").upper()
    if base_currency not in currencies:
        print("Invalid base currency code.")
        return

    # Choose target currency
    target_currency = input(
        f"Enter the target currency code (e.g., INR, current base currency is {base_currency}): ").upper()
    if target_currency not in currencies:
        print("Invalid target currency code.")
        return

    # Ask for amount to convert
    try:
        amount = float(input(f"Enter the amount to convert from {base_currency} to {target_currency}: "))
    except ValueError:
        print("Invalid amount.")
        return

    # Conversion
    base_to_usd = currencies[base_currency]
    target_to_usd = currencies[target_currency]
    converted_amount = (amount / base_to_usd) * target_to_usd

    print(f"\n{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")


currency_converter()
