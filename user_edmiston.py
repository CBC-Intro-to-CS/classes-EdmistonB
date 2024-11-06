class User:
    def __init__(self, first_name, last_name, age, where_they_live):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.where_they_live = where_they_live


    def describe_user(self):
        print(f"User Profile: ")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.where_they_live}")
       

  
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome.")
        

user1 = User("Bryce", "Edmiston", 17, "St.Louis")
user2 = User("Kaden", "Ellis", 18, "St.Louis")
user3 = User("Dominic", "Weingart", 17, "St.Louis")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

"""

"""
