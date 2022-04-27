-- SQL SELECT
SELECT * FROM Customers;
SELECT City FROM Customers;
SELECT DISTINCT Country FROM Customers;

-- SQL Where
SELECT * FROM Customers
  WHERE City = "Berlin";
SELECT * FROM Customers
  WHERE NOT City = "Berlin";
SELECT * FROM Customers
  WHERE CustomerID = 32;
SELECT * FROM Customers
  WHERE City = 'Berlin'
  AND PostalCode = 12209;
SELECT * FROM Customers
  WHERE City = 'Berlin'
  OR City = 'London';

-- SQL Order By (alphabetical default)
SELECT * FROM Customers
  ORDER BY City;
SELECT * FROM Customers
  ORDER BY City DESC;
SELECT * FROM Customers
  ORDER BY Country, City;

-- SQL Insert
INSERT INTO Customers (
  CustomerName,
  Address,
  City,
  PostalCode,
  Country
)
VALUES (
  'Hekkan Burger',
  'Gatveien 15',
  'Sandnes',
  '4306',
  'Norway'
)

-- SQL Null
SELECT * FROM Customers
  WHERE PostalCode IS NULL;
SELECT * FROM Customers
  WHERE PostalCode IS NOT NULL;

-- SQL Update
UPDATE Customers
  SET City = 'Oslo';
UPDATE Customers
  SET City = 'Oslo'
  WHERE Country = 'Norway';
UPDATE Customers
  SET
    City = 'Oslo',
    Country = 'Norway'
  WHERE Country = 'Norway';

-- SQL Delete
DELETE FROM Customers
  WHERE Country = 'Norway';
DELETE FROM Customers;

-- SQL Functions (MIN, MAX, COUNT, AVG, SUM)
SELECT MIN(Price) FROM Products;
SELECT MAX(Price) FROM Products;
SELECT COUNT(*) FROM Products
  WHERE Price = 18;
SELECT AVG(Price) FROM Products;
SELECT SUM(Price) FROM Products;

-- SQL Like
SELECT * FROM Customers
  WHERE City LIKE 'a%' -- Select all records where the value of the City column starts with the letter "a".
SELECT * FROM Customers
  WHERE City LIKE '%a' -- Select all records where the value of the City column ends with the letter "a".
SELECT * FROM Customers
  WHERE City LIKE '%a%' -- Select all records where the value of the City column contains the letter "a".
SELECT * FROM Customers
  WHERE City LIKE 'a%b' -- Select all records where the value of the City column starts with letter "a" and ends with the letter "b".
SELECT * FROM Customers
  WHERE City NOT LIKE 'a%'

-- SQL Wildcards
SELECT * FROM Customers
  WHERE City LIKE '_a%' -- second letter is an a
SELECT * FROM Customers
  WHERE City LIKE '[acs]%' -- first letter is "a" or "c" or "s"
SELECT * FROM Customers
  WHERE City LIKE '[a-f]%' -- first letter is a through f
SELECT * FROM Customers
  WHERE City LIKE '[!acf]%' -- first letter is NOT a, c, or f

-- SQL In
SELECT * FROM Customers
  WHERE Country IN ('Norway','France');

-- SQL Between
SELECT * FROM Products
  WHERE Price BETWEEN 10 AND 20;
SELECT * FROM Products
  WhERE ProductName BETWEEN 'Geitost' AND 'Pavlova'

-- SQL Alias
SELECT
  CustomerName,
  Address,
  PostalCode as Pno
  FROM Customers;
SELECT * FROM Customers AS Consumers;

-- SQL Join
SELECT * FROM Orders
  LEFT JOIN Customers
  On Orders.CustomerID=Customers.CustomerID; -- Insert the missing parts in the JOIN clause to join the two tables Orders and Customers, using the CustomerID field in both tables as the relationship between the two tables.
SELECT * FROM Orders
  INNER JOIN Customers
  On Orders.CustomerID=Customers.CustomerID; -- Choose the correct JOIN clause to select all records from the two tables where there is a match in both tables.
SELECT * FROM Orders
  RIGHT JOIN Customers
  On Orders.CustomerID=Customers.CustomerID; -- Choose the correct JOIN clause to select all records from the two tables where there is a match in both tables.

-- SQL Group By
SELECT COUNT(CustomerID), Country
  FROM Customers
  GROUP BY Country;
SELECT COUNT(CustomerID), Country
  FROM Customers
  GROUP BY Country
  ORDER BY COUNT(CustomerID) DESC; -- List the number of customers in each country, ordered by the country with the most customers first.

-- SQL Database
CREATE DATABASE testDB; -- create database
DROP DATABASE testDB; -- delete database
CREATE TABLE Persons (
  PersonID int,
  LastName varchar(255),
  FirstName varchar(255),
  Address varchar(255),
  City varchar(255)
);
DROP TABLE Persons;
TRUNCATE TABLE Persons; -- deletes all data inside table
ALTER TABLE Persons
  ADD Birthday DATE; -- add column of type DATE called Birthday
ALTER TABLE Persons
  DROP COLUMN Birthday; -- Delete the column Birthday from the Persons table.
