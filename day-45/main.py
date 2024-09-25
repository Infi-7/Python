from fileinput import close
from http.client import responses
from weakref import finalize

import requests
from bs4 import BeautifulSoup
'''
# access site
response_getter = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response_data = response_getter.text

# scrape
soup = BeautifulSoup(response_data, "html.parser")

# print(soup.find(name="h3").getText())
movie_data = soup.find_all(name="h3")
movie_names = []

for x in movie_data:
    movie_names.append(x.getText())
'''
temp_lst = ['100) Stand By Me', '99) Raging Bull', '98) Amelie', '97) Titanic', '96) Good Will Hunting', '95) Arrival', '94) Lost In Translation', '93) The Princess Bride', '92) The Terminator', '91) The Prestige', '90) No Country For Old Men', '89) Shaun Of The Dead', '88) The Exorcist', '87) Predator', '86) Indiana Jones And The Last Crusade', '85) LÃ©on', '84) Rocky', '83) True Romance', '82) Some Like It Hot', '81) The Social Network', '15) Spirited Away', '79) Captain America: Civil War', '78) Oldboy', '77) Toy Story', '76) A Clockwork Orange', '75) Fargo', '74) Mulholland Dr.', '73) Seven Samurai', '72) Rear Window', '71) Hot Fuzz', '70) The Lion King', "69) Singin' In The Rain", '68) Ghostbusters', '67) Memento', '66) Return Of The Jedi', '65) Avengers Assemble', '64) L.A. Confidential', '63) Donnie Darko', '62) La La Land', '61) Forrest Gump', '60) American Beauty', '59) E.T. â\x80\x93 The Extra Terrestrial', '58) Inglourious Basterds', '57) Whiplash', '56) Reservoir Dogs', "55) Pan's Labyrinth", '54) Vertigo', '53) Psycho', '52) Once Upon A Time In The West', "51) It's A Wonderful Life", '50) Lawrence Of Arabia', '49) Trainspotting', '48) The Silence Of The Lambs', '47) Interstellar', '46) Citizen Kane', '45) Drive', '44) Gladiator', "43) One Flew Over The Cuckoo's Nest", '42) There Will Be Blood', '41) Eternal Sunshine Of The Spotless Mind', '40) 12 Angry Men', '39) Saving Private Ryan', '38) Mad Max: Fury Road', '37) The Thing', '36) The Departed', '35) The Shining', '34) Guardians Of The Galaxy', "33) Schindler's List", '32) The Usual Suspects', '31) Taxi Driver', '30) Seven', '29) The Big Lebowski', '28) Casablanca', '27) The Good, The Bad And The Ugly', '26) Heat', '25) Terminator 2: Judgment Day', '24) The Matrix', '23) The Lord Of The Rings: The Two Towers', '22) Apocalypse Now', '21) 2001: A Space Odyssey', '20) Die Hard', '19) Jurassic Park', '18) Inception', '17) Fight Club', '16) The Lord Of The Rings: The Return Of The King', '15) Aliens', '14) Alien', '13) Blade Runner', '12: The Godfather Part II', '11) Back To The Future', '10) The Lord Of The Rings: The Fellowship Of The Ring', '9) Star Wars', '8) Jaws', '7) Raiders Of The Lost Ark', '6) Goodfellas', '5) Pulp Fiction', '4) The Shawshank Redemption', '3) The Dark Knight', '2) The Empire Strikes Back', '1) The Godfather']
name_only_lst = []
final_op = {}
for x in temp_lst:
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
    close()
finally:
    with open(file="Top_100_movies.txt", mode="a") as f:
        for x in range(1, len(final_op) + 1):
            f.write(f"{x}. {final_op[x]}\n")
splay