class People:
    def __init__(self, *child, name=None, age=15):
        self.age = age
        self.name = name
        self.child = list(child)


    def greet(self):
        return f'Hello {id(self)}'


if __name__ == '__main__':
    luna = People(name='Luna')
    shiny = People(name='Shiny')
    print(People.greet(luna))
    print(id(luna))
    print(luna.greet())
    print(luna.name)
    print(luna.age)
    for childs in shiny.child:
        print(childs.name)
