from unreliable_car import UnreliableCar

def main():
    # Create an UnreliableCar object
    my_car = UnreliableCar("UnreliableCar", 100, 70)  # Reliability is set to 70%

    # Test driving the car
    distance = 76
    distance_driven = my_car.drive(distance)
    print(f"Distance driven: {distance_driven} km")

if __name__ == "__main__":
    main()
