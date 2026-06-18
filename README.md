# Music Library System - Song Class

## Overview
A comprehensive Python implementation of a Song class designed for music library management. This class provides robust tracking and analytics capabilities for music collections, making it ideal for streaming services and music management applications.

## Features
- **Individual Song Management**: Create songs with name, artist, and genre attributes
- **Global Statistics**: Automatically track:
  - Total number of songs
  - Unique artists
  - Unique genres
  - Genre distribution counts
  - Artist distribution counts
- **Automatic Updates**: All class statistics update automatically when new songs are created
- **Comprehensive Reporting**: Get detailed insights about the entire song collection

## Class Architecture

### Attributes
**Instance Attributes:**
- `name` (str): Song title
- `artist` (str): Artist name
- `genre` (str): Musical genre

**Class Attributes:**
- `count` (int): Total number of songs
- `genres` (set): Unique genres in the collection
- `artists` (set): Unique artists in the collection
- `genre_count` (dict): Genre → song count mapping
- `artists_count` (dict): Artist → song count mapping

### Key Methods
- `__init__(name, artist, genre)`: Create a new song and update statistics
- `add_song_to_count()`: Increment total song count
- `add_to_genres(genre)`: Add genre to unique genres set
- `add_to_artists(artist)`: Add artist to unique artists set
- `add_to_genre_count(genre)`: Update genre count
- `add_to_artists_count(artist)`: Update artist count
- `get_song_info()`: Retrieve all global statistics

## Usage Examples

### Creating Songs
```python
from song import Song

# Create songs
song1 = Song("Bohemian Rhapsody", "Queen", "Rock")
song2 = Song("Shape of You", "Ed Sheeran", "Pop")
song3 = Song("Hello", "Adele", "Pop")
Viewing Statistics
python
# Get comprehensive song information
info = Song.get_song_info()
print(f"Total Songs: {info['total_songs']}")
print(f"Genre Count: {info['genre_count']}")
print(f"Artists Count: {info['artists_count']}")
Output Example
text
Total Songs: 3
Genre Count: {'Rock': 1, 'Pop': 2}
Artists Count: {'Queen': 1, 'Ed Sheeran': 1, 'Adele': 1}
Screenshot
https://screenshot.png
Figure 1: Song class implementation and test execution output

Installation & Setup
Clone the repository:

bash
git clone https://github.com/yourusername/music-library-system.git
Navigate to the project directory:

bash
cd music-library-system
Run the test script:

bash
python test_song.py
Best Practices Implemented
Comprehensive docstrings for all methods

Clear code comments explaining logic

Proper use of class methods for global state management

Set data structures for unique value tracking

No duplicate code or unnecessary complexity

Clean, maintainable code structure

Future Enhancements
Add support for multiple artists per song

Implement song search/filter functionality

Add file I/O for persistent storage

Create a REST API for the music library

Add playlist management features

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributors
[Your Name] - Initial implementation

Acknowledgments
MusicTech Innovations for the project opportunity

Python community for excellent documentation and resources

text

## Step 5: Push and Create PR

```bash
# Add all files to staging
git add song.py test_song.py README.md

# Commit changes with a descriptive message
git commit -m "feat: Implement Song class with global tracking capabilities

- Created Song class with comprehensive attributes and methods
- Implemented automatic statistics tracking for songs
- Added test script to demonstrate functionality
- Updated documentation with usage examples and screenshots"

# Push feature branch
git push origin feature/song-class


