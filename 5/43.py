from typing import Counter


class Person:
    count=0
    def __init__(self) -> None:
        Person.count=Person.count+1


a=Person()
b=Person()
c=Person()
d=Person()
e=Person()

print(Person.count)