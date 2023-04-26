strength = -1
dexterity = 3
constitution = 0
intelligence = 5
wisdom = 2
charisma = 2

proficiency = 3
expertise = proficiency*2
joat = proficiency//2

koboldhack = 2
rp = 1

space1 = joat
space2 = proficiency
space3 = 5
space4 = 10

damage = []
totaldamage = 0

def validInputRoll(roll):
    if roll in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', 'break']:
        return roll
    else:
        return ""

def validInputCheck(d20):
    if d20 in ['1', '2', '3', '4', '5', '6', '7']:
        return d20
    else:
        return ""

def validInputStat1(stat1):
    if stat1 in ['1', '2', '3', '4', '5']:
        return stat1
    else:
        return ""

def validInputDexCheck(dexcheck):
    if dexcheck in ['1', '2', '3', '4']:
        return dexcheck
    else:
        return ""

def validInputIntCheck(intcheck):
    if intcheck in ['1', '2', '3', '4', '5', '6', '7']:
        return intcheck
    else:
        return ""

def validInputWisCheck(wischeck):
    if wischeck in ['1', '2', '3', '4', '5', '6']:
        return wischeck
    else:
        return ""

def validInputDexCheck(chacheck):
    if chacheck in ['1', '2', '3', '4']:
        return chacheck
    else:
        return ""
    
def validInputToolCheck(toolcheck):
    if toolcheck in ['1', '2', '3', '4']:
        return toolcheck
    else:
        return ""

def validInputToolStat(toolstat):
    if toolstat in ['1', '2', '3', '4', '5', '6']:
        return toolstat
    else:
        return ""

def validInputTSaveThrow(savethrow):
    if savethrow in ['1', '2', '3', '4', '5', '6']:
        return savethrow
    else:
        return ""

def validInputAttackRoll(attackroll):
    if attackroll in ['1', '2', '3']:
        return attackroll
    else:
        return ""

def validInputAttackStat(attackstat):
    if attackstat in ['1', '2']:
        return attackstat
    else:
        return ""

def validInputStat2(stat2):
    if stat2 in ['1', '2', '3', '4', '5', '6']:
        return stat2
    else:
        return ""

def validInputSuccAttack(succattack):
    if succattack in ['1']:
        return succattack
    else:
        return ""

while True:
    roll = input("Insert your roll: ")
    if roll == "break":
        break            
    print()
    print("-" * 172)
    print("1: Skill Check\n2: Tool Check\n3: Saving Throw\n4: Attack Roll\n5: Initiative\n6: Straight Roll\n7: Spaceship Roll")
    d20 = input(str("Insert used check: "))
    print()
    print("-" * 172)
    if d20 == "1":
        print("1: Strength\n2: Dexterity\n3: Intelligence\n4: Wisdom\n5: Charisma")
        stat1 = input(str("Insert used stat: "))
        print()
        print("-" * 172)
        if stat1 == "1":
            total = int(roll) + strength
            print("Athletics: Roll", "("+ str(roll) + ")", "+ Strength Score", "(" + str(strength) + ")", "=", str(total))
            print()
            print("-" * 172)
        elif stat1 == "2":
            print("1: Acrobatics\n2: Hacking\n3: Sleight of Hand\n4: Stealth")
            dexcheck = input(str("Insert used skill: "))
            print()
            print("-" * 172)
            if dexcheck == "1":
                total = int(roll) + dexterity
                print("Acrobatics: Roll", "("+ str(roll) + ")", "+ Dexterity Score", "(" + str(dexterity) + ")", "=", str(total))
                print()
                print("-" * 172)
            elif dexcheck == "2":
                total = int(roll) + dexterity + proficiency + koboldhack
                print("Hacking: Roll", "("+ str(roll) + ")", "+ Dexterity Score", "(" + str(dexterity) + ")", "+ Proficiency", "(" + str(proficiency) + ")", "+ Innate Kobold Hacking", "(" + str(koboldhack) + ")", "=", str(total))
                print()
                print("-" * 172)
            elif dexcheck == "3":
                total = int(roll) + dexterity + proficiency
                print("Sleight of Hand: Roll", "("+ str(roll) + ")", "+ Dexterity Score", "(" + str(dexterity) + ")", "+ Proficiency", "(" + str(proficiency) + ")", "=", str(total))
                print()
                print("-" * 172)
            elif dexcheck == "4":
                total = int(roll) + dexterity
                print("Stealth: Roll", "("+ str(roll) + ")", "+ Dexterity Score", "(" + str(dexterity) + ")", "=", str(total))
                print()
                print("-" * 172)
        elif stat1 == "3":
            print("1: Arcana\n2: Engineering\n3: Extra-Sensory\n4: History\n5: Investigation\n6: Nature\n7: Religion")
            intcheck = input(str("Insert used skill: "))
            print()
            print("-" * 172)
            if intcheck == "1":
                total = int(roll) + intelligence + proficiency
                print("Arcana: Roll", "("+ str(roll) + ")", "+ Intelligence Score", "(" + str(intelligence) + ")", "+ Proficiency", "(" + str(proficiency) + ")", "=", str(total))
                print()
                print("-" * 172)
            elif intcheck == "2":
                total = int(roll) + intelligence + expertise
                print("Engineering: Roll", "("+ str(roll) + ")", "+ Intelligence Score", "(" + str(intelligence) + ")", "+ Expertise", "(" + str(expertise) + ")", "=", str(total))
                print()
                print("-" * 172)
            elif intcheck == "3":
                total = int(roll) + intelligence
                print("Extra-Sensory: Roll", "("+ str(roll) + ")", "+ Intelligence Score", "(" + str(intelligence) + ")", "=", str(total))
                print()
                print("-" * 172)
            elif intcheck == "4":
                total = int(roll) + intelligence + proficiency
                print("History: Roll", "("+ str(roll) + ")", "+ Intelligence Score", "(" + str(intelligence) + ")", "+ Proficiency", "(" + str(proficiency) + ")", "=", str(total))
                print()
                print("-" * 172)
            elif intcheck == "5":
                total = int(roll) + intelligence + proficiency
                print("Investigation: Roll", "("+ str(roll) + ")", "+ Intelligence Score", "(" + str(intelligence) + ")", "+ Proficiency", "(" + str(proficiency) + ")", "=", str(total))
                print()
                print("-" * 172)
            elif intcheck == "6":
                total = int(roll) + intelligence
                print("Nature: Roll", "("+ str(roll) + ")", "+ Intelligence Score", "(" + str(intelligence) + ")", "=", str(total))
                print()
                print("-" * 172)
            elif intcheck == "7":
                total = int(roll) + intelligence
                print("Religion: Roll", "("+ str(roll) + ")", "+ Intelligence Score", "(" + str(intelligence) + ")", "=", str(total))
                print()
                print("-" * 172)
        elif stat1 == "4":
            print("1: Animal Handling\n2: Diplomacy\n3: Insight\n4: Medicine\n5: Perception\n6: Survival")
            wischeck = input(str("Insert used skill: "))
            print()
            print("-" * 172)
            if wischeck == "1":
                total = int(roll) + wisdom
                print("Animal Handling: Roll", "("+ str(roll) + ")", "+ Wisdom Score", "(" + str(wisdom) + ")", "=", str(total))
                print()
                print("-" * 172)
            elif wischeck == "2":
                total = int(roll) + wisdom
                print("Diplomacy: Roll", "("+ str(roll) + ")", "+ Wisdom Score", "(" + str(wisdom) + ")", "=", str(total))
                print()
                print("-" * 172)
            elif wischeck == "3":
                total = int(roll) + wisdom
                print("Insight: Roll", "("+ str(roll) + ")", "+ Wisdom Score", "(" + str(wisdom) + ")", "=", str(total))
                print()
                print("-" * 172)
            elif wischeck == "4":
                total = int(roll) + wisdom
                print("Medicine: Roll", "("+ str(roll) + ")", "+ Wisdom Score", "(" + str(wisdom) + ")", "=", str(total))
                print()
                print("-" * 172)
            elif wischeck == "5":
                total = int(roll) + wisdom + proficiency
                print("Perception: Roll", "("+ str(roll) + ")", "+ Wisdom Score", "(" + str(wisdom) + ")", "+ Proficiency", "(" + str(proficiency) + ")", "=", str(total))
                print()
                print("-" * 172)
            elif wischeck == "6":
                total = int(roll) + wisdom
                print("Survival: Roll", "("+ str(roll) + ")", "+ Wisdom Score", "(" + str(wisdom) + ")", "=", str(total))
                print()
                print("-" * 172)
        elif stat1 == "5":
            print("1: Deception\n2: Intimidation\n3: Performance\n4: Persuasion")
            chacheck = input(str("Insert used skill: "))
            print()
            print("-" * 172)
            if chacheck == "1":
                total = int(roll) + charisma
                print("Deception: Roll", "("+ str(roll) + ")", "+ Charisma Score", "(" + str(charisma) + ")", "=", str(total))
                print()
                print("-" * 172)
            elif chacheck == "2":
                total = int(roll) + charisma
                print("Intimidation: Roll", "("+ str(roll) + ")", "+ Charisma Score", "(" + str(charisma) + ")", "=", str(total))
                print()
                print("-" * 172)
            elif chacheck == "3":
                total = int(roll) + charisma
                print("Performance: Roll", "("+ str(roll) + ")", "+ Charisma Score", "(" + str(charisma) + ")", "=", str(total))
                print()
                print("-" * 172)
            elif chacheck == "4":
                total = int(roll) + charisma
                print("Persuasion: Roll", "("+ str(roll) + ")", "+ Charisma Score", "(" + str(charisma) + ")", "=", str(total))
                print()
                print("-" * 172)
    elif d20 == "2":
        print("1: Alchemist's Supplies\n2: Smith's Tools\n3: Thieves' Tools\n4: Tinker's Tools")
        toolcheck = input("Insert used tool: ")
        print()
        print("-" * 172)
        if toolcheck == "1":
            print("1: Strength\n2: Dexterity\n3: Constitution\4: Intelligence\n5: Wisdom\n6: Charisma")
            toolstat = input("Insert stat used: ")
            print()
            print("-" * 172)
            if toolstat == "1":
                total = int(roll) + strength + proficiency
                print("Alchemist's Supplies: Roll", "("+ str(roll) + ")", "+ Strength Score", "(" + str(strength) + ")", "+ Proficiency", "(" + str(proficiency) + ")", "=", str(total))
                print()
                print("-" * 172)
            elif toolstat == "2":
                total = int(roll) + dexterity + proficiency
                print("Alchemist's Supplies: Roll", "("+ str(roll) + ")", "+ Dexterity Score", "(" + str(dexterity) + ")", "+ Proficiency", "(" + str(proficiency) + ")", "=", str(total))
                print()
                print("-" * 172)
            elif toolstat == "3":
                total = int(roll) + constitution + proficiency
                print("Alchemist's Supplies: Roll", "("+ str(roll) + ")", "+ Constitution Score", "(" + str(constitution) + ")", "+ Proficiency", "(" + str(proficiency) + ")", "=", str(total))
                print()
                print("-" * 172)
            elif toolstat == "4":
                total = int(roll) + intelligence + proficiency
                print("Alchemist's Supplies: Roll", "("+ str(roll) + ")", "+ Intelligence Score", "(" + str(intelligence) + ")", "+ Proficiency", "(" + str(proficiency) + ")", "=", str(total))
                print()
                print("-" * 172)
            elif toolstat == "5":
                total = int(roll) + wisdom + proficiency
                print("Alchemist's Supplies: Roll", "("+ str(roll) + ")", "+ Wisdom Score", "(" + str(wisdom) + ")", "+ Proficiency", "(" + str(proficiency) + ")", "=", str(total))
                print()
                print("-" * 172)
            elif toolstat == "6":
                total = int(roll) + charisma + proficiency
                print("Alchemist's Supplies: Roll", "("+ str(roll) + ")", "+ Charisma Score", "(" + str(charisma) + ")", "+ Proficiency", "(" + str(proficiency) + ")", "=", str(total))
                print()
                print("-" * 172)
        elif toolcheck == "2":
            print("1: Strength\n2: Dexterity\n3: Constitution\4: Intelligence\n5: Wisdom\n6: Charisma")
            toolstat = input("Insert stat used: ")
            print()
            print("-" * 172)
            if toolstat == "1":
                total = int(roll) + strength + proficiency
                print("Smith's Tools: Roll", "("+ str(roll) + ")", "+ Strength Score", "(" + str(strength) + ")", "+ Proficiency", "(" + str(proficiency) + ")", "=", str(total))
                print()
                print("-" * 172)
            elif toolstat == "2":
                total = int(roll) + dexterity + proficiency
                print("Smith's Tools: Roll", "("+ str(roll) + ")", "+ Dexterity Score", "(" + str(dexterity) + ")", "+ Proficiency", "(" + str(proficiency) + ")", "=", str(total))
                print()
                print("-" * 172)
            elif toolstat == "3":
                total = int(roll) + constitution + proficiency
                print("Smith's Tools: Roll", "("+ str(roll) + ")", "+ Constitution Score", "(" + str(constitution) + ")", "+ Proficiency", "(" + str(proficiency) + ")", "=", str(total))
                print()
                print("-" * 172)
            elif toolstat == "4":
                total = int(roll) + intelligence + proficiency
                print("Smith's Tools: Roll", "("+ str(roll) + ")", "+ Intelligence Score", "(" + str(intelligence) + ")", "+ Proficiency", "(" + str(proficiency) + ")", "=", str(total))
                print()
                print("-" * 172)
            elif toolstat == "5":
                total = int(roll) + wisdom + proficiency
                print("Smith's Tools: Roll", "("+ str(roll) + ")", "+ Wisdom Score", "(" + str(wisdom) + ")", "+ Proficiency", "(" + str(proficiency) + ")", "=", str(total))
                print()
                print("-" * 172)
            elif toolstat == "6":
                total = int(roll) + charisma + proficiency
                print("Smith's Tools: Roll", "("+ str(roll) + ")", "+ Charisma Score", "(" + str(charisma) + ")", "+ Proficiency", "(" + str(proficiency) + ")", "=", str(total))
                print()
                print("-" * 172)
            elif toolcheck == "3":
                print("1: Strength\n2: Dexterity\n3: Constitution\4: Intelligence\n5: Wisdom\n6: Charisma")
                toolstat = input("Insert stat used: ")
                print()
                print("-" * 172)
                if toolstat == "1":
                    total = int(roll) + strength + proficiency
                    print("Thieves' Tools: Roll", "("+ str(roll) + ")", "+ Strength Score", "(" + str(strength) + ")", "+ Proficiency", "(" + str(proficiency) + ")", "=", str(total))
                    print()
                    print("-" * 172)
                elif toolstat == "2":
                    total = int(roll) + dexterity + proficiency
                    print("Thieves' Tools: Roll", "("+ str(roll) + ")", "+ Dexterity Score", "(" + str(dexterity) + ")", "+ Proficiency", "(" + str(proficiency) + ")", "=", str(total))
                    print()
                    print("-" * 172)
                elif toolstat == "3":
                    total = int(roll) + constitution + proficiency
                    print("Thieves' Tools: Roll", "("+ str(roll) + ")", "+ Constitution Score", "(" + str(constitution) + ")", "+ Proficiency", "(" + str(proficiency) + ")", "=", str(total))
                    print()
                    print("-" * 172)
                elif toolstat == "4":
                    total = int(roll) + intelligence + proficiency
                    print("Thieves' Tools: Roll", "("+ str(roll) + ")", "+ Intelligence Score", "(" + str(intelligence) + ")", "+ Proficiency", "(" + str(proficiency) + ")", "=", str(total))
                    print()
                    print("-" * 172)
                elif toolstat == "5":
                    total = int(roll) + wisdom + proficiency
                    print("Thieves' Tools: Roll", "("+ str(roll) + ")", "+ Wisdom Score", "(" + str(wisdom) + ")", "+ Proficiency", "(" + str(proficiency) + ")", "=", str(total))
                    print()
                    print("-" * 172)
                elif toolstat == "6":
                    total = int(roll) + charisma + proficiency
                    print("Thieves' Tools: Roll", "("+ str(roll) + ")", "+ Charisma Score", "(" + str(charisma) + ")", "+ Proficiency", "(" + str(proficiency) + ")", "=", str(total))
                    print()
                    print("-" * 172)
        elif toolcheck == "4":
            print("1: Strength\n2: Dexterity\n3: Constitution\4: Intelligence\n5: Wisdom\n6: Charisma")
            toolstat = input("Insert stat used: ")
            print()
            print("-" * 172)
            if toolstat == "1":
                total = int(roll) + strength + proficiency
                print("Tinker's Tools: Roll", "("+ str(roll) + ")", "+ Strength Score", "(" + str(strength) + ")", "+ Proficiency", "(" + str(proficiency) + ")", "=", str(total))
                print()
                print("-" * 172)
            elif toolstat == "2":
                total = int(roll) + dexterity + proficiency
                print("Tinker's Tools: Roll", "("+ str(roll) + ")", "+ Dexterity Score", "(" + str(dexterity) + ")", "+ Proficiency", "(" + str(proficiency) + ")", "=", str(total))
                print()
                print("-" * 172)
            elif toolstat == "3":
                total = int(roll) + constitution + proficiency
                print("Tinker's Tools: Roll", "("+ str(roll) + ")", "+ Constitution Score", "(" + str(constitution) + ")", "+ Proficiency", "(" + str(proficiency) + ")", "=", str(total))
                print()
                print("-" * 172)
            elif toolstat == "4":
                total = int(roll) + intelligence + proficiency
                print("Tinker's Tools: Roll", "("+ str(roll) + ")", "+ Intelligence Score", "(" + str(intelligence) + ")", "+ Proficiency", "(" + str(proficiency) + ")", "=", str(total))
                print()
                print("-" * 172)
            elif toolstat == "5":
                total = int(roll) + wisdom + proficiency
                print("Tinker's Tools: Roll", "("+ str(roll) + ")", "+ Wisdom Score", "(" + str(wisdom) + ")", "+ Proficiency", "(" + str(proficiency) + ")", "=", str(total))
                print()
                print("-" * 172)
            elif toolstat == "6":
                total = int(roll) + charisma + proficiency
                print("Tinker's Tools: Roll", "("+ str(roll) + ")", "+ Charisma Score", "(" + str(charisma) + ")", "+ Proficiency", "(" + str(proficiency) + ")", "=", str(total))
                print()
                print("-" * 172)
    elif d20 == "3":
        print("1: Strength\n2: Dexterity\n3: Constitution\4: Intelligence\n5: Wisdom\n6: Charisma")
        savethrow = input(str("Insert used stat: "))
        print()
        print("-" * 172)
        if savethrow == "1":
            total = int(roll) + strength
            print("Strength Saving Throw: Roll", "("+ str(roll) + ")", "+ Strength Score", "(" + str(strength) + ")", "=", str(total))
            print()
            print("-" * 172)
        elif savethrow == "2":
            total = int(roll) + dexterity
            print("Dexterity Saving Throw: Roll", "("+ str(roll) + ")", "+ Dexterity Score", "(" + str(dexterity) + ")", "=", str(total))
            print()
            print("-" * 172)
        elif savethrow == "3":
            total = int(roll) + constitution + proficiency
            print("Constitution Saving Throw: Roll", "("+ str(roll) + ")", "+ Constitution Score", "(" + str(constitution) + ")", "+ Proficiency", "(" + str(proficiency) + ")", "=", str(total))
            print()
            print("-" * 172)
        elif savethrow == "4":
            total = int(roll) + intelligence + proficiency
            print("Intelligence Saving Throw: Roll", "("+ str(roll) + ")", "+ Intelligence Score", "(" + str(intelligence) + ")", "+ Proficiency", "(" + str(proficiency) + ")", "=", str(total))
            print()
            print("-" * 172)
        elif savethrow == "5":
            total = int(roll) + wisdom
            print("Wisdom Saving Throw: Roll", "("+ str(roll) + ")", "+ Wisdom Score", "(" + str(wisdom) + ")", "=", str(total))
            print()
            print("-" * 172)
        elif savethrow == "6":
            total = int(roll) + charisma
            print("Charisma Saving Throw: Roll", "("+ str(roll) + ")", "+ Charisma Score", "(" + str(charisma) + ")", "=", str(total))
            print()
            print("-" * 172)
    elif d20 == "4":
        print("1: Weapon Attack\n2: Spell Attack\n3: Unarmed Strike")
        attackroll = input("Insert used attack: ")
        print()
        print("-" * 172)
        if attackroll == "1":
            print("1: Strength\n2: Dexterity")
            attackstat = input("Insert used stat: ")
            print()
            print("-" * 172)
            if attackstat == "1":
                total = int(roll) + strength + proficiency
                print("Strength Attack Roll: Roll", "("+ str(roll) + ")", "+ Strength Score", "(" + str(strength) + ")", "+ Proficiency", "(" + str(proficiency) + ")", "=", str(total))
                print()
                print("-" * 172)
                print("1: Hit\n2: Miss")
                succattack = input("Insert if hit or miss: ")
                if succattack == "1":
                    print()
                    print("-" * 172)
                    while True:
                        dam = input("Insert damage (or e to exit): ")
                        if dam == "e": 
                            break
                        else:
                            damage.append(dam)
                    for x in range(len(damage)):
                        totaldamage += int(damage[x])
                    print("Total damage is:", totaldamage)
                    print()
                    print("-" * 172)
                    totaldamage = 0
                    damage.clear()
            elif attackstat == "2":
                total = int(roll) + dexterity + proficiency
                print("Dexterity Attack Roll: Roll", "("+ str(roll) + ")", "+ Dexterity Score", "(" + str(dexterity) + ")", "+ Proficiency", "(" + str(proficiency) + ")", "=", str(total))
                print("Or")
                total = int(roll) + dexterity + proficiency + rp
                print("Dexterity Attack Roll: Roll", "("+ str(roll) + ")", "+ Dexterity Score", "(" + str(dexterity) + ")", "+ Proficiency", "(" + str(proficiency) + ")", "+ Repeating Shot", "(" + str(rp) + ")", "=", str(total))
                print()
                print("-" * 172)
                print("1: Hit\n2: Miss")
                succattack = input("Insert if hit or miss: ")
                if succattack == "1":
                    print()
                    print("-" * 172)
                    while True:
                        dam = input("Insert damage (or e to exit): ")
                        if dam == "e":
                            break
                        else:
                            damage.append(dam)
                    for x in range(len(damage)):
                        totaldamage += int(damage[x])
                    print("Total damage is:", totaldamage)
                    print()
                    print("-" * 172)
                    totaldamage = 0
                    damage.clear()
                else:
                    print()
                    print("-" * 172)
        elif attackroll == "2":
            total = int(roll) + intelligence + proficiency
            print("Intelligence Spell Attack Roll: Roll", "("+ str(roll) + ")", "+ Intelligence Score", "(" + str(intelligence) + ")", "+ Proficiency", "(" + str(proficiency) + ")", "=", str(total))
            print()
            print("-" * 172)
            print("1: Hit\n2: Miss")
            succattack = input("Insert if hit or miss: ")
            if succattack == "1":
                print()
                print("-" * 172)
                while True:
                    dam = input("Insert damage (or e to exit): ")
                    if dam == "e":
                        break
                    else:
                        damage.append(dam)
                for x in range(len(damage)):
                    totaldamage += int(damage[x])
                print("Total damage is:", totaldamage)
                print()
                print("-" * 172)
                totaldamage = 0
                damage.clear()
            else:
                print()
                print("-" * 172)
        elif attackroll == "3":
            total = int(roll) + strength
            print("Unarmed Strike: Roll", "("+ str(roll) + ")", "+ Strength Score", "(" + str(strength) + ")", "=", str(total))
            print()
            print("-" * 172)
            print("1: Hit\n2: Miss")
            succattack = input("Insert if hit or miss: ")
            if succattack == "1":
                print()
                print("-" * 172)
                while True:
                    dam = input("Insert damage (or e to exit): ")
                    if dam == "e":
                        break
                    else:
                        damage.append(dam)
                for x in range(len(damage)):
                    totaldamage += int(damage[x])
                print("Total damage is:", totaldamage)
                print()
                print("-" * 172)
                totaldamage = 0
                damage.clear()
            else:
                print()
                print("-" * 172)
    elif d20 == "5":
        total = int(roll) + dexterity
        print("Initiative: Roll", "("+ str(roll) + ")", "+ Dexterity Score", "(" + str(dexterity) + ")", "=", str(total))
        print()
        print("-" * 172)
    elif d20 == "6":
        print("1: Strength\n2: Dexterity\n3: Constitution\4: Intelligence\n5: Wisdom\n6: Charisma")
        stat2 = input("Insert used stat: ")
        print()
        print("-" * 172)
        if stat2 == "1":
            total = int(roll) + strength
            print("Straight Strength Roll: Roll", "("+ str(roll) + ")", "+ Strength Score", "(" + str(strength) + ")", "=", str(total))
            print()
            print("-" * 172)
        elif stat2 == "2":
            total = int(roll) + dexterity
            print("Straight Dexterity Roll: Roll", "("+ str(roll) + ")", "+ Dexterity Score", "(" + str(dexterity) + ")", "=", str(total))
            print()
            print("-" * 172)
        elif stat2 == "3":
            total = int(roll) + constitution
            print("Straight Constitution Roll: Roll", "("+ str(roll) + ")", "+ Constitution Score", "(" + str(constitution) + ")", "=", str(total))
            print()
            print("-" * 172)
        elif stat2 == "4":
            total = int(roll) + intelligence
            print("Straight Intelligence Roll: Roll", "("+ str(roll) + ")", "+ Intelligence Score", "(" + str(intelligence) + ")", "=", str(total))
            print()
            print("-" * 172)
        elif stat2 == "5":
            total = int(roll) + wisdom
            print("Straight Wisdom Roll:", "("+ str(roll) + ")", "+ Wisdom Score", "(" + str(wisdom) + ")", "=", str(total))
            print()
            print("-" * 172)
        elif stat2 == "6":
            total = int(roll) + charisma
            print("Straight Charisma Roll: Roll", "("+ str(roll) + ")", "+ Charisma Score", "(" + str(charisma) + ")", "=", str(total))
            print()
            print("-" * 172)
    elif d20 == "7":
        print("1: Strength\n2: Dexterity\n3: Constitution\4: Intelligence\n5: Wisdom\n6: Charisma")
        stat2 = input("Insert used stat: ")
        print()
        print("-" * 172)
        if stat2 == "1":
            total = int(roll) + strength + space2
            print("Strength Spaceship Roll: Roll", "("+ str(roll) + ")", "+ Strength Score", "(" + str(strength) + ")", "+ Space Proficiency", "(" + str(space2) + ")", "=", str(total))
            print()
            print("-" * 172)
        elif stat2 == "2":
            total = int(roll) + dexterity + space2
            print("Dexterity Spaceship Roll: Roll", "("+ str(roll) + ")", "+ Dexterity Score", "(" + str(dexterity) + ")", "+ Space Proficiency", "(" + str(space2) + ")", "=", str(total))
            print()
            print("-" * 172)
        elif stat2 == "3":
            total = int(roll) + constitution + space2
            print("Constitution Spaceship Roll: Roll", "("+ str(roll) + ")", "+ Constitution Score", "(" + str(constitution) + ")", "+ Space Proficiency", "(" + str(space2) + ")", "=", str(total))
            print()
            print("-" * 172)
        elif stat2 == "4":
            total = int(roll) + intelligence + space2
            print("Intelligence Spaceship Roll: Roll", "("+ str(roll) + ")", "+ Intelligence Score", "(" + str(intelligence) + ")", "+ Space Proficiency", "(" + str(space2) + ")", "=", str(total))
            print()
            print("-" * 172)
        elif stat2 == "5":
            total = int(roll) + wisdom + space2
            print("Wisdom Spaceship Roll:", "("+ str(roll) + ")", "+ Wisdom Score", "(" + str(wisdom) + ")", "+ Space Proficiency", "(" + str(space2) + ")", "=", str(total))
            print()
            print("-" * 172)
        elif stat2 == "6":
            total = int(roll) + charisma + space2
            print("Charisma Spaceship Roll: Roll", "("+ str(roll) + ")", "+ Charisma Score", "(" + str(charisma) + ")", "+ Space Proficiency", "(" + str(space2) + ")", "=", str(total))
            print()
            print("-" * 172)