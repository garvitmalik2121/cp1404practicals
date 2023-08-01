from silver_service_taxi import SilverServiceTaxi


def main():
    my_taxi = SilverServiceTaxi("Camry", 200, 2)
    distance = 18
    my_taxi.drive(distance)
    fare = my_taxi.get_fare()
    print(f"Fare for {distance} km in a SilverServiceTaxi: ${fare:.2f}")


main()
