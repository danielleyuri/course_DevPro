class People:
    eyes = 2

    def __init__(self, *childrens, name=None, age=15):
        self.age = age
        self.name = name
        self.childrens = list(childrens)

    def greet(self):
        return f'Hello, my name is {self.name}.'

    def finish(self):
        return f'See you later! Bye,{self.name}'

    @staticmethod
    def static_method():
        return 42

    @classmethod
    def class_name_and_attribute(cls):
        return f'{cls} - eyes {cls.eyes}'


class Woman(People):
    def greet(self):
        greet_class = super().greet()
        return f'{greet_class} Handshake'


class Mutant(People):
    eyes = 3


if __name__ == '__main__':
    shiny = Mutant(name='Shiny')
    luna = Woman(shiny, name='Luna')
    print(People.greet(luna))
    print(id(luna))
    print(luna.greet())
    print(luna.name)
    print(luna.age)
    for children in luna.childrens:
        print(children.name)
    luna.lastname = 'Santos'
    del luna.childrens
    luna.eyes = 2
    del luna.eyes
    print(luna.__dict__)
    print(shiny.__dict__)
    print(People.eyes)
    print(luna.eyes)
    print(shiny.eyes)
    print(id(People.eyes), id(luna.eyes), id(shiny.eyes))
    print(People.static_method(), luna.static_method())
    print(People.class_name_and_attribute(), luna.class_name_and_attribute())
    people = People('Anonymus')
    print(isinstance(people, People))
    print(isinstance(people, Woman))
    print(isinstance(shiny, People))
    print(isinstance(shiny, Woman))
    print(shiny.eyes)
    print(luna.greet())
    print(shiny.greet())
    print(luna.finish())
    print(shiny.finish())
