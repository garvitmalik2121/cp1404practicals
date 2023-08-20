from taxi import Taxi


def main():
    my_taxi = Taxi("Puris 1", 100)
    my_taxi.drive(40)
    print("Taxi details after driving 40 km:")
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")
    my_taxi.start_fare()
    my_taxi.drive(100)
    print("\nTaxi details after driving an additional 100 km:")
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")


main()
