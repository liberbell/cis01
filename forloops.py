for i in range(5):
    print(i)
    # i += 1 

names = ["chris", "iftach", "jay"]
for name in names:
    print(name)

fruit_inventory = {"apples": 5, "peers": 2, "orange": 8}
print(list(fruit_inventory.items()))
for fruit in fruit_inventory:
    print(fruit)

for fruit in fruit_inventory.items():
    print(fruit)