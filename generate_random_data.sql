INSERT INTO Banks (name, location)
SELECT NEWID(), NEWID()
FROM sys.sysobjects
