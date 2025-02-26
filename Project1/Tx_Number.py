class Txnumber:
    def __init__(self):
        self._startValue=100

    def make_tx(self):
        self._startValue = self._startValue +1
        return self._startValue
    
t = Txnumber()

r = Txnumber()
print(t.make_tx())
print(t.make_tx())
print(r.make_tx())
print(r.make_tx())