class People:
    eyes = 2

    def __init__(self, *child, name=None, age=15):
        self.age = age
        self.name = name
        self.child = list(child)

    def greet(self):
        return f'Hello {id(self)}'

    def finish(self):
        return f'See you later {id(self)}'

    def finishs(self):
        return f'Bye {id(self)}'


if __name__ == '__main__':
    shiny = People(name='Shiny')
    luna = People(shiny, name='Luna')
    print(People.greet(luna))
    print(id(luna))
    print(luna.greet())
    print(luna.name)
    print(luna.age)
    for childs in luna.child:
        print(childs.name)
    luna.lastname = 'Santos'
    del luna.child
    luna.eyes = 1
    del luna.eyes
    print(luna.__dict__)
    print(shiny.__dict__)
    People.eyes = 2
    print(People.eyes)
    print(luna.eyes)
    print(shiny.eyes)
    print(id(People.eyes), id(luna.eyes), id(shiny.eyes))

    print(People.finish(luna))
    print(People.finishs(luna))
