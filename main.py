class BMW:
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return 240


class Ferrari:
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return 350



def car_details(car):
    print(f"Fuel Type: {car.fuel_type()}")
    print(f"Max Speed: {car.max_speed()} km/h")



bmw = BMW()
ferrari = Ferrari()