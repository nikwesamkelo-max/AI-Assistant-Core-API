import requests

def get_news():
    url = (
        "https://api.spaceflightnewsapi.net/v4/articles/"
        "?limit=5"
    )

    try:
        response = requests.get(url)
        data = response.json()

        articles = data["results"]

        news_list = []

        for article in articles:
            news_list.append(article["title"])

        return news_list

    except Exception:
        return ["Could not fetch news."]
