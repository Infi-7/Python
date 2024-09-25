import requests
from bs4 import BeautifulSoup

# variables
movie_names = []
name_only_lst = []
final_op = {}

# access site
response_getter = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response_data = response_getter.text

# scraping and data rearrangement
soup = BeautifulSoup(response_data, "html.parser")

movie_data = soup.find_all(name="h3")

for x in movie_data:
    movie_names.append(x.getText())

for x in movie_names:
    final = x.split()[1:]
    name_only_lst.append(' '.join(str(x) for x in final))

start = 100
for y in range(len(name_only_lst)):
    final_op[start - y] = name_only_lst[y]

# file error handling
try:
    with open(file="Top_100_movies.txt") as f:
        f.read()
except FileNotFoundError:
    open(file="Top_100_movies.txt", mode="x")
finally:
    with open(file="Top_100_movies.txt", mode="a") as f:
        for x in range(1, len(final_op) + 1):
            f.write(f"{x}. {final_op[x]}\n")
