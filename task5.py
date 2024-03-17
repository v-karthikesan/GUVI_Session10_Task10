class MusicPlayer:
    def __init__(self):
        self.current_song = None
        self.playlist = []

    def add_song_to_playlist(self, song):
        self.playlist.append(song)

    def remove_song_from_playlist(self, song):
        if song in self.playlist:
            self.playlist.remove(song)

    def play_next_song(self):
        if self.playlist:
            self.current_song = self.playlist.pop(0)
            print(f"Playing: {self.current_song}")
        else:
            print("Playlist is empty.")

    def display_playlist(self):
        print("Playlist:")
        for i, song in enumerate(self.playlist, 1):
            print(f"{i}. {song}")

# Test the MusicPlayer class
player = MusicPlayer()
player.add_song_to_playlist("Song 1")
player.add_song_to_playlist("Song 2")
player.add_song_to_playlist("Song 3")
player.display_playlist()
player.play_next_song()
player.remove_song_from_playlist("Song 2")
player.display_playlist()
player.play_next_song()

