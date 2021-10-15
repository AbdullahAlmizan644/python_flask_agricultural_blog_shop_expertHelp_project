-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 13, 2021 at 11:50 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `agroaid`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(200) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(200) NOT NULL,
  `phone_number` int(200) NOT NULL,
  `message` text NOT NULL,
  `date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `email`, `phone_number`, `message`, `date`) VALUES
(1, 'Abdullah Al Mizan', 'priyoakashi405@gmail.com', 1862856218, 'hi', '2021-01-16 14:11:41.639434'),
(2, 'Abdullah Al Mizan', 'priyoakashi405@gmail.com', 1862856218, 'hi', '2021-01-16 17:03:55.316750'),
(3, 'Abdullah Al Mizan', 'priyoakashi405@gmail.com', 1862856218, 'hi', '2021-01-16 17:04:40.881092'),
(4, 'Abdullah Al Mizan', 'abdullahalmizan644@gmail.com', 1862856218, 'hi', '2021-01-16 17:07:40.888303'),
(5, 'Abdullah Al Mizan', 'priyoakashi405@gmail.com', 1862856218, 'hi', '2021-01-16 17:08:55.242373'),
(6, 'Abdullah Al Mizan', 'priyoakashi405@gmail.com', 1862856218, 'hi', '2021-01-16 17:13:21.139657'),
(7, 'sunny leaon', 'priyoakashi405@gmail.com', 1862856218, 'hi karim', '2021-02-22 00:38:35.575171'),
(8, 'sunny leaon', 'priyoakashi405@gmail.com', 1862856218, 'hi karim', '2021-02-22 00:39:08.831116'),
(9, 'sunny leaon', 'priyoakashi405@gmail.com', 1862856218, 'hi karim', '2021-02-22 00:39:41.283721'),
(10, 'Abdullah Al Mizan', 'priyoakashi405@gmail.com', 1862856218, 'aWDADSAD', '2021-02-23 01:04:48.009036');

-- --------------------------------------------------------

--
-- Table structure for table `expert`
--

CREATE TABLE `expert` (
  `id` int(200) NOT NULL,
  `name` varchar(200) NOT NULL,
  `phone` varchar(200) NOT NULL,
  `image` varchar(200) NOT NULL,
  `address` varchar(200) NOT NULL,
  `workspace` varchar(200) NOT NULL,
  `research` varchar(200) NOT NULL,
  `education` varchar(200) NOT NULL,
  `username` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `expert`
--

INSERT INTO `expert` (`id`, `name`, `phone`, `image`, `address`, `workspace`, `research`, `education`, `username`, `password`, `email`) VALUES
(1, 'Dr. Md. Abdur Rahim', '+880*********', 'Abdur-Rahim.png', 'Email: dean.ag@bau.edu.bd', 'agriculture', 'agricuture', 'Bangladesh Agriculture University', 'rahim123', '12345', 'Email : dean.ag@bau.edu.bd'),
(2, 'Dr. Md. Abdus Salam', '+88-01760178542', 'abdus salam.jpg', '', 'Agronomy', 'agriculture', 'Bangladesh Agriculture University', 'salam123', '12345678', 'Email : head.agron@bau.edu.bd'),
(3, 'Dr. Mohammad Mofizur Rahman Jahangir', '+88 01719 648448', 'mmr-jahangir.jpg', 'BAU', 'Soil science', 'Soil Science', 'Bangladesh Agricultutre University', 'mofizur522', '12345678', 'head.ss@bau.edu.bd');

-- --------------------------------------------------------

--
-- Table structure for table `experthelp`
--

CREATE TABLE `experthelp` (
  `sno` int(200) NOT NULL,
  `expert_id` varchar(30) NOT NULL,
  `expert_name` varchar(40) NOT NULL,
  `person` varchar(40) NOT NULL,
  `problem` varchar(150) NOT NULL,
  `problem_image` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `experthelp`
--

INSERT INTO `experthelp` (`sno`, `expert_id`, `expert_name`, `person`, `problem`, `problem_image`) VALUES
(1, '1', 'Dr. Md. Abdus Salam', 'Abdullah Al Mizan', 'i have no problem', 'm,znfszn'),
(2, '2', 'Dr. Md. Abdur Rahim', 'fazlul karim', 'amar ta darai na', 'SFsfssf'),
(3, '3', 'Dr. Mohammad Mofizur Rahman Jahangir', 'Abdullah Al Mizan', 'i have also no problem', ''),
(4, '1', 'Dr. Md. Abdur Rahim', 'Mizan', 'AAa', ''),
(5, '1', 'Dr. Md. Abdur Rahim', 'Mizan', 'asas', ''),
(6, '1', 'Dr. Md. Abdur Rahim', 'Mizan', 'asas', ''),
(7, '1', 'Dr. Md. Abdur Rahim', 'Mizan', 'SDasUkcbZBcu', ''),
(8, '1', 'Dr. Md. Abdur Rahim', 'Mizan', 'ABJHBXhzxbz', 'mizan.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `sno` int(200) NOT NULL,
  `product_id` int(200) DEFAULT NULL,
  `product_name` varchar(200) DEFAULT NULL,
  `user_name` varchar(200) DEFAULT NULL,
  `user_district` varchar(200) DEFAULT NULL,
  `user_division` varchar(200) DEFAULT NULL,
  `user_upozila` varchar(200) DEFAULT NULL,
  `full_address` varchar(200) DEFAULT NULL,
  `payment_method` varchar(200) DEFAULT NULL,
  `product_price` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`sno`, `product_id`, `product_name`, `user_name`, `user_district`, `user_division`, `user_upozila`, `full_address`, `payment_method`, `product_price`) VALUES
(1, 1, 'karim', 'Mizan', '', '', '', NULL, NULL, '120Tk'),
(2, 1, 'karim', 'Mizan', '', '', '', NULL, NULL, '120Tk'),
(3, 1, 'karim', 'Mizan', '', '', '', NULL, NULL, '120Tk'),
(4, 1, 'karim', 'Mizan', '', '', '', NULL, NULL, '120Tk'),
(5, 1, 'karim', 'Mizan', '', '', '', NULL, NULL, '120Tk'),
(6, 1, 'karim', 'Mizan', '', '', '', NULL, NULL, '120Tk'),
(7, 1, 'karim', 'Mizan', '', '', '', NULL, NULL, '120Tk'),
(8, 1, 'karim', 'Mizan', '', '', '', NULL, NULL, '120Tk'),
(9, 1, 'karim', 'Mizan', '', '', '', NULL, 'cash on delivery', '120Tk'),
(10, 1, 'karim', 'Mizan', '', '', '', NULL, 'Bikash', '120Tk'),
(11, 1, 'karim', 'Mizan', '', '', '', NULL, 'Bikash', '120Tk'),
(12, 1, 'karim', 'Mizan', '', '', '', NULL, 'Bikash', '120Tk'),
(13, 1, 'karim', 'sayma', 'Noakhali', 'Chattogram', 'Begumganj', NULL, 'Bikash', '120Tk'),
(14, 1, 'karim', 'Mizan', 'Dhaka', 'Dhaka', 'Dhamrai', NULL, 'cash on delivery', '120Tk');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(200) NOT NULL,
  `title` text NOT NULL,
  `slug` varchar(200) NOT NULL,
  `tagline` varchar(200) NOT NULL,
  `content` varchar(2000) NOT NULL,
  `image` varchar(200) NOT NULL,
  `date` datetime(6) NOT NULL,
  `active` varchar(10) NOT NULL,
  `post_by` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `slug`, `tagline`, `content`, `image`, `date`, `active`, `post_by`) VALUES
(1, 'this is first post', 'first-post', 'this is first post', 'karim chacha cha lo', 'first-post.jpeg', '2021-01-16 17:25:59.000000', '1', 'Admin'),
(12, 'This is last post', 'last-post', 's', 'karim chacha c', 'dfdf', '2021-03-13 18:44:06.391896', '1', 'Admin'),
(13, 'SDNSKd', 'sdsd', 'sdsd', 'sdsd', 'sdsd', '2021-03-13 19:22:04.636475', '1', 'Admin'),
(15, 'This is last post', 'last-post', 'sdsd', 's', 'aWDASD', '2021-03-13 20:56:33.952033', '1', ''),
(16, 'f', 'last-post', 'a', 'z', 'z', '2021-03-13 20:58:00.842910', '1', ''),
(17, 'This is last post1', 'SCSC', 'SCSC', 'SCSCS', 'SCSC', '2021-03-14 02:54:25.310649', '1', 'Mizan'),
(18, 'qwqwew', 'wewewe', 'wwe', 'wewewe', 'ewewe', '2021-03-14 03:10:15.301367', '1', 'Admin'),
(19, 'ksDHDSDS', 'SSD', 'SDSD', 'SDSDSD', 'SDSDSD', '2021-03-14 03:52:00.610861', '1', 'Mizan');

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `sno` int(200) NOT NULL,
  `name` varchar(200) NOT NULL,
  `slug` varchar(200) NOT NULL,
  `image` varchar(200) NOT NULL,
  `price` varchar(200) NOT NULL,
  `description` varchar(200) NOT NULL,
  `catagory` varchar(36) NOT NULL,
  `date` datetime(6) NOT NULL,
  `active` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`sno`, `name`, `slug`, `image`, `price`, `description`, `catagory`, `date`, `active`) VALUES
(1, 'karim', 'product-burger', 'burger.jpg', '120Tk', 'This is a very tasty', 'Rent', '2021-01-30 21:20:32.000000', '1'),
(2, 'pizza', 'product-pizza', 'pizza.jpeg', '200Tk', 'very tasty.try it.', 'Buy', '2021-01-30 21:22:40.000000', '1'),
(3, 'grill', 'grill-post', 'gril.jpeg', '80Tk(per piece)', 'Nice and good.', 'Rent', '2021-01-30 21:22:40.000000', '1'),
(4, 'ssdd', 'dsdsd', 'sdsd', 'sdsd', 'sdsd', 'sdsd', '2021-02-28 16:29:45.247713', '1'),
(8, 'tracktor', 'srsdff', 'tracktor.jpg', 'araef', 'asfdf', 'Rent', '2021-03-04 20:47:52.778006', '1'),
(9, 'ssdd', 'dsdsd', 'sdsd', 'sdsd', 'asdasd', 'Rent', '2021-03-08 12:59:38.098909', '1'),
(10, 'SASAASAS', 'ASAS', 'ASAS', 'ASAS', 'ASAS', 'Rent', '2021-03-13 21:47:38.245925', '1'),
(11, 'SSD', 'dsdsd', 'ASAS', 'araef', 'ASAS', 'Buy', '2021-03-13 21:48:16.488151', '1'),
(12, 'miaa', 'add', 'img/tracktor.jpg', 'ASAS', 'very tasty.try .', 'Buy', '2021-03-13 22:40:52.809926', '1');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `sno` int(200) NOT NULL,
  `first_name` varchar(20) NOT NULL,
  `last_name` varchar(20) NOT NULL,
  `email` varchar(25) NOT NULL,
  `mobile` varchar(40) NOT NULL,
  `password` varchar(8) NOT NULL,
  `gender` varchar(200) NOT NULL,
  `division` varchar(200) NOT NULL,
  `district` varchar(200) NOT NULL,
  `upozila` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`sno`, `first_name`, `last_name`, `email`, `mobile`, `password`, `gender`, `division`, `district`, `upozila`) VALUES
(6, 'Abdullah', 'Mizan', 'mizan@gmail.com', '01862856218', '12345', 'male', 'Dhaka', 'Dhaka', 'Dhamrai'),
(7, 'esha', 'sayma', 'esha@gmail.com', '0120192109', '54321', 'female', 'Chattogram', 'Noakhali', 'Begumganj');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `expert`
--
ALTER TABLE `expert`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `experthelp`
--
ALTER TABLE `experthelp`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `expert`
--
ALTER TABLE `expert`
  MODIFY `id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `experthelp`
--
ALTER TABLE `experthelp`
  MODIFY `sno` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `sno` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `sno` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `sno` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
