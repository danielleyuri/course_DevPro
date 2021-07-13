class People:
    def greet (self):
        return f'Hello {id(self)}'


if __name__ == '__main__':
    p = People()
    print(People.greet(p))
    print(id(p))
    print(p.greet())