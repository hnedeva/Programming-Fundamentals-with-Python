# My version with 85/100 in Judge
# name = input()
#
# while name != "Welcome!":
#     if len(name) < 5:
#         print(f"{name} goes to Gryffindor.")
#     elif len(name) == 5:
#         print(f"{name} goes to Slytherin.")
#     elif len(name) == 6:
#         print(f"{name} goes to Ravenclaw.")
#     elif len(name) > 6:
#         print(f"{name} goes to Hufflepuff.")
#     name = input()
#     if name == "Welcome!":
#         print("Welcome to Hogwarts.")
#     if name == "Voldemort":
#         print("You must not speak of that name!")
#         break

# Correctly solve
while True:
    name = input()
    if name == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    elif name == "Voldemort":
        print("You must not speak of that name!")
        break
    elif len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    else:
        print(f"{name} goes to Hufflepuff.")