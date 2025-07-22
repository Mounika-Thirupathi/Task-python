class mobile:
    brand="Android"
    ram="16gb"
    storage="128gb"
    camera="100mp"
    def fun(self):
        return "it is a mobile"
mi=mobile()
print(mi.brand)
print(mi.ram)
print(mi.storage)
print(mi.camera)
print(mi.fun())

s24=mobile()
print(s24.brand)
print(s24.ram)
print(s24.storage)
print(s24.camera)
print(s24.fun())

vivo=mobile()
print(vivo.brand)
print(vivo.ram)
print(vivo.storage)
print(vivo.camera)
print(vivo.fun())



class laptop:
    brand="hp"
    def __init__(self,ram,storage,cpu,ssd):
        self.ram=ram
        self.ram=ram
        self.storage=storage
        self.cpu=cpu
        self.ssd=ssd
    def fun(self):
        return "This is a laptop"

lenovo=laptop("16gb","512gb","i5","100")
print(lenovo.ram)
print(lenovo.storage)
print(lenovo.cpu)
print(lenovo.ssd)
print(lenovo.fun())



