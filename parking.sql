/*!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19  Distrib 10.6.18-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: parking_db
-- ------------------------------------------------------
-- Server version	9.0.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roles` (
  `id` int NOT NULL AUTO_INCREMENT,
  `role` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'client'),(2,'admin');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `contact` int NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `role_id` int NOT NULL,
  `fullname` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `fk_users_roles` (`role_id`),
  CONSTRAINT `fk_users_roles` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'$2b$12$bqDd4mZmBc.xv1vlp998VeNC.2ri9lsAnqZ3vbXAHA2M2W7Z2vrAi','luke@mail.com',649339154,'2025-01-13 23:56:42',1,'Luke Skywalker'),(2,'$2b$12$Rnn6Hu3F6cxXvp3hUjuWNOPW8dfpqQHZBMBGMfldeZNP8acoCRwBW','ferran@m.m',657489675,'2025-01-14 17:37:05',1,'Ferran Roca'),(3,'$2b$12$DTJS9oI9RKNwJnIqqaBTAeDelP4AFgiQQxjlnZN2JQTxycM3txiOu','user1@example.com',123456790,'2025-01-14 19:02:44',2,'User Fullname 1'),(4,'$2b$12$IeOAE50IfC7csYIrQOJIyehCgcBds/f1ZWQGc5nEFFian/bVmP1ge','user2@example.com',123456791,'2025-01-14 19:02:44',1,'User Fullname 2'),(5,'$2b$12$tq7jF29ut3aHHY3a/EtSM.g1K02vuRfE6.vUXyBz.ba50m5si0Fna','user3@example.com',123456792,'2025-01-14 19:02:45',2,'User Fullname 3'),(6,'$2b$12$qDR/MJpHKVSKjJKTOfJmQebVwhMnU1eOHYTPOyaAcF39h/PBjhKSK','user4@example.com',123456793,'2025-01-14 19:02:45',1,'User Fullname 4'),(7,'$2b$12$.WxucdhpX6Q9hzDYXSMgO.744LbXVzp27KSZdL7144vdDMDoANHY6','user5@example.com',123456794,'2025-01-14 19:02:46',2,'User Fullname 5'),(8,'$2b$12$hewfEGbEXj1LQQNnJLjZv.TcwElZnDhCRQ98jbToMZLA0ZWHxwfYS','user6@example.com',123456795,'2025-01-14 19:02:47',1,'User Fullname 6'),(9,'$2b$12$vgsRNPJN7wMcZwWRxa8M0.97ViH3c0dDVpKHrPLny1e3SzBznU2hS','user7@example.com',123456796,'2025-01-14 19:02:47',2,'User Fullname 7'),(10,'$2b$12$qf0ybrGfXCQy1nI5SzNwJuxFIrMrJZ.lDemTZD3zZ.ioWvdWQytzi','user8@example.com',123456797,'2025-01-14 19:02:48',1,'User Fullname 8'),(11,'$2b$12$QPwQbS8FaqWTVZN/TAPqi.QaKYHrHMHz2rI6UCgrHUXDaG6PWsJou','user9@example.com',123456798,'2025-01-14 19:02:48',2,'User Fullname 9'),(12,'$2b$12$7n/690ry6AHgC0jHvvAOTeXIKTBJgrkOe8PV2DTLWR9JBpWKej95i','user10@example.com',123456799,'2025-01-14 19:02:49',1,'User Fullname 10'),(13,'$2b$12$9JFoez.80nPxNA70Of2cr.iCvkp7VGSswnqiel67H5Wym.NM1WNJm','user11@example.com',123456800,'2025-01-14 19:02:50',2,'User Fullname 11'),(14,'$2b$12$aCcoYvprnhcq9xTru.yzweheh2tn.AocGXlu1SuReYkikOFVOK5Ue','user12@example.com',123456801,'2025-01-14 19:02:50',1,'User Fullname 12'),(15,'$2b$12$EzX4YNPI8Jyo66WyM2aex.vnLjPScFlGTSYa1vJiYsT9QF0NAW8Tu','user13@example.com',123456802,'2025-01-14 19:02:51',2,'User Fullname 13'),(16,'$2b$12$/gOwlw7sqRTMeWW3w15rgOG3b/r9D9jnzBmJL1oLBaQL4CkEOnRmO','user14@example.com',123456803,'2025-01-14 19:02:51',1,'User Fullname 14'),(17,'$2b$12$x1cLq2ZLH9/h001k9RvoX.CL/vMMie2iQSfcGUdLeOVF4/xBcVG4W','user15@example.com',123456804,'2025-01-14 19:02:52',2,'User Fullname 15'),(18,'$2b$12$UUC0.8Kksg7Yqs7c4DHkmeFmd/SRZDaBgV8Tcexbck.1i0o6skxsq','user16@example.com',123456805,'2025-01-14 19:02:53',1,'User Fullname 16'),(19,'$2b$12$UCrae1rOdtlbafAXpv4zYeOqs8nRHcjy/ZmF/GCWqvc0yYbdBet5q','user17@example.com',123456806,'2025-01-14 19:02:53',2,'User Fullname 17'),(20,'$2b$12$Tf0CQItBRxx1KCaH/G6C6ujXbPuI8ePNDgG1jjVCl5ylnnwnF/fdO','user18@example.com',123456807,'2025-01-14 19:02:54',1,'User Fullname 18'),(21,'$2b$12$F0JzKDbE1kPxU6TcBzyLGOQdW6XumPhJX0nQC/YotfsTUT/jpCoR6','user19@example.com',123456808,'2025-01-14 19:02:54',2,'User Fullname 19'),(22,'$2b$12$N.nBhSkdpmxt.RLPyOW2Ue4.JgiVzMtb/mgXQd.wyrAx9aCWsn34a','user20@example.com',123456809,'2025-01-14 19:02:55',1,'User Fullname 20'),(23,'$2b$12$wvPyK1gZvMuoIeYaZaNSr.4UZOxx2z1u1vCzfLVIN8xKsluvA.sju','user21@example.com',123456810,'2025-01-14 19:02:56',2,'User Fullname 21'),(24,'$2b$12$upaUMdGoNyX0awYWk6oh7ODUcwp13zhewRCB32vp/2hP/QTJwk8ES','user22@example.com',123456811,'2025-01-14 19:02:56',1,'User Fullname 22'),(25,'$2b$12$SHYLvSwMAxGSMDhIO7L1d.HfPsyNHlNYjQMWEUloqlCqU0CYhVX1.','user23@example.com',123456812,'2025-01-14 19:02:57',2,'User Fullname 23'),(26,'$2b$12$okjjpXg39CDAwClJempwfuP8ozSghCm7eyVEUx58yeDMdxIxgP.Uq','user24@example.com',123456813,'2025-01-14 19:02:57',1,'User Fullname 24'),(27,'$2b$12$ta3hlbitzqaFIdjEoVrLF.CpC.XIdugQjbrWOZrocHGJF52kDj7h6','user25@example.com',123456814,'2025-01-14 19:02:58',2,'User Fullname 25'),(28,'$2b$12$o6w9Ng2nwrO1lyJaWhwVMuMay0U15fWRFI58ThMdb25qBCNu3ERcC','user26@example.com',123456815,'2025-01-14 19:02:59',1,'User Fullname 26'),(29,'$2b$12$Ltaru6uSCLQ4LihaUWAI8OiRRbPTkjfmWesZKBzWZ2rk79uAcFEX2','user27@example.com',123456816,'2025-01-14 19:02:59',2,'User Fullname 27'),(30,'$2b$12$9kbwBj9Lvhe8XEux7s/g9e9JeXTJF3JQEcrtiqzF5RkG4daQbiH.e','user28@example.com',123456817,'2025-01-14 19:03:00',1,'User Fullname 28'),(31,'$2b$12$/OANgjuyRH.VRNHi8WL.q.aMVC7F4RLrOsBiQepfBxhVNdSg4zZrC','user29@example.com',123456818,'2025-01-14 19:03:00',2,'User Fullname 29'),(32,'$2b$12$2qroKblwIb9w63YJYPhI5OZzlxKQAIQelOK7HOR7Fg9apaDD02Hm6','user30@example.com',123456819,'2025-01-14 19:03:01',1,'User Fullname 30');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-01-14 20:47:25
