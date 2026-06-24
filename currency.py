import requests

BASE_URL = "https://open.er-api.com/v6/latest"

def convert_currency(from_currency, to_currency, amount):
    try:
        response = requests.get(
            f"{BASE_URL}/{from_currency.upper()}"
        )

        data = response.json()

        rates = data["rates"]

        rate = rates[to_currency.upper()]

        result = amount * rate

        return (
            f"{amount} {from_currency.upper()} "
            f"= {result:.2f} {to_currency.upper()}"
        )

    except Exception:
        return "Currency conversion failed."
