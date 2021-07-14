class Car:
    def __init__(self, direction, motor):
        self.motor = motor
        self.direction = direction

    def calculate_velocity(self):
        return self.motor.velocity

    def accelerate(self):
        self.motor.accelerate()

    def brake(self):
        self.motor.brake()

    def calculate_direction(self):
        return self.direction.value

    def spin_the_right(self):
        self.direction.spin_the_right()

    def spin_the_left(self):
        self.direction.spin_the_left()


NORTH = 'North'
SOUTH = 'South'
EAST = 'East'
WEST = 'West'


class Direction:
    rotation_the_right_dct = {
        NORTH: EAST, EAST: SOUTH, SOUTH: WEST, WEST: NORTH
    }
    rotation_the_left_dct = {
        NORTH: WEST, EAST: NORTH, SOUTH: EAST, WEST: SOUTH
    }

    def __init__(self):
        self.value = NORTH

    def rotation_the_right(self):
        self.value = self.rotation_the_right_dct[self.value]

    def rotation_the_left(self):
        self.value = self.rotation_the_left_dct[self.value]



