class Vehicle:
    # TODO: Please write your code here
    pass


class Car(Vehicle):
    # TODO: Please write your code here
    pass


class Truck(Vehicle):
    # TODO: Please write your code here
    pass


# Do not change or remove the code below this point
def main():
    car = Car("Toyota", "Corolla", 2021, 4)
    print(car.get_description())  # Expected: "2021 Toyota Corolla, 4-door"

    truck = Truck("Ford", "F-150", 2020, 1.5)
    print(truck.get_description())  # Expected: "2020 Ford F-150, Payload capacity: 1.5 tons"


if __name__ == "__main__":
    main()
