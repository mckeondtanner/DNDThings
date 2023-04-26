class Character:
    def __init__(self, name, maxhp, hp, temphp, maxtranshp, transhp):
        self.name = name
        self.maxhp = maxhp
        self.hp = hp
        self.temphp = temphp
        self.maxtranshp = maxtranshp
        self.transhp = transhp

    def all(self):
        print("\nCharacter: " + self.name)
        print("Maximum HP: " + str(self.maxhp))
        print("Current HP: " + str(self.hp))
        print("Current Temporary HP: " + str(self.temphp))
        print("Current Transform HP: " + str(self.transhp))
        print("\n" + "-" * 133)

    def healhp(self, heal):
        self.hp += heal
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        print("\nCurrent HP: " + str(self.hp))
        print("\n" + "-" * 133)
    
    def healtranshp(self, heal):
        self.transhp += heal
        if self.transhp > self.maxtranshp:
            self.transhp = self.maxtranshp
        print("\nCurrent Transform HP: " + str(self.transhp))
        print("\n" + "-" * 133)
    
    def gaintemphp(self, gain):
        if self.temphp > 0:
            self.temphp = 0
        self.temphp += gain
        print("\nCurrent Temporary HP: " + str(self.temphp))
        print("\n" + "-" * 133)
    
    def gaintransformhp(self, gain):
        if self.maxtranshp > 0:
            self.transhp = 0
            self.maxtranshp = 0
        self.transhp = gain
        self.maxtranshp = gain
        print("\nCurrent Transform HP: " + str(self.transhp))
        print("\n" + "-" * 133)

    def hpdamage(self, damage):
        self.hp -= damage
        if self.hp > 0:
            print("\nCurrent HP: " + str(self.hp))
            print("\n" + "-" * 133)
        elif self.hp <= 0 and self.hp > -(self.maxhp):
            print("\n" + self.name + " is unconscious.")
            print("\n" + "-" * 133)
            self.hp = 0
        else:
            print("\n" + self.name + " is dead.")
            print("\n" + "-" * 133)
            self.hp = 0
        
    def tempdamage(self, damage):
        self.temphp -= damage
        if self.temphp < 1:
            storage = -(self.temphp)
            self.temphp = 0
            self.hpdamage(storage)
        else:
            print("\nCurrent Temporary HP: " + str(self.temphp))
            print("\n" + "-" * 133)
    
    def transdamage(self, damage):
        self.transhp -= damage
        if self.transhp > 0:
            print("\nCurrent Transform HP: " + str(self.transhp))
            print("\n" + "-" * 133)
        else:
            storage = -(self.transhp)
            self.transhp = 0
            self.maxtranshp = 0
            self.hpdamage(storage)
    
    def temptransdamage(self, damage):
        self.temphp -= damage
        if self.temphp > 0:
            print("\nCurrent Temporary HP: " + str(self.temphp))
            print("Current Transform HP: " + str(self.transhp))
            print("\n" + "-" * 133)
        elif self.temphp <= 0:
            storage = -(self.temphp)
            self.temphp = 0
            self.transdamage(storage)
    
    def longrest(self):
        self.hp = self.maxhp
        self.temphp = 0
        self.transhp = 0
        self.maxtranshp = 0
        self.all()

def validhp(edit):
    if edit in ['1', '2', '3', '4', '5', 'break']:
        return edit
    else:
        return ""

def validchar(char):
    if char in ['1', '2', '3']:
        return char
    else:
        return ""

Mordekai = Character("Miro", 51, 51, 0, 0, 0)
Sid = Character("Sid", 77, 77, 0, 0, 0)
Wrench = Character("Wrench", 52, 52, 0, 0, 0)

while True:
    print("1: Miro\n2: Sid\n3: Wrench")
    char = input("Insert Character: ")
    print("\n" + "-" * 133)
    if char == "1":
        while True:
            print("\n1: Damage\n2: Heal\n3: Temporary HP\n4: Transform HP\n5: Long Rest\n6: See All HP")
            edit = input("Insert Damage, Heal, Temp HP, Transform HP, Long Rest, or All: ")
            print("\n" + "-" * 133)
            if edit == "1":
                damage = input("Insert damage taken: ")
                if Mordekai.temphp > 0 and Mordekai.maxtranshp > 0:
                    Mordekai.temptransdamage(int(damage))
                elif Mordekai.temphp == 0 and Mordekai.maxtranshp > 0:
                    Mordekai.transdamage(int(damage))
                elif Mordekai.temphp > 0 and Mordekai.maxtranshp == 0:
                    Mordekai.tempdamage(int(damage))
                else:
                    Mordekai.hpdamage(int(damage))
            elif edit == "2":
                heal = input("Insert heal taken: ")
                if Mordekai.maxtranshp > 0:
                    Mordekai.healtranshp(int(heal))
                else:
                    Mordekai.healhp(int(heal))
            elif edit == "3":
                gain = input("Insert temporary HP gained: ")
                Mordekai.gaintemphp(int(gain))
            elif edit == "4":
                gain = input("Insert transform HP gained: ")
                Mordekai.gaintransformhp(int(gain))
            elif edit == "5":
                Mordekai.longrest()
            elif edit == "6":
                Mordekai.all()
            elif edit == "break":
                break
    if char == "2":
        while True:
            print("1: Damage\n2: Heal\n3: Temporary HP\n4: Transform HP\n5: Long Rest\n6: See All HP")
            edit = input("Insert Damage, Heal, Temp HP, Transform HP, Long Rest, or All: ")
            print("\n" + "-" * 133)
            if edit == "1":
                damage = input("Insert damage taken: ")
                if Sid.temphp > 0 and Sid.maxtranshp > 0:
                    Sid.temptransdamage(int(damage))
                elif Sid.temphp == 0 and Sid.maxtranshp > 0:
                    Sid.transdamage(int(damage))
                elif Sid.temphp > 0 and Sid.maxtranshp == 0:
                    Sid.tempdamage(int(damage))
                else:
                    Sid.hpdamage(int(damage))
            elif edit == "2":
                heal = input("Insert heal taken: ")
                if Sid.maxtranshp > 0:
                    Sid.healtranshp(int(heal))
                else:
                    Sid.healhp(int(heal))
            elif edit == "3":
                gain = input("Insert temporary HP gained: ")
                Sid.gaintemphp(int(gain))
            elif edit == "4":
                gain = input("Insert transform HP gained: ")
                Sid.gaintransformhp(int(gain))
            elif edit == "5":
                Sid.longrest()
            elif edit == "6":
                Sid.all()
            elif edit == "break":
                break
    if char == "3":
        while True:
            print("1: Damage\n2: Heal\n3: Temporary HP\n4: Transform HP\n5: Long Rest\n6: See All HP")
            edit = input("Insert Damage, Heal, Temp HP, Transform HP, Long Rest, or All: ")
            print("\n" + "-" * 133)
            if edit == "1":
                damage = input("Insert damage taken: ")
                if Wrench.temphp > 0 and Wrench.maxtranshp > 0:
                    Wrench.temptransdamage(int(damage))
                elif Wrench.temphp == 0 and Wrench.maxtranshp > 0:
                    Wrench.transdamage(int(damage))
                elif Wrench.temphp > 0 and Wrench.maxtranshp == 0:
                    Wrench.tempdamage(int(damage))
                else:
                    Wrench.hpdamage(int(damage))
            elif edit == "2":
                heal = input("Insert heal taken: ")
                if Wrench.maxtranshp > 0:
                    Wrench.healtranshp(int(heal))
                else:
                    Wrench.healhp(int(heal))
            elif edit == "3":
                gain = input("Insert temporary HP gained: ")
                Wrench.gaintemphp(int(gain))
            elif edit == "4":
                gain = input("Insert transform HP gained: ")
                Wrench.gaintransformhp(int(gain))
            elif edit == "5":
                Wrench.longrest()
            elif edit == "6":
                Wrench.all()
            elif edit == "break":
                break