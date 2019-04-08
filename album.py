from album_function import *

while True:
    print("\nEnter 'q' at any time to quit")
    print("Enter information about the album.")

    artist = input("Artist: ")
    if artist == 'q':
        break

    title = input("Title: ")
    if title == 'q':
        break

    album = make_album(artist, title)
    print(album)
