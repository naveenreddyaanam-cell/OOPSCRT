class BikeShop:
    def __init__(self,stock):
        self.stock = stock
    def ShowBike(self):
        print("Total Bikes :",self.stock)
    def rentBike(self,quantity):

        if quantity <= 0:
            print("please Enter the positive value or grater than zero")
        elif quantity > self.stock:
            print("Enter the value (less than stock)")
        else:
            self.stock = self.stock - quantity
            print("Total price :",uantity*100)
            print("Total Bike",self.stock)
while True:
    obj = BikeShop(100)
    print("IT BIKE RENTAL SYSTEM")
    user_input = int(input('''
    1->Display stock
    2->Rent a Bike
    3->Exit
            '''))
    if user_input == 1:
        obj.Showlike()
    elif user_input == 2:
        n = int(input("Enter the rent Bike :->"))
        obj.rentBike(n)
    else:
        break

    
