# lib/song.py

class Song:
    """
 A class to represent a song in the music library system.
    """
  
    # Class attributes to track global song data
    count = 0  # Total number of songs created
    genres = []  # List of unique genres across all songs
    artists = []  # List of unique artists across all songs
    genre_count = {}  # Dictionary mapping genre -> number of songs
    artists_count = {}  # Dictionary mapping artist -> number of songs
    
    def __init__(self, name, artist, genre):
        """
        Initialize a new Song instance.
        
        Args:
            name (str): The name/title of the song
            artist (str): The artist who performed the song
            genre (str): The musical genre of the song
        """
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # These methods must be called manually in tests
        # but we'll also call them automatically for convenience
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)
    
    @classmethod
    def add_song_to_count(cls):
        """Increment the total song count by one."""
        cls.count += 1
    
    @classmethod
    def add_to_genres(cls, genre):
        """
        Add a new genre to the global genres list if it doesn't already exist.
        Ensures only unique genres are stored.
        """
        if genre not in cls.genres:
            cls.genres.append(genre)
    
    @classmethod
    def add_to_artists(cls, artist):
        """
        Add a new artist to the global artists list if they don't already exist.
        Ensures only unique artists are stored.
        """
        if artist not in cls.artists:
            cls.artists.append(artist)
    
    @classmethod
    def add_to_genre_count(cls, genre):
        """
    Update the genre count dictionary.
    Increments the count for the given genre by 1. If the genre doesn't
    exist in the dictionary, it's added with a count of 1.
        """
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
    
    @classmethod
    def add_to_artists_count(cls, artist):
        """
    Update the artist count dictionary.
    Increments the count for the given artist by 1. If the artist doesn't
    exist in the dictionary, they're added with a count of 1.
        """
        if artist in cls.artists_count:
            cls.artists_count[artist] += 1
        else:
         cls.artists_count[artist] = 1