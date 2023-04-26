DROP TABLE IF EXISTS guild;
DROP TABLE IF EXISTS object;
DROP TABLE IF EXISTS location;
DROP TABLE IF EXISTS creatureinstance;
DROP TABLE IF EXISTS creaturegroup;
DROP TABLE IF EXISTS creature;

CREATE TABLE creature (
CID INT AUTO_INCREMENT,
name VARCHAR(50) NOT NULL,
description VARCHAR(500),
PRIMARY KEY (CID)
) ENGINE = INNODB;

CREATE TABLE creaturegroup (
    CGID INT AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(500),
    PRIMARY KEY (CGID)
) ENGINE = INNODB;

CREATE TABLE creatureinstance (
    CIID INT AUTO_INCREMENT,
    CID INT,
    CGID INT,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(500),
    PRIMARY KEY (CIID),
    FOREIGN KEY (CID) REFERENCES creature(CID)
    FOREIGN KEY (CGID) REFERENCES creaturegroup(CGID)
) ENGINE = INNODB;

CREATE TABLE planet (
    PID INT AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    description(500),
    PRIMARY KEY (PID)
) ENGINE = INNODB;

CREATE TABLE location (
    LocID INT AUTO_INCREMENT,
    PID INT,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(500),
    PRIMARY KEY (LocID)
    FOREIGN KEY (PID) REFERENCES planet(PID)
) ENGINE = INNODB;

CREATE TABLE object (
    ObjID INT AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(500),
    PRIMARY KEY (ObjID)
) ENGINE = INNODB;

CREATE TABLE guild (
    GID INT AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(500),
    PRIMARY KEY (GID)
) ENGINE = INNODB;

INSERT INTO creature (CID, name, description) VALUES
(1, "Human", "Normal"),
(2, "Dwarf", "Short"),
(3, "Elf", "Lives long"),
(4, "Genasi / Giant", "Half n half"),
(5, "Dragonborn", "Humanoid dragon people"),
(6, "Kobold", "Small dragonborn, techies"),
(7, "Chrysallis", "Mantis people made by radiation mutation"),
(8, "Tabaxi", "Cat people"),
(9, "Owlin", "Owl people, can fly"),
(10, "Gnome", "Small people, similar to Halfling"),
(11, "Dungwhoops", "Space trash pandas, thrive on garbage, nasty and dirty, leaves waste all over space"),
(12, "Nardwhal", "Predators, generally not aggressive, uses telepathy for communication"),
(13, "Kneealfalid", "Gargantuan aberration"),
(14, "Minotaur", "Half human, half bull"),
(15, "Monolith", "Head of an octopus, multiple arms, translucent"),
(16, "Karablast", "Not of this dimension, mix between humanoid and plant, intelligent, can manipulate and communicate with nature, can live for centuries"),
(17, "Ice Phoenix", "What it sounds like"),
(18, "God", "Divine beings"),
(19, "Maw Demon", "Plant creature with teeth and eyes on its body, fiend"),
(20, "Plasmoid", "Slime people"),
(21, "Yuan-Ti", "Snake humanoids"),
(22, "Hobgoblin", "Tall, furry humanoids"),
(23, "Palandrum", "Intelligent sentient androids, natural emotions, do not eat, sleep, or breathe computer minds, hivemind"),
(24, "Harengon", "Passive bunny people"),

INSERT INTO creaturegroup (CGID, name, description) VALUES
(1, "The Wrecking Crew", "Group 1 player characters"),
(2, "Agents of Chaos", "Group 2 player characters"),
(3, "Archer", "A family that inherited a mine with various minerals until recently, sells gold, silver, and obsidian"),
(4, "The Shadows", "Kind of like Scythe and Cipher, very dangerous"),
(5, "Palimmor", "The telepaths of Peria")

INSERT INTO creatureinstance (CIID, CID, CGID, name, description) VALUES
(1, 4, 2, "Obsidian 'Sid'", "Rune Knight Fighter / Grave Cleric"),
(2, 5, 2, "Scorch", "Wild Magic Barbarian"),
(3, 6, NULL, "Squelch", "-- Artificer"),
(4, 7, 2, "Mira", "Wild Magic Sorcerer"),
(5, 8, 2, "Bonito", "Shadow Monk"),
(6, 9, 2, "Saffron", "Pyrotechnician Artificer / Creation Bard"),
(7, 3, 2, "Kasimir", "Watchers Paladin / Hexblade Warlock"),
(8, 1, NULL, "Aoife", "Valor Bard - Deceased"),
(9, 6, 1, "Wrench", "Pyrotechnician Artificer"),
(10, 9, 1, "Oliver", "Wildfire Druid"),
(11, 2, 1, "Oleg", "Trickery Cleric"),
(12, 1, NULL, "Jitaro", "War Magic Wizard - Deceased"),
(13, 1, 1, "Blec", "Drakewarden Ranger"),
(14, 1, 1, "Arlo", "Arcane Trickster Rogue"),
(15, 1, NULL, "Denebis", "Crypto traitor"),
(16, 5, NULL, "Cynthia", "Well-liked in Crypto, champion of the people - Deceased"),
(17, 10, NULL, "Darleen", "Diplomat for Crypto")
(18, 6, NULL, "Starava", "Green, works for both Kobolds and Crypto"),
(19, NULL, NULL, "Thesaurus", "Crypto traitor, one of their top spies"),
(20, NULL, NULL, "Visulai", "Head of one of Vision's monestaries"),
(21, NULL, NULL, "Tyroman", "Can move upon great distances, lives in Terraintula"),
(22, 18, NULL, "Parta", "Sun God"),
(23, 18, NULL, "Kabuk", "Fish god"),
(24, NULL, NULL, "The Seer", "Humanoid with great power"),
(25, 20, NULL, "Amolga", "Plasmoid"),
(26, 21, NULL, "Y(something)", "Emissary of Vision"),
(27, NULL, NULL, "Commander of the First Watch of the House of Remus"),
(28, 22, 4, "Scythe - Big guy of The Shadows"),
(29, 10, 4, "Cipher - Small guy of The Shadows"),
(30, 1, 1, "Cyrus - Oath of Glory Paladin"),

INSERT INTO planet (PID, name, description) VALUES
(1, "Space", "Space"),
(2, "Dimension", "Dimension"),
(3, "Azul Gigante", "Home planet for many, plagued with pointless warfare"),
(4, "Sonar Tech", "Way more technologically advanced than Azul Gigante"),
(5, "Terrera", "Primal planet, ruled by dragons and dragon people"),
(6, "Truidia", "Pleasure/vacation planet"),
(7, "Terraintula", "Covered in insecects, swamps, and lakes, strange poision permeates the atmosphere"),
(8, "Zorgoth", "Planet for Mindflayer Empire, plagued by ion storms from distortions in space"),
(9, "Morish", "Grass planet with skyscraper cacti, ruled by minotaurs, part of the Mindflayer Empire"),
(10, "Elen", "homeworld of the Astral Elves"),
(11, "Globalose", "Marsh and sea covered planet - has a giant sun with 3 phoenixes"),
(12, "Arelia", "Controlled by the Mindflayer Empire"),
(13, "Swordoff", "In a constant state of ion storms and normal storms, run by giants that are constantly at war"),
(14, "Collexia", "In the Mindflayer Empire, desolate desert, filled with slaves of other races"),
(15, "Wawllo", "Plasmoid planet where Rag hails from"),
(16, "Versaii", "Planet of telepaths"),

INSERT INTO location (LocID, PID, name, description) VALUES
(1, 3, "Einey Oasis", "Capital of the Divine Lizard Kobolds"),
(2, 3, "Silver Twilight", "Capital of Crypto"),
(3, 3, "Crystal Cave", "Near Silver Twilight, has a bunch of crystals in it, houses Chrysalis"),
(4, 2, "Spaceship Repair Shop and Floating Tacos", "Ship repair and space tacos"),
(5, 3, "Glizzar's Technological Array", "In the Underground in Silver Twilight"),
(6, 9, "City of Cyprus", "Main city on Morish"),
(7, 3, "Bartholomew Center", "Small town"),
(8, 3, "Dead Knock Forest", "Tainted with toxic fumes, undead forest, distorted trees, no leaves, no grass, mutated wildlife"),
(9, 2, "Negative Dimension", "The dimension the otherworldly creatures are coming from"),
(10, 3, "Arlomene", "Golden Pirates port city"),

INSERT INTO object (ObjID, name, description) VALUES
(1, "Archknight Phoenix 3000", "Crypto spaceship - aka Ohio - aka Rancid Mayonnaise Jar"),
(2, "Rubik's Cube", "Takes us to wierd places"),
(3, "The Knuckle Breaker", "DLK spaceship"),

INSERT INTO guild (GID, name, description) VALUES
(1, "Crypto", "Wizards - doesn't like technology very much"),
(2, "Divine Lizard Kobolds", "Kobolds - technologically advanced"),
(3, "House of Remus", "Dwarves - bloodthirsty - had harsh civil war"),
(4, "Vision", "Hobgoblins, Tabaxi, etc. - can see more than usual"),
(5, "The Crucibles", "Dragonborn - has dragons - mostly a warrior guild"),
(6, "The Hearth of Elements", "Genasi, Half-Giants, Giants - to be revealed"),
(7, "Mindflayer Empire", "Mindflayers - evil"),
(8, "The Alliance", "Human, etc. - the good guys / the vigilantes"),
(9, "Plasmoids", "Plasmoids - our allies"),
(10, "Golden Pirates Guild", "-- - Mercenaries"),
(11, "Tribes of Gilda", "Humans, etc. - nomads, hate technology"),
(12, "Euthia", "Euthia - fish people - follow the Mother")