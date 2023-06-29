import os
import shutil
from vtt_to_srt.vtt_to_srt import ConvertDirectories
from yt_concate.settings import DOWNLOADS_DIR
from yt_concate.settings import VIDEOS_DIR
from yt_concate.settings import CAPTIONS_DIR

class Utils:
    def __init__(self):
        pass

    def creat_dirs(self):
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)

    @staticmethod
    def convert_vtt_to_srt():
        recursive = False
        convert_file = ConvertDirectories('.', recursive, "utf-8")
        convert_file.convert()

    @staticmethod
    def move_srt_files():
        files = [f for f in os.listdir() if '.srt' in f.lower()]
        for file in files:
            new_path = os.path.join(CAPTIONS_DIR, file + '.txt')
            shutil.move(file, new_path)

    @staticmethod
    def remove_vtt():
        vtts = [f for f in os.listdir() if '.vtt' in f.lower()]
        for vtt in vtts:
            os.remove(vtt)
        print("All vtt Files Deleted successfully")

    @staticmethod
    def get_video_list_filepath(channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + '.txt')

    def caption_file_exists(self, yt):
        filepath = yt.caption_filepath
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0

    def video_file_exists(self, yt):
        filepath = yt.video_filepath
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0

    def video_list_file_exists(self, channel_id):
        path = self.get_video_list_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0
