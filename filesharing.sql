-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema filesharing
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `filesharing` ;

-- -----------------------------------------------------
-- Schema filesharing
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `filesharing` DEFAULT CHARACTER SET utf8 ;
USE `filesharing` ;

-- -----------------------------------------------------
-- Table `filesharing`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `filesharing`.`user` ;

CREATE TABLE IF NOT EXISTS `filesharing`.`user` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `login` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `login_UNIQUE` (`login` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 128
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `filesharing`.`file`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `filesharing`.`file` ;

CREATE TABLE IF NOT EXISTS `filesharing`.`file` (
  `id` VARCHAR(45) NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `user_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`, `user_id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE,
  INDEX `fk_File_user_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_File_user`
    FOREIGN KEY (`user_id`)
    REFERENCES `filesharing`.`user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


INSERT INTO `filesharing`.`user` (`login`, `password`) VALUES ('Alesha', 'safeasf');
INSERT INTO `filesharing`.`file` (`id`, `name`, `user_id`) VALUES ('1', 'mpsy', '128');

