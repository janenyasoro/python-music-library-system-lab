# lib/testing/song_test.py

import pytest
from lib.song import Song

class TestSong:
    """Test suite for the Song class."""
    
    def setup_method(self):
        """Reset class attributes before each test."""
        Song.count = 0
        Song.genres = set()
        Song.artists = set()
        Song.genre_count = {}
        Song.artists_count = {}
    
    def test_song_creation(self):
        """Test that a Song instance is created with correct attributes."""
        song = Song("Bohemian Rhapsody", "Queen", "Rock")
        
        assert song.name == "Bohemian Rhapsody"
        assert song.artist == "Queen"
        assert song.genre == "Rock"
    
    def test_song_count_increments(self):
        """Test that total song count increments when songs are created."""
        assert Song.count == 0
        
        Song("Song 1", "Artist 1", "Pop")
        assert Song.count == 1
        
        Song("Song 2", "Artist 2", "Rock")
        assert Song.count == 2
        
        Song("Song 3", "Artist 3", "Jazz")
        assert Song.count == 3
    
    def test_add_to_genres_unique(self):
        """Test that only unique genres are stored."""
        assert len(Song.genres) == 0
        
        Song("Song 1", "Artist 1", "Pop")
        assert len(Song.genres) == 1
        assert "Pop" in Song.genres
        
        Song("Song 2", "Artist 2", "Rock")
        assert len(Song.genres) == 2
        assert "Rock" in Song.genres
        
        Song("Song 3", "Artist 3", "Pop")  # Duplicate genre
        assert len(Song.genres) == 2  # Should still be 2
        assert "Pop" in Song.genres
    
    def test_add_to_artists_unique(self):
        """Test that only unique artists are stored."""
        assert len(Song.artists) == 0
        
        Song("Song 1", "Adele", "Pop")
        assert len(Song.artists) == 1
        assert "Adele" in Song.artists
        
        Song("Song 2", "Ed Sheeran", "Pop")
        assert len(Song.artists) == 2
        assert "Ed Sheeran" in Song.artists
        
        Song("Song 3", "Adele", "Soul")  # Duplicate artist
        assert len(Song.artists) == 2  # Should still be 2
        assert "Adele" in Song.artists
    
    def test_genre_count_updates(self):
        """Test that genre counts are updated correctly."""
        assert Song.genre_count == {}
        
        Song("Song 1", "Artist 1", "Pop")
        assert Song.genre_count == {"Pop": 1}
        
        Song("Song 2", "Artist 2", "Rock")
        assert Song.genre_count == {"Pop": 1, "Rock": 1}
        
        Song("Song 3", "Artist 3", "Pop")
        assert Song.genre_count == {"Pop": 2, "Rock": 1}
        
        Song("Song 4", "Artist 4", "Jazz")
        assert Song.genre_count == {"Pop": 2, "Rock": 1, "Jazz": 1}
    
    def test_artists_count_updates(self):
        """Test that artist counts are updated correctly."""
        assert Song.artists_count == {}
        
        Song("Song 1", "Adele", "Pop")
        assert Song.artists_count == {"Adele": 1}
        
        Song("Song 2", "Ed Sheeran", "Pop")
        assert Song.artists_count == {"Adele": 1, "Ed Sheeran": 1}
        
        Song("Song 3", "Adele", "Soul")
        assert Song.artists_count == {"Adele": 2, "Ed Sheeran": 1}
        
        Song("Song 4", "Beyonce", "R&B")
        assert Song.artists_count == {"Adele": 2, "Ed Sheeran": 1, "Beyonce": 1}
    
    def test_multiple_songs_tracking(self):
        """Test comprehensive tracking with multiple songs."""
        # Create multiple songs
        songs_data = [
            ("Bohemian Rhapsody", "Queen", "Rock"),
            ("Shape of You", "Ed Sheeran", "Pop"),
            ("Juice", "Lizzo", "Pop"),
            ("Lose Yourself", "Eminem", "Hip Hop"),
            ("Hello", "Adele", "Pop"),
            ("Hotel California", "Eagles", "Rock"),
        ]
        
        for name, artist, genre in songs_data:
            Song(name, artist, genre)
        
        # Check total count
        assert Song.count == 6
        
        # Check unique genres
        expected_genres = {"Rock", "Pop", "Hip Hop"}
        assert Song.genres == expected_genres
        
        # Check unique artists
        expected_artists = {"Queen", "Ed Sheeran", "Lizzo", "Eminem", "Adele", "Eagles"}
        assert Song.artists == expected_artists
        
        # Check genre counts
        expected_genre_count = {"Rock": 2, "Pop": 3, "Hip Hop": 1}
        assert Song.genre_count == expected_genre_count
        
        # Check artist counts
        expected_artists_count = {
            "Queen": 1,
            "Ed Sheeran": 1,
            "Lizzo": 1,
            "Eminem": 1,
            "Adele": 1,
            "Eagles": 1
        }
        assert Song.artists_count == expected_artists_count
    
    def test_get_song_info(self):
        """Test the get_song_info class method."""
        # Create some songs
        Song("Song 1", "Artist A", "Pop")
        Song("Song 2", "Artist B", "Rock")
        Song("Song 3", "Artist A", "Pop")
        
        info = Song.get_song_info()
        
        assert info['total_songs'] == 3
        assert sorted(info['unique_genres']) == ["Pop", "Rock"]
        assert sorted(info['unique_artists']) == ["Artist A", "Artist B"]
        assert info['genre_count'] == {"Pop": 2, "Rock": 1}
        assert info['artists_count'] == {"Artist A": 2, "Artist B": 1}
    
    def test_string_representation(self):
        """Test the string representation of a Song instance."""
        song = Song("Bohemian Rhapsody", "Queen", "Rock")
        assert str(song) == "'Bohemian Rhapsody' by Queen (Rock)"
    
    def test_repr_representation(self):
        """Test the repr representation of a Song instance."""
        song = Song("Bohemian Rhapsody", "Queen", "Rock")
        expected_repr = "Song(name='Bohemian Rhapsody', artist='Queen', genre='Rock')"
        assert repr(song) == expected_repr