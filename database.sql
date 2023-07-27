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
  `weight` decimal(10,2) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`branchcode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT='		';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbbranches`
--

LOCK TABLES `tbbranches` WRITE;
/*!40000 ALTER TABLE `tbbranches` DISABLE KEYS */;
INSERT INTO `tbbranches` VALUES ('001','HEAD OFFICE','ទីស្នាក់ការកណ្តាល','P.O. Box 25, Norodm Blvd.','ផ្ទះលេខ PO.Box 25, ផ្លូវ នរោត្តម, សង្កាត់ , ខណ្ឌ ដូនពេញ រាជធានី​ ភ្នំពេញ',0.00,' '),('002','KANDAL','កណ្តាល','Street 104, Phum Takmao, Khum-Srok Takhmao','ផ្ទះលេខ, ផ្លូវ 104, ភូមិ តាខ្មៅ, ឃុំ តាខ្មៅ, ស្រុក តាខ្មៅ ខេត្ត កណ្តាល',0.09,' '),('003','KAMPONG CHAM','កំពង់ចាម','Street Preah Monivong, Khum-Srok Kampong Cham','ផ្ទះលេខ, ផ្លូវ ព្រះមន្នីវង្ស, ឃុំ កំពង់ចាម, ស្រុក កំពង់ចាម, ខេត្ត កំពង់ចាម',0.11,' '),('004','BATTAMBONG','បាត់ដំបង','Street 3, Phum Kampong Krorbey, Khum Svaypor, Srok Battambong','ផ្ទះលេខ, ផ្លូវ 3, ភូមិ កំពង់ក្របី, ឃុំ ស្វាយប៉ោ , ស្រុក បាត់ដំបង, ខេត្ត បាត់ដំបង',0.08,' '),('005','PREY VENG','ព្រៃវែង','Street Matonlei, Phum 3, Khum-Srok Kampong Leav','ផ្ទះលេខ, ផ្លូវ មាត់ទន្លេ, ភូមិ 3, ឃុំ កំពង់លាវ, ស្រុក កំពង់លាវ, ខេត្ត ព្រៃវែង',0.07,' '),('006','SIEM REAP','សៀមរាប','Street 9-10, Mondul 1, Khum Svay Dangkum Srok','ផ្ទះលេខ, ផ្លូវ 9-10, ភូមិ មណ្ឌល១, ឃុំ ស្វាយដង្កោម , ស្រុក, ខេត្ត សៀមរាប',0.07,' '),('007','KAMPONG THOM','កំពង់ធំ','Street Stung Sen, Phum 1, Khum Kampong Thom, Srok Stung Sen','ផ្ទះលេខ, ផ្លូវ ស្ទឹងសែន, ភូមិ 1, ឃុំ កំពង់ធំ , ស្រុក ស្ទឹងសែន ខេត្ត កំពង់ធំ',0.04,' '),('008','TAKEO','តាកែវ','Street 11, Phum 1, Khum Rokarknong, Srok Donkeo ','ផ្ទះលេខ, ផ្លូវ 11, ភូមិ 1, ឃុំ រកាក្នុង , ស្រុក ដូនកែវ, ខេត្ត តាកែវ',0.06,' '),('009','SVAY REANG','ស្វាយរៀង','Phum Suon Thmey, Khum Prek Chhlak, Srok Svay Rieng','ផ្ទះលេខ, ផ្លូវ , ភូមិ សួនថ្មី, ឃុំ ព្រែកឆ្លាក់ , ស្រុក ស្វាយរៀង, ខេត្ត ស្វាយរៀង',0.04,' '),('010','PURSAT','ពោធិ៍សាត់','Street 1, Phum Popeal Nhek 2, Khum Ptas Prey, Srok Sampeuvmeas','ផ្ទះលេខ, ផ្លូវ 1, ភូមិ ពពាលញឹក2, ឃុំ ផ្ទះព្រៃ, ស្រុក សំពៅមាស, ខេត្ត ពោធិសាត់',0.03,' '),('011','KAMPONG CHHNANG','កំពង់ឆ្នាំង','Street Norodom, Phum Klang Prak, Khum Phaei, Srok Kampong Chhnang','ផ្ទះលេខ, ផ្លូវ នរោត្តម, ភូមិ ឃ្លាំងប្រាក់, ឃុំ ភ័យ , ស្រុក តាខ្មៅ, ខេត្ត កំពង់ឆ្នាំង',0.04,' '),('012','KAMPONG SPUE','កំពង់ស្ពឺ','National Road No 4, Phum Peanichkam, Khum Rokarthom, Srok Chbar Mon','ផ្ទះលេខ, ផ្លូវ ជាតិលេខ៤, ភូមិ ពានិជ្ជកម្ម, ឃុំ រកាធំ , ស្រុក ច្បារម៉ន, ខេត្ត កំពង់ស្ពឺ',0.05,' '),('013','KAMPOT','កំពត','Street Matprek, Phum 1 Ousaphea, Khum Kampong Kandal, Srok Kampong Bay','ផ្ទះលេខ, ផ្លូវ មាត់ព្រែក, ភូមិ ១ឧសភា, ឃុំ តាខ្មៅ , ស្រុក តាខ្មៅ, ខេត្ត កណ្តាល',0.05,' '),('014','SIHANOUK VILLE','ក្រុងព្រះសីហនុ','Street Pokambor, Sangkat 3, Khan Mitapheap','ផ្ទះលេខ, ផ្លូវ ពោធិកំបោរ, សង្កាត់ ៣, ខ័ណ្ឌ មិត្តភាព , ក្រុង ព្រះសីហនុ',0.02,' '),('015','KOH KONG','កោះកុង','Street Matprek, Phum 1, Khum-Srok Smach Meanchey','ផ្ទះលេខ, ផ្លូវ មាត់ព្រែក, ភូមិ ១, ឃុំ ស្មាច់មានជ័យ, ស្រុក ស្មាច់មានជ័យ, ខេត្ត កោះកុង',0.01,' '),('017','KRATIE BRANCH','ក្រចេះ','Street Kosamak, Phum Kratie, Srok Kratie','ផ្ទះលេខ, ផ្លូវ កុសមៈ, ភូមិ ក្រចេះ, ឃុំ , ស្រុក ក្រចេះ, ខេត្ត ក្រចេះ',0.03,' '),('018','RATTANAKIRI','រតនៈគីរី','Street 19, Phum 1, Khum Labanseak, Srok Banlung','ផ្ទះលេខ, ផ្លូវ 19, ភូមិ 1, ឃុំ ឡាបានសៀក, ស្រុក បានលុង, ខេត្ត រតនៈគីរី',0.01,' '),('020','STUNG TRENG','ស្ទឹងត្រែង','Street 2, Phum Prek, Khum-Srok Stung Treng','ផ្ទះលេខ, ផ្លូវ ២, ភូមិ ព្រែក, ឃុំ  , ស្រុក ស្ទឹងត្រែង, ខេត្ត ស្ទឹងត្រែង',0.01,' '),('021','BANTEAY MEANCHEY','បន្ទាយមានជ័យ','Blok Uy, Phum 3, Khum Preah Punlear, Srok Serei Sophoan','ផ្ទះលេខ, ផ្លូវ , ភូមិ ៣, ឃុំ ព្រះពន្លឺ , ស្រុក សិរីសោភ័ណ, ខេត្ត បន្ទាយមានជ័យ',0.05,' '),('023','PHNOM PENH','ភ្នំពេញ','#273, Street 110-67, Sangkat Wat Phnom, Khan Daun Penh','ផ្ទះលេខ​273, ផ្លូវ​ 110-67, ភូមិ , សង្កាត់ វត្តភ្នំ , ខ័ណ្ឌ ដូនពេញ, រាជធានីភ្នំពេញ',0.14,' ');
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
  `baseprice` decimal(10,2) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`catid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbcategories`
--

LOCK TABLES `tbcategories` WRITE;
/*!40000 ALTER TABLE `tbcategories` DISABLE KEYS */;
INSERT INTO `tbcategories` VALUES (1,'1','Food','ម្ហូបអាហារ',0,11685.39,' '),(2,'1.1','Rice','អង្ករ',1,2732.35,' '),(3,'1.2','Ingredients','គ្រឿងទេស',1,3176.47,' '),(4,'1.3','Meat','សាច់',1,21579.88,' '),(5,'1.4','Fish and Seafood','ត្រី​ និង​គ្រឿងសមុទ្រ',1,19100.00,' '),(6,'1.5','Fruit','ផ្លែឈើ',1,5896.66,' '),(7,'1.6','Vegetables','បន្លែ',1,3769.07,' '),(8,'2','Beverages and Tobacco','ភេសជ្ជៈ​ និងថ្នាំជក់',0,1415.62,' '),(9,'3','Restaurant','ភោជនីយដ្ឋាន',0,6200.00,' '),(10,'4','Clothes and Shoes','សំលៀកបំពាក់ និងស្បែកជើង',0,37028.36,' '),(11,'5','Transportation','ការដឹកជញ្ជូន',0,150265.30,' '),(12,'6','Medicine','ថ្នាំពេទ្យ',0,5592.59,' '),(13,'7','Housing','ផ្ទះសម្បែង',0,41146.02,'');
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
INSERT INTO `tbmenus` VALUES (1,'Dashboard','ផ្ទាំងគ្រប់គ្រង','bx-clipboard',0,'/dashboard',' ',0),(2,'Food','អាហារ','bxs-food-menu',0,'/food','foods',1),(3,'Rice','អង្ករ',' ',2,'/rice',' ',2),(4,'Ingredients','គ្រឿងផ្សំ',' ',2,'/ingredients',' ',3),(5,'Meat','សាច់',' ',2,'/meat',' ',4),(6,'Fish and Seafood','ត្រី និងអាហារសមុទ្រ',' ',2,'/fishandseafood',' ',5),(7,'Fruit','ផ្លែឈើ',' ',2,'/fruit',' ',6),(8,'Vegetables','បន្លែ',' ',2,'/vegetables',' ',7),(9,'Beverages and Tobacco','ភេសជ្ជៈ និងថ្នាំជក់','bxs-drink',0,'/beveragestobacco',' ',8),(10,'Restaurant','ភោជនីយដ្ឋាន','bxs-data',0,'/restaurant',' ',9),(11,'Clothes and Shoes','សម្លៀកបំពាក់ និងស្បែកជើង','bx-male',0,'/clothesshoes',' ',10),(12,'Transportation','ការដឹកជញ្ជូន','bx-shopping-bag',0,'/shipping',' ',11),(13,'Medicine','ថ្នាំ','bx-plus-medical',0,'/medicine',' ',12),(14,'Housing','លំនៅដ្ឋាន','bxs-building-house',0,'/housing',' ',13),(15,'Submitted Trans','ប្រតិបត្តិការដែលបានដាក់ស្នើ','bxs-paper-plane',0,'/submittedtrans',' ',0),(16,'Authorized Trans','ប្រតិបត្តិការដែលមានការអនុញ្ញាត','bxs-notification',0,'/authorizedtrans',' ',0),(17,'Checked Trans','បានពិនិត្យប្រតិបត្តិការ','bxs-badge-check',0,'/checkedtrans',' ',0),(18,'History of Trans','ប្រវត្តិប្រតិបត្តិការ','bx-history',0,'/historyoftrans/1',' ',0),(19,'Users Setting','ការកំណត់អ្នកប្រើប្រាស់','bx-slider-alt',0,'/user','usersetting',0),(20,'User Profile','កម្រងព័ត៌មានអ្នកប្រើប្រាស់',' ',19,'/userprofile',' ',0),(21,'Change Password','ផ្លាស់ប្តូរពាក្យសម្ងាត់',' ',19,'/changepassword',' ',0),(22,'Logout','ចាកចេញ',' ',19,'/login',' ',0),(23,'Users Management','ការគ្រប់គ្រងអ្នកប្រើប្រាស់','bxs-user-account',0,'/users','usersmanagement',0),(24,'Create Users','បង្កើតអ្នកប្រើប្រាស់',' ',23,'/createusers',' ',0),(25,'Update Users','ធ្វើបច្ចុប្បន្នភាពអ្នកប្រើប្រាស់',' ',23,'/updateusers',' ',0),(26,'View Users','មើលអ្នកប្រើប្រាស់',' ',23,'/viewusers',' ',0),(27,'Roles Management','ការគ្រប់គ្រងតួនាទី','bx bxs-user-detail',0,'/role','rolesmangement',0),(28,'Create Role','បង្កើតតួនាទី',' ',27,'/createroles',' ',0),(29,'Create Permission','បង្កើតការអនុញ្ញាត',' ',27,'/createpermission',' ',0),(30,'View Roles','មើលតួនាទី',' ',27,'/attachedrolepermission',' ',0),(31,'Products Management','ការគ្រប់គ្រងផលិតផល','bx bx-category',0,'/product','productsmanagement',0),(32,'Categories','ប្រភេទ',' ',31,'/createcategories',' ',0),(36,'Products','ផលិតផល',' ',31,'/viewproducts',' ',0),(37,'Session Management','ការគ្រប់គ្រងរយៈពេល','bxs-building-house',0,'/session','sessionmanagement',0),(38,'Branch Session','សាខារយៈពេល','',37,'/branchsession',' ',0),(39,'Session Duration','ពេលវេលារយៈពេល',' ',37,'/sessionduration',' ',0),(40,'Branch Management','ការគ្រប់គ្រងសាខា','bx-shopping-bag',0,'/branchmanagement','branchmanagement',0),(41,'Create Branch','បង្កើតសាខា','',40,'/createbranch','',0),(42,'View Branches','មើលសាខា','',40,'/viewbranches','',0);
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
  `baseprice` decimal(10,2) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`prodid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbproducts`
--

LOCK TABLES `tbproducts` WRITE;
/*!40000 ALTER TABLE `tbproducts` DISABLE KEYS */;
INSERT INTO `tbproducts` VALUES (1,'1.1.1','Jasmine rice','អង្ករផ្កាម្លិះ',2.01,2,'រៀល/គក្រ','Riel/kg',3600.00,''),(2,'1.1.2','Phaka Kanhey rice','អង្ករផ្កាខ្ញី',2.01,2,'រៀល/គក្រ','Riel/kg',2800.00,' '),(3,'1.1.3','Neang Menh rice','អង្ករនាងមិញ',2.29,2,'រៀល/គក្រ','Riel/kg',2200.00,' '),(4,'1.1.4','Neang Khon rice','អង្ករនាងខុន',2.29,2,'រៀល/គក្រ','Riel/kg',3000.00,' '),(5,'1.1.5','Glutinous rice','អង្ករដំណើប',1.71,2,'រៀល/គក្រ','Riel/kg',3500.00,' '),(6,'1.1.6','Other grains','ធញ្ញជាតិផ្សេងៗ​ (សណ្តែកបាយ ក្រហម ខៀវ)',1.02,2,'រៀល/គក្រ','Riel/kg',7000.00,' '),(7,'1.2.1','Oils and fats','ប្រេងឆា និងខ្លាញ់',0.90,3,'រៀល/ដប','Riel/bottle',4000.00,' '),(8,'1.2.2','Fish sauce','ទឹកត្រី',0.40,3,'រៀល/ដប','Riel/bottle',3000.00,' '),(9,'1.2.3','Sugar','ស្ករ​​ស',0.50,3,'រៀល/គក្រ','Riel/kg',3000.00,' '),(10,'1.2.4','Brown sugar','ស្ករត្នោត',0.50,3,'រៀល/គក្រ','Riel/kg',4500.00,' '),(11,'1.2.5','Salt','អំបិល',0.50,3,'រៀល/គក្រ','Riel/kg',1500.00,' '),(12,'1.2.6','Soup powder','ម្សៅស៊ុប ',0.60,3,'រៀល/កញ្ចប់','Riel/packet',2500.00,' '),(13,'1.3.1','Beef','សាច់គោ',3.30,4,'រៀល/គក្រ','Riel/kg',40000.00,' '),(14,'1.3.2','Pork','សាច់ជ្រូក',4.62,4,'រៀល/គក្រ','Riel/kg',18000.00,' '),(15,'1.3.3','Chicken meat','សាច់មាន់',1.10,4,'រៀល/គក្រ','Riel/kg',20000.00,' '),(16,'1.3.4','Duck meat','សាច់ទា',0.90,4,'រៀល/គក្រ','Riel/kg',12000.00,' '),(17,'1.3.5','Chicken eggs','ស៊ុតមាន់',1.01,4,'រៀល/១០គ្រាប់','Riel/10 eggs',4500.00,' '),(18,'1.3.6','Duck eggs','ស៊ុតទា',1.01,4,'រៀល/១០គ្រាប់','Riel/10 eggs',5200.00,' '),(19,'1.4.1','Giant snakehead fish (free-range)','ត្រីរ៉ស់ (ស្រែ)',1.70,5,'រៀល/គក្រ','Riel/kg',25000.00,' '),(20,'1.4.2','Giant snakehead fish (farm-raised)','ត្រីរ៉ស់ (ចិញ្ចឹម)',2.40,5,'រៀល/គក្រ','Riel/kg',19000.00,' '),(21,'1.4.3','Striped snakehead','ត្រីឆ្តោ',1.70,5,'រៀល/គក្រ','Riel/kg',15000.00,' '),(22,'1.4.4','Walking catfish','ត្រីអណ្តែង',0.90,5,'រៀល/គក្រ','Riel/kg',17000.00,' '),(23,'1.4.5','Tilapia fish','ត្រីទីឡាបយ៉ា',0.90,5,'រៀល/គក្រ','Riel/kg',12000.00,' '),(24,'1.4.6','Dried fish ','ត្រីងៀត',1.00,5,'រៀល/គក្រ','Riel/kg',34000.00,' '),(25,'1.4.7','Phork','ផ្អក',0.80,5,'រៀល/គក្រ','Riel/kg',8000.00,' '),(26,'1.4.8','Prahok','ប្រហុក',0.80,5,'រៀល/គក្រ','Riel/kg',12000.00,' '),(27,'1.4.9','Salted-water fish','ត្រីសមុទ្រ ​(កាម៉ុងចំហុយ)',0.80,5,'រៀល/គក្រ','Riel/kg',18000.00,' '),(28,'1.4.10','Shrimp','បង្គា',1.40,5,'រៀល/គក្រ','Riel/kg',25000.00,' '),(29,'1.4.11','Squid','មឹក',1.30,5,'រៀល/គក្រ','Riel/kg',15000.00,' '),(30,'1.4.12','Oyster','ងាវ',1.00,5,'រៀល/គក្រ','Riel/kg',12000.00,' '),(31,'1.5.1','Namva banana','ចេកណាំវ៉ា',3.00,6,'រៀល/ស្និត','Riel/cluster',3150.00,' '),(32,'1.5.2','Apple','ប៉ោម',1.40,6,'រៀល/គក្រ','Riel/kg',10016.66,' '),(33,'1.5.3','Pursat Orange','ក្រូចពោធិសាត់',1.30,6,'រៀល/គក្រ','Riel/kg',14500.00,' '),(34,'1.5.4','Longan','មៀន',1.10,6,'រៀល/គក្រ','Riel/kg',10000.00,' '),(35,'1.5.5','Grape','ទំពាំងបាយជូរធម្មតា',1.30,6,'រៀល/គក្រ','Riel/kg',8000.00,' '),(36,'1.6.1','Water convolvulus','ត្រកួន',0.80,7,'រៀល/គក្រ','Riel/kg',4000.00,' '),(37,'1.6.2','Sawl','ស្ពៃចង្កឹះ',0.40,7,'រៀល/គក្រ','Riel/kg',4500.00,' '),(38,'1.6.3','Cucumber','ត្រសក់',1.00,7,'រៀល/គក្រ','Riel/kg',3000.00,' '),(39,'1.6.4','Carrot','ការ៉ុត',0.50,7,'រៀល/គក្រ','Riel/kg',3000.00,' '),(40,'1.6.5','Tomato','ប៉េងប៉ោះ',0.40,7,'រៀល/គក្រ','Riel/kg',3400.00,' '),(41,'1.6.6','Chinese kale','ដើមខាត់ណា',0.20,7,'រៀល/គក្រ','Riel/kg',4000.00,' '),(42,'1.6.7','Long cabbage','ស្ពៃក្តោប',0.20,7,'រៀល/គក្រ','Riel/kg',2500.00,' '),(43,'1.6.8','Leaf Lettuce','សាឡាដ',0.40,7,'រៀល/គក្រ','Riel/kg',3000.00,' '),(44,'1.6.9','Wax gourd','ត្រឡាច',0.30,7,'រៀល/គក្រ','Riel/kg',2500.00,' '),(45,'1.6.10','Eggplant','ត្រប់វែង',0.30,7,'រៀល/គក្រ','Riel/kg',2500.00,' '),(46,'1.6.11','Ginger','ខ្ញី',0.30,7,'រៀល/គក្រ','Riel/kg',3500.00,' '),(47,'1.6.12','Garlic','ខ្ទឹមស​ ',0.60,7,'រៀល/គក្រ','Riel/kg',4000.00,' '),(48,'1.6.13','Onion','ខ្ទឹមបារាំង',0.40,7,'រៀល/គក្រ','Riel/kg',3000.00,' '),(49,'1.6.14','Mushroom','ផ្សិត',0.30,7,'រៀល/គក្រ','Riel/kg',4000.00,' '),(50,'1.6.15','Bitter melon','ម្រះ',0.20,7,'រៀល/គក្រ','Riel/kg',3500.00,' '),(51,'2.1','Mineral water (Vital)','ទឹកសុទ្ធវីតាល់',1.00,8,'រៀល/ដប','Riel/bottle',1000.00,' '),(52,'2.2','Angkor Beer','ស្រាបៀរអង្គរ',0.80,8,'រៀល/កំប៉ុង','Riel/can',2000.00,' '),(53,'2.3','Coca-Cola','ទឹកក្រូចកូកាកូឡា',0.70,8,'រៀល/កំប៉ុង','Riel/can',1500.00,' '),(54,'2.4','Canned juice','ទឹកផ្លែឈើ',0.50,8,'រៀល/កំប៉ុង','Riel/can',2000.00,' '),(55,'2.5','Energy drinks','ភេសជ្ជៈប៉ូវកំលាំង (គោជល់ បាកាស...)',0.50,8,'រៀល/កំប៉ុង','Riel/can',2500.00,' '),(56,'2.6','Spirit','ស្រាបិទ',0.10,8,'រៀល/លីត្រ','Riel/litre',2500.00,' '),(57,'2.7','Iced Latte','កាហ្វេទឹកដោះគោទឹកកក',0.80,8,'រៀល/កែវ','Riel/glass',2000.00,' '),(58,'2.8','Cigarette','បារី',0.40,8,'រៀល/កញ្ចប់','Riel/packet',3000.00,' '),(59,'3.1','Noodles (breakfast)','គុយទាវធម្មតា (ព្រឹក)',2.80,9,'រៀល/ចាន','Riel/bowl',6000.00,' '),(60,'3.2','Lunch','បាយម្ហូបកម្ម៉ង់ថ្ងៃត្រង់មួយចម្អែត',1.50,9,'រៀល/ឈុត','Riel/set',6000.00,' '),(61,'3.3','Beef skewer','សាច់គោអាំង',0.50,9,'រៀល/ចាន','Riel/plate',7000.00,' '),(62,'3.4','Chicken rice','បាយសាច់មាន់ ',0.60,9,'រៀល/ចាន','Riel/plate',5000.00,' '),(63,'3.5','Pork rice','បាយសាច់ជ្រូក',0.60,9,'រៀល/ចាន','Riel/plate',4000.00,' '),(64,'3.6','Rice Porridge','បបរគ្រឿង',0.50,9,'រៀល/ចាន','Riel/bowl',3000.00,' '),(65,'3.7','Soup','ស៊ុប',0.60,9,'រៀល/ឆ្នាំង','Riel/set',20000.00,' '),(66,'4.1','Clothing for men','សំលៀកបំពាក់បុរស',0.62,10,'រៀល/សម្រាប់','Riel/piece',40000.00,' '),(67,'4.2','Clothing for women','សំលៀកបំពាក់នារី',0.90,10,'រៀល/សម្រាប់','Riel/piece',50000.00,' '),(68,'4.3','Clothing for kids','សំលៀកបំពាក់កូនក្មេង',0.30,10,'រៀល/សម្រាប់','Riel/piece',20000.00,' '),(69,'4.4','Footwear','ស្បែកជើង',0.40,10,'រៀល/គូរ','Riel/pair',16000.00,' '),(70,'5.1','Bicycles','កង់',1.10,11,'រៀល/គ្រឿង','Riel/bike',200000.00,' '),(71,'5.2','Honda Dream ,Motor cycles (Honda Dream)','ម៉ូតូ Honda Dream',1.70,11,'រៀល/គ្រឿង','Riel/motor',720000.00,' '),(72,'5.3','Gasoline','ប្រេងសាំងធម្មតា',4.00,11,'រៀល/លីត្រ','Riel/litre',4000.00,' '),(73,'5.4','Diesel','ប្រេងម៉ាស៊ូត',3.00,11,'រៀល/លីត្រ','Riel/litre',4200.00,' '),(74,'6.1','Paracetamol','ប៉ារ៉ា',1.20,12,'រៀល/កញ្ចប់','Riel/packet',6000.00,' '),(75,'6.2','Amoxicillin','អាម៉ុកស៊ីលីន',1.10,12,'រៀល/កញ្ចប់','Riel/packet',5000.00,' '),(76,'6.3','Vitamin C','វីតាមីន C',0.40,12,'រៀល/កញ្ចប់','Riel/packet',6000.00,' '),(77,'7.1','Water utilities','ថ្លៃប្រើប្រាស់ទឹក',3.60,13,'រៀល/ម៉ែត្រគីប','Riel/m3',700.00,' '),(78,'7.2','Electrical utilities','ថ្លៃប្រើប្រាស់ភ្លើង',8.60,13,'រៀល/គីឡូវ៉ាត់','Riel/kw',750.00,' '),(79,'7.3','Gas (15 kilograms)','ឧស្ម័ន (១៥គីឡូក្រាម)',3.30,13,'រៀល/១៥គក្រ','Riel/15kg',64000.00,' '),(80,'7.4','Rent','ថ្លៃជួលបន្ទប់ស្នាក់នៅ',2.10,13,'រៀល/ខែ','Riel/month',240000.00,' ');
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
INSERT INTO `tbrolemenu` VALUES (1,1,'','admin','2023-07-25 16:07:43',5),(1,19,'','admin','2023-07-25 16:07:43',5),(1,20,'','admin','2023-07-25 16:07:43',5),(1,21,'','admin','2023-07-25 16:07:43',5),(1,22,'','admin','2023-07-25 16:07:43',5),(1,23,'','admin','2023-07-25 16:07:43',5),(1,24,'','admin','2023-07-25 16:07:43',5),(1,26,'','admin','2023-07-25 16:07:43',5),(1,27,'','admin','2023-07-25 16:07:43',5),(1,28,'','admin','2023-07-25 16:07:43',5),(1,30,'','admin','2023-07-25 16:07:43',5),(1,31,'','admin','2023-07-25 16:07:43',5),(1,32,'','admin','2023-07-25 16:07:43',5),(1,36,'','admin','2023-07-25 16:07:43',5),(1,37,'','admin','2023-07-25 16:07:43',5),(1,38,'','admin','2023-07-25 16:07:43',5),(1,39,'','admin','2023-07-25 16:07:43',5),(1,40,'','admin','2023-07-25 16:07:43',5),(1,41,'','admin','2023-07-25 16:07:43',5),(1,42,'','admin','2023-07-25 16:07:43',5),(3,1,'','admin','2023-05-19 18:01:00',5),(3,2,'','admin','2023-05-19 18:01:00',5),(3,3,'','admin','2023-05-19 18:01:00',5),(3,4,'','admin','2023-05-19 18:01:00',5),(3,5,'','admin','2023-05-19 18:01:00',5),(3,6,'','admin','2023-05-19 18:01:00',5),(3,7,'','admin','2023-05-19 18:01:00',5),(3,8,'','admin','2023-05-19 18:01:00',5),(3,9,'','admin','2023-05-19 18:01:00',5),(3,10,'','admin','2023-05-19 18:01:00',5),(3,11,'','admin','2023-05-19 18:01:00',5),(3,12,'','admin','2023-05-19 18:01:00',5),(3,13,'','admin','2023-05-19 18:01:00',5),(3,14,'','admin','2023-05-19 18:01:00',5),(3,15,'','admin','2023-05-19 18:01:00',5),(3,18,'','admin','2023-05-19 18:01:00',5),(3,19,'','admin','2023-05-19 18:01:00',5),(3,20,'','admin','2023-05-19 18:01:00',5),(3,21,'','admin','2023-05-19 18:01:00',5),(3,22,'','admin','2023-05-19 18:01:00',5),(3,49,'','admin','2023-05-19 18:01:00',5),(4,1,'','admin','2023-05-19 18:01:11',5),(4,16,'','admin','2023-05-19 18:01:11',5),(4,18,'','admin','2023-05-19 18:01:11',5),(4,19,'','admin','2023-05-19 18:01:11',5),(4,20,'','admin','2023-05-19 18:01:11',5),(4,21,'','admin','2023-05-19 18:01:11',5),(4,22,'','admin','2023-05-19 18:01:11',5),(5,1,'','admin','2023-07-25 16:07:21',5),(5,17,'','admin','2023-07-25 16:07:21',5),(5,18,'','admin','2023-07-25 16:07:21',5),(5,19,'','admin','2023-07-25 16:07:21',5),(5,20,'','admin','2023-07-25 16:07:21',5),(5,21,'','admin','2023-07-25 16:07:21',5),(5,22,'','admin','2023-07-25 16:07:21',5);
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
INSERT INTO `tbroles` VALUES (1,'Administrator',' Administrator'),(3,'Inputter',' Inputter'),(4,'Authorizer','Authorizer'),(5,'Checker','Checker');
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
  `baseprice` decimal(10,2) DEFAULT NULL,
  `branchweight` decimal(10,2) DEFAULT NULL,
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
  `phonenumber` varchar(45) DEFAULT NULL,
  `telegram` varchar(150) DEFAULT NULL,
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
INSERT INTO `tbusers` VALUES ('admin','gAAAAABkawroLag12cpFEBd-lCL37WKAYRO2uNLoqYi7dC3ekYElCV72-7Ks4aQRszwsuh363XdNeTHSP_tzi39lHGrJvlwcLA==','e_VrNdrMv--3qRk1LS9bAeQsnud8Cy0QKqMLCE6L6aE=',1,'admin','Male','001','administrator','admin','admin@nbc.gov.org',5,'2','2','EN');
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

-- Dump completed on 2023-07-27  9:58:17
