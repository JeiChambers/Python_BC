playlist = {
    'title': 'Slow Grooves',
    'author': 'johnny chambers jr',
    'songs': [
        {'title': 'Really Love', 'artist': ["D'Angelo"], 'duration': 5.44 },
        {'title': 'Stand Still', 'artist': ["Sabrina Claudio"], 'duration': 4.43 },
        {'title': 'Lust for Life', 'artist': ["Lana Del Rey", "The Weeknd"], 'duration': 4.24 }
    ]
}

total_length = 0
for song in playlist['songs']:
    total_length += song['duration']

print(total_length)