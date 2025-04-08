import requests
from send_email import send_email

api_key = "5f9d1f4deecd4a988acefbf32c2d0ed4"
url = ("https://newsapi.org/v2/everything?q=tesla&"\
       "from=2025-03-07&sortBy=publishedAt&apiKey="\
       "5f9d1f4deecd4a988acefbf32c2d0ed4")

# Make request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

# Accsess the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)