class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        txt = f"{self.name} {self.age}"
        return txt

    def update_age(self, new_age: int):
        self.age = new_age
        return new_age
    