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
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `course` (
  `course_id` int NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`course_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course`
--

LOCK TABLES `course` WRITE;
/*!40000 ALTER TABLE `course` DISABLE KEYS */;
INSERT INTO `course` VALUES (0,'Math'),(1,'English'),(2,'German');
/*!40000 ALTER TABLE `course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `course_school_class`
--

DROP TABLE IF EXISTS `course_school_class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `course_school_class` (
  `course_school_class_id` int NOT NULL,
  `couse_id` int NOT NULL,
  `school_class_id` int NOT NULL,
  PRIMARY KEY (`course_school_class_id`),
  KEY `fk_couse_id_idx` (`couse_id`),
  KEY `fk_school_class_id_idx` (`school_class_id`),
  CONSTRAINT `fk_couse_id` FOREIGN KEY (`couse_id`) REFERENCES `course` (`course_id`),
  CONSTRAINT `fk_school_class_id` FOREIGN KEY (`school_class_id`) REFERENCES `school_class` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course_school_class`
--

LOCK TABLES `course_school_class` WRITE;
/*!40000 ALTER TABLE `course_school_class` DISABLE KEYS */;
INSERT INTO `course_school_class` VALUES (0,0,0),(1,1,0);
/*!40000 ALTER TABLE `course_school_class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `homework`
--

DROP TABLE IF EXISTS `homework`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `homework` (
  `homework_id` int NOT NULL,
  `school_class_id` int NOT NULL,
  `course_id` int NOT NULL,
  `file_path` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`homework_id`),
  KEY `fk_school_class_id_hw_idx` (`school_class_id`),
  KEY `fk_couse_id_hw_idx` (`course_id`),
  CONSTRAINT `fk_couse_id_hw` FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`),
  CONSTRAINT `fk_school_class_id_hw` FOREIGN KEY (`school_class_id`) REFERENCES `school_class` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `homework`
--

LOCK TABLES `homework` WRITE;
/*!40000 ALTER TABLE `homework` DISABLE KEYS */;
INSERT INTO `homework` VALUES (0,0,0,'/path/to/file.pdf');
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

--
-- Table structure for table `teacher_school_class`
--

DROP TABLE IF EXISTS `teacher_school_class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teacher_school_class` (
  `teacher_school_class_id` int NOT NULL,
  `teacher_id` int NOT NULL,
  `school_class_id` int NOT NULL,
  PRIMARY KEY (`teacher_school_class_id`),
  KEY `t_teacher_id_idx` (`teacher_id`),
  KEY `t_school_class_id_idx` (`school_class_id`),
  CONSTRAINT `t_school_class_id_teacher_school_class` FOREIGN KEY (`school_class_id`) REFERENCES `school_class` (`id`),
  CONSTRAINT `t_teacher_id_teacher_school_class` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher_school_class`
--

LOCK TABLES `teacher_school_class` WRITE;
/*!40000 ALTER TABLE `teacher_school_class` DISABLE KEYS */;
INSERT INTO `teacher_school_class` VALUES (0,0,0);
/*!40000 ALTER TABLE `teacher_school_class` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-03-21 18:54:33
