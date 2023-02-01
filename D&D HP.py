MaxSHP = 59
SHP = 59
MaxWHP = 44
WHP = 44
MaxMHP = 29
MHP = 29
MaxTransformHP = 0
TransformHP = 0
TempHP = 0

def validInputCharacter(CHP):
    if CHP in ['1', '2', '3']:
        return CHP
    else:
        return ""
        
def validInputHealth(HP):
    if HP in ['1', '2', '3', '4', '5', 'break']:
        return HP
    else:
        return ""

print("1: Sid\n2: Wrench\n3: Mordekai")
CHP = input("Insert used character: ")
print()
print("-" * 172)
if CHP == "1":
    while True:
        print("1: Damage\n2: Heal\n3: Temporary HP\n4: Transform HP\n5: Long Rest")
        HP = input("Insert Damage, Heal, Temp HP, Transform HP, or Long Rest: ")
        print()
        print("-" * 172)
        if HP == "1":
            damage = input("Insert damage taken: ")
            if TempHP > 0 and TransformHP > 0:
                TempHP -= int(damage)
                if TempHP >= 0:
                    print("Current Temporary HP:", TempHP)
                    print("Current Transformation HP:", TransformHP)
                    print("Current HP:", SHP)
                    print()
                    print("-" * 172)
                elif TempHP < 0 and TransformHP > 0:
                    TransformHP -= -(TempHP)
                    TempHP = 0
                    if TransformHP > 0:
                        print("Current Temporary HP:", TempHP)
                        print("Current Transformation HP:", TransformHP)
                        print("Current HP:", SHP)
                        print()
                        print("-" * 172)
                    elif TransformHP <= 0:
                        SHP -= -(TransformHP)
                        MaxTransformHP = 0
                        TransformHP = 0
                        if SHP > 0:
                            print("Current Temporary HP:", TempHP)
                            print("Current Transformation HP:", TransformHP)
                            print("Current HP:", SHP)
                            print()
                            print("-" * 172)
                        elif SHP <= 0:
                            if SHP <= 0 and SHP > -(MaxSHP):
                                SHP = 0
                                print("Current Temporary HP:", TempHP)
                                print("Current Transformation HP:", TransformHP)
                                print("Current HP:", SHP)
                                print("Sid is unconscious.")
                                print()
                                print("-" * 172)
                            elif SHP <= -(MaxSHP):
                                SHP = 0
                                print("Sid is not unconscious, he is dead...") 
            elif TempHP > 0 and TransformHP == 0:
                TempHP -= int(damage)
                if TempHP >= 0:
                    print("Current Temporary HP:", TempHP)
                    print("Current HP:", SHP)
                    print()
                    print("-" * 172)
                elif TempHP < 0:
                    SHP -= -(TempHP)
                    TempHP = 0
                    if SHP > 0:
                        print("Current Temporary HP:", TempHP)
                        print("Current HP:", SHP)
                        print()
                        print("-" * 172)
                    elif SHP <= 0:
                        if SHP <= 0 and SHP > -(MaxSHP):
                            SHP = 0
                            print("Current Temporary HP:", TempHP)
                            print("Current HP:", SHP)
                            print("Sid is unconscious.")
                            print()
                            print("-" * 172)
                        elif SHP <= -(MaxSHP):
                            SHP = 0
                            print("Sid is not unconscious, he is dead...")
            elif TempHP == 0 and TransformHP > 0:
                TransformHP -= int(damage)
                if TransformHP > 0:
                    print("Current Transformation HP:", TransformHP)
                    print("Current HP:", SHP)
                    print()
                    print("-" * 172)
                elif TransformHP <= 0:
                    SHP -= -(TransformHP)
                    MaxTransformHP = 0
                    TransformHP = 0
                    if SHP > 0:
                        print("Current Temporary HP:", TempHP)
                        print("Current HP:", SHP)
                        print()
                        print("-" * 172)
                    elif SHP <= 0:
                        if SHP <= 0 and SHP > -(MaxSHP):
                            SHP = 0
                            print("Current Transformation HP:", TransformHP)
                            print("Current HP:", SHP)
                            print("Sid is unconscious.")
                            print()
                            print("-" * 172)
                        elif SHP <= -(MaxSHP):
                            SHP = 0
                            print("Sid is not unconscious, he is dead...")
            elif TempHP == 0 and TransformHP == 0:
                SHP -= int(damage)
                if SHP > 0:
                    print("Current HP:", SHP)
                    print()
                    print("-" * 172)
                elif SHP <= 0:
                    if SHP <= 0 and SHP > -(MaxSHP):
                        SHP = 0
                        print("Current HP:", SHP)
                        print("Sid is unconscious.")
                        print()
                        print("-" * 172)
                    elif SHP <= -(MaxSHP):
                        SHP = 0
                        print("Sid is not unconscious, he is dead...")
        if HP == "2":
            heal = input("Insert heal amount: ")
            if TransformHP > 0:
                TransformHP += int(heal)
                if TransformHP > MaxTransformHP:
                    TransformHP = MaxTransformHP
                print("Current Transformation HP:", TransformHP)
                print("Current HP:", SHP)
                print()
                print("-" * 172)
            elif TransformHP == 0:
                SHP += int(heal)
                if SHP > MaxSHP:
                    SHP = MaxSHP
                print("Current HP:", SHP)
                print()
                print("-" * 172)
        elif HP == "3":
            thp = input("Insert temporary HP gain: ")
            TempHP += int(thp)
            print("Current Temporary HP:", TempHP)
            print("Current HP:", SHP)
            print()
            print("-" * 172)
        elif HP == "4":
            trhp = input("Insert transformation HP: ")
            MaxTransformHP = int(trhp)
            TransformHP = int(trhp)
            print("Current Transformation HP:", TransformHP)
            print()
            print("-" * 172)
        elif HP == "5":
            SHP = MaxSHP
            TempHP = 0
            print("Current HP:", SHP)
            print()
            print("-" * 172)
elif CHP == "2":
    while True:
        print("1: Damage\n2: Heal\n3: Temporary HP\n4: Transform HP\n5: Long Rest")
        HP = input("Insert Damage, Heal, Temp HP, Transform HP, or Long Rest: ")
        print()
        print("-" * 172)
        if HP == "1":
            damage = input("Insert damage taken: ")
            if TempHP > 0 and TransformHP > 0:
                TempHP -= int(damage)
                if TempHP >= 0:
                    print("Current Temporary HP:", TempHP)
                    print("Current Transformation HP:", TransformHP)
                    print("Current HP:", WHP)
                    print()
                    print("-" * 172)
                elif TempHP < 0 and TransformHP > 0:
                    TransformHP -= -(TempHP)
                    TempHP = 0
                    if TransformHP > 0:
                        print("Current Temporary HP:", TempHP)
                        print("Current Transformation HP:", TransformHP)
                        print("Current HP:", WHP)
                        print()
                        print("-" * 172)
                    elif TransformHP <= 0:
                        WHP -= -(TransformHP)
                        MaxTransformHP = 0
                        TransformHP = 0
                        if WHP > 0:
                            print("Current Temporary HP:", TempHP)
                            print("Current Transformation HP:", TransformHP)
                            print("Current HP:", WHP)
                            print()
                            print("-" * 172)
                        elif WHP <= 0:
                            if WHP <= 0 and WHP > -(MaxWHP):
                                WHP = 0
                                print("Current Temporary HP:", TempHP)
                                print("Current Transformation HP:", TransformHP)
                                print("Current HP:", WHP)
                                print("Wrench is unconscious.")
                                print()
                                print("-" * 172)
                            elif WHP <= -(MaxWHP):
                                WHP = 0
                                print("Wrench is not unconscious, he is dead...") 
            elif TempHP > 0 and TransformHP == 0:
                TempHP -= int(damage)
                if TempHP >= 0:
                    print("Current Temporary HP:", TempHP)
                    print("Current HP:", WHP)
                    print()
                    print("-" * 172)
                elif TempHP < 0:
                    WHP -= -(TempHP)
                    TempHP = 0
                    if WHP > 0:
                        print("Current Temporary HP:", TempHP)
                        print("Current HP:", WHP)
                        print()
                        print("-" * 172)
                    elif WHP <= 0:
                        if WHP <= 0 and WHP > -(MaxWHP):
                            WHP = 0
                            print("Current Temporary HP:", TempHP)
                            print("Current HP:", WHP)
                            print("Wrench is unconscious.")
                            print()
                            print("-" * 172)
                        elif WHP <= -(MaxWHP):
                            WHP = 0
                            print("Wrench is not unconscious, he is dead...")
            elif TempHP == 0 and TransformHP > 0:
                TransformHP -= int(damage)
                if TransformHP > 0:
                    print("Current Transformation HP:", TransformHP)
                    print("Current HP:", WHP)
                    print()
                    print("-" * 172)
                elif TransformHP <= 0:
                    WHP -= -(TransformHP)
                    MaxTransformHP = 0
                    TransformHP = 0
                    if WHP > 0:
                        print("Current Temporary HP:", TempHP)
                        print("Current HP:", WHP)
                        print()
                        print("-" * 172)
                    elif WHP <= 0:
                        if WHP <= 0 and WHP > -(MaxWHP):
                            WHP = 0
                            print("Current Transformation HP:", TransformHP)
                            print("Current HP:", WHP)
                            print("Wrench is unconscious.")
                            print()
                            print("-" * 172)
                        elif WHP <= -(MaxWHP):
                            WHP = 0
                            print("Wrench is not unconscious, he is dead...")
                            print()
                            print("-" * 172)
            elif TempHP == 0 and TransformHP == 0:
                WHP -= int(damage)
                if WHP > 0:
                    print("Current HP:", WHP)
                    print()
                    print("-" * 172)
                elif WHP <= 0:
                    if WHP <= 0 and WHP > -(MaxWHP):
                        WHP = 0
                        print("Current HP:", WHP)
                        print("Wrench is unconscious.")
                        print()
                        print("-" * 172)
                    elif WHP <= -(MaxWHP):
                        WHP = 0
                        print("Wrench is not unconscious, he is dead...")
                        print()
                        print("-" * 172)
        if HP == "2":
            heal = input("Insert heal amount: ")
            if TransformHP > 0:
                TransformHP += int(heal)
                if TransformHP > MaxTransformHP:
                    TransformHP = MaxTransformHP
                print("Current Transformation HP:", TransformHP)
                print("Current HP:", WHP)
                print()
                print("-" * 172)
            elif TransformHP == 0:
                WHP += int(heal)
                if WHP > MaxWHP:
                    WHP = MaxWHP
                print("Current HP:", WHP)
                print()
                print("-" * 172)
        elif HP == "3":
            thp = input("Insert temporary HP gain: ")
            TempHP += int(thp)
            print("Current Temporary HP:", TempHP)
            print("Current HP:", WHP)
            print()
            print("-" * 172)
        elif HP == "4":
            trhp = input("Insert transformation HP: ")
            MaxTransformHP = int(trhp)
            TransformHP = int(trhp)
            print("Current Transformation HP:", TransformHP)
            print()
            print("-" * 172)
        elif HP == "5":
            WHP = MaxWHP
            TempHP = 0
            print("Current HP:", WHP)
            print()
            print("-" * 172)
        elif HP == "break":
            break
elif CHP == "3":
    while True:
        print("1: Damage\n2: Heal\n3: Temporary HP\n4: Transform HP\n5: Long Rest")
        HP = input("Insert Damage, Heal, Temp HP, Transform HP, or Long Rest: ")
        print()
        print("-" * 172)
        if HP == "1":
            damage = input("Insert damage taken: ")
            if TempHP > 0 and TransformHP > 0:
                TempHP -= int(damage)
                if TempHP >= 0:
                    print("Current Temporary HP:", TempHP)
                    print("Current Transformation HP:", TransformHP)
                    print("Current HP:", MHP)
                    print()
                    print("-" * 172)
                elif TempHP < 0 and TransformHP > 0:
                    TransformHP -= -(TempHP)
                    TempHP = 0
                    if TransformHP > 0:
                        print("Current Temporary HP:", TempHP)
                        print("Current Transformation HP:", TransformHP)
                        print("Current HP:", MHP)
                        print()
                        print("-" * 172)
                    elif TransformHP <= 0:
                        MHP -= -(TransformHP)
                        MaxTransformHP = 0
                        TransformHP = 0
                        if MHP > 0:
                            print("Current Temporary HP:", TempHP)
                            print("Current Transformation HP:", TransformHP)
                            print("Current HP:", MHP)
                            print()
                            print("-" * 172)
                        elif MHP <= 0:
                            if MHP <= 0 and MHP > -(MaxMHP):
                                MHP = 0
                                print("Current Temporary HP:", TempHP)
                                print("Current Transformation HP:", TransformHP)
                                print("Current HP:", MHP)
                                print("Mordekai is unconscious.")
                                print()
                                print("-" * 172)
                            elif MHP <= -(MaxMHP):
                                MHP = 0
                                print("Mordekai is not unconscious, he is dead...") 
            elif TempHP > 0 and TransformHP == 0:
                TempHP -= int(damage)
                if TempHP >= 0:
                    print("Current Temporary HP:", TempHP)
                    print("Current HP:", MHP)
                    print()
                    print("-" * 172)
                elif TempHP < 0:
                    MHP -= -(TempHP)
                    TempHP = 0
                    if MHP > 0:
                        print("Current Temporary HP:", TempHP)
                        print("Current HP:", MHP)
                        print()
                        print("-" * 172)
                    elif MHP <= 0:
                        if MHP <= 0 and MHP > -(MaxMHP):
                            MHP = 0
                            print("Current Temporary HP:", TempHP)
                            print("Current HP:", MHP)
                            print("Mordekai is unconscious.")
                            print()
                            print("-" * 172)
                        elif MHP <= -(MaxMHP):
                            MHP = 0
                            print("Mordekai is not unconscious, he is dead...")
            elif TempHP == 0 and TransformHP > 0:
                TransformHP -= int(damage)
                if TransformHP > 0:
                    print("Current Transformation HP:", TransformHP)
                    print("Current HP:", MHP)
                    print()
                    print("-" * 172)
                elif TransformHP <= 0:
                    MHP -= -(TransformHP)
                    MaxTransformHP = 0
                    TransformHP = 0
                    if MHP > 0:
                        print("Current Temporary HP:", TempHP)
                        print("Current HP:", MHP)
                        print()
                        print("-" * 172)
                    elif MHP <= 0:
                        if MHP <= 0 and MHP > -(MaxMHP):
                            MHP = 0
                            print("Current Transformation HP:", TransformHP)
                            print("Current HP:", MHP)
                            print("Mordekai is unconscious.")
                            print()
                            print("-" * 172)
                        elif MHP <= -(MaxMHP):
                            MHP = 0
                            print("Mordekai is not unconscious, he is dead...")
            elif TempHP == 0 and TransformHP == 0:
                MHP -= int(damage)
                if MHP > 0:
                    print("Current HP:", MHP)
                    print()
                    print("-" * 172)
                elif MHP <= 0:
                    if MHP <= 0 and MHP > -(MaxMHP):
                        MHP = 0
                        print("Current HP:", MHP)
                        print("Mordekai is unconscious.")
                        print()
                        print("-" * 172)
                    elif MHP <= -(MaxMHP):
                        MHP = 0
                        print("Mordekai is not unconscious, he is dead...")
        if HP == "2":
            heal = input("Insert heal amount: ")
            if TransformHP > 0:
                TransformHP += int(heal)
                if TransformHP > MaxTransformHP:
                    TransformHP = MaxTransformHP
                print("Current Transformation HP:", TransformHP)
                print("Current HP:", MHP)
                print()
                print("-" * 172)
            elif TransformHP == 0:
                MHP += int(heal)
                if MHP > MaxMHP:
                    MHP = MaxMHP
                print("Current HP:", MHP)
                print()
                print("-" * 172)
        elif HP == "3":
            thp = input("Insert temporary HP gain: ")
            TempHP += int(thp)
            print("Current Temporary HP:", TempHP)
            print("Current HP:", MHP)
            print()
            print("-" * 172)
        elif HP == "4":
            trhp = input("Insert transformation HP: ")
            MaxTransformHP = int(trhp)
            TransformHP = int(trhp)
            print("Current Transformation HP:", TransformHP)
            print()
            print("-" * 172)
        elif HP == "5":
            MHP = MaxMHP
            TempHP = 0
            print("Current HP:", MHP)
            print()
            print("-" * 172)