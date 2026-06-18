# lib/testing/song_test.py

import pytest
from lib.song import Song


class TestSong:
    """Test suite for the Song class."""
    
    def setup_method(self):
        """Reset class attributes before each test."""
        Song.count = 0
        Song.genres = []
        Song.artists = []
        Song.genre_count = {}
        Song.artists_count = {}
    
    def test_song_instantiates_with_name_artist_genre(self):
        """Test that a Song instance is created with correct attributes."""
        song = Song("Bohemian Rhapsody", "Queen", "Rock")
        
        assert song.name == "Bohemian Rhapsody"
        assert song.artist == "Queen"
        assert song.genre == "Rock"
    
    def test_song_count_tracks_total_songs(self):
        """Test that total song count increments when songs are created."""
        # Reset count
        Song.count = 0
        
        Song("Song 1", "Artist 1", "Pop")
        assert Song.count == 1
        
        Song("Song 2", "Artist 2", "Rock")
        assert Song.count == 2
        
        Song("Song 3", "Artist 3", "Jazz")
        assert Song.count == 3
    
    def test_song_tracks_all_genres(self):
        """Test that all unique genres are tracked."""
        # Reset genres
        Song.genres = []
        
        Song("Song 1", "Artist 1", "Pop")
        assert "Pop" in Song.genres
        assert len(Song.genres) == 1
        
        Song("Song 2", "Artist 2", "Rock")
        assert "Rock" in Song.genres
        assert len(Song.genres) == 2
        
        Song("Song 3", "Artist 3", "Pop")  # Duplicate genre
        assert len(Song.genres) == 2  # Should still be 2
        assert Song.genres == ["Pop", "Rock"]
    
    def test_song_tracks_all_artists(self):
        """Test that all unique artists are tracked."""
        # Reset artists
        Song.artists = []
        
        Song("Song 1", "Adele", "Pop")
        assert "Adele" in Song.artists
        assert len(Song.artists) == 1
        
        Song("Song 2", "Ed Sheeran", "Pop")
        assert "Ed Sheeran" in Song.artists
        assert len(Song.artists) == 2
        
        Song("Song 3", "Adele", "Soul")  # Duplicate artist
        assert len(Song.artists) == 2  # Should still be 2
        assert Song.artists == ["Adele", "Ed Sheeran"]
    
    def test_song_counts_songs_per_genre(self):
        """Test that genre counts are updated correctly."""
        # Reset genre_count
        Song.genre_count = {}
        
        Song("Song 1", "Artist 1", "Pop")
        assert Song.genre_count["Pop"] == 1

        Song("Song 2", "Artist 2", "Rock")
        assert Song.genre_count["Rock"] == 1
        assert Song.genre_count["Pop"] == 1
        
        Song("Song 3", "Artist 3", "Pop")
        assert Song.genre_count["Pop"] == 2
        assert Song.genre_count["Rock"] == 1
        
        assert Song.genre_count == {"Pop": 2, "Rock": 1}
    
    def test_song_counts_songs_per_artist(self):
        """Test that artist counts are updated correctly."""
        # Reset artists_count
        Song.artists_count = {}
        
        Song("Song 1", "Adele", "Pop")
        assert Song.artists_count["Adele"] == 1
        
        Song("Song 2", "Ed Sheeran", "Pop")
        assert Song.artists_count["Ed Sheeran"] == 1
        assert Song.artists_count["Adele"] == 1
        
        Song("Song 3", "Adele", "Soul")
        assert Song.artists_count["Adele"] == 2
        assert Song.artists_count["Ed Sheeran"] == 1
        
        assert Song.artists_count == {"Adele": 2, "Ed Sheeran": 1}
    
    def test_multiple_songs_comprehensive_tracking(self):
        """Test comprehensive tracking with multiple songs."""
        # Reset all class attributes
        Song.count = 0
        Song.genres = []
        Song.artists = []
        Song.genre_count = {}
        Song.artists_count = {}
        
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
        expected_genres = ["Rock", "Pop", "Hip Hop"]
        assert sorted(Song.genres) == sorted(expected_genres)
        
        # Check unique artists
        expected_artists = ["Queen", "Ed Sheeran", "Lizzo", "Eminem", "Adele", "Eagles"]
        assert sorted(Song.artists) == sorted(expected_artists)
        
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