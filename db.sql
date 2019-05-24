CREATE DATABASE intoj CHARACTER SET utf8;
use intoj;
CREATE TABLE zisheng(
	id INT NOT NULL PRIMARY KEY auto_increment,
	username VARCHAR(20),
	message TEXT,
	send_time VARCHAR(50)
);
CREATE TABLE contests(
	id INT NOT NULL PRIMARY KEY auto_increment,
	title VARCHAR(100),
	subtitle VARCHAR(100),
	begin_time VARCHAR(50),
	end_time VARCHAR(50),
	description TEXT,
	rule TEXT,
	holder_name VARCHAR(20),
	problems TEXT,
	admins TEXT
);
CREATE TABLE contest_players(
	id INT NOT NULL PRIMARY KEY auto_increment,
	username VARCHAR(20),
	contest_id INT,
	detail TEXT
);
CREATE TABLE problems(
	`id` BIGINT NOT NULL PRIMARY KEY auto_increment,
	`title` VARCHAR(100),
	`description` TEXT,
	`input_format` TEXT,
	`output_format` TEXT,
	`example` TEXT,
	`limit_and_hint` TEXT,
	`time_limit` BIGINT,
	`memory_limit` BIGINT,
	`is_public` TINYINT(1) DEFAULT 1
);
CREATE TABLE records(
	`id` BIGINT(20) NOT NULL PRIMARY KEY auto_increment,
	`problem_id` BIGINT(20) NOT NULL,
	`code` MEDIUMTEXT,
	`language` VARCHAR(50),
	`status` INT,
	`score` DOUBLE,
	`compilation` LONGTEXT,
	`result` LONGTEXT,
	`time_usage` INT,
	`memory_usage` INT,
	`system_message` TEXT,
	`username` VARCHAR(20),
	`contest_id` INT,
	`submit_time` VARCHAR(50)
);
CREATE TABLE users(
	`id` INT(11) NOT NULL PRIMARY KEY auto_increment,
	`username` VARCHAR(20),
	`password_sha256` VARCHAR(170),
	`password_sha1` VARCHAR(170),
	`email` VARCHAR(100),
	`sex` INT(2),
	`signature` TEXT,
	`group` VARCHAR(100),
	`background_url` VARCHAR(200),
	`total_ac` INT(10),
	`total_submit` INT(10),
	`ac_list` TEXT
);
CREATE TABLE user_privileges(
	`id` INT(11) NOT NULL PRIMARY KEY auto_increment,
	`username` VARCHAR(20),
	`is_admin` TINYINT(1) default 0,
	`is_user_manager` TINYINT(1) default 0,
	`is_problem_manager` TINYINT(1) default 0,
	`is_contest_manager` TINYINT(1) default 0,
	`is_tag_manager` TINYINT(1) default 0
);
