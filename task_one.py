class Restaurant():
    def __init__(self, restaurantName, restaurantType):
        self.restaurantName= restaurantName
        self.restaurantType = restaurantType
        self.restaurantRating = 00
        
    def describe_restaurant(self, restaurantSurface, numberWorkers):
        self.restaurantSurface = restaurantSurface
        self.numberWorkers = numberWorkers
        print(f"Our restaurant has a surface equal of: {restaurantSurface}, in this restaurant work: {numberWorkers}")

    def update_rating(self):
        newRating = input("The restaurant rating: ")
        self.restaurantRating = newRating

class IceCreamStand(Restaurant):
    def __init__(self,restaurantName,  restaurantType, iceFlavors):
        super().__init__(restaurantName, restaurantType)
        # iceFlavors= ["Banana","Cherry", "Mango", "Strawberry", "Biscuit Tortoni", "Caramel", "Chocolate", "Pistachio", "Vanilla"]
        self.iceFlavors = iceFlavors

    def print_flavors(self):
        print(self.iceFlavors)

newIceCreamShop = IceCreamStand("Ice cream parlor",  "Ice cream parlor",  ["Banana","Cherry", "Mango", "Strawberry", "Biscuit Tortoni", "Caramel", "Chocolate", "Pistachio", "Vanilla"])
newIceCreamShop.print_flavors()