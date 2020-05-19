-- Create a DB named companyHR
#CREATE DATABASE companyHR;

-- Use this specific DB for the proceeding transacions
#USE companyHR;

-- Drop a database if it exists
#DROP DATABASE IF EXISTS companyHR;

DROP DATABASE IF EXISTS companyHR;
CREATE DATABASE IF NOT EXISTS companyHR;
USE companyHR;
-- Create an employees table (named co_employees to be manipulated later)
/*
CREATE TABLE co_employees (
	id 				INT PRIMARY KEY AUTO_INCREMENT,
    em_name 		VARCHAR(255) NOT NULL,
    gender 			CHAR(1) NOT NULL,
    contact_number 	VARCHAR(255),
    age 			INT NOT NULL,
    date_created 	TIMESTAMP NOT NULL DEFAULT NOW()
);
*/

DROP TABLE IF EXISTS co_employees;
CREATE TABLE IF NOT EXISTS co_employees (
	id 				INT PRIMARY KEY AUTO_INCREMENT,
    em_name 		VARCHAR(255) NOT NULL,
    gender 			CHAR(1) NOT NULL,
    contact_number 	VARCHAR(255),
    age 			INT NOT NULL,
    date_created 	TIMESTAMP NOT NULL DEFAULT NOW()
);