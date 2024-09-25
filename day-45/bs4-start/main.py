from http.client import responses

from bs4 import BeautifulSoup
# import lxml
import requests

'''
with open(file="website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title.string)

all_anchor_tags = soup.find_all(name="a")
for tag in all_anchor_tags:
    print(tag.getText())
'''


response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
articles_text = []
articles_links = []

for article in articles:
    text  = article.getText()
    articles_text.append(text)

    link = article.get("href")
    articles_links.append(link)


article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

max_index = article_upvote.index(max(article_upvote))

print(articles_text[max_index])
print(articles_links[max_index])
print(article_upvote[max_index])
