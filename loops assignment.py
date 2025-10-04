def print_menu():
    #Prints the Taco Palace menu
    print("Taco Palace Menu")
    print("1. Taco")
    print("2. Burrito")
    print("3. Nachos")
    print("4. Soft Drink")
    print("5. Quit")


def get_price(item_number):
    #Returns the price of a menu item based on its number
    prices = {
        1: 2.50,
        2: 6.75,
        3: 5.25,
        4: 1.75
    }
    return prices.get(item_number, 0)


def get_item_name(item_number):
    #Returns the name of a menu item based on its number
    item_names = {
        1: "Taco",
        2: "Burrito",
        3: "Nachos",
        4: "Soft Drink"
    }
    return item_names.get(item_number, "Unknown Item")


def main():
    #Main function to run the Taco Palace ordering system
    print("Welcome to Taco Palace! Please view the menu below and enter the number that represents your selection.")
    print_menu()

    order_list = []
    total_due = 0.0

    while True:
        try:
            selection = int(input("\nEnter your selection (1-5): "))

            if selection == 5:
                break
            elif 1 <= selection <= 4:
                item_name = get_item_name(selection)
                item_price = get_price(selection)

                print(f"You selected a {item_name}")

                order_list.append(item_name)
                total_due += item_price
            else:
                print("Invalid selection. Please choose a number between 1 and 5.")

        except ValueError:
            print("Please enter a valid number.")

    if order_list:
        print(f"\nYou ordered a {', '.join(order_list)}.")
        print(f"Your total is ${total_due:.2f}")



main()