from abc import *
class Company(ABC):
    @abstractmethod
    def cal_leaves(self):
        pass