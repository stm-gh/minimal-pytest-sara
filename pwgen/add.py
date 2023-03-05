def squareDecorator(func):
    def wrapper(*args, **kwargs):
        print("Start of wrap")
        result = func(*args, **kwargs)*func(*args, **kwargs)
        ##result = func + func
        print(result)
        return result
    return wrapper

@squareDecorator
def add(a: int, b: int) -> int:
    return a + b

print("End of add.py")