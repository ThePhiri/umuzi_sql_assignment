#requirements
import mysql.connector 
#connect to database
connection = mysql.connector.connect(host='localhost',
                            database='Umuzi',
                            user='root',
                            password='root')
# Create a Cursor object to execute queries.
cursor = connection.cursor()
cursor.execute("""CREATE SCHEMA IF NOT EXISTS `Umuzi` DEFAULT CHARACTER SET latin1 """)
#-- -----------------------------------------------------
#-- Table `Umuzi`.`Customers`
#-- -----------------------------------------------------
cursor.execute("""CREATE TABLE IF NOT EXISTS `Umuzi`.`Customers` (
  `CustomerID` INT(11) NOT NULL AUTO_INCREMENT,
  `FirstName` VARCHAR(100) NULL DEFAULT NULL,
  `LastName` VARCHAR(100) NULL DEFAULT NULL,
  `Gender` ENUM('M', 'F') NULL DEFAULT NULL,
  `Address` VARCHAR(250) NULL DEFAULT NULL,
  `Phone` INT(12) NULL DEFAULT NULL,
  `Email` VARCHAR(100) NULL DEFAULT NULL,
  `City` VARCHAR(100) NULL DEFAULT NULL,
  `Country` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`CustomerID`)) """)
#-- -----------------------------------------------------
#-- Table `Umuzi`.`Employees`
#-- -----------------------------------------------------
cursor.execute("""CREATE TABLE IF NOT EXISTS `Umuzi`.`Employees` (
  `EmployeeID` INT(11) NOT NULL AUTO_INCREMENT,
  `FirstName` VARCHAR(50) NULL DEFAULT NULL,
  `LastName` VARCHAR(50) NULL DEFAULT NULL,
  `Email` VARCHAR(100) NULL DEFAULT NULL,
  `JobTitle` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`EmployeeID`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = latin1;""")
#-- -----------------------------------------------------
#-- Table `Umuzi`.`Orders`
#-- -----------------------------------------------------
cursor.execute("""CREATE TABLE IF NOT EXISTS `Umuzi`.`Orders` (
  `OrderID` INT(11) NOT NULL AUTO_INCREMENT,
  `OrderDate` DATETIME NULL DEFAULT NULL,
  `RequiredDate` DATE NULL DEFAULT NULL,
  `ShippedDate` DATE NULL DEFAULT NULL,
  `Status` ENUM('SHIPPED', 'NOTSHIPPED') NULL DEFAULT 'NOTSHIPPED',
  PRIMARY KEY (`OrderID`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = latin1;""")
#-- -----------------------------------------------------
#-- Table `Umuzi`.`Payments`
#-- -----------------------------------------------------
cursor.execute("""CREATE TABLE IF NOT EXISTS `Umuzi`.`Payments` (
  `PaymentID` INT(11) NOT NULL AUTO_INCREMENT,
  `CustomerID` INT(11) NULL DEFAULT NULL,
  `PaymentDate` DATETIME NULL DEFAULT NULL,
  `Amount` DECIMAL(10,2) NULL DEFAULT NULL,
  PRIMARY KEY (`PaymentID`),
  INDEX `fk_CustomerID_idx` (`CustomerID` ASC),
  CONSTRAINT `fk_CustomerID`
    FOREIGN KEY (`CustomerID`)
    REFERENCES `Umuzi`.`Customers` (`CustomerID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = latin1;""")
#-- -----------------------------------------------------
#-- Table `Umuzi`.`Products`
#-- -----------------------------------------------------
cursor.execute("""CREATE TABLE IF NOT EXISTS `Umuzi`.`Products` (
  `ProductID` INT(11) NOT NULL AUTO_INCREMENT,
  `ProductName` VARCHAR(100) NULL DEFAULT NULL,
  `Description` VARCHAR(150) NULL DEFAULT NULL,
  `BuyPrice` DECIMAL(10,2) NULL DEFAULT NULL,
  PRIMARY KEY (`ProductID`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = latin1;""")


#7. SELECT ALL records from table Customers.
cursor.execute("SELECT * FROM Customers")
records = cursor.fetchall()

print ("Printing each row's column values i.e.  developer record")
for row in records:
    print("CustomerID = ", row[0], )
    print("FirstName = ", row[1])
    print("LastName  = ", row[2])
    print("Gender  = ", row[3])
    print("Address  = ", row[4])
    print("Phone  = ", row[5])
    print("Email  = ", row[6])
    print("City  = ", row[7])
    print("Country  = ", row[8])
    print(" ")


# 8. SELECT records only from the name column in the Customers table.
cursor.execute("SELECT FirstName, LastName FROM Customers")
records = cursor.fetchall()

print ("Printing each row's column values i.e.  developer record")
for row in records:
    print("FirstName = ", row[0], )
    print("LastName = ", row[1])
    
    print(" ")
cursor.close()

 
#9. 	Show the name of the Customer whose CustomerID is 1.
 
10.  UPDATE the record for CustomerID =1  on the Customer table so that the name is “Lerato Mabitso”.
 
11.  DELETE the record from the Customers table for customer 2 (CustomerID = 2).
 
12.  Select all unique values from the table Products.
 
13.  Return the MAXIMUM payment made on the PAYMENTS table.
 
14.  Create a query that selects all customers from the "Customers" table, sorted by the "Country" column.
 
15.  Create a query that selects all Products with a price BETWEEN R100 and R600.
 
16.  Create a query that selects all fields from "Customers" where country is "Germany" AND city is "Berlin".
 
17.  Create a query that selects all fields from "Customers" where city is "Cape Town" OR "Durban".
 
18.  Select all records from Products where the Price is GREATER than R500.
 
19.  Return the sum of the Amounts on the Payments table.
 
20.  Count the number of shipped orders in the Orders table.

21.  Return the average price of all Products, in Rands and in Dollars (assume the exchange rate is R12 to the Dollar).
 
22.  Using INNER JOIN create a query that selects all Orders with Customer information.
 
23.  Document what information is stored in your database. Be sure to say what information is kept in what table, and which keys link the records between tables.

  