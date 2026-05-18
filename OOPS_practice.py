
class car:
    color = "white"
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def display_properties(self):
        print("Max Speed:", self.max_speed)
        print("Seating Capacity:", self.seating_capacity)
        print("Colour:", self.color)
        print("Mileage:", self.mileage)
print("For Car 1:")
vehicle1 = car(200, 50000)
vehicle1.assign_seating_capacity(5)
vehicle1.display_properties()

print("for car 2:")
vehicle2 = car(180, 75000)
vehicle2.assign_seating_capacity(4)
vehicle2.display_properties()
