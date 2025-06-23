-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: quicksters_db
-- ------------------------------------------------------
-- Server version	8.0.42

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
-- Table structure for table `categoria`
--

DROP TABLE IF EXISTS `categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categoria` (
  `idcategoria` int NOT NULL,
  `idjuego` int NOT NULL,
  `nombre_categoria` varchar(100) NOT NULL,
  PRIMARY KEY (`idcategoria`,`idjuego`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categoria`
--

LOCK TABLES `categoria` WRITE;
/*!40000 ALTER TABLE `categoria` DISABLE KEYS */;
INSERT INTO `categoria` VALUES (1,1,'ANY%'),(1,2,'ANY%'),(2,1,'100%'),(2,2,'100%'),(3,1,'All Hero Lives');
/*!40000 ALTER TABLE `categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `juegos`
--

DROP TABLE IF EXISTS `juegos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `juegos` (
  `idjuego` int NOT NULL AUTO_INCREMENT,
  `juego` varchar(100) NOT NULL,
  `url_icono` varchar(255) DEFAULT NULL,
  `url_banner` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idjuego`),
  UNIQUE KEY `idjuegos_UNIQUE` (`idjuego`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `juegos`
--

LOCK TABLES `juegos` WRITE;
/*!40000 ALTER TABLE `juegos` DISABLE KEYS */;
INSERT INTO `juegos` VALUES (1,'FANTASY LIFE i: The Girl Who Steals Time','https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2993780/header.jpg?t=1749900924','https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2993780/page_bg_raw.jpg?t=1749900924'),(2,'Counter-Strike 2','https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/730/header.jpg?t=1749053861','https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/730/page_bg_raw.jpg?t=1749053861'),(8,'DRAPLINE','https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/3103780/header.jpg?t=1750065632','https://store.akamai.steamstatic.com/images/storepagebackground/app/3103780?t=1750065632'),(9,'Rust','https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/252490/header.jpg?t=1747389753','https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/252490/page_bg_raw.jpg?t=1747389753'),(10,'ELDEN RING NIGHTREIGN','https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2622380/header.jpg?t=1749150157','https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2622380/page_bg_raw.jpg?t=1749150157'),(11,'PEAK','https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/3527290/31bac6b2eccf09b368f5e95ce510bae2baf3cfcd/header.jpg?t=1750093258','https://store.akamai.steamstatic.com/images/storepagebackground/app/3527290?t=1750093258'),(12,'Shadowverse: Worlds Beyond','https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2584990/bab5a90e2765d340ca3ba8553e1b0ee679176dda/header.jpg?t=1750319997','https://store.akamai.steamstatic.com/images/storepagebackground/app/2584990?t=1750319997'),(13,'Banana','https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2923300/6d550eab6dcbc01a824763edbafa9e439e625d5e/header.jpg?t=1748551280','https://store.akamai.steamstatic.com/images/storepagebackground/app/2923300?t=1748551280'),(14,'REMATCH','https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2138720/header.jpg?t=1750327757','https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2138720/page_bg_raw.jpg?t=1750327757'),(15,'Tametsi','https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/709920/header.jpg?t=1691590878','https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/709920/page_bg_raw.jpg?t=1691590878'),(16,'Minecraft Dungeons','https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1672970/header.jpg?t=1717003107','https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1672970/page_bg_raw.jpg?t=1717003107'),(17,'Stardew Valley','https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/413150/header.jpg?t=1711128146','https://store.akamai.steamstatic.com/images/storepagebackground/app/413150?t=1711128146'),(18,'Team Fortress 2','https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/440/header.jpg?t=1745368581','https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/440/page_bg_raw.jpg?t=1745368581'),(19,'7 Days to Die','https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/251570/header.jpg?t=1749691592','https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/251570/page_bg_raw.jpg?t=1749691592'),(20,'R.E.P.O.','https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/3241660/1ea445e044a2d5b09cfa8291350b63ebed6e5741/header.jpg?t=1749626961','https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/3241660/page_bg_raw.jpg?t=1749626961'),(21,'ARK: Survival Ascended','https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2399830/header.jpg?t=1750290390','https://store.akamai.steamstatic.com/images/storepagebackground/app/2399830?t=1750290390'),(22,'ELDEN RING','https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1245620/header.jpg?t=1748630546','https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1245620/page_bg_raw.jpg?t=1748630546');
/*!40000 ALTER TABLE `juegos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `speedrun`
--

DROP TABLE IF EXISTS `speedrun`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `speedrun` (
  `idspeedrun` int NOT NULL AUTO_INCREMENT,
  `idusuario` int NOT NULL,
  `idcategoria` int NOT NULL,
  `idjuego` int NOT NULL,
  `url_video` varchar(255) NOT NULL,
  `verificado` tinyint NOT NULL,
  `duracion` varchar(12) NOT NULL,
  `fecha` date NOT NULL,
  PRIMARY KEY (`idspeedrun`),
  UNIQUE KEY `idspeedrun_UNIQUE` (`idspeedrun`),
  KEY `idusuario_idx` (`idusuario`),
  KEY `idcategoria_idx` (`idcategoria`),
  KEY `idjuego_idx` (`idjuego`),
  CONSTRAINT `idcategoria` FOREIGN KEY (`idcategoria`) REFERENCES `categoria` (`idcategoria`),
  CONSTRAINT `idusuario` FOREIGN KEY (`idusuario`) REFERENCES `usuario` (`idusuario`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `speedrun`
--

LOCK TABLES `speedrun` WRITE;
/*!40000 ALTER TABLE `speedrun` DISABLE KEYS */;
INSERT INTO `speedrun` VALUES (1,1,1,1,'https://youtu.be/n7gOKTqKbC8',1,'02:26:04','2025-06-04'),(2,2,1,2,'https://youtu.be/A0gFk33JYbA',1,'00:00:40','2025-05-05'),(3,1,2,1,'https://youtu.be/n7gOKTqKbC8',1,'02:26:03','2025-06-04'),(4,1,3,1,'https://youtu.be/n7gOKTqKbC8',1,'02:26:03','2025-06-04'),(5,2,1,1,'https://youtu.be/n7gOKTqKbC8',1,'02:26:03','2025-06-04'),(6,3,2,1,'https://www.youtube.com/watch?v=n7gOKTqKbC8',1,'00:11:22','2025-06-23');
/*!40000 ALTER TABLE `speedrun` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `idusuario` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `correo` varchar(50) NOT NULL,
  `nacionalidad` varchar(50) NOT NULL,
  `contraseña` varchar(100) NOT NULL,
  PRIMARY KEY (`idusuario`),
  UNIQUE KEY `idusuario_UNIQUE` (`idusuario`),
  UNIQUE KEY `username_UNIQUE` (`username`),
  UNIQUE KEY `correo_UNIQUE` (`correo`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'Eliseo','eliseo@probando.com','Chile','$2b$12$oXz3cScPZrY5T0a3H3IaUOsIflaW6OGGadG3FRWKAAKD/e0Ar96L2'),(2,'Manuel','manuel@probando.com','Uruguay','$2b$12$v24QNInulT5FVnEUwcuwbuubrDHHo9mUobv7.y5K3qdEStwnWH7Dm'),(3,'Alex','alex@probando.com','Peru','$2b$12$2C7rBcnJUzVS4lmLbRUeNeJoqjFHTC2MHWjChqVaaXTkqIEwv153C'),(4,'Vicente','vicente@probando.com','Bolivia','$2b$12$GsNVu0uyX5OUMFW82yKsPuyyVzMx5fgbdu/ENsMTuN0kbGbUteoLq'),(19,'Matias','matias@probando.com','China','$2b$12$e.s/c.4SjauiEdw71rejx.rO4ZOOl0.KXitIxk0HC0PoBVD.xztHC'),(20,'Rodrigo','rodrigo@probando.com','Paraguay','$2b$12$7ls125WT3MLmIiYzvN8SkOzi/hEkA5bwjcJxdEDz4O7xiEpRakTAu');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-23 12:10:31
