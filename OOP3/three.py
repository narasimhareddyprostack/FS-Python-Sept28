
from abc import *


class Account(ABC):

    @abstractmethod
    def cal_bal(self):
        pass


Account()
