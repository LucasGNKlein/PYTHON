liked_songs = {
    'The Line': "Twenty One Pilots",
    'Lost in The Echo': "Linkin Park",
    'My Songs Know What You Did in The Dark': "Fall Out Boys",
    'Ambiente Errado': "Luan Santana",
    'Me Porto Bonito': "Bad Bunny",
    'Ojitos Lindos': "Bad Bunny",
    'Paradise': "Bazzi",
    'Voodoo Doll': "5 Seconds of Summer",
    'Is There Someone Else': "The Weeknd",
    'How Do I Make You Love Me?': "The Weeknd",
    'Better Now': "Post Malone",
    'Chemical': "Post Malone",
    'Holding On To You': "Twenty One Pilots"
}

def write_liked_songs_to_file(liked_songs, filename):
    with open(filename, "w") as file:
        file.write("Liked Songs:\n")
        for song, artist in liked_songs.items():
            file.write(f' {song} by {artist}\n')
    print(f"Successfully added Liked songs to {filename} ❤️")

write_liked_songs_to_file(liked_songs, "all_time_favourites.txt")
