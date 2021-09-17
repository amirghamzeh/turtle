from models.coffeeshop import CoffeeShop


ole = CoffeeShop('Ole', 8, 20)
if ole.isOpen():
    print(ole.name, 'Is open')
else:
    print(ole.name, 'Is close')