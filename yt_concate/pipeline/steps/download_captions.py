# from pytube import YouTube
# 錯誤訊息：AttributeError: 'NoneType' object has no attribute 'generate_srt_captions'
import yt_dlp
import time
from .step import Step
from .step import StepException


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        ydl_opts = {
            'writesubtitles': True,
            'writeautomaticsub': True,
            'skip_download': True,
            'subtitleslangs': ['en'],
            'outtmpl': '%(id)s',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            for yt in data:
                print('downloading caption for', yt.id)
                if utils.caption_file_exists(yt):
                    print('found existing caption file')
                    continue
                ydl.download([yt.url])
                # try:
                #
                # except Warning:
                #     print('WARNING was raised when downloading', yt.url)
                #     continue
            utils.convert_vtt_to_srt()
            utils.move_srt_files()
            utils.remove_vtt()
        end = time.time()
        print('took', end - start, 'seconds')

        return data

    # For pytube
    # 錯誤訊息：AttributeError: 'NoneType' object has no attribute 'generate_srt_captions'
    # def process(self, data, inputs):
    #     # download the package by:  pip install pytube
    #     for url in data:
    #         source = YouTube(url)
    #         en_caption = source.captions.get_by_language_code('a.en')
    #         en_caption_convert_to_srt = (en_caption.generate_srt_captions())
    #         print(en_caption_convert_to_srt)
    #         # save the caption to a file named Output.txt
    #         text_file = open("Output.txt", "w")
    #         text_file.write(en_caption_convert_to_srt)
    #         text_file.close()
    #         break
