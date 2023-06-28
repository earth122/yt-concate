import os
from pprint import pprint
from .step import Step
from yt_concate.settings import CAPTIONS_DIR


class ReadCaption(Step):
    def process(self, data, inputs, utils):
        # data = []
        data = {}  # 此處建議註解
        for caption_file in os.listdir(CAPTIONS_DIR):
            captions = {}
            with open(os.path.join(CAPTIONS_DIR, caption_file), 'r') as f:
                # main 所在路徑與caption_file的路徑不同，需要重新調整檔案路徑
                time_line = False
                time = None
                caption = None
                for line in f:
                    line = line.strip()
                    if '-->' in line:
                        time_line = True
                        time = line.strip()
                        continue
                    if time_line:
                        caption = line
                        captions[caption] = time  # 思考要用 caption or time 當 key
                        time_line = False  # reset time_line
            # data.appends(captions) 沒有記錄字幕是出自哪個影片
            data[caption_file] = captions
        pprint(data)
        return data
