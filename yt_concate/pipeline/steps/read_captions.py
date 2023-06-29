from .step import Step



class ReadCaption(Step):
    def process(self, data, inputs, utils):
        for yt in data:
            if not utils.caption_file_exists(yt):
                continue

            captions = {}
            with open(yt.caption_filepath, 'r') as f:
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
            yt.captions = captions
        return data
