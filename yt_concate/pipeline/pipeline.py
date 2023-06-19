from .steps.step import StepException # 示範相對路徑寫法

class Pipeline:
    def __init__(self, steps):
        self.steps = steps
    def run(self, inputs):
        data = None
        for step in self.steps:
            try:
                data = step.process(data, inputs)
            except StepException as e:
                print('Exception happened:', e)
                break

