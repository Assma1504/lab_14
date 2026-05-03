class Restaurant():
    def __init__(self, restaurantName, restaurantType ):
        self.restaurantName= restaurantName 
        self.restaurantType = restaurantType
    
    # def describe_restaurant(self, restaurantSurface, numberWorkers):
    #     self.restaurantSurface = restaurantSurface
    #     self.numberWorkers = numberWorkers
    #     print(f"Our restaurant has a surface equal of: {restaurantSurface}, in this restaurant work: {numberWorkers}")


iceCreamParlor = Restaurant("Ice cream parlor",  "Ice cream parlor")
print(f"The restaurant name: {iceCreamParlor.restaurantName}, its type is {iceCreamParlor.restaurantType}")


class IceCreamStand(Restaurant):
    iceFlavors = ["Banana","Cherry", "Mango", "Strawberry", "Biscuit Tortoni", "Caramel", "Chocolate", "Pistachio", "Vanilla"]

    def print_flavors(self):
        print(self.iceFlavors)

newIceCreamShop = IceCreamStand("Ice cream parlor",  "Ice cream parlor")
print(newIceCreamShop.iceFlavors)