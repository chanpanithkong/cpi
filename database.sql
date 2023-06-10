-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: dbcpi
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tbbatches`
--

DROP TABLE IF EXISTS `tbbatches`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbbatches` (
  `batchid` int NOT NULL,
  `batch` varchar(45) DEFAULT NULL,
  `detail` varchar(45) DEFAULT NULL,
  `createdate` datetime DEFAULT NULL,
  `createby` varchar(45) DEFAULT NULL,
  `branch` varchar(10) DEFAULT NULL,
  `statusid` int DEFAULT NULL,
  PRIMARY KEY (`batchid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbbatches`
--

LOCK TABLES `tbbatches` WRITE;
/*!40000 ALTER TABLE `tbbatches` DISABLE KEYS */;
INSERT INTO `tbbatches` VALUES (1,'batch1','0001001','2023-06-10 15:18:33','0001','001',9);
/*!40000 ALTER TABLE `tbbatches` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbbranches`
--

DROP TABLE IF EXISTS `tbbranches`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbbranches` (
  `branchcode` varchar(10) NOT NULL,
  `nameen` varchar(45) DEFAULT NULL,
  `namekh` varchar(100) DEFAULT NULL,
  `addressen` varchar(255) DEFAULT NULL,
  `addresskh` varchar(255) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`branchcode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT='		';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbbranches`
--

LOCK TABLES `tbbranches` WRITE;
/*!40000 ALTER TABLE `tbbranches` DISABLE KEYS */;
INSERT INTO `tbbranches` VALUES ('001','HEAD OFFICE','ទីស្នាក់ការកណ្តាល','P.O. Box 25, Norodm Blvd.','P.O. ប្រអប់លេខ ២៥ មហាវិថីនរោត្តម',' '),('002','KANDAL','កណ្តាល','Street 104, Phum Takmao, Khum-Srok Takhmao','ផ្លូវ 104 ប៉ាហុនតាខ្មៅ ឃុំ-ស្រុកតាខ្មៅ',' '),('003','KAMPONG CHAM','កំពង់ចាម','Street Preah Monivong, Khum-Srok Kampong Cham','ផ្លូវព្រះមុនីវង្ស, កាយូ-ស្ត្រូកំពង់ចាម',' '),('004','BATTAMBONG','បាត់ដំបង','Street 3, Phum Kampong Krorbey, Khum Svaypor, Srok Battambong','ផ្លូវលេខ៣ អាហារកំពង់ក្របី ឃុំសំបួរ ផ្លូវបាត់ដំបង',' '),('005','PREY VENG','ព្រៃវែង','Street Matonlei, Phum 3, Khum-Srok Kampong Leav','ផ្លូវ Matonlei, Pahun 3, Kayu-Strok កំពង់លាវ',' '),('006','SIEM REAP','សៀមរាប','Street 9-10, Mondul 1, Khum Svay Dangkum Srok','ផ្លូវ I-10, មណ្ឌល 1, ភូមិ ស្វាយដង្គុំ ស្រុក',' '),('007','KAMPONG THOM','កំពង់ធំ','Street Stung Sen, Phum 1, Khum Kampong Thom, Srok Stung Sen','ផ្លូវ Satung Sen, Pahun 1, ឃុំកំពង់ធំ, Saok Satung Sen',' '),('008','TAKEO','តាកែវ','Street 11, Phum 1, Khum Rokarknong, Srok Donkeo ','ផ្លូវលេខ១១ ប៉ាហុន១ សាយរកាកោង ស្តុបដូនកែវ',' '),('009','SVAY REANG','ស្វាយរៀង','Phum Suon Thmey, Khum Prek Chhlak, Srok Svay Rieng','ភូមិសួនថ្មី ភូមិព្រែកឆ្លាក់ ខេត្តស្វាយរៀង',' '),('010','PURSAT','ពោធិ៍សាត់','Street 1, Phum Popeal Nhek 2, Khum Ptas Prey, Srok Sampeuvmeas','ផ្លូវលេខ១ ភូមិពពាលញែក២ ឃុំត្រពាំងព្រៃ ស្រុកសំពៅមាស',' '),('011','KAMPONG CHHNANG','កំពង់ឆ្នាំង','Street Norodom, Phum Klang Prak, Khum Phaei, Srok Kampong Chhnang','ផ្លូវនរោត្តម ភូមិប៉ាហុន កាឡាំងប្រក់ កុយហ្វៃ ក្រុងកំពង់ឆ្នាំង',' '),('012','KAMPONG SPUE','កំពង់ស្ពឺ','National Road No 4, Phum Peanichkam, Khum Rokarthom, Srok Chbar Mon','ផ្លូវជាតិលេខ៤ ភោជនីយដ្ធាន ឃុំរការធម្ម ផ្លូវច្បារមន',' '),('013','KAMPOT','កំពត','Street Matprek, Phum 1 Ousaphea, Khum Kampong Kandal, Srok Kampong Bay','ផ្លូវ ម៉ាត់ព្រិច ភូមិ១ ឧស្សាហ៍ ឃុំកំពង់កណ្តាល ស្រុកកំពង់បាយ',' '),('014','SIHANOUK VILLE','ក្រុងព្រះសីហនុ','Street Pokambor, Sangkat 3, Khan Mitapheap','ផ្លូវពោធិកំបោរ សង្កាត់៣ ខណ្ឌមិត្តភាព',' '),('015','KOH KONG','កោះកុង','Street Matprek, Phum 1, Khum-Srok Smach Meanchey','សម្រាប់​ផ្លូវ​ប៉ា​ហ៊ូ​១ និយាយ​ថា​-​ផ្លូវ​សំរោង​មាន​ជ័យ​',' '),('017','KRATIE BRANCH','ក្រចេះ','Street Kosamak, Phum Kratie, Srok Kratie','ផ្លូវកុសមៈ ភូមិក្រចេះ ស្រុកក្រចេះ',' '),('018','RATTANAKIRI','រតនៈគីរី','Street 19, Phum 1, Khum Labanseak, Srok Banlung','ផ្លូវ 19, ប៉ាហុន 1, ឃុំ Labansek, Sarok Banglung',' '),('020','STUNG TRENG','ស្ទឹងត្រែង','Street 2, Phum Prek, Khum-Srok Stung Treng','ផ្លូវលេខ២ ភូមិប៉ាហុនព្រែក ឃុំ-សារគរ សត្យារាម',' '),('021','BANTEAY MEANCHEY','បន្ទាយមានជ័យ','Blok Uy, Phum 3, Khum Preah Punlear, Srok Serei Sophoan','Block Duy, Ph.3, Khum Prah Punalar, Sarok​សិរីសោភ័ណ',' '),('023','PHNOM PENH','ភ្នំពេញ','#273, Street 110-67, Sangkat Wat Phnom, Khan Daun Penh','ផ្ទះលេខ២៧៣ ផ្លូវ១១០-៦៧ សង្កាត់វត្តភ្នំ ខណ្ឌដូនពេញ',' ');
/*!40000 ALTER TABLE `tbbranches` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbcategories`
--

DROP TABLE IF EXISTS `tbcategories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbcategories` (
  `catid` int NOT NULL,
  `catcode` varchar(10) DEFAULT NULL,
  `nameen` varchar(100) DEFAULT NULL,
  `namekh` varchar(200) DEFAULT NULL,
  `parentid` int DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`catid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbcategories`
--

LOCK TABLES `tbcategories` WRITE;
/*!40000 ALTER TABLE `tbcategories` DISABLE KEYS */;
INSERT INTO `tbcategories` VALUES (1,'1','Food','ម្ហូបអាហារ',0,' '),(2,'1.1','Rice','អង្ករ',1,' '),(3,'1.2','Ingredients','គ្រឿងទេស',1,' '),(4,'1.3','Meat','សាច់',1,' '),(5,'1.4','Fish and Seafood','ត្រី​ និង​គ្រឿងសមុទ្រ',1,' '),(6,'1.5','Fruit','ផ្លែឈើ',1,' '),(7,'1.6','Vegetables','បន្លែ',1,' '),(8,'2','Beverages and Tobacco','ភេសជ្ជៈ​ និងថ្នាំជក់',0,' '),(9,'3','Restaurant','ភោជនីយដ្ឋាន',0,' '),(10,'4','Clothes and Shoes','សំលៀកបំពាក់ និងស្បែកជើង',0,' '),(11,'5','Shipping','ការដឹកជញ្ជូន',0,' '),(12,'6','Medicine','ថ្នាំពេទ្យ',0,' '),(13,'7','Housing','ផ្ទះសម្បែង',0,' ');
/*!40000 ALTER TABLE `tbcategories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbmeasurement`
--

DROP TABLE IF EXISTS `tbmeasurement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbmeasurement` (
  `mid` int NOT NULL,
  `unit` varchar(45) DEFAULT NULL,
  `measurement` decimal(10,0) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`mid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbmeasurement`
--

LOCK TABLES `tbmeasurement` WRITE;
/*!40000 ALTER TABLE `tbmeasurement` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbmeasurement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbmenus`
--

DROP TABLE IF EXISTS `tbmenus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbmenus` (
  `menuid` int NOT NULL,
  `nameen` varchar(100) DEFAULT NULL,
  `namekh` varchar(200) DEFAULT NULL,
  `icon` varchar(100) DEFAULT NULL,
  `parentid` int DEFAULT NULL,
  `functions` varchar(45) DEFAULT NULL,
  `details` varchar(255) DEFAULT NULL,
  `iscat` int DEFAULT NULL,
  PRIMARY KEY (`menuid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbmenus`
--

LOCK TABLES `tbmenus` WRITE;
/*!40000 ALTER TABLE `tbmenus` DISABLE KEYS */;
INSERT INTO `tbmenus` VALUES (1,'Dashboard','ផ្ទាំងគ្រប់គ្រង','bx-clipboard',0,'/dashboard',' ',0),(2,'Food','អាហារ','bxs-food-menu',0,'/food','foods',1),(3,'Rice','អង្ករ',' ',2,'/rice',' ',2),(4,'Ingredients','គ្រឿងផ្សំ',' ',2,'/ingredients',' ',3),(5,'Meat','សាច់',' ',2,'/meat',' ',4),(6,'Fish and Seafood','ត្រី និងអាហារសមុទ្រ',' ',2,'/fishandseafood',' ',5),(7,'Fruit','ផ្លែឈើ',' ',2,'/fruit',' ',6),(8,'Vegetables','បន្លែ',' ',2,'/vegetables',' ',7),(9,'Beverages and Tobacco','ភេសជ្ជៈ និងថ្នាំជក់','bxs-drink',0,'/beveragestobacco',' ',8),(10,'Restaurant','ភោជនីយដ្ឋាន','bxs-data',0,'/restaurant',' ',9),(11,'Clothes and Shoes','សម្លៀកបំពាក់ និងស្បែកជើង','bx-male',0,'/clothesshoes',' ',10),(12,'Shipping','ការដឹកជញ្ជូន','bx-shopping-bag',0,'/shipping',' ',11),(13,'Medicine','ថ្នាំ','bx-plus-medical',0,'/medicine',' ',12),(14,'Housing','លំនៅដ្ឋាន','bxs-building-house',0,'/housing',' ',13),(15,'Submitted Trans','ប្រតិបត្តិការដែលបានដាក់ស្នើ','bxs-paper-plane',0,'/submittedtrans',' ',0),(16,'Authorized Trans','ប្រតិបត្តិការដែលមានការអនុញ្ញាត','bxs-notification',0,'/authorizedtrans',' ',0),(17,'Checked Trans','បានពិនិត្យប្រតិបត្តិការ','bxs-badge-check',0,'/checkedtrans',' ',0),(18,'History of Trans','ប្រវត្តិប្រតិបត្តិការ','bx-history',0,'/historyoftrans',' ',0),(19,'Users Setting','ការកំណត់អ្នកប្រើប្រាស់','bx-slider-alt',0,'/user','usersetting',0),(20,'User Profile','កម្រងព័ត៌មានអ្នកប្រើប្រាស់',' ',19,'/userprofile',' ',0),(21,'Change Password','ផ្លាស់ប្តូរពាក្យសម្ងាត់',' ',19,'/changepassword',' ',0),(22,'Logout','ចាកចេញ',' ',19,'/login',' ',0),(23,'Users Management','ការគ្រប់គ្រងអ្នកប្រើប្រាស់','bxs-user-account',0,'/users','usersmanagement',0),(24,'Create Users','បង្កើតអ្នកប្រើប្រាស់',' ',23,'/createusers',' ',0),(25,'Update Users','ធ្វើបច្ចុប្បន្នភាពអ្នកប្រើប្រាស់',' ',23,'/updateusers',' ',0),(26,'View Users','មើលអ្នកប្រើប្រាស់',' ',23,'/viewusers',' ',0),(27,'Roles Management','ការគ្រប់គ្រងតួនាទី','bx bxs-user-detail',0,'/role','rolesmangement',0),(28,'Create Role','បង្កើតតួនាទី',' ',27,'/createroles',' ',0),(29,'Create Permission','បង្កើតការអនុញ្ញាត',' ',27,'/createpermission',' ',0),(30,'View Roles','មើលតួនាទី',' ',27,'/attachedrolepermission',' ',0),(31,'Products Management','ការគ្រប់គ្រងផលិតផល','bx bx-category',0,'/product','productsmanagement',0),(32,'Categories','ប្រភេទ',' ',31,'/createcategories',' ',0),(36,'Products','ផលិតផល',' ',31,'/viewproducts',' ',0);
/*!40000 ALTER TABLE `tbmenus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbproducts`
--

DROP TABLE IF EXISTS `tbproducts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbproducts` (
  `prodid` int NOT NULL,
  `productcode` varchar(10) DEFAULT NULL,
  `nameen` varchar(100) DEFAULT NULL,
  `namekh` varchar(200) DEFAULT NULL,
  `weight` decimal(10,2) DEFAULT NULL,
  `catid` int DEFAULT NULL,
  `unitkh` varchar(150) DEFAULT NULL,
  `uniten` varchar(150) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`prodid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbproducts`
--

LOCK TABLES `tbproducts` WRITE;
/*!40000 ALTER TABLE `tbproducts` DISABLE KEYS */;
INSERT INTO `tbproducts` VALUES (1,'1.1.1','Jasmine rice','អង្ករផ្កាម្លិះ',2.01,2,'រៀល/គក្រ','Riel/kg',' '),(2,'1.1.2','Phaka Kanhey rice','អង្ករផ្កាខ្ញី',2.01,2,'រៀល/គក្រ','Riel/kg',' '),(3,'1.1.3','Neang Menh rice','អង្ករនាងមិញ',2.29,2,'រៀល/គក្រ','Riel/kg',' '),(4,'1.1.4','Neang Khon rice','អង្ករនាងខុន',2.29,2,'រៀល/គក្រ','Riel/kg',' '),(5,'1.1.5','Glutinous rice','អង្ករដំណើប',1.71,2,'រៀល/គក្រ','Riel/kg',' '),(6,'1.1.6','Other grains','ធញ្ញជាតិផ្សេងៗ​ (សណ្តែកបាយ ក្រហម ខៀវ)',1.02,2,'រៀល/គក្រ','Riel/kg',' '),(7,'1.2.1','Oils and fats','ប្រេងឆា និងខ្លាញ់',0.90,3,'រៀល/ដប','Riel/bottle',' '),(8,'1.2.2','Fish sauce','ទឹកត្រី',0.40,3,'រៀល/ដប','Riel/bottle',' '),(9,'1.2.3','Sugar','ស្ករ​​ស',0.50,3,'រៀល/គក្រ','Riel/kg',' '),(10,'1.2.4','Brown sugar','ស្ករត្នោត',0.50,3,'រៀល/គក្រ','Riel/kg',' '),(11,'1.2.5','Salt','អំបិល',0.50,3,'រៀល/គក្រ','Riel/kg',' '),(12,'1.2.6','Soup powder','ម្សៅស៊ុប ',0.60,3,'រៀល/កញ្ចប់','Riel/packet',' '),(13,'1.3.1','Beef','សាច់គោ',3.30,4,'រៀល/គក្រ','Riel/kg',' '),(14,'1.3.2','Pork','សាច់ជ្រូក',4.62,4,'រៀល/គក្រ','Riel/kg',' '),(15,'1.3.3','Chicken meat','សាច់មាន់',1.10,4,'រៀល/គក្រ','Riel/kg',' '),(16,'1.3.4','Duck meat','សាច់ទា',0.90,4,'រៀល/គក្រ','Riel/kg',' '),(17,'1.3.5','Chicken eggs','ស៊ុតមាន់',1.01,4,'រៀល/១០គ្រាប់','Riel/10 eggs',' '),(18,'1.3.6','Duck eggs','ស៊ុតទា',1.01,4,'រៀល/១០គ្រាប់','Riel/10 eggs',' '),(19,'1.4.1','Giant snakehead fish (free-range)','ត្រីរ៉ស់ (ស្រែ)',1.70,5,'រៀល/គក្រ','Riel/kg',' '),(20,'1.4.2','Giant snakehead fish (farm-raised)','ត្រីរ៉ស់ (ចិញ្ចឹម)',2.40,5,'រៀល/គក្រ','Riel/kg',' '),(21,'1.4.3','Striped snakehead','ត្រីឆ្តោ',1.70,5,'រៀល/គក្រ','Riel/kg',' '),(22,'1.4.4','Walking catfish','ត្រីអណ្តែង',0.90,5,'រៀល/គក្រ','Riel/kg',' '),(23,'1.4.5','Tilapia fish','ត្រីទីឡាបយ៉ា',0.90,5,'រៀល/គក្រ','Riel/kg',' '),(24,'1.4.6','Dried fish ','ត្រីងៀត',1.00,5,'រៀល/គក្រ','Riel/kg',' '),(25,'1.4.7','Phork','ផ្អក',0.80,5,'រៀល/គក្រ','Riel/kg',' '),(26,'1.4.8','Prahok','ប្រហុក',0.80,5,'រៀល/គក្រ','Riel/kg',' '),(27,'1.4.9','Salted-water fish','ត្រីសមុទ្រ ​(កាម៉ុងចំហុយ)',0.80,5,'រៀល/គក្រ','Riel/kg',' '),(28,'1.4.10','Shrimp','បង្គា',1.40,5,'រៀល/គក្រ','Riel/kg',' '),(29,'1.4.11','Squid','មឹក',1.30,5,'រៀល/គក្រ','Riel/kg',' '),(30,'1.4.12','Oyster','ងាវ',1.00,5,'រៀល/គក្រ','Riel/kg',' '),(31,'1.5.1','Namva banana','ចេកណាំវ៉ា',3.00,6,'រៀល/ស្និត','Riel/cluster',' '),(32,'1.5.2','Apple','ប៉ោម',1.40,6,'រៀល/គក្រ','Riel/kg',' '),(33,'1.5.3','Pursat Orange','ក្រូចពោធិសាត់',1.30,6,'រៀល/គក្រ','Riel/kg',' '),(34,'1.5.4','Longan','មៀន',1.10,6,'រៀល/គក្រ','Riel/kg',' '),(35,'1.5.5','Grape','ទំពាំងបាយជូរធម្មតា',1.30,6,'រៀល/គក្រ','Riel/kg',' '),(36,'1.6.1','Water convolvulus','ត្រកួន',0.80,7,'រៀល/គក្រ','Riel/kg',' '),(37,'1.6.2','Sawl','ស្ពៃចង្កឹះ',0.40,7,'រៀល/គក្រ','Riel/kg',' '),(38,'1.6.3','Cucumber','ត្រសក់',1.00,7,'រៀល/គក្រ','Riel/kg',' '),(39,'1.6.4','Carrot','ការ៉ុត',0.50,7,'រៀល/គក្រ','Riel/kg',' '),(40,'1.6.5','Tomato','ប៉េងប៉ោះ',0.40,7,'រៀល/គក្រ','Riel/kg',' '),(41,'1.6.6','Chinese kale','ដើមខាត់ណា',0.20,7,'រៀល/គក្រ','Riel/kg',' '),(42,'1.6.7','Long cabbage','ស្ពៃក្តោប',0.20,7,'រៀល/គក្រ','Riel/kg',' '),(43,'1.6.8','Leaf Lettuce','សាឡាដ',0.40,7,'រៀល/គក្រ','Riel/kg',' '),(44,'1.6.9','Wax gourd','ត្រឡាច',0.30,7,'រៀល/គក្រ','Riel/kg',' '),(45,'1.6.10','Eggplant','ត្រប់វែង',0.30,7,'រៀល/គក្រ','Riel/kg',' '),(46,'1.6.11','Ginger','ខ្ញី',0.30,7,'រៀល/គក្រ','Riel/kg',' '),(47,'1.6.12','Garlic','ខ្ទឹមស​ ',0.60,7,'រៀល/គក្រ','Riel/kg',' '),(48,'1.6.13','Onion','ខ្ទឹមបារាំង',0.40,7,'រៀល/គក្រ','Riel/kg',' '),(49,'1.6.14','Mushroom','ផ្សិត',0.30,7,'រៀល/គក្រ','Riel/kg',' '),(50,'1.6.15','Bitter melon','ម្រះ',0.20,7,'រៀល/គក្រ','Riel/kg',' '),(51,'2.1','Mineral water (Vital)','ទឹកសុទ្ធវីតាល់',1.00,8,'រៀល/ដប','Riel/bottle',' '),(52,'2.2','Angkor Beer','ស្រាបៀរអង្គរ',0.80,8,'រៀល/កំប៉ុង','Riel/can',' '),(53,'2.3','Coca-Cola','ទឹកក្រូចកូកាកូឡា',0.70,8,'រៀល/កំប៉ុង','Riel/can',' '),(54,'2.4','Canned juice','ទឹកផ្លែឈើ',0.50,8,'រៀល/កំប៉ុង','Riel/can',' '),(55,'2.5','Energy drinks','ភេសជ្ជៈប៉ូវកំលាំង (គោជល់ បាកាស...)',0.50,8,'រៀល/កំប៉ុង','Riel/can',' '),(56,'2.6','Spirit','ស្រាបិទ',0.10,8,'រៀល/លីត្រ','Riel/litre',' '),(57,'2.7','Iced Latte','កាហ្វេទឹកដោះគោទឹកកក',0.80,8,'រៀល/កែវ','Riel/glass',' '),(58,'2.8','Cigarette','បារី',0.40,8,'រៀល/កញ្ចប់','Riel/packet',' '),(59,'3.1','Noodles (breakfast)','គុយទាវធម្មតា (ព្រឹក)',2.80,9,'រៀល/ចាន','Riel/bowl',' '),(60,'3.2','Lunch','បាយម្ហូបកម្ម៉ង់ថ្ងៃត្រង់មួយចម្អែត',1.50,9,'រៀល/ឈុត','Riel/set',' '),(61,'3.3','Beef skewer','សាច់គោអាំង',0.50,9,'រៀល/ចាន','Riel/plate',' '),(62,'3.4','Chicken rice','បាយសាច់មាន់ ',0.60,9,'រៀល/ចាន','Riel/plate',' '),(63,'3.5','Pork rice','បាយសាច់ជ្រូក',0.60,9,'រៀល/ចាន','Riel/plate',' '),(64,'3.6','Rice Porridge','បបរគ្រឿង',0.50,9,'រៀល/ចាន','Riel/bowl',' '),(65,'3.7','Soup','ស៊ុប',0.60,9,'រៀល/ឆ្នាំង','Riel/set',' '),(66,'4.1','Clothing for men','សំលៀកបំពាក់បុរស',0.62,10,'រៀល/សម្រាប់','Riel/piece',' '),(67,'4.2','Clothing for women','សំលៀកបំពាក់នារី',0.90,10,'រៀល/សម្រាប់','Riel/piece',' '),(68,'4.3','Clothing for kids','សំលៀកបំពាក់កូនក្មេង',0.30,10,'រៀល/សម្រាប់','Riel/piece',' '),(69,'4.4','Footwear','ស្បែកជើង',0.40,10,'រៀល/គូរ','Riel/pair',' '),(70,'5.1','Bicycles','កង់',1.10,11,'រៀល/គ្រឿង','Riel/bike',' '),(71,'5.2','Honda Dream ,Motor cycles (Honda Dream)','ម៉ូតូ Honda Dream',1.70,11,'រៀល/គ្រឿង','Riel/motor',' '),(72,'5.3','Gasoline','ប្រេងសាំងធម្មតា',4.00,11,'រៀល/លីត្រ','Riel/litre',' '),(73,'5.4','Diesel','ប្រេងម៉ាស៊ូត',3.00,11,'រៀល/លីត្រ','Riel/litre',' '),(74,'6.1','Paracetamol','ប៉ារ៉ា',1.20,12,'រៀល/កញ្ចប់','Riel/packet',' '),(75,'6.2','Amoxicillin','អាម៉ុកស៊ីលីន',1.10,12,'រៀល/កញ្ចប់','Riel/packet',' '),(76,'6.3','Vitamin C','វីតាមីន C',0.40,12,'រៀល/កញ្ចប់','Riel/packet',' '),(77,'7.1','Water utilities','ថ្លៃប្រើប្រាស់ទឹក',3.60,13,'រៀល/ម៉ែត្រគីប','Riel/m3',' '),(78,'7.2','Electrical utilities','ថ្លៃប្រើប្រាស់ភ្លើង',8.60,13,'រៀល/គីឡូវ៉ាត់','Riel/kw',' '),(79,'7.3','Gas (15 kilograms)','ឧស្ម័ន (១៥គីឡូក្រាម)',3.30,13,'រៀល/១៥គក្រ','Riel/15kg',' '),(80,'7.4','Rent','ថ្លៃជួលបន្ទប់ស្នាក់នៅ',2.10,13,'រៀល/ខែ','Riel/month',' ');
/*!40000 ALTER TABLE `tbproducts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbrolemenu`
--

DROP TABLE IF EXISTS `tbrolemenu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbrolemenu` (
  `roleid` int NOT NULL,
  `menuid` int NOT NULL,
  `details` varchar(45) DEFAULT NULL,
  `createby` varchar(100) DEFAULT NULL,
  `createdate` datetime DEFAULT NULL,
  `statusid` int DEFAULT NULL,
  PRIMARY KEY (`roleid`,`menuid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbrolemenu`
--

LOCK TABLES `tbrolemenu` WRITE;
/*!40000 ALTER TABLE `tbrolemenu` DISABLE KEYS */;
INSERT INTO `tbrolemenu` VALUES (1,1,'','ITO0001','2023-05-19 18:00:29',5),(1,19,'','ITO0001','2023-05-19 18:00:29',5),(1,20,'','ITO0001','2023-05-19 18:00:29',5),(1,21,'','ITO0001','2023-05-19 18:00:29',5),(1,22,'','ITO0001','2023-05-19 18:00:29',5),(1,23,'','ITO0001','2023-05-19 18:00:29',5),(1,24,'','ITO0001','2023-05-19 18:00:29',5),(1,26,'','ITO0001','2023-05-19 18:00:29',5),(1,27,'','ITO0001','2023-05-19 18:00:29',5),(1,28,'','ITO0001','2023-05-19 18:00:29',5),(1,30,'','ITO0001','2023-05-19 18:00:29',5),(1,31,'','ITO0001','2023-05-19 18:00:29',5),(1,32,'','ITO0001','2023-05-19 18:00:29',5),(1,36,'','ITO0001','2023-05-19 18:00:29',5),(3,1,'','ITO0001','2023-05-19 18:01:00',5),(3,2,'','ITO0001','2023-05-19 18:01:00',5),(3,3,'','ITO0001','2023-05-19 18:01:00',5),(3,4,'','ITO0001','2023-05-19 18:01:00',5),(3,5,'','ITO0001','2023-05-19 18:01:00',5),(3,6,'','ITO0001','2023-05-19 18:01:00',5),(3,7,'','ITO0001','2023-05-19 18:01:00',5),(3,8,'','ITO0001','2023-05-19 18:01:00',5),(3,9,'','ITO0001','2023-05-19 18:01:00',5),(3,10,'','ITO0001','2023-05-19 18:01:00',5),(3,11,'','ITO0001','2023-05-19 18:01:00',5),(3,12,'','ITO0001','2023-05-19 18:01:00',5),(3,13,'','ITO0001','2023-05-19 18:01:00',5),(3,14,'','ITO0001','2023-05-19 18:01:00',5),(3,15,'','ITO0001','2023-05-19 18:01:00',5),(3,18,'','ITO0001','2023-05-19 18:01:00',5),(3,19,'','ITO0001','2023-05-19 18:01:00',5),(3,20,'','ITO0001','2023-05-19 18:01:00',5),(3,21,'','ITO0001','2023-05-19 18:01:00',5),(3,22,'','ITO0001','2023-05-19 18:01:00',5),(3,49,'','ITO0001','2023-05-19 18:01:00',5),(4,1,'','ITO0001','2023-05-19 18:01:11',5),(4,16,'','ITO0001','2023-05-19 18:01:11',5),(4,18,'','ITO0001','2023-05-19 18:01:11',5),(4,19,'','ITO0001','2023-05-19 18:01:11',5),(4,20,'','ITO0001','2023-05-19 18:01:11',5),(4,21,'','ITO0001','2023-05-19 18:01:11',5),(4,22,'','ITO0001','2023-05-19 18:01:11',5),(5,1,'','ITO0001','2023-05-19 18:01:24',5),(5,17,'','ITO0001','2023-05-19 18:01:24',5),(5,18,'','ITO0001','2023-05-19 18:01:24',5),(5,19,'','ITO0001','2023-05-19 18:01:24',5),(5,20,'','ITO0001','2023-05-19 18:01:24',5),(5,21,'','ITO0001','2023-05-19 18:01:24',5),(5,22,'','ITO0001','2023-05-19 18:01:24',5);
/*!40000 ALTER TABLE `tbrolemenu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbroles`
--

DROP TABLE IF EXISTS `tbroles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbroles` (
  `roleid` int NOT NULL,
  `rolename` varchar(45) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`roleid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbroles`
--

LOCK TABLES `tbroles` WRITE;
/*!40000 ALTER TABLE `tbroles` DISABLE KEYS */;
INSERT INTO `tbroles` VALUES (1,'Administrator',' '),(3,'Inputter',' '),(4,'Authorizer',' '),(5,'Checker',' ');
/*!40000 ALTER TABLE `tbroles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbstatus`
--

DROP TABLE IF EXISTS `tbstatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbstatus` (
  `statusid` int NOT NULL,
  `status` varchar(100) DEFAULT NULL,
  `details` varchar(150) DEFAULT NULL,
  `icon` varchar(145) DEFAULT NULL,
  PRIMARY KEY (`statusid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbstatus`
--

LOCK TABLES `tbstatus` WRITE;
/*!40000 ALTER TABLE `tbstatus` DISABLE KEYS */;
INSERT INTO `tbstatus` VALUES (1,'Submitted','primary','bx bxs-coin-stack'),(2,'Rejected',NULL,NULL),(3,'Authorized','success','bx bxs-dashboard'),(4,'Reopen',NULL,NULL),(5,'Active',NULL,NULL),(6,'Deactivated',NULL,NULL),(7,'Pending','warning','bx bx-grid-alt'),(8,'Closed',NULL,NULL),(9,'Open',NULL,NULL),(10,'Rejected By Authorizer','danger','bx bxs-grid-alt'),(11,'Rejected By Checker','danger','bx bxl-trello'),(12,'Saved','secondary','bx bx-coin-stack'),(13,'Accepted','info','bx bx-list-check');
/*!40000 ALTER TABLE `tbstatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbtrans`
--

DROP TABLE IF EXISTS `tbtrans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbtrans` (
  `tid` int NOT NULL,
  `branchcode` varchar(5) DEFAULT NULL,
  `productid` int DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `weight` decimal(10,2) DEFAULT NULL,
  `submitter` varchar(10) DEFAULT NULL,
  `submitdate` datetime DEFAULT NULL,
  `submitternote` varchar(255) DEFAULT NULL,
  `authorizer` varchar(10) DEFAULT NULL,
  `authorizedate` datetime DEFAULT NULL,
  `authorizernote` varchar(255) DEFAULT NULL,
  `checker` varchar(10) DEFAULT NULL,
  `checkerdate` datetime DEFAULT NULL,
  `checkernote` varchar(255) DEFAULT NULL,
  `status` int DEFAULT NULL,
  `valuedate` datetime DEFAULT NULL,
  `trandate` datetime DEFAULT NULL,
  `countsubmitted` int DEFAULT NULL,
  `batchid` int DEFAULT NULL,
  PRIMARY KEY (`tid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbtrans`
--

LOCK TABLES `tbtrans` WRITE;
/*!40000 ALTER TABLE `tbtrans` DISABLE KEYS */;
INSERT INTO `tbtrans` VALUES (1,'001',70,1.00,1.10,'0001','2023-06-10 15:19:01','1','0002','2023-06-10 15:40:45','1','0003','2023-06-10 15:45:15','',13,'2023-06-10 15:19:01','2023-06-10 15:19:01',0,1),(2,'001',71,1.00,1.70,'0001','2023-06-10 15:19:01','1','0002','2023-06-10 15:40:45','1','0003','2023-06-10 15:45:15','',13,'2023-06-10 15:19:01','2023-06-10 15:19:01',0,1),(3,'001',72,1.00,4.00,'0001','2023-06-10 15:19:01','1','0002','2023-06-10 15:40:45','1','0003','2023-06-10 15:45:15','',13,'2023-06-10 15:19:01','2023-06-10 15:19:01',0,1),(4,'001',73,1.00,3.00,'0001','2023-06-10 15:19:01','1','0002','2023-06-10 15:40:45','1','0003','2023-06-10 15:45:15','',13,'2023-06-10 15:19:01','2023-06-10 15:19:01',0,1),(5,'001',51,1.00,1.00,'0001','2023-06-10 15:19:23','1','','2023-06-10 15:19:23','','','2023-06-10 15:19:23','',12,'2023-06-10 15:19:23','2023-06-10 15:19:23',0,1),(6,'001',52,1.00,0.80,'0001','2023-06-10 15:19:23','1','','2023-06-10 15:19:23','','','2023-06-10 15:19:23','',12,'2023-06-10 15:19:23','2023-06-10 15:19:23',0,1),(7,'001',53,1.00,0.70,'0001','2023-06-10 15:19:23','11','','2023-06-10 15:19:23','','','2023-06-10 15:19:23','',12,'2023-06-10 15:19:23','2023-06-10 15:19:23',0,1),(8,'001',54,1.00,0.50,'0001','2023-06-10 15:19:23','1','','2023-06-10 15:19:23','','','2023-06-10 15:19:23','',12,'2023-06-10 15:19:23','2023-06-10 15:19:23',0,1),(9,'001',55,1.00,0.50,'0001','2023-06-10 15:19:23','1','','2023-06-10 15:19:23','','','2023-06-10 15:19:23','',12,'2023-06-10 15:19:23','2023-06-10 15:19:23',0,1),(10,'001',56,1.00,0.10,'0001','2023-06-10 15:19:23','1','','2023-06-10 15:19:23','','','2023-06-10 15:19:23','',12,'2023-06-10 15:19:23','2023-06-10 15:19:23',0,1),(11,'001',57,1.00,0.80,'0001','2023-06-10 15:19:23','1','','2023-06-10 15:19:23','','','2023-06-10 15:19:23','',12,'2023-06-10 15:19:23','2023-06-10 15:19:23',0,1),(12,'001',58,1.00,0.40,'0001','2023-06-10 15:19:23','1','','2023-06-10 15:19:23','','','2023-06-10 15:19:23','',12,'2023-06-10 15:19:23','2023-06-10 15:19:23',0,1);
/*!40000 ALTER TABLE `tbtrans` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbusers`
--

DROP TABLE IF EXISTS `tbusers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbusers` (
  `userid` varchar(10) NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  `key` varchar(255) DEFAULT NULL,
  `roleid` int DEFAULT NULL,
  `username` varchar(45) DEFAULT NULL,
  `gender` varchar(45) DEFAULT NULL,
  `branchcode` varchar(45) DEFAULT NULL,
  `details` varchar(45) DEFAULT NULL,
  `position` varchar(100) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `status` int DEFAULT NULL,
  `languages` varchar(100) DEFAULT 'EN',
  PRIMARY KEY (`userid`),
  UNIQUE KEY `userid_UNIQUE` (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbusers`
--

LOCK TABLES `tbusers` WRITE;
/*!40000 ALTER TABLE `tbusers` DISABLE KEYS */;
INSERT INTO `tbusers` VALUES ('0001','gAAAAABkguuZO4yYxX8tQwKyW_-8Utq7pvMnUzaKMmzjlyxigAsrbhAezHY1s7q8tIjj-vZSvmcIeOGBKI3Gt-VK7z4K_r4b3Q==','RfffSGQPI1fP5jS8RnUKEPaQ5uSWxTKzzefPP0EGtwg=',3,'0001','Female','001','0001','0001','0001',5,'KH'),('0002','gAAAAABkhB5B_UEIHKdQR9JCYx-iVPb1T2NM1CQU-G5jeJEpdE1clZR_ZO--NQEkiBVZC9DdEMo2S72wQBZANFMH5NFOCTkcbA==','m0vQPsTtCzwr0MNDsC2coZbR2x9hvXUuYAqqT9vHDqo=',4,'0002','Female','001','0002','0002','0002',5,'KH'),('0003','gAAAAABkhB5NAbzTmgnJIFtfzaWqQPQUFh53EFWGkeSUE7aIGh1ZBsUGWtdSL4suJAVL6hcRP02BWnYWPR7rR4D8YSW3ATQVVw==','ALaMFCgEAbO_2ileMjVtLdUjGzjMLzfdRedbWazR1e0=',5,'0003','Female','001','0003','0003','0003',5,'KH'),('admin','gAAAAABkawroLag12cpFEBd-lCL37WKAYRO2uNLoqYi7dC3ekYElCV72-7Ks4aQRszwsuh363XdNeTHSP_tzi39lHGrJvlwcLA==','e_VrNdrMv--3qRk1LS9bAeQsnud8Cy0QKqMLCE6L6aE=',1,'admin','Male','001','administrator','admin','admin@nbc.gov.org',5,'KH');
/*!40000 ALTER TABLE `tbusers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-10 20:24:30
