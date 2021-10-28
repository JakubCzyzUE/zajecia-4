
class Property:
    def __init__(self, area: str, rooms: int, price: str, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self)->str :
        return f'PROPERTY' \
               f' area: {self.area},' \
               f' rooms: {self.rooms},' \
               f' price: {self.price},' \
               f' adress: {self.address}.'

class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area,rooms,price,address)
        self.plot = plot

    def __str__(self)->str:
        return f'HOUSE' \
               f' area: {self.area},' \
               f' rooms: {self.rooms},' \
               f' price: {self.price},' \
               f' adress: {self.address},' \
               f' plot: {self.plot}m2.'

class Flat(Property):
    def __init__(self,area, rooms, price, address, floor):
        super().__init__(area,rooms,price,address)
        self.floor = floor

    def __str__(self)->str:
        return f'FLAT' \
               f' area: {self.area},' \
               f' rooms: {self.rooms},' \
               f' price: {self.price},' \
               f' adress: {self.address},' \
               f' floor: {self.floor}.'



p1 = Property('miasto',4,'100 000 000','Olsztyn ul.Stawowa 15')
print(p1.__str__())
h1 = House('miasto',5,'200 000 000','Zielonki ul.zielona 13',1560)
print(h1.__str__())
f1 = Flat('miasto',3,'170 000 00','Krakwo','pierwsze')
print(f1.__str__())