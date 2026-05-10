class Restaurant():
    def __init__(self, restaurantName, restaurantType ):
        self.restaurantName= restaurantName 
        self.restaurantType = restaurantType

iceCreamParlor = Restaurant("Ice cream parlor",  "Ice cream parlor")
print(f"The restaurant name: {iceCreamParlor.restaurantName}, its type is {iceCreamParlor.restaurantType}")


class IceCreamStand(Restaurant):
    iceFlavors = ["Banana","Cherry", "Mango", "Strawberry", "Biscuit Tortoni", "Caramel", "Chocolate", "Pistachio", "Vanilla"]

    def print_flavors(self):
        print(self.iceFlavors)

newIceCreamShop = IceCreamStand("Ice cream parlor",  "Ice cream parlor")
print(newIceCreamShop.iceFlavors)