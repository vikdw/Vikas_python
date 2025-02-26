class Counter:
    def __init__(self):
        self.value=10
    def __add__(self, other):
        if isinstance(other, Counter):
            print(f"{self.__class__.__name__}")
            return self.value + other.value
            
        else:
          
            raise ValueError(f"other is not object of '{self.__class__.__name__}' calss")
        
    def __repr__(self):
        return f"this is '{self.__class__.__name__}' class."
    
class Runner(Counter):
    def __init__(self, power):
        super().__init__()
        self.power= self.value*power

    def __repr__(self):
        return f"{super().__repr__()} with {self.power} power." 



class Point2D():
    def __init__(self,x,y):
        print("setting x")
        self.x = x
        print("setting y")
        self.y = y 
    @property
    def x(self):
        print("gettng x")
        return self._x
    @x.setter
    def x(self, value):
        print("x setter called")
        self._x = int(value)
    @property
    def y(self):
        print("gettng y")
        return self._y
    @y.setter
    def y(self, value):
        print("y setter called")
        self._y = int(value)

p = Point2D(3,4)

print(p.x)
print(p._x)

print(dir(p))
print(p.__dict__)
    
# c1 = Counter()
# print(c1)
# r1= Runner(3)
# print(r1)




