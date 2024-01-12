class Test:
    def __init__(self):
        self.a = "a"
        self.one = 1
        self.list = [11,1,1]
    
    def func(self):
        print("func called")
        
test = Test()

for key, value in test.__dict__.items():
    print(key)
    print(value)

setattr(test, "a", "b")

for key, value in test.__dict__.items():
    print(key)
    print(value)