numbers = []
totalnumber = 0

print("1: Duke\n2: Mordekai\n3: Sid\n4: Wrench")
character = input("Insert character being used: ")
print()
print("-" * 172)
if character == "1":
    while True:
        while True:
            inputNumbers = input("Insert number(s) (or e to exit): ")
            if inputNumbers == "e":
                break
            else:
                numbers.append(inputNumbers)
        for x in range(len(numbers)):
            totalnumber += int(numbers[x])
        print("Total:", totalnumber)
        print()
        print("-" * 172)
        numbers.clear()
        totalnumber = 0
if character == "2":
    while True:
        print("Favored Foe: Add 1d4 damage\n")
        print("Foe Slayer: Add Wisdom modifier to attack roll or damage roll.\n")
        print("Gathered Swarm:\n  1d6 piercing damage\n  Succeed strength saving throw or be moved up to 15 feet horizontally in a direction of your choice\n  You move 5 feet horizontally in a direction of your choice\n")
        print("Active Spells: Trigger their effects\n")
        while True:
            inputNumbers = input("Insert number(s) (or e to exit): ")
            if inputNumbers == "e":
                break
            else:
                numbers.append(inputNumbers)
        for x in range(len(numbers)):
            totalnumber += int(numbers[x])
        print("Total:", totalnumber)
        print()
        print("-" * 172)
        numbers.clear()
        totalnumber = 0
if character == "3":
    while True:
        print("Giant Might: Add 1d6\n")
        print("Great Weapon Fighting: Reroll 1s and 2s on damage dice\n")
        print("Great Weapon Master: -5 to attack | +10 damage\n")
        print("Savage Attacker: Roll damage dice twice and use higher results\n")
        while True:
            inputNumbers = input("Insert number(s) (or e to exit): ")
            if inputNumbers == "e":
                break
            else:
                numbers.append(inputNumbers)
        for x in range(len(numbers)):
            totalnumber += int(numbers[x])
        print("Total:", totalnumber)
        print()
        print("-" * 172)
        numbers.clear()
        totalnumber = 0
if character == "4":
    while True:
        print("Repeating Shot: +1 weapon\n")
        print("Scope: +2 to hit\n")
        print("Active Spells: Trigger their effects\n")
        while True:
            inputNumbers = input("Insert number(s) (or e to exit): ")
            if inputNumbers == "e":
                break
            else:
                numbers.append(inputNumbers)
        for x in range(len(numbers)):
            totalnumber += int(numbers[x])
        print("Total:", totalnumber)
        print()
        print("-" * 172)
        numbers.clear()
        totalnumber = 0