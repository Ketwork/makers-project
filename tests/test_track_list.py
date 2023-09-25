from lib.track_list import TrackList
import pytest

"""
Initially there are no tracks
"""
def test_initially_has_no_tracks():
    track_list = TrackList()
    assert track_list.list_tracks() == []

"""
When a song is added
it is reflected in the list of tracks
"""
def test_add_song_reflected_in_track_list():
    track_list = TrackList()
    track_list.add("Sunny Day - Brandy")
    assert track_list.list_tracks() == ["Sunny Day - Brandy"]

"""
When multiple songs are added
they are all reflected in the list of tracks
"""
def test_add_multiple_tracks():
    track_list = TrackList()
    track_list.add("Sunny Day - Brandy")
    track_list.add("Cloudy Day - Brandy")
    track_list.add("Windy Day - Brandy")
    assert track_list.list_tracks() == ["Sunny Day - Brandy", "Cloudy Day - Brandy", "Windy Day - Brandy"]

"""
When an empty string is added
it will give us an error
"""
def test_error_on_empty_string():
    track_list = TrackList()
    with pytest.raises(Exception) as err:
        track_list.add("")
    assert str(err.value) == "Entry must contain song"