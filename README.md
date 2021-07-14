# course_DevPro
Small Projects in Python!

**Obeject and orientation.

The People Project:
-----------------------------------------------------------------------------
*Data attribute
*Complex attribute
*Dinamic attribute
*Class atributte
*Class method
___________________________________________________________________________
Project Car:
---------------------------------------------------------------------------

"""
You must create a car class that will have
two attributes composed of two other classes:
1) Motor
2) Direction

The engine will be responsible for controlling the speed.
It offers the following attributes:
1) Speed data attribute
2) Accelerate method, which should increase the speed of one unit
3) Brake method that should decrease the speed by two units

The direction will have the responsibility to control the direction.
the following attributes:
1) Direction value with possible values: North, South, East and West.
2) Rotate_right_method
2) Left_turn method

    N
W       E
    S

Example:
# Test Motor 
motor = Motor()

motor.velocity

0

motor.speedup()

motor.velocity

1

motor.speedup()

motor.velocity
 
2

motor.speedup()

motor.velocity

3

motor.brake()

motor.velocity

1

motor.brake()

motor.velocity

0

# Test Direction 

direction = Direction()

direction.value

'North'

direction.spin_the_right()

direction.value
 
'East'
 
direction.spin_the_right()
 
direction.value
 
'South'
 
direction.spin_the_right()
 
direction.value
 
'West'
 
direction.spin_the_right()

direction.value

'North'

direction.spin_the_left()

direction.value

'West'

direction.spin_the_left()

direction.value

'South'

direction.spin_the_left()

direction.value

'East'

direction.spin_the_left()

direction.value

'North'

car = Car (direction, motor)

car.calculate_velocity()

0

car.accelerate()

car.accelerate_velocity()

1

car.accelerate()

car.accelerate_velocity()

2

car.frear()

car.accelerate_velocity()

0

car.calculate_direction()

'North'

car.spin_the_right()

car.calculate_direction()

'East'

car.spin_the_left()

car.calculate_direction()

'North'

car.spin_the_left()

car.calculate_direction()

'West'

"""
