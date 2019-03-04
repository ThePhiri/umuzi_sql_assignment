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
    ON DELETE CASCADE
    ON UPDATE CASCADE)
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


for row in records:
    print("FirstName = ", row[0], )
    print("LastName = ", row[1])
    print(" ")

print("9. Show the name of the Customer whose CustomerID is 1.")
cursor.execute("SELECT * FROM Customers WHERE CustomerID = 1")
records = cursor.fetchall()

for row in records:
    print("FirstName = ", row[1], )
    print("LastName = ", row[2])
    print(" ")

print("10.  UPDATE the record for CustomerID =1  on the Customer table so that the name is Lerato Mabitso.")

cursor.execute("UPDATE Customers SET FirstName = 'Lerato', LastName = 'Mabitso' WHERE CustomerID = 1 ")
cursor.execute("SELECT * FROM Customers WHERE CustomerID = 1")
records = cursor.fetchall()
for row in records:
    print("FirstName = ", row[1], )
    print("LastName = ", row[2])
    print(" ")

print("11.  DELETE the record from the Customers table for customer 2 (CustomerID = 2).")
cursor.execute("DELETE FROM Customers WHERE CustomerID = 2 ")
cursor.execute("SELECT * FROM Customers")
records = cursor.fetchall()


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


cursor.close()