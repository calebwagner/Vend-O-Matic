CREATE TABLE `Coin` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`coin`	INTEGER NOT NULL
);

CREATE TABLE `SodaType` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE `Soda` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `cost`    INTEGER NOT NULL,
    `soda_type_id` INTEGER NOT NULL,
    FOREIGN KEY(`soda_type_id`) REFERENCES `SodaType`(`id`)
);

INSERT INTO `Coin` VALUES (null, 1);
INSERT INTO `Coin` VALUES (null, 1);

INSERT INTO `SodaType` VALUES (null);
INSERT INTO `SodaType` VALUES (null);
INSERT INTO `SodaType` VALUES (null);

INSERT INTO `Soda` VALUES (null, 2, 1);
INSERT INTO `Soda` VALUES (null, 2, 1);
INSERT INTO `Soda` VALUES (null, 2, 1);
INSERT INTO `Soda` VALUES (null, 2, 1);
INSERT INTO `Soda` VALUES (null, 2, 1);

INSERT INTO `Soda` VALUES (null, 2, 2);
INSERT INTO `Soda` VALUES (null, 2, 2);
INSERT INTO `Soda` VALUES (null, 2, 2);
INSERT INTO `Soda` VALUES (null, 2, 2);
INSERT INTO `Soda` VALUES (null, 2, 2);


INSERT INTO `Soda` VALUES (null, 2, 3);
INSERT INTO `Soda` VALUES (null, 2, 3);
INSERT INTO `Soda` VALUES (null, 2, 3);
INSERT INTO `Soda` VALUES (null, 2, 3);
INSERT INTO `Soda` VALUES (null, 2, 3);







