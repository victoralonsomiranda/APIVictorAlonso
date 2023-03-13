-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 14-03-2023 a las 00:21:56
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `apivictor`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `peliculas`
--

CREATE TABLE `peliculas` (
  `id` int(250) NOT NULL,
  `nombre` varchar(1000) NOT NULL,
  `año` int(250) NOT NULL,
  `director` varchar(1000) NOT NULL,
  `genero` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `peliculas`
--

INSERT INTO `peliculas` (`id`, `nombre`, `año`, `director`, `genero`) VALUES
(12, 'El Padrino', 1972, 'Francis Ford Coppola', 'Drama'),
(13, 'La Lista de Schindler', 1993, 'Steven Spielberg', 'Drama histórico'),
(14, 'Forrest Gump', 1994, 'Robert Zemeckis', 'Drama/Comedia dramática'),
(15, 'Pulp Fiction', 1994, 'Quentin Tarantino', 'Cine negro/Comedia negra'),
(16, 'El Rey León', 1994, 'Roger Allers, Rob Minkoff', 'Animación/Musical'),
(17, 'Matrix', 1999, 'Lana y Lilly Wachowski', 'Ciencia ficción/Acción'),
(18, 'El Señor de los Anillos: La Comunidad del Anillo', 2001, 'Peter Jackson', 'Fantasía/Aventuras'),
(19, 'Buscando a Nemo', 2003, 'Andrew Stanton, Lee Unkrich', 'Animación/Aventuras'),
(20, 'La La Land', 2016, 'Damien Chazelle', 'Musical/Romance'),
(21, 'Get Out', 2017, 'Jordan Peele', 'Terror/Comedia negra'),
(22, 'Coco', 2017, 'Lee Unkrich, Adrian Molina', 'Animación/Fantasía'),
(23, 'El Gran Hotel Budapest', 2014, 'Wes Anderson', 'Comedia/Drama'),
(24, 'Call Me by Your Name', 2017, 'Luca Guadagnino', 'Drama/Romance'),
(25, 'Bohemian Rhapsody', 2018, 'Bryan Singer', 'Drama/Biográfico');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `peliculas`
--
ALTER TABLE `peliculas`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `peliculas`
--
ALTER TABLE `peliculas`
  MODIFY `id` int(250) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
