from abc import ABC, abstractmethod


class test(ABC):
    @abstractmethod
    def test1():
        pass

class result(test):
    
    def test1(self):
        print('this is reult.')


r = result()

print(r.mro())