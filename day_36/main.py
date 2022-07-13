import requests
from  datetime import date
import json

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "JWTWN8E1DK0R0QX1"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "ad3dd025f5954c7194791c7423917315"


parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

stock_obj = requests.get(STOCK_ENDPOINT, params=parameters)
stock_obj.raise_for_status()
stock_data = stock_obj.json()

before_day_stock_close, before_2days_stock_close = \
    [float(value["4. close"]) for key, value in stock_data["Time Series (Daily)"].items()][:2]


percent =  round((before_day_stock_close - before_2days_stock_close) / before_2days_stock_close * 100, 2)

percent_str = f"🔺{percent}%" if percent > 0 else f"🔻{abs(percent)}%"

now = date.today()
params = {
    "q": STOCK,
    "from": now.strftime("%Y-%m-%d"),
    "sortBy":"popularity",
    "apikey": NEWS_API_KEY
}
news_obj = requests.get(NEWS_ENDPOINT, params=params)
news_obj.raise_for_status()
news_data = news_obj.json()
needed_article = list(filter(lambda x: "Tesla" in x["title"] or "tesla" in x["title"], news_data["articles"]))[0]

message = f"{STOCK}: {percent_str}\nHeadline: {needed_article['title']}\nBrief: {needed_article['description']}"


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

