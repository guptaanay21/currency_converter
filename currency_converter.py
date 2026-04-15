import requests

BASE_URL = "https://api.exchangerate-api.com/v4/latest/"


def get_currencies():
    try:
        response = requests.get(BASE_URL + "USD")
        data = response.json()
        return list(data["rates"].keys())
    except:
        print("Error fetching currencies.")
        return []


def print_currencies(currencies):
    print("\nAvailable currencies:")
    for cur in currencies:
        print(cur, end=" ")
    print()


def get_rate(base, target):
    try:
        response = requests.get(BASE_URL + base)
        data = response.json()

        if "rates" not in data:
            print("Invalid base currency.")
            return None

        rate = data["rates"].get(target)

        if rate is None:
            print("Invalid target currency.")
            return None

        return rate

    except:
        print("Error fetching exchange rate.")
        return None


def convert(base, target, amount):
    rate = get_rate(base, target)

    if rate is None:
        return

    try:
        amount = float(amount)
    except:
        print("Invalid amount.")
        return

    result = rate * amount
    print(f"{amount} {base} = {result} {target}")


def main():
    print(" Currency Converter (Working Version)")
    print("Commands: list | convert | rate | q")

    currencies = get_currencies()

    while True:
        cmd = input("\nEnter command: ").lower()

        if cmd == "q":
            print("Goodbye!")
            break

        elif cmd == "list":
            print_currencies(currencies)

        elif cmd == "rate":
            base = input("Base currency: ").upper()
            target = input("Target currency: ").upper()

            rate = get_rate(base, target)
            if rate:
                print(f"{base} -> {target} = {rate}")

        elif cmd == "convert":
            base = input("Base currency: ").upper()
            amount = input(f"Amount in {base}: ")
            target = input("Convert to: ").upper()

            convert(base, target, amount)

        else:
            print("Invalid command!")


if __name__ == "__main__":
    main()