from datetime import datetime
import re


class Dog:
    def __init__(self, name: str, breed: str, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("woof woof!")


class Owner:
    def __init__(self, name: str, address: str, contact_number: str):
        self.name = name
        self.address = address
        self.phone_number = contact_number


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello my name is {self.name} and I'm {self.age} years old ")


class User:
    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self._email = email
        self.password = password

    @property
    def email(self):
        print(f"Email Accessed at {datetime.now()}")
        return self._email

    @email.setter
    def email(self, inbound_email):
        pattern = re.compile(r"[a-zA-Z0-9+-_]*@[a-z]*\.[a-z]*")
        if re.match(pattern, inbound_email):
            print(f"Email Updated at {datetime.now()}")
            self._email = inbound_email
        else:
            print("Error! the email is not valid")


# owner_1 = Owner("Danny", "122, Springfield Drive", "111222333")
# dog1 = Dog("Bruce", "Rottweiler", owner_1)
# print(dog1.name, dog1.breed, dog1.owner.name)

# owner_2 = Owner("Sally", "122, Springfield Drive", "111222333")
# dog2 = Dog("Leia", "Greyhound", owner_2)
# print(dog2.name, dog2.breed, dog2.owner.name)


# person_1 = Person("Alice", 30)
# person_1.greet()

# person_2 = Person("Bob", 42)
# person_2.greet()


user1 = User("dantheman", "dan@gmail.com", "123")
print(user1.email)

user1.email = "validemail@gmail.com"
