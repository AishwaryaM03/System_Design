class Car:
    def drive(self):
        print("Driving a car")


class Bike:
    def drive(self):
        print("Riding a bike")


class Truck:
    def drive(self):
        print("Driving a truck")


class VehicleFactory:

    @staticmethod
    def get_vehicle(vehicle_type):

        if vehicle_type == "car":
            return Car()

        elif vehicle_type == "bike":
            return Bike()

        elif vehicle_type == "truck":
            return Truck()

        else:
            return None