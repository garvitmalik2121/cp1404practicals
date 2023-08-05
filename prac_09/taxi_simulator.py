from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def display_taxis(taxis):
    """Display the available taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill_to_date = 0.0

    print("Let's drive!")
    print("q)uit, c)hoose taxi, d)rive")
    choice = input(">>> ").lower()

    while choice != 'q':
        if choice == 'c':
            print("Taxis available:")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            if 0 <= taxi_choice < len(taxis):
                current_taxi = taxis[taxi_choice]
                print(f"Bill to date: ${bill_to_date:.2f}")
            else:
                print("Invalid taxi choice")
        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                try:
                    distance = float(input("Drive how far? "))  # Prompt for distance driven
                    fare = current_taxi.drive(distance)  # Use the drive method to update fare and distance driven
                    print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
                    bill_to_date += fare
                    print(f"Bill to date: ${bill_to_date:.2f}")

                    # Update the taxi's odometer and fuel attributes
                    current_taxi.start_fare()

                except ValueError:
                    print("Invalid distance. Please enter a number.")
        else:
            print("Invalid option")

        # Prompt for the next choice
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


if __name__ == '__main__':
    main()
