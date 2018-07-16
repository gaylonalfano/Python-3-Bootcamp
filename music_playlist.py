# Creating a playlist for iTunes
playlist_properties = ['Playlist Title', 'Playlist Author', 'Track', 'Song Title', 'Artist',
                       'Album', 'Date Added', 'Duration']

playlist = dict.fromkeys(playlist_properties, None)  # Creating empty playlist with defaults

song1 = playlist.copy()
print(song1.values())
song1_values = ['PTitle', 'PAuthor', '#2', 'Le Mer', 'Olafur Arnolds', 'Album', 5/29/1981, 3.2]
song1.values() = song1_values
