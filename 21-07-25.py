class laptop:
    def __init__(self,ram,storage,processor,model,cost):
        self.ram=ram
        self.storage=storage
        self.processor=processor
        self.model=model
        self.cost=cost
    def fun(self,ram):
        self.ram=ram
        print(self.ram)
    def fun1(self,storage):
        self.storage=storage
        print(self.storage)
    def fun2(self,processor):
        self.processor=processor
        print(self.processor)
    def fun3(self,model):
        self.model=model
        print(self.model)
    def fun4(self,cost):
        self.cost=cost
        print(self.cost)
    
      
hp=laptop("16gb","128gb","i5","ios","2000")
print(hp.ram)
hp.fun("16gb")

dell=laptop("18gb","512gb","i6","android","3000")
print(dell.storage)
dell.fun1("220gb")

virtus=laptop("20gb","128gb","i7","ios","4000")
print(virtus.processor)
virtus.fun2("i8")

mac=laptop("22gb","512gb","i8","Android","5000")
print(mac.model)
mac.fun3("andriod")

realme=laptop("24gb","512gb","i9","ios","60000")
print(realme.ram)
realme.fun4("1000")