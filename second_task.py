from task_one import Restaurant
class IceCreamStand(Restaurant):
    def __init__(self,restaurantName,  restaurantType, iceFlavors, restaurantLocation, timeWorking):
        super().__init__(restaurantName, restaurantType)
        self.iceFlavors = iceFlavors        
        self.restaurantLocation = restaurantLocation
        self.timeWorking = timeWorking

    # def print_flavors(self):
    #     print(self.iceFlavors)

    def add_flavor(self):
        newFlavor = input("If you have ideas for new flavors, please let us know:  ")
        if newFlavor.strip().capitalize() in self.iceFlavors:
            print("We have already this flavor, thank you for your participation")
        else:
            self.iceFlavors.append(newFlavor.strip().capitalize())
            print("Flavour added, thank you")

    def delete_flavor(self):
        deletedFlavor = input("Which flavor you want to delete: ")
        if deletedFlavor.strip().capitalize() in self.iceFlavors:
            self.iceFlavors.remove(deletedFlavor)
            print("Flavor was deleted")
            print(self.iceFlavors)
        else:
            print("We haven't this flavor, plase check again")
    
    def check_flavor(self):
        chackedFlavor = input("Which flavor you want to try: ")

        if chackedFlavor.strip().capitalize() in self.iceFlavors:
            print("Yes we have flavor, w'ill wait your order")
        else:
            print("Oooops, we haven't this flavor")
    
    def ice_popsicle(self):
        print("popsicle")

    def soft_ice_cream(self):
        print("soft ice cream")

    def ice_gelato(self):
        print("gelato")


newRes = IceCreamStand()




