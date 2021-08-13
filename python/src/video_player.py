"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._now_playing = None
        self._paused = False
        self.playlists = {}

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        all_videos = [
            f"{vid._title} ({vid._video_id}) [{' '.join(vid._tags)}]" for vid in self._video_library.get_all_videos()]
        all_videos.sort()

        print("Here's a list of all available videos:")
        for entry in all_videos:
            print(" " + entry)

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        all_ids = dict([(vid._video_id, vid._title)
                       for vid in self._video_library.get_all_videos()])
        if video_id not in all_ids:
            print("Cannot play video: Video does not exist")
        else:
            if (self._now_playing != None):
                self.stop_video()
            print(f"Playing video: {all_ids[video_id]}")
            self._now_playing = video_id

    def stop_video(self):
        """Stops the current video."""
        if (self._now_playing == None):
            print("Cannot stop video: No video is currently playing")
        else:
            print(
                f"Stopping video: {self._video_library.get_video(self._now_playing)._title}")
            self._now_playing = None
            self._paused = False

    def play_random_video(self):
        """Plays a random video from the video library."""
        all_ids = dict([(vid._video_id, vid._title)
                       for vid in self._video_library.get_all_videos()])
        if (self._now_playing != None):
            self.stop_video()
        vid_id = random.choice(list(all_ids.keys()))
        print(f"Playing video: {all_ids[vid_id]}")
        self._now_playing = vid_id

    def pause_video(self):
        """Pauses the current video."""
        if (self._now_playing == None):
            print("Cannot pause video: No video is currently playing")
        else:
            if self._paused:
                print(
                    f"Video already paused: {self._video_library.get_video(self._now_playing)._title}")
            else:
                print(
                    f"Pausing video: {self._video_library.get_video(self._now_playing)._title}")
                self._paused = True

    def continue_video(self):
        """Resumes playing the current video."""
        if (self._now_playing == None):
            print("Cannot continue video: No video is currently playing")
        else:
            if self._paused == False:
                print(f"Cannot continue video: Video is not paused")
            else:
                print(
                    f"Continuing video: {self._video_library.get_video(self._now_playing)._title}")
                self._paused = False

    def show_playing(self):
        """Displays video currently playing."""
        if self._now_playing == None:
            print("No video is currently playing")
        else:
            vid = self._video_library.get_video(self._now_playing)
            playing = f"{vid._title} ({vid._video_id}) [{' '.join(vid._tags)}]"
            if self._paused:
                playing = playing + " - PAUSED"
            print(f"Currently playing: {playing}")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.upper() in self.playlists:
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            self.playlists[playlist_name.upper()] = Playlist(playlist_name)
            print(f"Successfully created new playlist: {playlist_name}")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        if playlist_name.upper() not in self.playlists:
            print(
                f"Cannot add video to {playlist_name}: Playlist does not exist")
        else:
            vid = self._video_library.get_video(video_id)
            if vid == None:
                print(
                    f"Cannot add video to {playlist_name}: Video does not exist")
            else:
                pl = self.playlists[playlist_name.upper()]
                if pl.videos.get(video_id, None) != None:
                    print(
                        f"Cannot add video to {playlist_name}: Video already added")
                else:
                    pl.add_vid(video_id, vid)
                    print(f"Added video to {playlist_name}: {vid._title}")

    def show_all_playlists(self):
        """Display all playlists."""
        if not self.playlists:
            print("No playlists exist yet")
        else:
            ks = list(self.playlists.keys())
            ks.sort()
            print("Showing all playlists:")
            for k in ks:
                print(f" {self.playlists[k].name}")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
