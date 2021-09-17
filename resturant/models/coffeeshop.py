from models.resturant import Restaurant


class CoffeeShop(Restaurant):
    def __init__(self, name, startime, endtime):
        super().__init__()
        self.name = name
        self.startTime = startime
        self.endTime = endtime
        self.type = 'coffee-shop'
