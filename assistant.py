from weather import get_weather
from currency import convert_currency
from news import get_news
from utils import print_line

while True:
    print_line()
    user = input("You: ").lower()

    if user == "exit":
        print("Assistant: Goodbye!")
        break

    elif "weather" in user:
        city = input("Enter city: ")
        print("Assistant:", get_weather(city))

    elif "convert" in user:
        from_currency = input("From: ")
        to_currency = input("To: ")
        amount = float(input("Amount: "))

        result = convert_currency(
            from_currency,
            to_currency,
            amount
        )

        print("Assistant:", result)

    elif "news" in user:
        articles = get_news()

        print("Assistant: Latest News")
        for article in articles:
            print("-", article)

    else:
        print(
            "Assistant: I can help with "
            "weather, currency and news."
        )
