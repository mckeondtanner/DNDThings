import random
from re import sub

classes = random.randrange(1, 14)
subclasses3 = random.randrange(1, 3)
subclasses4 = random.randrange(1, 4)
subclasses7 = random.randrange(1, 7)
subclasses8 = random.randrange(1, 8)
subclasses9 = random.randrange(1, 9)
subclasses10 = random.randrange(1, 10)
subclasses12 = random.randrange(1, 12)
subclasses13 = random.randrange(1, 13)
subclasses15 = random.randrange(1, 15)

if classes == 1:
    if subclasses4 == 1:
        print("Alchemist Artificer")
    elif subclasses4 == 2:
        print("Armorer Artificer")
    elif subclasses4 == 3:
        print("Artillerist Artificer")
    elif subclasses4 == 4:
        print("Battlesmith Artificer")
elif classes == 2:
    if subclasses8 == 1:
        print("Path of the Ancestral Guardian Barbarian")
    elif subclasses8 == 2:
        print("Path of the Battlerager Barbarian")
    elif subclasses8 == 3:
        print("Path of the Beast Barbarian")
    elif subclasses8 == 4:
        print("Path of the Berserker Barbarian")
    elif subclasses8 == 5:
        print("Path of the Storm Herald Barbarian")
    elif subclasses8 == 6:
        print("Path of the Totem Warrior Barbarian")
    elif subclasses8 == 7:
        print("Path of Wild Magic Barbarian")
    elif subclasses8 == 8:
        print("Path of the Zealot Barbarian")
elif classes == 3:
    if subclasses8 == 1:
        print("College of Creation Bard")
    elif subclasses8 == 2:
        print("College of Eloquence Bard")
    elif subclasses8 == 3:
        print("College of Lore Bard")
    elif subclasses8 == 4:
        print("College of Glamour Bard")
    elif subclasses8 == 5:
        print("College of Spirits Bard")
    elif subclasses8 == 6:
        print("College of Swords Bard")
    elif subclasses8 == 7:
        print("College of Valor Bard")
    elif subclasses8 == 8:
        print("College of Whispers Bard")
elif classes == 4:
    if subclasses3 == 1:
        print("Ghostslayer Bloodhunter")
    elif subclasses3 == 2:
        print("Lycan Bloodhunter")
    elif subclasses3 == 3:
        print("Mutant Bloodhunter")
elif classes == 5:
    if subclasses13 == 1:
        print("Arcana Cleric")
    elif subclasses13 == 2:
        print("Forge Cleric")
    elif subclasses13 == 3:
        print("Grave Cleric")
    elif subclasses13 == 4:
        print("Knowledge Cleric")
    elif subclasses13 == 5:
        print("Life Cleric")
    elif subclasses13 == 6:
        print("Light Cleric")
    elif subclasses13 == 7:
        print("Nature Cleric")
    elif subclasses13 == 8:
        print("Order Cleric")
    elif subclasses13 == 9:
        print("Peace Cleric")
    elif subclasses13 == 10:
        print("Tempest Cleric")
    elif subclasses13 == 11:
        print("Trickery Cleric")
    elif subclasses13 == 12:
        print("Twilight Cleric")
    elif subclasses13 == 13:
        print("War Cleric")
elif classes == 6:
    if subclasses7 == 1:
        print("Dreams Druid")
    elif subclasses7 == 2:
        print("Land Druid")
    elif subclasses7 == 3:
        print("Moon Druid")
    elif subclasses7 == 4:
        print("Shepherd Druid")
    elif subclasses7 == 5:
        print("Spores Druid")
    elif subclasses7 == 6:
        print("Stars Druid")
    elif subclasses7 == 7:
        print("Wildfire Druid")
elif classes == 7:
    if subclasses12 == 1:
        print("Arcane Archer Fighter")
    elif subclasses12 == 2:
        print("Battle Master Fighter")
    elif subclasses12 == 3:
        print("Cavalier Fighter")
    elif subclasses12 == 4:
        print("Champion Fighter")
    elif subclasses12 == 5:
        print("Echo Knight Fighter")
    elif subclasses12 == 6:
        print("Eldrich Knight Fighter")
    elif subclasses12 == 7:
        print("Gunslinger Fighter")
    elif subclasses12 == 8:
        print("Psi Warrior Fighter")
    elif subclasses12 == 9:
        print("Psychic Warrior Fighter")
    elif subclasses12 == 10:
        print("Purple Dragon Knight Fighter")
    elif subclasses12 == 11:
        print("Rune Knight Fighter")
    elif subclasses12 == 12:
        print("Samurai Fighter")
elif classes == 8:
    if subclasses12 == 1:
        print("Ascendant Dragon Monk")
    elif subclasses12 == 2:
        print("Astral Self Monk")
    elif subclasses12 == 3:
        print("Cobalt Soul Monk")
    elif subclasses12 == 4:
        print("Drunken Master Monk")
    elif subclasses12 == 5:
        print("Four Elements Monk")
    elif subclasses12 == 6:
        print("Kensei Monk")
    elif subclasses12 == 7:
        print("Long Death Monk")
    elif subclasses12 == 8:
        print("Mercy Monk")
    elif subclasses12 == 9:
        print("Open Hand Monk")
    elif subclasses12 == 10:
        print("Shadow Monk")
    elif subclasses12 == 11:
        print("Soul Knife Monk")
    elif subclasses12 == 12:
        print("Sun Soul Monk")
elif classes == 9:
    if subclasses10 == 1:
        print("Oath of the Ancients Paladin")
    elif subclasses10 == 2:
        print("Oath of Conquest Paladin")
    elif subclasses10 == 3:
        print("Oath of the Crown Paladin")
    elif subclasses10 == 4:
        print("Oath of Devotion Paladin")
    elif subclasses10 == 5:
        print("Oath of Glory Paladin")
    elif subclasses10 == 6:
        print("Oath of Heroism Paladin")
    elif subclasses10 == 7:
        print("Oath Breaker Paladin")
    elif subclasses10 == 8:
        print("Oath of Redemption Paladin")
    elif subclasses10 == 9:
        print("Oath of Vengeance Paladin")
    elif subclasses10 == 10:
        print("Oath of the Watchers Paladin")
elif classes == 10:
    if subclasses8 == 1:
        print("Beast Master Ranger")
    elif subclasses8 == 2:
        print("Drakewarden Ranger")
    elif subclasses8 == 3:
        print("Fey Wanderer Ranger")
    elif subclasses8 == 4:
        print("Gloom Stalker Ranger")
    elif subclasses8 == 5:
        print("Horizon Walker Ranger")
    elif subclasses8 == 6:
        print("Hunter Ranger")
    elif subclasses8 == 7:
        print("Monster Slayer Ranger")
    elif subclasses8 == 8:
        print("Swarm Keeper Ranger")
elif classes == 11:
    if subclasses10 == 1:
        print("Arcane Trickster Rogue")
    elif subclasses10 == 2:
        print("Assassin Rogue")
    elif subclasses10 == 3:
        print("Inquisitive Rogue")
    elif subclasses10 == 4:
        print("Mastermind Rogue")
    elif subclasses10 == 5:
        print("Phantom Rogue")
    elif subclasses10 == 6:
        print("Revived Rogue")
    elif subclasses10 == 7:
        print("Scout Rogue")
    elif subclasses10 == 8:
        print("Soulknife Rogue")
    elif subclasses10 == 9:
        print("Swashbuckler Rogue")
    elif subclasses10 == 10:
        print("Thief Rogue")
elif classes == 12:
    if subclasses9 == 1:
        print("Abberant Mind Sorcerer")
    elif subclasses9 == 2:
        print("Clockwork Soul Sorcerer")
    elif subclasses9 == 3:
        print("Divine Soul Sorcerer")
    elif subclasses9 == 4:
        print("Draconic Bloodline Sorcerer")
    elif subclasses9 == 5:
        print("Giant Soul Sorcerer")
    elif subclasses9 == 6:
        print("Psionic Mind Sorcerer")
    elif subclasses9 == 7:
        print("Shadow Magic Sorcerer")
    elif subclasses9 == 8:
        print("Storm Sorcery Sorcerer")
    elif subclasses9 == 9:
        print("Wild Magic Sorcerer")
elif classes == 13:
    if subclasses8 == 1:
        print("Archfey Warlock")
    elif subclasses10 == 2:
        print("Celestial Warlock")
    elif subclasses10 == 3:
        print("Fathomless Warlock")
    elif subclasses10 == 4:
        print("Fiend Warlock")
    elif subclasses10 == 5:
        print("Great Old One Warlock")
    elif subclasses10 == 6:
        print("Hexblade Warlock")
    elif subclasses10 == 7:
        print("Lurker in the Deep Warlock")
    elif subclasses10 == 8:
        print("Genie Warlock")
    elif subclasses10 == 9:
        print("Undead Warlock")
    elif subclasses10 == 10:
        print("Undying Warlock")
elif classes == 14:
    if subclasses15 == 1:
        print("Abjuration Wizard")
    elif subclasses15 == 2:
        print("Bladesinging Wizard")
    elif subclasses15 == 3:
        print("Chronurgy Wizard")
    elif subclasses15 == 4:
        print("Conjuration Wizard")
    elif subclasses15 == 5:
        print("Divination Wizard")
    elif subclasses15 == 6:
        print("Enchantment Wizard")
    elif subclasses15 == 7:
        print("Evocation Wizard")
    elif subclasses15 == 8:
        print("Graviturgy Wizard")
    elif subclasses15 == 9:
        print("Illusion Wizard")
    elif subclasses15 == 10:
        print("Necromancy Wizard")
    elif subclasses15 == 11:
        print("Onomancy Wizard")
    elif subclasses15 == 12:
        print("Order of Scribes Wizard")
    elif subclasses15 == 13:
        print("Psionics Wizard")
    elif subclasses15 == 14:
        print("Transmutation Wizard")
    elif subclasses15 == 15:
        print("War Magic Wizard")

races = random.randrange(1, 43)
subraces2 = random.randrange(1, 2)
subraces3 = random.randrange(1, 3)
subraces4 = random.randrange(1, 4)
subraces5 = random.randrange(1, 5)
subraces6 = random.randrange(1, 6)
subraces9 = random.randrange(1, 9)

if races == 1:
    print("Aarakocra")
elif races == 2:
    if subraces3 == 1:
        print("Protector Aasimar")
    elif subraces3 == 2:
        print("Scourge Aasimar")
    elif subraces3 == 3:
        print("Fallen Aasimar")
elif races == 3:
    print("Bugbear")
elif races == 4:
    print("Centaur")
elif races == 5:
    print("Changling")
elif races == 6:
    print("Dragonborn")
elif races == 7:
    if subraces4 == 1:
        print("Duergar Dwarf")
    elif subraces4 == 2:
        print("Hill Dwarf")
    elif subraces4 == 3:
        print("Mark of Warding")
    elif subraces4 == 4:
        print("Mountain Dwarf")
elif races == 8:
    if subraces9 == 1:
        print("Avariel Elf")
    elif subraces9 == 2:
        print("Dark Elf")
    elif subraces9 == 3:
        print("Eladrin Elf")
    elif subraces9 == 4:
        print("Grugach Elf")
    elif subraces9 == 5:
        print("High Elf")
    elif subraces9 == 6:
        print("Mark of Shadows Elf")
    elif subraces9 == 7:
        print("Sea Elf")
    elif subraces9 == 8:
        print("Shadar-kai Elf")
    elif subraces9 == 9:
        print("Wood Elf")
elif races == 9:
    print("Fairy")
elif races == 10:
    print("Firbolg")
elif races == 11:
    if subraces4 == 1:
        print("Air Genasi")
    elif subraces4 == 2:
        print("Earth Genasi")
    elif subraces4 == 3:
        print("Fire Genasi")
    elif subraces4 == 4:
        print("Water Genasi")
elif races == 12:
    if subraces2 == 1:
        print("Githyanki")
    elif subraces2 == 2:
        print("Githzerai")
elif races == 13:
    if subraces4 == 1:
        print("Forest Gnome")
    elif subraces4 == 2:
        print("Deep Gnome")
    elif subraces4 == 3:
        print("Mark of Scribing Gnome")
    elif subraces4 == 4:
        print("Rock Gnome")
elif races == 14:
    print("Goblin")
elif races == 15:
    print("Goliath")
elif races == 16:
    print("Grung")
elif races == 17:
    if subraces2 == 1:
        print("Mark of Detection")
    elif subraces2 == 2:
        print("Mark of Storm")
elif races == 18:
    print("Mark of Finding Half-Orc")
elif races == 19:
    if subraces6 == 1:
        print("Lightfoot Halfling")
    elif subraces6 == 2:
        print("Ghostwise Halfling")
    elif subraces6 == 3:
        print("Mark of Healing Halfling")
    elif subraces6 == 4:
        print("Mark of Hospitality Halfling")
    elif subraces6 == 5:
        print("Stout Halfling")
    elif subraces6 == 6:
        print("Lotusden Halfling")
elif races == 20:
    print("Harengon")
elif races == 21:
    print("Hobgoblin")
elif races == 22:
    if subraces5 == 1:
        print("Mark of Finding Human")
    elif subraces5 == 2:
        print("Mark of Handling Human")
    elif subraces5 == 3:
        print("Mark of Making- Human")
    elif subraces5 == 4:
        print("Mark of Passage Human")
    elif subraces5 == 5:
        print("Mark of Sentinel Human")
elif races == 23:
    print("Kalashtar")
elif races == 24:
    print("Kenku")
elif races == 25:
    print("Kobold")
elif races == 26:
    print("Leonin")
elif races == 27:
    print("Lizardfolk")
elif races == 28:
    print("Locathah")
elif races == 29:
    print("Loxodon")
elif races == 30:
    print("Minotaur")
elif races == 31:
    print("Orc")
elif races == 32:
    print("Owlin")
elif races == 33:
    print("Satyr")
elif races == 34:
    print("Shifter")
elif races == 35:
    print("Simic Hybrid")
elif races == 36:
    print("Tabaxi")
elif races == 37:
    if subraces9 == 1:
        print("Asmodeus Tiefling")
    elif subraces9 == 2:
        print("Baalebul Tiefling")
    elif subraces9 == 3:
        print("Dispater Tiefling")
    elif subraces9 == 4:
        print("Fierna Tiefling")
    elif subraces9 == 5:
        print("Glasya Tiefling")
    elif subraces9 == 6:
        print("Levistus Tiefling")
    elif subraces9 == 7:
        print("Mammon Tiefling")
    elif subraces9 == 8:
        print("Mephistopheles Tiefling")
    elif subraces9 == 9:
        print("Zariel Tiefling")
elif races == 38:
    print("Tortle")
elif races == 39:
    print("Triton")
elif races == 40:
    print("Vendalken")
elif races == 41:
    print("Verdan")
elif races == 42:
    print("Warforged")
elif races == 43:
    print("Yuan-Ti Pureblood")

background = random.randrange(1, 60)

if background == 1:
    print("Acolyte")
elif background == 2:
    print("Anthropologist")
elif background == 3:
    print("Archaeologist")
elif background == 4:
    print("Athlete")
elif background == 5:
    print("Azorius Functionary")
elif background == 6:
    print("Boros Legionnaire")
elif background == 7:
    print("Celebrity Adventurer's Scion")
elif background == 8:
   print("Charlatan")
elif background == 9:
    print("City Watch / Investigator")
elif background == 10:
    print("Clan Crafter")
elif background == 11:
    print("Cloistered Scholar")
elif background == 12:
    print("Courtier")
elif background == 13:
    print("Criminal / Spy")
elif background == 14:
    print("Dimir Operative")
elif background == 15:
    print("Entertainer / Gladiator")
elif background == 16:
    print("Faceless")
elif background == 17:
    print("Faction Agent")
elif background == 18:
    print("Failed Merchant")
elif background == 19:
    print("Far Traveler")
elif background == 20:
    print("Feylost")
elif background == 21:
    print("Fisher")
elif background == 22:
    print("Folk Hero")
elif background == 23:
    print("Gambler")
elif background == 24:
    print("Golgari Agent")
elif background == 25:
    print("Grinner")
elif background == 26:
    print("Gruul Anarch")
elif background == 27:
    print("Guild Artisan / Guild Merchant")
elif background == 28:
    print("Haunted One")
elif background == 29:
    print("Hermit")
elif background == 30:
    print("House Agent")
elif background == 31:
    print("Inheritor")
elif background == 32:
    print("Investigator")
elif background == 33:
    print("Izzet Engineer")
elif background == 34:
    print("Knight of the Order")
elif background == 35:
    print("Lorehold Student")
elif background == 36:
    print("Marine")
elif background == 37:
    print("Mercenary Veteran")
elif background == 38:
    print("Noble / Knight")
elif background == 39:
    print("Orzhov Representative")
elif background == 40:
    print("Outlander")
elif background == 41:
    print("Prismari Student")
elif background == 42:
    print("Plaintiff")
elif background == 43:
    print("Quandrix Student")
elif background == 44:
    print("Rakdos Student")
elif background == 45:
    print("Rival Intern")
elif background == 46:
    print("Sage")
elif background == 47:
    print("Sailor / Pirate")
elif background == 48:
    print("Selesnya Initiate")
elif background == 49:
    print("Shipwrite")
elif background == 50:
    print("Silverquill Student")
elif background == 51:
    print("Simic Scientist")
elif background == 52:
    print("Smuggler")
elif background == 53:
    print("Soldier")
elif background == 54:
    print("Urban Bounty Hunter")
elif background == 55:
    print("Urchin")
elif background == 56:
    print("Uthgardt Tribe Member")
elif background == 57:
    print("Volstrucker Agent")
elif background == 58:
    print("Waterdhavian Noble")
elif background == 59:
    print("Witchlight Hand")
elif background == 60:
    print("Witherbloom Student")