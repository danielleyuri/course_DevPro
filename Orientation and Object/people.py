class People:
    def __init__(self, name=None, age=15):
        self.age = age
        self.name = name


    def greet(self):
        return f'Hello {id(self)}'


if __name__ == '__main__':
    p = People('Luna')
    print(People.greet(p))
    print(id(p))
    print(p.greet())
    print(p.name)
    p.name = 'Shiny'
    print(p.name)
    print(p.age)