-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: 172.16.33.8    Database: better_part_picker
-- ------------------------------------------------------
-- Server version	8.0.41-0ubuntu0.22.04.1

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
-- Table structure for table `PreBuilt`
--

DROP TABLE IF EXISTS `PreBuilt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PreBuilt` (
  `PreSerial` int NOT NULL,
  `PreName` varchar(30) NOT NULL,
  `PreBrand` varchar(30) NOT NULL,
  `PrePrice` int NOT NULL,
  `PWRSerial` int NOT NULL,
  `MoboSerial` int NOT NULL,
  `CPUSerial` int NOT NULL,
  `GPUSerial` int NOT NULL,
  `RAMSerial` int NOT NULL,
  PRIMARY KEY (`PreSerial`),
  KEY `PWRSerial` (`PWRSerial`),
  KEY `MoboSerial` (`MoboSerial`),
  KEY `CPUSerial` (`CPUSerial`),
  KEY `GPUSerial` (`GPUSerial`),
  KEY `RAMSerial` (`RAMSerial`),
  CONSTRAINT `PreBuilt_ibfk_1` FOREIGN KEY (`PWRSerial`) REFERENCES `PowerSupply` (`PWRSerial`),
  CONSTRAINT `PreBuilt_ibfk_2` FOREIGN KEY (`MoboSerial`) REFERENCES `Motherboard` (`MoboSerial`),
  CONSTRAINT `PreBuilt_ibfk_3` FOREIGN KEY (`CPUSerial`) REFERENCES `CPU` (`CPUSerial`),
  CONSTRAINT `PreBuilt_ibfk_4` FOREIGN KEY (`GPUSerial`) REFERENCES `GPU` (`GPUSerial`),
  CONSTRAINT `PreBuilt_ibfk_5` FOREIGN KEY (`RAMSerial`) REFERENCES `Memory` (`RAMSerial`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PreBuilt`
--

LOCK TABLES `PreBuilt` WRITE;
/*!40000 ALTER TABLE `PreBuilt` DISABLE KEYS */;
/*!40000 ALTER TABLE `PreBuilt` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-02-24 11:28:57
