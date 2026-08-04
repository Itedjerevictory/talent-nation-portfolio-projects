# class CoffeeCup:
#     def __init__(self, size, owner):
#         self.size = size
#         self.owner = owner
#         self.contents = "empty"

# alice_cup = CoffeeCup("small", "Alice")

# print(alice_cup.size)
# print(alice_cup.owner)
# print(alice_cup.contents)




class CoffeeCup:
    def __init__(self, size, owner):
        self.size = size
        self.owner = owner
        self.contents = "empty"

alice_cup = CoffeeCup("small", "Alice")
bob_cup = CoffeeCup("large", "Bob")

print(f"the cup size is : {alice_cup.size}, and owned by {alice_cup.owner}")
print(f"the cup size is : {bob_cup.size}, and owned by {bob_cup.owner}")