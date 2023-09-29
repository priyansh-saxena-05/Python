class MyFile:
    
    def __init__(self):
        pass

    def calculate(self, x, y):
        session = x * y
        return {"myfile": session}


class MyClass:
    
    def __init__(self):
        pass

    def calculate(self, x, y):
        session = x + y
        return {"myclass": session}
    

class Yes:
    
    def __init__(self):
        pass

    def values(self, x, y):
        ans = {}
        x += 500
        y += 10
        obj = MyFile()
        resp1 = obj.calculate(x, y)
        ans.update(resp1)
        obj = MyClass()
        resp2 = obj.calculate(x, y)
        ans.update(resp2)
        return {"resp": ans}
