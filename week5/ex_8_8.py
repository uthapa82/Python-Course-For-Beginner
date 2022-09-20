def make_album(artist_name, title, tracks=""):
    """returning dictonary of information of artist"""
    artist_dict = {
        'artist': artist_name.title(),
        'title': title.title(),
        }
    if tracks:
        artist_dict['tracks'] = tracks

    return artist_dict

while True:
    print("\n please tell me the name of the song ")
    print("\n who is the artist ")
    print("(enter 'q' at any time to quit)")
    
    artist_name = input("artist ")
    if artist_name == 'q':
        break
    title = input("song name ")
    if title == 'q':
        break

    artist = make_album(artist_name, title)
    print(artist)