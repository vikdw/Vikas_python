

def d(func):
    def inner(y):
        y = 'vikas'
        return func(y)
    return inner

@d
def func(x):
    s = f"hello {x}"
    return s


print(func('dwivedi'))