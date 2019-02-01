-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.1.13-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win32
-- HeidiSQL Version:             9.5.0.5196
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for phyruss_bank
CREATE DATABASE IF NOT EXISTS `phyruss_bank` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `phyruss_bank`;

-- Dumping structure for table phyruss_bank.amnt
CREATE TABLE IF NOT EXISTS `amnt` (
  `ID` int(30) NOT NULL AUTO_INCREMENT,
  `MAIN_BALANCE` double DEFAULT '0',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- Dumping data for table phyruss_bank.amnt: ~0 rows (approximately)
/*!40000 ALTER TABLE `amnt` DISABLE KEYS */;
INSERT INTO `amnt` (`ID`, `MAIN_BALANCE`) VALUES
	(1, 3000);
/*!40000 ALTER TABLE `amnt` ENABLE KEYS */;

-- Dumping structure for table phyruss_bank.blacklist_transactions
CREATE TABLE IF NOT EXISTS `blacklist_transactions` (
  `ID` int(60) NOT NULL AUTO_INCREMENT,
  `NAME` char(50) NOT NULL DEFAULT '0',
  `UNAME` char(50) NOT NULL DEFAULT '0',
  `PIN_RECORD` varchar(50) NOT NULL DEFAULT '0',
  `ACTIVITY` longtext NOT NULL,
  `DATE_OF_ACTION` date DEFAULT NULL,
  `TIME` time DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=latin1;

-- Dumping data for table phyruss_bank.blacklist_transactions: ~12 rows (approximately)
/*!40000 ALTER TABLE `blacklist_transactions` DISABLE KEYS */;
INSERT INTO `blacklist_transactions` (`ID`, `NAME`, `UNAME`, `PIN_RECORD`, `ACTIVITY`, `DATE_OF_ACTION`, `TIME`) VALUES
	(13, 'Angad', 'angadkadam08@gmail.com', '6904(R)', 'PIN CHANGE', '2018-12-26', '22:59:40');
INSERT INTO `blacklist_transactions` (`ID`, `NAME`, `UNAME`, `PIN_RECORD`, `ACTIVITY`, `DATE_OF_ACTION`, `TIME`) VALUES
	(14, 'Angad', 'angadkadam08@gmail.com', '6904(R)', 'PIN CHANGE', '2018-12-26', '23:03:24');
INSERT INTO `blacklist_transactions` (`ID`, `NAME`, `UNAME`, `PIN_RECORD`, `ACTIVITY`, `DATE_OF_ACTION`, `TIME`) VALUES
	(16, 'Angad', 'angadkadam08@gmail.com', '40999(E)', 'BALANCE ADDITION', '2018-12-26', '23:19:46');
INSERT INTO `blacklist_transactions` (`ID`, `NAME`, `UNAME`, `PIN_RECORD`, `ACTIVITY`, `DATE_OF_ACTION`, `TIME`) VALUES
	(18, 'Angad', 'angadkadam08@gmail.com', '40966(R)', 'PIN CHANGE', '2018-12-26', '23:21:51');
INSERT INTO `blacklist_transactions` (`ID`, `NAME`, `UNAME`, `PIN_RECORD`, `ACTIVITY`, `DATE_OF_ACTION`, `TIME`) VALUES
	(19, 'Angad', 'angadkadam08@gmail.com', '6190(R)', 'LIVE BANKING SESSION', '2018-12-27', '12:46:02');
INSERT INTO `blacklist_transactions` (`ID`, `NAME`, `UNAME`, `PIN_RECORD`, `ACTIVITY`, `DATE_OF_ACTION`, `TIME`) VALUES
	(21, 'Angad', 'angadkadam08@gmail.com', '61900(E)', 'BALANCE ADDITION', '2018-12-27', '13:19:40');
INSERT INTO `blacklist_transactions` (`ID`, `NAME`, `UNAME`, `PIN_RECORD`, `ACTIVITY`, `DATE_OF_ACTION`, `TIME`) VALUES
	(24, 'Angad', 'angadkadam08@gmail.com', '6190(R)', 'BALANCE ADDITION', '2018-12-27', '13:28:09');
INSERT INTO `blacklist_transactions` (`ID`, `NAME`, `UNAME`, `PIN_RECORD`, `ACTIVITY`, `DATE_OF_ACTION`, `TIME`) VALUES
	(25, 'Angad', 'angadkadam08@gmail.com', '6190(R)', 'BALANCE ADDITION', '2018-12-27', '18:23:51');
INSERT INTO `blacklist_transactions` (`ID`, `NAME`, `UNAME`, `PIN_RECORD`, `ACTIVITY`, `DATE_OF_ACTION`, `TIME`) VALUES
	(26, 'Angad', 'angadkadam08@gmail.com', '6904(R)', 'PIN CHANGE', '2018-12-27', '19:08:31');
INSERT INTO `blacklist_transactions` (`ID`, `NAME`, `UNAME`, `PIN_RECORD`, `ACTIVITY`, `DATE_OF_ACTION`, `TIME`) VALUES
	(27, 'Angad', 'angadkadam08@gmail.com', '6904(R)', 'BALANCE CHECK', '2019-01-12', '11:29:11');
INSERT INTO `blacklist_transactions` (`ID`, `NAME`, `UNAME`, `PIN_RECORD`, `ACTIVITY`, `DATE_OF_ACTION`, `TIME`) VALUES
	(29, 'Angad', 'angadkadam08@gmail.com', '40967(E)', 'BALANCE CHECK', '2019-01-12', '11:32:10');
INSERT INTO `blacklist_transactions` (`ID`, `NAME`, `UNAME`, `PIN_RECORD`, `ACTIVITY`, `DATE_OF_ACTION`, `TIME`) VALUES
	(30, 'Angad', 'angadkadam08@gmail.com', '40967(E)', 'PIN CHANGE', '2019-01-12', '11:33:05');
INSERT INTO `blacklist_transactions` (`ID`, `NAME`, `UNAME`, `PIN_RECORD`, `ACTIVITY`, `DATE_OF_ACTION`, `TIME`) VALUES
	(31, 'Angad', 'angadkadam08@gmail.com', '6904(R)', 'BALANCE CHECK', '2019-01-12', '11:35:13');
/*!40000 ALTER TABLE `blacklist_transactions` ENABLE KEYS */;

-- Dumping structure for table phyruss_bank.phyruss_userdetails
CREATE TABLE IF NOT EXISTS `phyruss_userdetails` (
  `ID` int(90) NOT NULL AUTO_INCREMENT,
  `NAME` varchar(50) NOT NULL,
  `UNAME` varchar(50) NOT NULL,
  `DATE_OF_SERVICE` date NOT NULL,
  `PIN` int(90) NOT NULL,
  `TIME_OF_ACTION` time NOT NULL,
  `TRANSACTION_BALANCE` float NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `ID` (`ID`),
  KEY `NAME` (`NAME`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=latin1;

-- Dumping data for table phyruss_bank.phyruss_userdetails: ~9 rows (approximately)
/*!40000 ALTER TABLE `phyruss_userdetails` DISABLE KEYS */;
INSERT INTO `phyruss_userdetails` (`ID`, `NAME`, `UNAME`, `DATE_OF_SERVICE`, `PIN`, `TIME_OF_ACTION`, `TRANSACTION_BALANCE`) VALUES
	(28, 'Angad', 'angadkadam08@gmail.com', '2018-12-23', 4096, '00:33:38', 1000);
INSERT INTO `phyruss_userdetails` (`ID`, `NAME`, `UNAME`, `DATE_OF_SERVICE`, `PIN`, `TIME_OF_ACTION`, `TRANSACTION_BALANCE`) VALUES
	(41, 'Rudra', 'rudrasanerwal1080@gmail.com', '2018-12-24', 8192, '21:43:25', 1750.77);
INSERT INTO `phyruss_userdetails` (`ID`, `NAME`, `UNAME`, `DATE_OF_SERVICE`, `PIN`, `TIME_OF_ACTION`, `TRANSACTION_BALANCE`) VALUES
	(42, 'Isha', 'ishasanerwal18@gmail.com', '2018-12-24', 1024, '21:45:17', 80001.4);
INSERT INTO `phyruss_userdetails` (`ID`, `NAME`, `UNAME`, `DATE_OF_SERVICE`, `PIN`, `TIME_OF_ACTION`, `TRANSACTION_BALANCE`) VALUES
	(43, 'Aryaan', 'aryanbharadwaj85@gmail.com', '2018-12-24', 2048, '21:47:11', 2481630);
INSERT INTO `phyruss_userdetails` (`ID`, `NAME`, `UNAME`, `DATE_OF_SERVICE`, `PIN`, `TIME_OF_ACTION`, `TRANSACTION_BALANCE`) VALUES
	(44, 'Jibraan', 'jibrank46@gmail.com', '2018-12-24', 1080, '21:48:26', 20484100);
INSERT INTO `phyruss_userdetails` (`ID`, `NAME`, `UNAME`, `DATE_OF_SERVICE`, `PIN`, `TIME_OF_ACTION`, `TRANSACTION_BALANCE`) VALUES
	(45, 'Sangita', 'sangitakadam1309@gmail.com', '2018-12-25', 1309, '15:21:45', 400);
INSERT INTO `phyruss_userdetails` (`ID`, `NAME`, `UNAME`, `DATE_OF_SERVICE`, `PIN`, `TIME_OF_ACTION`, `TRANSACTION_BALANCE`) VALUES
	(50, 'Sara', 'sarab@gmail.com', '2018-12-27', 1140, '19:32:24', 7000);
INSERT INTO `phyruss_userdetails` (`ID`, `NAME`, `UNAME`, `DATE_OF_SERVICE`, `PIN`, `TIME_OF_ACTION`, `TRANSACTION_BALANCE`) VALUES
	(54, 'Apple', 'mango@django.com', '2018-12-27', 7689, '19:57:08', 7000);
INSERT INTO `phyruss_userdetails` (`ID`, `NAME`, `UNAME`, `DATE_OF_SERVICE`, `PIN`, `TIME_OF_ACTION`, `TRANSACTION_BALANCE`) VALUES
	(68, 'D', 'F', '2019-01-23', 3456, '15:14:03', 1000);
/*!40000 ALTER TABLE `phyruss_userdetails` ENABLE KEYS */;

-- Dumping structure for table phyruss_bank.pylog
CREATE TABLE IF NOT EXISTS `pylog` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `PID` varchar(50) NOT NULL DEFAULT '0',
  `PPASSWORD` varchar(50) NOT NULL DEFAULT '0',
  `PNAME` char(50) NOT NULL DEFAULT '0',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- Dumping data for table phyruss_bank.pylog: ~0 rows (approximately)
/*!40000 ALTER TABLE `pylog` DISABLE KEYS */;
INSERT INTO `pylog` (`ID`, `PID`, `PPASSWORD`, `PNAME`) VALUES
	(1, 'rudrasanerwal1080@gmail.com', '@12345678', 'Rudra');
/*!40000 ALTER TABLE `pylog` ENABLE KEYS */;

-- Dumping structure for table phyruss_bank.py_wallet
CREATE TABLE IF NOT EXISTS `py_wallet` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `NAME` char(50) DEFAULT NULL,
  `UNAME` varchar(50) DEFAULT NULL,
  `DATE_OF_ADD` date DEFAULT NULL,
  `TIME_OF_ADD` time DEFAULT NULL,
  `WALL_BALANCE` float DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- Dumping data for table phyruss_bank.py_wallet: ~3 rows (approximately)
/*!40000 ALTER TABLE `py_wallet` DISABLE KEYS */;
INSERT INTO `py_wallet` (`ID`, `NAME`, `UNAME`, `DATE_OF_ADD`, `TIME_OF_ADD`, `WALL_BALANCE`) VALUES
	(2, 'Angad', 'angadkadam08@gmail.com', '2019-01-23', '10:37:41', 7010);
INSERT INTO `py_wallet` (`ID`, `NAME`, `UNAME`, `DATE_OF_ADD`, `TIME_OF_ADD`, `WALL_BALANCE`) VALUES
	(3, 'Sangita', 'sangitakadam1309@gmail.com', '2019-02-01', '19:22:08', 400);
/*!40000 ALTER TABLE `py_wallet` ENABLE KEYS */;

-- Dumping structure for table phyruss_bank.user_transdetails
CREATE TABLE IF NOT EXISTS `user_transdetails` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `NAME` char(10) NOT NULL,
  `UNAME` varchar(50) NOT NULL,
  `TRANSACTION_RECORD` char(50) NOT NULL,
  `TIME_OF_TRANSACTION` time NOT NULL,
  `DATE_OF_TRANSACTION` date NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=152 DEFAULT CHARSET=latin1;

-- Dumping data for table phyruss_bank.user_transdetails: ~13 rows (approximately)
/*!40000 ALTER TABLE `user_transdetails` DISABLE KEYS */;
INSERT INTO `user_transdetails` (`ID`, `NAME`, `UNAME`, `TRANSACTION_RECORD`, `TIME_OF_TRANSACTION`, `DATE_OF_TRANSACTION`) VALUES
	(129, 'Angad', 'angadkadam08@gmail.com', '+1000.0', '13:50:03', '2019-01-23');
INSERT INTO `user_transdetails` (`ID`, `NAME`, `UNAME`, `TRANSACTION_RECORD`, `TIME_OF_TRANSACTION`, `DATE_OF_TRANSACTION`) VALUES
	(130, 'Angad', 'angadkadam08@gmail.com', '+1000.0', '14:23:49', '2019-01-23');
INSERT INTO `user_transdetails` (`ID`, `NAME`, `UNAME`, `TRANSACTION_RECORD`, `TIME_OF_TRANSACTION`, `DATE_OF_TRANSACTION`) VALUES
	(131, 'Angad', 'angadkadam08@gmail.com', '+100.0', '14:24:33', '2019-01-23');
INSERT INTO `user_transdetails` (`ID`, `NAME`, `UNAME`, `TRANSACTION_RECORD`, `TIME_OF_TRANSACTION`, `DATE_OF_TRANSACTION`) VALUES
	(132, 'Angad', 'angadkadam08@gmail.com', '+40.0', '14:25:37', '2019-01-23');
INSERT INTO `user_transdetails` (`ID`, `NAME`, `UNAME`, `TRANSACTION_RECORD`, `TIME_OF_TRANSACTION`, `DATE_OF_TRANSACTION`) VALUES
	(133, 'Angad', 'angadkadam08@gmail.com', '+10.0', '14:27:01', '2019-01-23');
INSERT INTO `user_transdetails` (`ID`, `NAME`, `UNAME`, `TRANSACTION_RECORD`, `TIME_OF_TRANSACTION`, `DATE_OF_TRANSACTION`) VALUES
	(134, 'Angad', 'angadkadam08@gmail.com', '-100.0', '14:41:18', '2019-01-23');
INSERT INTO `user_transdetails` (`ID`, `NAME`, `UNAME`, `TRANSACTION_RECORD`, `TIME_OF_TRANSACTION`, `DATE_OF_TRANSACTION`) VALUES
	(135, 'Angad', 'angadkadam08@gmail.com', '-100.0', '14:41:57', '2019-01-23');
INSERT INTO `user_transdetails` (`ID`, `NAME`, `UNAME`, `TRANSACTION_RECORD`, `TIME_OF_TRANSACTION`, `DATE_OF_TRANSACTION`) VALUES
	(136, 'Angad', 'angadkadam08@gmail.com', '+1000.0', '14:43:11', '2019-01-23');
INSERT INTO `user_transdetails` (`ID`, `NAME`, `UNAME`, `TRANSACTION_RECORD`, `TIME_OF_TRANSACTION`, `DATE_OF_TRANSACTION`) VALUES
	(147, 'Angad', 'angadkadam08@gmail.com', '-100.0', '15:20:44', '2019-01-23');
INSERT INTO `user_transdetails` (`ID`, `NAME`, `UNAME`, `TRANSACTION_RECORD`, `TIME_OF_TRANSACTION`, `DATE_OF_TRANSACTION`) VALUES
	(148, 'Angad', 'angadkadam08@gmail.com', '-900.0', '19:40:34', '2019-01-28');
INSERT INTO `user_transdetails` (`ID`, `NAME`, `UNAME`, `TRANSACTION_RECORD`, `TIME_OF_TRANSACTION`, `DATE_OF_TRANSACTION`) VALUES
	(149, 'Sangita', 'sangitakadam1309@gmail.com', '+500.0', '19:25:49', '2019-02-01');
INSERT INTO `user_transdetails` (`ID`, `NAME`, `UNAME`, `TRANSACTION_RECORD`, `TIME_OF_TRANSACTION`, `DATE_OF_TRANSACTION`) VALUES
	(150, 'Sangita', 'sangitakadam1309@gmail.com', 'W[-200.0]', '19:28:21', '2019-02-01');
INSERT INTO `user_transdetails` (`ID`, `NAME`, `UNAME`, `TRANSACTION_RECORD`, `TIME_OF_TRANSACTION`, `DATE_OF_TRANSACTION`) VALUES
	(151, 'Sangita', 'sangitakadam1309@gmail.com', 'W[+100.0]', '19:34:08', '2019-02-01');
/*!40000 ALTER TABLE `user_transdetails` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
