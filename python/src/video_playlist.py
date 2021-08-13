"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""

    def __init__(self, playlist_name):
        self.name = playlist_name
        self.videos = {}

    def add_vid(self, vid_id, vid):  # Do I need 'vid' here?
        self.videos[vid_id] = vid
