import requests

api_key = "5f9d1f4deecd4a988acefbf32c2d0ed4"
url = ("https://newsapi.org/v2/everything?q=tesla&"\
       "from=2025-03-07&sortBy=publishedAt&apiKey="\
       "5f9d1f4deecd4a988acefbf32c2d0ed4")

# Make request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

# Accsess the article titles and description
for article in content["articles"]:
    print(article["title"])