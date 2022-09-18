def make_album(artist_name, title):
    """returning dictonary of information of artist"""
    artist = {
        'first ': artist_name,
        'last ': title,
        }
    return artist

musician = make_album('Abhishek', 'singer')
print(musician)
while True:
    print("\n please tell me your name")
    print("(enter 'q' at any time to quit)")
    
    artist_name = input("first ")
    if artist_name == 'q':
        break
    title = input("last ")
    if title == 'q':
        break

message = make_album('abhi ', 'singer ')