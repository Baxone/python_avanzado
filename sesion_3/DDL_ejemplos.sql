CREATE DATABASE tienda
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE tienda;

CREATE TABLE productos (
id INT auto_increment primary key,
nombre VARCHAR(20) NOT NULL,
precio DECIMAL(4,2) NOT NULL,
cantidad int NOT NULL
) CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

DROP database biblioteca;

ALTER TABLE productos
ADD COLUMN stock TINYINT;


