# inventories for an rpg

# charachter inventories
bigGun = {
    "boot":
    {"description": "well fit to hold feet and tools",
        "armour": 1.5, "damage": 1, "quantity": (2)},
    "Gun":
    {"description": "a solid item for shooting someone, with bullets",
        "armour": 0, "damage": 5, "quantity": 1},
    "really cool hat":
    {"description": "it looks rather dapper",
        "armour": 4, "damage": 1, "quantity": 1}}


salmanBydy = {
    "bottle":
    {"description": "for holding liquids or seeing things far away",
        "armour": -1, "damage": 4, "quantity": 5},
    "belt buckle":
    {"description": "people really want to break it",
        "armour": 5, "damage": 0, "quantity": 1},
    "step stool":
    {"description": "meant for steppin', used for hittin'",
        "armour": 2, "damage": 3, "quantity": 1}}


goonList = {
    "BIG GUN": {"""the Biggest Gun of the Trudyhomes inc. realestate agency Big Gun is
known for not selling houses because he is Big Gun not Resident Residence"""},

    "Salman": {"""An odd person who has a pension for
    fights with a peculiar lack of pistols"""}}


# thing for showing all parts of a list
def showInventory(goon):
    print
    for i in (goon):
        print(f"{i}")
        for d in (goon)[i]:
            print(f"{d} - {(goon)[i][d]}")

# slecting your charachter

menuPrinted = 1
print
for i in goonList:
    print(f"{i}")
    for e in goonList[i]:
        print(f"{e}")
        print(" ")
while menuPrinted == 1:
    goonSelect = input("choose your main goon ")
    if goonSelect.lower() == "big gun":
        print(" ")
        print("Big Gun's inventory")
        showInventory(bigGun)
        menuPrinted = 2
    elif goonSelect.lower() == "salman":
        print(" ")
        print("Salman's inventory")
        showInventory(salmanBydy)
        menuPrinted = 2
    else:
        print(" ")
        print("that goon doesn't exist yet")
        print(" ")
