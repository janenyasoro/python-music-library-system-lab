# lib/song.py
class Song:
    """
    A class to represent a song in the music library system.
    
    This class encapsulates song properties and maintains global insights
    about the entire song collection, including tracking artists, genres,
    and statistical counts.
    """
    
    # Class attributes to track global song data
    count = 0  # Total number of songs created
    genres = set()  # Unique genres across all songs
    artists = set()  # Unique artists across all songs
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
        
        # Trigger class methods to update global statistics
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)
    
    @classmethod
    def add_song_to_count(cls):
        """
        Increment the total song count by one.
        
        This method is called automatically when a new song is created.
        """
        cls.count += 1
    
    @classmethod
    def add_to_genres(cls, genre):
        """
        Add a new genre to the global genres set if it doesn't already exist.
        
        Ensures only unique genres are stored in the collection.
        
        Args:
            genre (str): The genre to add
        """
        cls.genres.add(genre)  # Set automatically handles duplicates
    
    @classmethod
    def add_to_artists(cls, artist):
        """
        Add a new artist to the global artists set if they don't already exist.
        
        Ensures only unique artists are stored in the collection.
        
        Args:
            artist (str): The artist to add
        """
        cls.artists.add(artist)  # Set automatically handles duplicates
    
    @classmethod
    def add_to_genre_count(cls, genre):
        """
        Update the genre count dictionary.
        
        Increments the count for the given genre by 1. If the genre doesn't
        exist in the dictionary, it's added with a count of 1.
        
        Args:
            genre (str): The genre to update in the count
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
        
        Args:
            artist (str): The artist to update in the count
        """
        if artist in cls.artists_count:
            cls.artists_count[artist] += 1
        else:
            cls.artists_count[artist] = 1
    
    @classmethod
    def get_song_info(cls):
        """
        Get comprehensive information about all songs in the library.
        
        Returns:
            dict: A dictionary containing all global statistics including:
                - total_songs: Total count of songs
                - unique_genres: List of all unique genres
                - unique_artists: List of all unique artists
                - genre_count: Dictionary of genre counts
                - artists_count: Dictionary of artist counts
        """
        return {
            'total_songs': cls.count,
            'unique_genres': sorted(list(cls.genres)),
            'unique_artists': sorted(list(cls.artists)),
            'genre_count': dict(sorted(cls.genre_count.items())),
            'artists_count': dict(sorted(cls.artists_count.items()))
        }
    
    def __str__(self):
        """String representation of a Song instance."""
        return f"'{self.name}' by {self.artist} ({self.genre})"
    
    def __repr__(self):
        """Developer-friendly representation of a Song instance."""
        return f"Song(name='{self.name}', artist='{self.artist}', genre='{self.genre}')"