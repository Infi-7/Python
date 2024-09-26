import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

# Variables
h3_list = []
final_list = []
song_urls_list = []
filter_extra = ['Songwriter(s):', 'Producer(s):', 'Imprint/Promotion Label:', 'Gains in Weekly Performance', 'Additional Awards']
spotipy_endpoint = "https://api.spotify.com/authorize"

# .env File Execution
load_dotenv()

SPOTIFY_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIFY_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIFY_URL = os.getenv('SPOTIPY_REDIRECT_URI')


# User input
user_input = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# requesting data from website
response = requests.get(f"https://www.billboard.com/charts/hot-100/{user_input}/#")
entries = response.text

# Scraping
soup = BeautifulSoup(entries, "html.parser")
h3_finder = soup.find_all(name="h3")

for h3 in h3_finder:
    value = h3.getText().strip()
    if value in filter_extra:
        continue
    else:
        h3_list.append(value)
print(h3_list)

# temp_list replace with h3_list
# temp_list = ['I Had Some Help', 'I Had Some Help', 'A Bar Song (Tipsy)', 'Not Like Us', 'Espresso', 'Please Please Please', 'Million Dollar Baby', 'Too Sweet', 'Beautiful Things', 'Lose Control', 'Birds Of A Feather', 'Good Luck, Babe!', 'Pour Me A Drink', 'Pink Skies', 'Like That', 'Cowgirls', 'Houdini', 'Fortnight', 'Saturn', 'Austin', 'I Remember Everything', 'Whiskey Whiskey', 'Feather', "We Can't Be Friends (Wait For Your Love)", 'Miles On It', 'Lunch', 'Wanna Be', 'Lovin On Me', 'High Road', 'The Boy Is Mine', 'Stick Season', 'I Am Not Okay', 'Yeah Glo!', 'Gata Only', 'Si Antes Te Hubiera Conocido', 'Devil Is A Lie', 'Us.', "Ain't No Love In Oklahoma", 'Hot To Go!', 'BAND4BAND', 'End Of Beginning', 'Slow It Down', 'Get It Sexyy', 'Where It Ends', 'Euphoria', 'Bulletproof', 'Red Wine Supernova', 'TGIF', 'Greedy', 'Stargazing', 'I Can Do It With A Broken Heart', 'Dirt Cheap', 'Whatever She Wants', 'You Look Like You Love Me', 'Chihiro', 'Type Shit', 'One Of Wun', 'Parking Lot', 'I Like The Way You Kiss Me', 'Illusion', 'Close To You', 'Nasty', 'We Ride', 'Girl, So Confusing', 'Sweet Dreams', "Wind Up Missin' You", 'Pink Pony Club', 'U My Everything', 'Down Bad', 'Reloj', 'Kehlani', 'Remember Him That Way', 'After Hours', 'Si No Quieres No', 'Scared To Start', 'Wildflower', 'Nights Like This', 'Wine Into Whiskey', 'The Door', '360', "Think I'm In Love With You", 'feelslikeimfallinginlove', 'Casual', 'Beautiful As You', "L'amour De Ma Vie", 'Let Your Boys Be Country', "Who's Afraid Of Little Old Me?", 'Halfway To Hell', 'Belong Together', 'Hang Tight Honey', "Texas Hold 'Em", 'Vino Tinto', "We Don't Fight Anymore", 'Hell N Back', 'Risk', 'Chevrolet', 'The Man He Sees In Me', 'Brother Stone', 'Guilty As Sin?', 'La Patrulla', 'Bandit', "Hollywood Can’t Ditch Its Teslas Fast Enough: “They're Destroying Their Leases and Walking Away”", 'Diddy’s Frantic Text To Cassie After Hotel Assault Read Aloud During Bail Appeal', 'Archaeologists Solve Mystery Behind Black Tombstone Found in Jamestown Carrying an English Knight', 'Morbid Royal Rule Set to ‘Separate’ Prince George & Princess Charlotte Next Year', 'ABC, CNN and National Geographic Among Top Winners at 2024 News Emmys', 'Diddy And Kim Porter’s Kids Break Silence, Dismiss Al B Sure!’s Call For Investigation Into Her\xa0Death', 'Rare Diamond Neglige Necklace Linked to Marie Antoinette’s Downfall and French Revolution Comes to Sotheby’s\xa0Auction', 'Celtics’ Jaylen Brown Launches Shoe Brand After Nike\xa0Spat', 'St. Vincent Says Her Spanish Album Was an ‘Escape Hatch to More Joy’', 'Follow Us', 'Have a Tip?', 'The Daily', 'Have a Tip?', 'Account', 'Charts\n\n\n\n\t\t\t\t\tExpand charts menu', 'Music\n\n\n\n\t\t\t\t\tExpand music menu', 'Videos\n\n\n\n\t\t\t\t\tExpand videos menu', 'Culture\n\n\n\n\t\t\t\t\tExpand culture menu', 'Media\n\n\n\n\t\t\t\t\tExpand media menu', 'Business\n\n\n\n\t\t\t\t\tExpand business menu', 'Pro Tools\n\n\n\n\t\t\t\t\tExpand pro-tools menu', 'Billboard Español\n\n\n\n\t\t\t\t\tExpand billboard-espanol menu', 'Get Up Anthems by Tres\n\n\n\n\t\t\t\t\tExpand get-up-anthems-by-tres menu', 'Honda Music\n\n\n\n\t\t\t\t\tExpand honda-music menu', '', '']
for x in range(1, len(h3_list)):
    if x < 101:
        final_list.append(h3_list[x])
    else:
        break


# spotipy to spotify connections
scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_ID,
                                               client_secret=SPOTIFY_SECRET,
                                               redirect_uri=SPOTIFY_URL,
                                               show_dialog=True,
                                               cache_path=".cache",
                                               scope=scope))
user_id = sp.current_user()["id"]

for x in final_list:
    results = sp.search(q=f"{x}", limit=1, type="track")
    song_urls = results['tracks']['items'][0]['uri']
    song_urls_list.append(song_urls)


custom_playlist = input("Enter the name of your playlist: ")

playlist = sp.user_playlist_create(user=user_id, name=f"{custom_playlist} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_urls_list)
