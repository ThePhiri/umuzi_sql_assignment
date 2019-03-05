-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema Umuzi
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Umuzi
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Umuzi` DEFAULT CHARACTER SET latin1 ;
USE `Umuzi` ;

-- -----------------------------------------------------
-- Table `Umuzi`.`Customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Umuzi`.`Customers` (
  `CustomerID` INT(11) NOT NULL AUTO_INCREMENT,
  `FirstName` VARCHAR(100) NULL DEFAULT NULL,
  `LastName` VARCHAR(100) NULL DEFAULT NULL,
  `Gender` ENUM('M', 'F') NULL DEFAULT NULL,
  `Address` VARCHAR(250) NULL DEFAULT NULL,
  `Phone` INT(12) NULL DEFAULT NULL,
  `Email` VARCHAR(100) NULL DEFAULT NULL,
  `City` VARCHAR(100) NULL DEFAULT NULL,
  `Country` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`CustomerID`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `Umuzi`.`Employees`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Umuzi`.`Employees` (
  `EmployeeID` INT(11) NOT NULL AUTO_INCREMENT,
  `FirstName` VARCHAR(50) NULL DEFAULT NULL,
  `LastName` VARCHAR(50) NULL DEFAULT NULL,
  `Email` VARCHAR(100) NULL DEFAULT NULL,
  `JobTitle` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`EmployeeID`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `Umuzi`.`Orders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Umuzi`.`Orders` (
  `OrderID` INT(11) NOT NULL AUTO_INCREMENT,
  `OrderDate` DATETIME NULL DEFAULT NULL,
  `RequiredDate` DATE NULL DEFAULT NULL,
  `ShippedDate` DATE NULL DEFAULT NULL,
  `Status` ENUM('SHIPPED', 'NOTSHIPPED') NULL DEFAULT 'NOTSHIPPED',
  PRIMARY KEY (`OrderID`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `Umuzi`.`Payments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Umuzi`.`Payments` (
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
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `Umuzi`.`Products`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Umuzi`.`Products` (
  `ProductID` INT(11) NOT NULL AUTO_INCREMENT,
  `ProductName` VARCHAR(100) NULL DEFAULT NULL,
  `Description` VARCHAR(150) NULL DEFAULT NULL,
  `BuyPrice` DECIMAL(10,2) NULL DEFAULT NULL,
  PRIMARY KEY (`ProductID`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = latin1;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
