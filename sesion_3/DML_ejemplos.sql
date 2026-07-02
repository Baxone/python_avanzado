#INSERCIÓN

# opcion 1 sentencia larga
INSERT INTO productos (precio, cantidad, stock, nombre) 
VALUES (12.20, 10, 1, 'leche'),
(13,10,1,'carne');


# opcion 2 sentencia corta
INSERT INTO productos VALUES (null,'pan', 3, 10, 1),(null,'cereales', 2, 2, 1);

# DELETE - siempre por favor no os olvideis del WHERE
DELETE FROM productos WHERE id= 5;
# UPDATE - siempre por favor con WHERE
UPDATE productos SET precio = 79 WHERE id=6;

# SELECT 

SELECT * FROM productos;

# seleccionar algunos campos solo
SELECT id, nombre, precio FROM productos;

# seleccionar un unico elemento por id o por lo que fuera WHERE
SELECT id, nombre, precio FROM productos WHERE id=6;

# SELECT SUM
SELECT SUM(precio) as precio_total FROM productos;
# Contar la cantidad de producto que hay en mi tabla
SELECT COUNT(id) as cantidad FROM productos;

## filtro >< BETWEEN
SELECT id, nombre, precio FROM productos WHERE precio >= 2.00 AND precio <= 3.00;
SELECT id, nombre, precio FROM productos WHERE precio BETWEEN 2.00 and 3.00 ORDER BY precio ASC;

# limitar nuestras consultas
SELECT id, nombre, precio FROM productos LIMIT 2;

# DISTINT evitar productos duplicados
SELECT distinct precio FROM productos;










