def make_album(artist_name, title, tracks=""):
    """returning dictonary of information of artist"""
    artist_dict = {
        'artist': artist_name.title(),
        'title': title.title(),
        }
    if tracks:
        artist_dict['tracks'] = tracks

    return artist_dict

album_0 = make_album('AC/DC', 'highway to hell')
print(album_0)

album_1 = make_album('Anusha', 'poemist')
print(album_1)

album_2= make_album('Anu', 'thapa', tracks = 8)
print(album_2)

