
seats = {
    1: "emergency", 2: "emergency", 3: "emergency", 4: "emergency", 5: "emergency",
    6: "regular", 7: "first-class", 8: "first-class", 9: "first-class", 10: "regular",
    11: "regular", 12: "regular", 13: "regular", 14: "regular", 15: "regular",
    16: "emergency", 17: "emergency", 18: "emergency", 19: "emergency", 20: "emergency"
}


taken_seats = {2, 10, 15}

first_class_fee = 50
regular_fee = 0


def display_seats():
    print("\nAirplane Seating:")
    for i in range(1, 21):
        if i in taken_seats:
            status = "X"
        elif seats[i] == "first-class":
            status = f"{i}(F)"
        elif seats[i] == "emergency":
            status = f"{i}(E)"
        else:
            status = str(i)
        print(f"{status:>5}", end=" ")
        if i % 5 == 0:
            print()
    print()


def purchase_seats():
    display_seats()

    selection = input("Enter the seat numbers you want to purchase (comma-separated): ")
    try:
        seat_numbers = [int(num.strip()) for num in selection.split(",")]
    except ValueError:
        print("Invalid input. Please enter seat numbers separated by commas.")
        return

    total_cost = 0
    for seat in seat_numbers:
        if seat < 1 or seat > 20:
            print(f"Seat {seat} does not exist.")
            continue
        if seat in taken_seats:
            print(f"Seat {seat} is already taken.")
            continue


        if seats[seat] == "emergency":
            accept = input(
                f"Seat {seat} is an emergency seat. You must be able to help in case of an emergency. Accept? (yes/no): ")
            if accept.lower() != "yes":
                print(f"Seat {seat} not purchased.")
                continue

        if seats[seat] == "first-class":
            total_cost += first_class_fee

        taken_seats.add(seat)
        print(f"Seat {seat} successfully purchased.")

    print(f"\nTotal cost: ${total_cost}")


def main():
    print("Welcome to the Airplane Seat Booking System!")
    while True:
        purchase_seats()
        more = input("Do you want to purchase more seats? (yes/no): ")
        if more.lower() != "yes":
            break


if __name__ == "__main__":
    main()
