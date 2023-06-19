from abc import ABC
from abc import abstractmethod


class Step(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def process(self, data, inputs): # 隨著開發專案，再思考需要哪些參數
        pass


class StepException(Exception): # Exception python內建
    pass
