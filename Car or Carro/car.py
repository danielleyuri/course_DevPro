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
    >>> # Motor Test
    >>> motor = Motor()
    >>> motor.velocity
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocity
    2
    >>> motor.acelerar()
    >>> motor.velocity
    3
    >>> motor.frear()
    >>> motor.velocity
    1
    >>> motor.frear()
    >>> motor.velocity
    0
    >>> # Testando Direção
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocity()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocity()
    2
    >>> carro.frear()
    >>> carro.calcular_velocity()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
"""


