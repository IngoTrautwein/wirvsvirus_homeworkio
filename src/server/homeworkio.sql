CREATE DATABASE  IF NOT EXISTS `homeworkio` /*!40100 DEFAULT CHARACTER SET latin1 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `homeworkio`;
-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: homeworkio
-- ------------------------------------------------------
-- Server version	8.0.19

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
-- Table structure for table `homework`
--

DROP TABLE IF EXISTS `homework`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `homework` (
  `id` int NOT NULL,
  `school_class_id` int NOT NULL,
  `subject_id` int NOT NULL,
  `file_path` varchar(100) DEFAULT NULL,
  `start_event` datetime DEFAULT NULL,
  `end_event` datetime DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_school_class_id_hw_idx` (`school_class_id`),
  KEY `fk_couse_id_hw_idx` (`subject_id`),
  CONSTRAINT `fk_school_class_id_hw` FOREIGN KEY (`school_class_id`) REFERENCES `school_class` (`id`),
  CONSTRAINT `fk_subject_id_hw` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `homework`
--

LOCK TABLES `homework` WRITE;
/*!40000 ALTER TABLE `homework` DISABLE KEYS */;
INSERT INTO `homework` VALUES (0,0,0,'/path/to/file.pdf','2020-03-21 19:09:22','2020-03-22 19:09:22','Here are your homeworks for the next week.');
/*!40000 ALTER TABLE `homework` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `school`
--

DROP TABLE IF EXISTS `school`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `school` (
  `id` int NOT NULL,
  `name` varchar(20) NOT NULL,
  `address` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `school_class_id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `school`
--

LOCK TABLES `school` WRITE;
/*!40000 ALTER TABLE `school` DISABLE KEYS */;
INSERT INTO `school` VALUES (0,'SP Gymnasium','address 123');
/*!40000 ALTER TABLE `school` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `school_class`
--

DROP TABLE IF EXISTS `school_class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `school_class` (
  `id` int NOT NULL,
  `student_id` int NOT NULL,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `teacher_id` (`id`),
  KEY `student_id` (`id`),
  KEY `t_student_school_class_ibfk_1` (`student_id`),
  CONSTRAINT `t_student_school_class_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `student` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `school_class`
--

LOCK TABLES `school_class` WRITE;
/*!40000 ALTER TABLE `school_class` DISABLE KEYS */;
INSERT INTO `school_class` VALUES (0,0,'4a');
/*!40000 ALTER TABLE `school_class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `id` int NOT NULL,
  `surname` varchar(20) NOT NULL,
  `first_name` varchar(20) NOT NULL,
  `school_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_school_id_idx` (`school_id`),
  CONSTRAINT `fk_school_id_student` FOREIGN KEY (`school_id`) REFERENCES `school` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (0,'Cartman','Eric',0),(1,'Marsh','Stan',0),(2,'Browslowski','Kyle',0),(3,'Mc Cormick','Kenny',0);
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subject`
--

DROP TABLE IF EXISTS `subject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `subject` (
  `id` int NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subject`
--

LOCK TABLES `subject` WRITE;
/*!40000 ALTER TABLE `subject` DISABLE KEYS */;
INSERT INTO `subject` VALUES (0,'Math'),(1,'English'),(2,'German');
/*!40000 ALTER TABLE `subject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subject_school_class`
--

DROP TABLE IF EXISTS `subject_school_class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `subject_school_class` (
  `id` int NOT NULL,
  `subject_id` int NOT NULL,
  `school_class_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_couse_id_idx` (`subject_id`),
  KEY `fk_school_class_id_idx` (`school_class_id`),
  CONSTRAINT `fk_school_class_id` FOREIGN KEY (`school_class_id`) REFERENCES `school_class` (`id`),
  CONSTRAINT `fk_subject_id` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subject_school_class`
--

LOCK TABLES `subject_school_class` WRITE;
/*!40000 ALTER TABLE `subject_school_class` DISABLE KEYS */;
INSERT INTO `subject_school_class` VALUES (0,0,0),(1,1,0);
/*!40000 ALTER TABLE `subject_school_class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher`
--

DROP TABLE IF EXISTS `teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teacher` (
  `id` int NOT NULL,
  `surname` varchar(20) NOT NULL,
  `first_name` varchar(20) NOT NULL,
  `school_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_school_id_idx` (`school_id`),
  KEY `fk_school_id_teacher_idx` (`school_id`),
  CONSTRAINT `fk_school_id_teacher` FOREIGN KEY (`school_id`) REFERENCES `school` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher`
--

LOCK TABLES `teacher` WRITE;
/*!40000 ALTER TABLE `teacher` DISABLE KEYS */;
INSERT INTO `teacher` VALUES (0,'Marsh','Randy',0);
/*!40000 ALTER TABLE `teacher` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-03-21 19:42:41
