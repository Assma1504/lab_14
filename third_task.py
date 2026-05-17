# from second_task import IceCreamStand
from tkinter import*
from tkinter import ttk
from tkinter import messagebox

class iceCreamStandInterface:
   
    def __init__(self, shopName):
        self.myFrame = Tk()
        self.myFrame.title("Ice cream shop")
        self.myFrame.geometry("600x500")
        self.shopName = shopName
        # self.myFrame.columnconfigure(0, weight=1)
        # self.myFrame.columnconfigure(1, weight=2)
        self.operation=StringVar()
        self.operation.set("none")
        self.addFlavorLabel = Label(self.myFrame)
        self.addFlavorEntry = Entry(self.myFrame)
        self.deleteFlavorLabel = Label(self.myFrame)
        self.deleteFlavorEntry  = Entry(self.myFrame)
        #this list is just an example, later I'll remove it and every instance will have its owen list of flavors
        self.flavors = ["Banana","Cherry", "Mango", "Strawberry", "Biscuit Tortoni", "Caramel", "Chocolate", "Pistachio", "Vanilla"]


        self.title = Label(self.myFrame, text=self.shopName , font="Calibri 20 bold")
        self.title.grid(row=0, column=1, columnspan=2,sticky="we", padx=5)

        self.listFlavors = Label(self.myFrame, text="List flavors: ", font="Calibri 12 bold")
        self.listFlavors.grid(row=1, column=0, pady=10, padx=5, sticky="w")
        

        self.flavorOptions = ttk.Combobox(self.myFrame, values = self.flavors)
        # newIceCreamShop.print_flavors()
        self.flavorOptions.grid( row=1 , column=1, sticky="ew", padx=10, pady=10)
        self.flavorOptions.current(0)




        self.welcomeMessage = Label(self.myFrame, text="Add/Delete flavor: ", font="Calibri 12 bold")
        self.welcomeMessage.grid(row=2, column=0, pady=10, padx=5)

        self.operationAddFlavor = Radiobutton(self.myFrame, text="Add flavor", variable= self.operation, value="add", font=("Calibri", 12), command=self.defined_operation)
        self.operationAddFlavor.grid(row=3, column=0, sticky="w", pady=5, padx=5)

        self.operationDeleteFlavor = Radiobutton(self.myFrame, text="Delete flavor", variable= self.operation, value="delete", command=self.defined_operation)
        self.operationDeleteFlavor.grid(row=4, column=0, sticky="w", pady=5, padx=5)
        



    def defined_operation(self):
        operationChoice = self.operation.get() 
         
        if operationChoice == "add":
            self.show_add_flavor_elements()
        else:
            self.show_delete_flavor_elements()

    def destroy_all_elements(self):
        self.addFlavorLabel.destroy()
        self.addFlavorEntry.destroy()
        self.deleteFlavorLabel.destroy()
        self.deleteFlavorEntry.destroy()
        



    def show_add_flavor_elements(self):
        self.destroy_all_elements()
        self.addFlavorLabel = Label(self.myFrame, text="Add flavor",font="Calibri 14 bold" )
        self.addFlavorLabel.grid(row=5, column=0, padx=5, pady=10, sticky="w")
        self.addFlavorEntry = Entry(self.myFrame, width=40, font=("Calibri", 12))
        self.addFlavorEntry.grid(row=5, column=1, padx=5, pady=10, ipadx=5, sticky="w")


    def show_delete_flavor_elements(self):
        self.destroy_all_elements()
        self.flavorDeleted =  self.flavorOptions.get()
        clickedBtn = messagebox.askyesno("Delete ", f"Are you sure that you want to delete {self.flavorDeleted} flavor")
        if clickedBtn:
            self.flavors.remove(self.flavorDeleted)
            messagebox.showinfo("Flavor deleted", f"The {self.flavorDeleted} flavor was deleted")
            self.myFrame.quit()





        # self.deleteFlavorLabel = Label(self.myFrame, text="Delete flavor",font="Calibri 14 bold" )
        # self.deleteFlavorLabel.grid(row=5, column=0, sticky="w")
        # self.deleteFlavorEntry = Entry(self.myFrame, width=40,font=("Calibri", 12))
        # self.deleteFlavorEntry.grid(row=5, column=1, pady=20, ipady=5, ipadx=5)









        
       

        # btnAddFlavor = Button(self.myFrame, text="Add flavor", bg="#009900", fg="white", font="Calibri 10 bold")
        # btnAddFlavor.grid(row=4, column=0,  padx=(10, 20), pady=30, sticky="e", ipadx=5, ipady=5)

        # btnDeleteFlavor = Button(self.myFrame, text="Delete flavor", bg="#F83131", fg="white", font="Calibri 10 bold")
        # btnDeleteFlavor.grid(row=4, column=1, padx=(20,10), pady=30, sticky="w", ipadx=5, ipady=5)





shopApp = iceCreamStandInterface("Hello there")


# shopApp.defined_operation()




shopApp.myFrame.mainloop()