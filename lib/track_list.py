class TrackList:

    def __init__(self):
        self._tracks = []

    def add(self, track):
        if track == "":
            raise Exception("Entry must contain song")
        self._tracks.append(track)

    def list_tracks(self):
        return self._tracks