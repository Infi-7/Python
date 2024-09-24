from bs4 import BeautifulSoup
# import lxml

with open(file="website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title.string)

all_anchor_tags = soup.find_all(name="a")
for tag in all_anchor_tags:
    print(tag.getText())
