## SELECT de columnas concretas + alias de campo
## Enunciado: Muestra el título y el año de publicación de todos
## los libros. Las columnas del resultado deben llamarse
## "Título del libro" y "Año de publicación".

SELECT titulo as 'Titulo del Libro' , anio_publicacion as 'Año publicación' FROM libros;

# EJERCICIO 3 — Alias de tabla + WHERE (igualdad)
# Muestra el título y el año de publicación de los libros escritos por el autor con id_autor = 3.

SELECT l.titulo, l.anio_publicacion FROM libros as l WHERE l.id_libro= 3;

#  EJERCICIO 4 — WHERE con LIKE - Muestra el nombre y los apellidos de los autores
-- cuyo apellido empiece por la letra "C".

#empiece por letra A
SELECT nombre, apellidos FROM autores WHERE nombre LIKE "a%";

#contenga la letra a
SELECT nombre, apellidos FROM autores WHERE nombre LIKE "%a%";

#termina por la letra l
SELECT nombre, apellidos FROM autores WHERE nombre LIKE "%l";

# EJERCICIO 5 — WHERE con BETWEEN. Muestra el título y el año de los libros publicados
-- entre 1980 y 2000, ambos años incluidos.
SELECT titulo, anio_publicacion FROM libros WHERE anio_publicacion BETWEEN 1980 AND 2000;
SELECT titulo, anio_publicacion FROM libros 
WHERE anio_publicacion>= 1980 AND anio_publicacion <= 2000;


# EJERCICIO 7 — ORDER BY - Muestra todos los libros ordenados por año de
-- publicación, del más reciente al más antiguo.

SELECT titulo, anio_publicacion FROM libros ORDER BY anio_publicacion DESC;


# EJERCICIO 8 — Funciones agregadas: COUNT, AVG, MIN, MAX, Muestra en una sola consulta: el número total de
-- libros registrados, el año de publicación medio, el año más
-- antiguo y el año más reciente.

SELECT COUNT(*) as 'libros_registrados' , AVG(anio_publicacion) as anio, 
MIN(anio_publicacion) as mas_antiguo, MAX(anio_publicacion) mas_moderno FROM libros;

# -- EJERCICIO 9 — GROUP BY - Muestra cuántos libros hay registrados para cada
-- id_autor, ordenado de mayor a menor número de libros.

SELECT COUNT(*) as total_libros, id_autor FROM libros
GROUP BY id_autor ORDER BY total_libros DESC; 

SELECT COUNT(*) as total_libros, l.id_autor, a.nombre
FROM libros l, autores a
WHERE l.id_autor = a.id_autor
GROUP BY id_autor, nombre


# EJERCICIO 10 — GROUP BY + HAVING - Muestra únicamente los id_autor que tienen MÁS DE
-- 1 libro publicado.

SELECT id_autor, COUNT(*) as total_libros FROM libros
GROUP BY id_autor HAVING COUNT(*)> 1;


# EJERCICIO 11 - CONCAT -  Muestra un listado con el nombre completo de cada
-- autor (nombre y apellidos juntos, separados por un espacio)
-- en una única columna llamada "autor_completo", junto con su
-- nacionalidad.

SELECT CONCAT_WS(' - ', nombre, apellidos) as 'c1', 
CONCAT(nombre, ' - ', apellidos) as 'c2',
nacionalidad FROM autores;

-- EJERCICIO 12 — INNER JOIN  Muestra el título de cada libro junto con el
-- nombre y los apellidos de su autor, ordenado por apellidos.

SELECT l.titulo, CONCAT(a.nombre, " ", a.apellidos) as nombre_completo
FROM libros as l
INNER JOIN autores as a ON l.id_autor = a.id_autor
ORDER BY a.apellidos;


-- EJERCICIO 13 — INNER JOIN con tabla intermedia (relación N:N) - Muestra el título de cada libro junto con el
-- nombre de todas las categorías a las que pertenece.

SELECT l.titulo, c.nombre as categoria FROM libros as l
INNER JOIN libros_categorias as lc ON l.id_libro = lc.id_libro
INNER JOIN categorias as c ON lc.id_categoria = c.id_categoria
ORDER BY l.titulo;


-- EJERCICIO 14 — LEFT JOIN - Muestra todos los autores junto con el número de
-- libros que tienen registrados, incluyendo también a los
-- autores que no tienen ningún libro (deben aparecer con 0).

SELECT a.nombre, a.apellidos, COUNT(l.id_libro) as total_libros
FROM autores as a
LEFT JOIN libros as l ON a.id_autor = l.id_autor
GROUP BY a.nombre, a.apellidos
ORDER BY total_libros DESC;

-- EJERCICIO 15 — RIGHT JOIN - Muestra todas las categorías junto con el número
-- de libros que tiene asignados cada una, incluyendo también
-- las categorías que no tienen ningún libro (deben aparecer
-- con 0).

SELECT c.nombre as categorias, COUNT(lc.id_libro) as total_libros
FROM libros_categorias as lc
RIGHT JOIN categorias as c ON lc.id_categoria = c.id_categoria
GROUP BY categorias
ORDER BY total_libros DESC;

-- EJERCICIO 16 — Subconsultas

-- Muestra el título y el año de los libros
-- escritos por autores de nacionalidad "Británica", usando una
-- subconsulta (sin usar JOIN).

SELECT titulo, anio_publicacion FROM libros WHERE id_autor IN (
	SELECT id_autor FROM autores WHERE nacionalidad = 'Británica'
) ORDER BY anio_publicacion;

SELECT titulo, anio_publicacion FROM libros
INNER JOIN autores ON autores.id_autor = libros.id_autor
WHERE autores.nacionalidad = 'Británica' ORDER BY anio_publicacion;

































