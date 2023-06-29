from .step import Step
from yt_concate.model.found import Found

class Search(Step):
    def process(self, data, inputs, utils):
        search_word = inputs['search_word']

        found = []
        for yt in data:
            captions = yt.captions
            if not captions:
                continue

            for caption in captions:
                # for caption, time in captions.items() 會降低運算效能
                if search_word in caption:
                    time = captions[caption]
                    f = Found(yt, caption, time)
                    found.append(f)
                    # found.append((yt, caption, time))
                    # append 只能加一個東西，所以用 tuple
        print(len(found)) # 需使用__str__ __repo__，因此建立 found method
        return found