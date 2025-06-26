class User:
    user_count = 0

    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email
        User.user_count += 1

    def display(self):
        print(f"Username: {self.username}\nEmail:{self.email}")


user_1 = User("dantheman", "dan@gmail.com")
user_2 = User("sally123", "sally@gmail.com")

print(User.user_count)
print(user_1.user_count)
print(user_2.user_count)
