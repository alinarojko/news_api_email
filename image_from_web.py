import requests
url = "https://en.wikipedia.org/wiki/Cat#/media/File:Cat_August_2010-4.jpg"
response = requests.get(url)
with open("image_cat.jpg", "wb") as file:
    file.write(response.content)