
class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price



class VendingMachine:
    def __init__(self):

        self.beverages = [
            Beverage("Coke", 1.50),
            Beverage("Pepsi", 1.50),
            Beverage("Water", 1.00),
            Beverage("Orange Juice", 2.00),
            Beverage("Tea", 1.25),
            Beverage("Coffee", 1.75)
        ]

    def show_menu(self):
        print("----- MENU -----")
        index = 1
        for item in self.beverages:
            print(str(index) + ". " + item.name + " - $" + str(item.price))
            index += 1
        print("----------------")

    def vend(self):
        while True:
            self.show_menu()

            choice = int(input("Select a beverage (1-6): "))

            if choice < 1 or choice > len(self.beverages):
                print("Invalid selection.\n")
                continue

            beverage = self.beverages[choice - 1]

            print("You selected: " + beverage.name)
            money = float(input("Insert money: "))

            if money < beverage.price:
                print("Not enough money. Money returned.\n")

            else:
                print("Vending " + beverage.name + "...")
                change = money - beverage.price
                if change > 0:
                    print("Returning change: $" + str(round(change, 2)))
                print("Enjoy!\n")



machine = VendingMachine()
machine.vend()
