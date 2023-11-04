from abc import *


class Account(ABC):

    @abstractmethod
    def cal_bal(self):
        pass


a = Account()
print(a)
print(id(a))
