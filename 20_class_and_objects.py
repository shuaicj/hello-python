#!/usr/bin/env python3

class Animal(object):
    DEFAULT_NAME = 'A'

    def __init__(self, name):
        self.__name = name

    @classmethod
    def fromName(cls, name=None):
        if name is None:
            return cls(cls.DEFAULT_NAME)
        return cls(name)

    @staticmethod
    def get_static_default_name():
        return Animal.DEFAULT_NAME

    @classmethod
    def get_class_default_name(cls):
        return cls.DEFAULT_NAME

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def eat(self):
        print('Animal %s is eating.' % self.name)

class Cat(Animal):
    DEFAULT_NAME = 'C'

    def eat(self):
        print('Cat %s is eating.' % self.name)

class Dog(Animal):
    def eat(self):
        print('Dog %s is eating.' % self.name)


a = Animal('a')
c = Cat('c')
d = Dog('d')

print('Animal.DEFAULT_NAME =', Animal.DEFAULT_NAME)
print('Cat.DEFAULT_NAME =', Cat.DEFAULT_NAME)
print('Dog.DEFAULT_NAME =', Dog.DEFAULT_NAME)
print('a.DEFAULT_NAME =', a.DEFAULT_NAME)
print('c.DEFAULT_NAME =', c.DEFAULT_NAME)
print('d.DEFAULT_NAME =', d.DEFAULT_NAME)
print()

print('Animal.get_static_default_name() =', Animal.get_static_default_name())
print('Cat.get_static_default_name() =', Cat.get_static_default_name())
print('Dog.get_static_default_name() =', Dog.get_static_default_name())
print('a.get_static_default_name() =', a.get_static_default_name())
print('c.get_static_default_name() =', c.get_static_default_name())
print('d.get_static_default_name() =', d.get_static_default_name())
print()

print('Animal.get_class_default_name() =', Animal.get_class_default_name())
print('Cat.get_class_default_name() =', Cat.get_class_default_name())
print('Dog.get_class_default_name() =', Dog.get_class_default_name())
print('a.get_class_default_name() =', a.get_class_default_name())
print('c.get_class_default_name() =', c.get_class_default_name())
print('d.get_class_default_name() =', d.get_class_default_name())
print()

print('a.name =', a.name)
print('c.name =', c.name)
print('d.name =', d.name)
print()

c.name = 'c'

a.eat()
c.eat()
d.eat()

print()

a = Animal.fromName('aa')
c = Cat.fromName()
d = Dog.fromName('dd')

print('a.name =', a.name)
print('c.name =', c.name)
print('d.name =', d.name)

