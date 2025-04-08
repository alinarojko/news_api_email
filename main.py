import requests
from send_email import send_email

topic = "tesla"

api_key = "aaba35adaafc41ea9a07556d6f57ae58"
url = "https://newsapi.org/v2/everything?" \
       f"q={topic}&" \
       "from=2025-03-08&" \
       "sortBy=publishedAt&" \
       "apiKey=aaba35adaafc41ea9a07556d6f57ae58&language=ru"

# Make request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

# Accsess the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" \
                + article["description"] + \
                "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)