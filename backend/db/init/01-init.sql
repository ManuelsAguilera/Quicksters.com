CREATE DATABASE  IF NOT EXISTS `quicksters_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `quicksters_db`;
-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: quicksters_db
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
  `nombre_categoria` varchar(45) NOT NULL,
  `juego` varchar(45) NOT NULL,
  PRIMARY KEY (`idcategoria`),
  KEY `idjuego_idx` (`idjuego`),
  CONSTRAINT `idjuego` FOREIGN KEY (`idjuego`) REFERENCES `juegos` (`idjuego`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categoria`
--

LOCK TABLES `categoria` WRITE;
/*!40000 ALTER TABLE `categoria` DISABLE KEYS */;
INSERT INTO `categoria` VALUES (1,1,'ANY%',''),(2,2,'ANY%','');
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `juegos`
--

LOCK TABLES `juegos` WRITE;
/*!40000 ALTER TABLE `juegos` DISABLE KEYS */;
INSERT INTO `juegos` VALUES (1,'The Binding of Isaac','https://cdn2.steamgriddb.com/thumb/d22605e2bddb461a4034acb67334c1f7.jpg','https://cdn2.steamgriddb.com/grid/76ad456b5dfc57b0b1d20f249a5f8453.png'),(2,'Super Mario Bros.(1985)',NULL,NULL),(4,'Hentai Furry','https://cdn2.steamgriddb.com/thumb/d22605e2bddb461a4034acb67334c1f7.jpg','https://cdn2.steamgriddb.com/grid/76ad456b5dfc57b0b1d20f249a5f8453.png');
/*!40000 ALTER TABLE `juegos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `speedrun`
--

DROP TABLE IF EXISTS `speedrun`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `speedrun` (
  `idspeedrun` int NOT NULL,
  `idusuario` int NOT NULL,
  `idcategoria` int NOT NULL,
  `url_video` varchar(255) DEFAULT NULL,
  `verificado` tinyint NOT NULL,
  `duracion` time DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `usuario` varchar(50) NOT NULL,
  `categoria` varchar(50) NOT NULL,
  PRIMARY KEY (`idspeedrun`),
  UNIQUE KEY `idspeedrun_UNIQUE` (`idspeedrun`),
  KEY `idusuario_idx` (`idusuario`),
  KEY `idcategoria_idx` (`idcategoria`),
  CONSTRAINT `idcategoria` FOREIGN KEY (`idcategoria`) REFERENCES `categoria` (`idcategoria`),
  CONSTRAINT `idusuario` FOREIGN KEY (`idusuario`) REFERENCES `usuario` (`idusuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `speedrun`
--

LOCK TABLES `speedrun` WRITE;
/*!40000 ALTER TABLE `speedrun` DISABLE KEYS */;
INSERT INTO `speedrun` VALUES (1,1,1,'https://www.youtube.com/watch?v=AzUjFXsVcQo',0,NULL,'2025-06-07','Alecs','ANY%'),(9,2,2,NULL,0,NULL,'2025-06-06','Manuel','ANY%');
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
  `contraseña` varchar(20) NOT NULL,
  PRIMARY KEY (`idusuario`),
  UNIQUE KEY `idusuario_UNIQUE` (`idusuario`),
  UNIQUE KEY `username_UNIQUE` (`username`),
  UNIQUE KEY `correo_UNIQUE` (`correo`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'Alecs','alecs@gmail.com','chile','a'),(2,'Manuel','Manuel@gmail.com','venezuela','b'),(5,'ELISEO','eliuwu@gmail.com','peru','123456');
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

-- Dump completed on 2025-06-08  7:53:47
