import yt_dlp
from .step import Step
from yt_concate.settings import VIDEOS_DIR


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        # 避免重複下載
        yt_set = set([found.yt for found in data])
        print('video to download= ', len(yt_set))

        ydl_opts = {
            'format': 'mp4/bestvideo/best',
            'outtmpl': VIDEOS_DIR + '/%(id)s' + '.mp4',
        }
        for yt in yt_set:
            url = yt.url
            if utils.video_file_exists(yt):
                print(f'found existing video file for {url}, skipping')
                continue
            print('downloading', url)
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        return data
    