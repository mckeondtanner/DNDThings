DROP TABLE IF EXISTS comments;
DROP TABLE IF EXISTS pc;

CREATE TABLE pc (
PCID INT AUTO_INCREMENT,
fname VARCHAR(20) NOT NULL,
lname VARCHAR(20),
race VARCHAR(50) NOT NULL,
class VARCHAR(50) NOT NULL,
description VARCHAR(500),
PRIMARY KEY (PCID)
) ENGINE = INNODB;

CREATE TABLE comments (
    CID INT AUTO_INCREMENT,
    comment VARCHAR(500) NOT NULL,
    PRIMARY KEY (CID)
) ENGINE = INNODB;

INSERT INTO pc (PCID, fname, lname, race, class, description) VALUES
(1, "Aoife", NULL,"Human", "Valor Bard", "Deceased - Rich - A drunk"),
(2, "Arlo", NULL, "Human", "Arcane Trickster Rogue", "Yoru from Valorant"),
(3, "Blec", NULL, "Human", "Drakewarden Ranger", "Likes to brood"),
(4, "Bonito", NULL, "Tabaxi", "Shadow Monk", "Likes fish"),
(5, "Cyrus", "Victorious", "Human", "Oath of Glory Paladin", "Likes winning - Former professional athlete before a devastating leg injury"),
(6, "Jitaro", NULL, "Human", "War Magic Wizard", "Deceased - Crypto grunt"),
(7, "Kasimir", NULL, "Elf?", "Watchers Paladin / Hexblade Warlock", "Has a passion for killing evil and bringing justice to otherworldly beings"),
(8, "Obsidian", NULL, "Earth Genasi / Stone Giant", "Rune Knight Fighter / Grave Cleric", "A giant unhuggable rock - Focuses on the balance of life and death"),
(9, "Oleg", "Drawd", "Dwarf", "Trickery Cleric", "Cleric of Tymora - Dislikes Wrench"),
(10, "Oliver", "Le'vandrin", "Owlin", "Wildfire Druid", "Owlin deez nuts"),
(11, "Mira", NULL, "Chrysallis", "Wild Magic Sorcerer", "Just wanted to leave home and have fun"),
(12, "Saffron", NULL, "Fairy", "Pyrotechnician Artificer / Creation Bard", "Likes to watch TikTok for an hour before bed"),
(13, "Scorch", NULL, "Red Dragonborn", "Wild Magic Barbarian", "Own power is killing himself, possible ticking time bomb"),
(14, "Squelch", NULL, "Kobold", "-- Artificer", "Left the party - Eco terrorist - Blew up his own lab in Silver Twilight"),
(15, "Wrench", NULL, "Kobold", "Pyrotechnician Artificer", "200IQ - Majorly dislikes Crypto - Has a fascination with anything technology");