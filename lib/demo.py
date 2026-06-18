# lib/demo.py

from song import Song

def run_demo():
    """Run a demonstration of the Song class functionality."""
    
    print("=" * 60)
    print("MUSIC LIBRARY SYSTEM DEMO")
    print("=" * 60)
    
    # Create some songs
    print("\n📀 Creating songs...")
    songs = [
        ("Bohemian Rhapsody", "Queen", "Rock"),
        ("Shape of You", "Ed Sheeran", "Pop"),
        ("Juice", "Lizzo", "Pop"),
        ("Lose Yourself", "Eminem", "Hip Hop"),
        ("Uptown Funk", "Mark Ronson", "Funk"),
        ("Hello", "Adele", "Pop"),
        ("Hotel California", "Eagles", "Rock"),
    ]
    
    for name, artist, genre in songs:
        song = Song(name, artist, genre)
        print(f"   ✓ {song}")
    
    # Display statistics
    print("\n📊 Library Statistics:")
    info = Song.get_song_info()
    
    print(f"\n   Total Songs: {info['total_songs']}")
    
    print(f"\n   🎤 Artists ({len(info['unique_artists'])}):")
    for artist in info['unique_artists']:
        count = info['artists_count'][artist]
        print(f"      • {artist}: {count} song(s)")
    
    print(f"\n   🎵 Genres ({len(info['unique_genres'])}):")
    for genre in info['unique_genres']:
        count = info['genre_count'][genre]
        print(f"      • {genre}: {count} song(s)")
    
    print("\n" + "=" * 60)
    print("✨ Demo completed successfully!")
    print("=" * 60)

if __name__ == "__main__":
    run_demo()