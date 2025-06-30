CREATE DATABASE IF NOT EXISTS bloodconnect;
USE bloodconnect;

CREATE TABLE IF NOT EXISTS donors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    blood_group VARCHAR(10),
    city VARCHAR(50),
    phone VARCHAR(15),
    email VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS requests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    requester_name VARCHAR(100),
    blood_group_needed VARCHAR(10),
    city VARCHAR(50),
    contact_phone VARCHAR(15),
    contact_email VARCHAR(100),
    reason TEXT
);
