IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'BankDB')
BEGIN
    CREATE DATABASE BankDB;
END

USE BankDB;

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Banks')
BEGIN
    CREATE TABLE Banks (
        id INT IDENTITY(1,1) PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        location VARCHAR(50) NOT NULL
    );
END
