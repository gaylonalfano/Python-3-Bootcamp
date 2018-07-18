# Creating a playlist for iTunes
# I believe the best way is to have a DICT represent the playlist (pl_title, pl_author, songs[list of dicts], etc)
# But the songs will be a LIST of DICT with all the song properties
from typing import Dict, List, Union

playlist_properties = ['Playlist Title', 'Playlist Author', 'Songs']

playlist = dict.fromkeys(playlist_properties, None)  # Creating empty playlist with defaults

song1 = playlist.copy()
print(song1.values())
song1_values = ['PTitle', 'PAuthor', '#2', 'Le Mer', 'Olafur Arnolds', 'Album', 5/29/1981, 3.2]
# song1.values() = song1_values
# ??? How to loop through a list of song properties and add them to another dictionary?
# for key, i in playlist.keys() and range(len(song1_values)):
#     playlist[key] = song1_values[i]
# print(playlist)

print(playlist)

print(song1)

print(song1_values[0])

# Below won't work since .fromkeys() matches k-v pairs. V will result in list so no good.
# song2 = dict.fromkeys(playlist_properties, [i for i in song1_values])
# print(f'Song 2: {song2}')

print([i for i in song1_values])
print([song1_values[n] for n in range(len(song1_values))])

# Can you create a list that contains multiple dictionaries???
# Can you loop over the properties of a single song and add those properties to a dictionary? YES!

song1 = {
    'Track': 1,
    'Song Title': 'La Mer',
    'Artist': 'Olafur Arnolds',
    'Album': 'Heat Soundtrack',
    'Date Added': 5/29/1981,
    'Duration': 3.2
}

song2 = {
    'Track': 2,
    'Song Title': 'First Snow',
    'Artist': 'Clint Mansell',
    'Album': 'The Fountain Soundtrack',
    'Date Added': 5/29/2018,
    'Duration': 4
}
songs: List[Dict[str, Union[int, str, float]]] = [song1, song2]
print(songs)

# Wait, should playlist be a LIST of DICT instead? With each D representing a unique song or vice versa?
# Or should it be a DICT of DICT? Ex. {'Playlist Title': , 'Playlist Author': , Songs: [dict1, dict2, etc.]}??
playlist = {
    'Playlist Title': 'My First Playlist',
    'Playlist Author': 'Gaylon',
    'Songs': songs
}
print(playlist)

### Above is my attempt; Below is instructor's
# playlist = pl
pl = {
    'title': 'patagonia bus',
    'author': 'colt steele',
    'songs': [
        {'title': 'song1', 'artist': ['blue'], 'duration': 2.5},
        {'title': 'song2', 'artist': ['kitty', 'djcat'], 'duration': 5.6},
        {'title': 'meowmeow', 'artist': ['garfield'], 'duration': 2.0}
    ]
}
print(pl)

# How to calc the total length of the playlist?
pl_duration = 0
for song in pl['songs']:
    pl_duration += song['duration']
print(f'Total playlist duration: {pl_duration} minutes')

