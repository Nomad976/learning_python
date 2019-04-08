def make_album(name, title, number=''):
    album = {'artist_name': name, 'album_title': title}
    if number:
        album['number_of_tracks'] = number
    return album
