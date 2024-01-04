# class Person:
#     def __init__(self, name):
#         self_name = name


# class Teen(Person):
#     def __init__(
#         self,
#         name,
#     ):
#         super().__init__(name)
#         self.age = 8


# t = Teen("John")
# print(t.age)


def validate_name(name):
    has_num = any(type(char) == int for char in name)
    if len(name) < 6 or has_num:
        return True
    return False


player_name = ""

while validate_name(player_name):
    print("Please enter a valid name (at least 6 characters long)")
    player_name = input("Enter your name: ").strip()
