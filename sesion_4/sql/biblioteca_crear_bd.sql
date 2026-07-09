-- ============================================================
-- Ejercicio: Biblioteca
-- Relación 1-N   : autores (1) -> libros (N)
-- Relación N-N   : libros (N) <-> categorias (N)  vía libros_categorias
-- ============================================================

DROP DATABASE IF EXISTS biblioteca;

CREATE DATABASE biblioteca CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE biblioteca;

-- ------------------------------------------------------------
-- Tabla: autores
-- ------------------------------------------------------------
CREATE TABLE autores (
    id_autor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellidos VARCHAR(100) NOT NULL,
    nacionalidad VARCHAR(50),
    fecha_nacimiento DATE
) ENGINE = InnoDB;

-- ------------------------------------------------------------
-- Tabla: libros  (lado "N" de la relación 1-N con autores)
-- ------------------------------------------------------------
CREATE TABLE libros (
    id_libro INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    isbn VARCHAR(20) UNIQUE,
    anio_publicacion YEAR,
    id_autor INT NOT NULL,
    CONSTRAINT fk_libros_autor FOREIGN KEY (id_autor) REFERENCES autores (id_autor) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE = InnoDB;

-- ------------------------------------------------------------
-- Tabla: categorias
-- ------------------------------------------------------------
CREATE TABLE categorias (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE,
    descripcion VARCHAR(255)
) ENGINE = InnoDB;

-- ------------------------------------------------------------
-- Tabla intermedia: libros_categorias (relación N-N)
-- ------------------------------------------------------------
CREATE TABLE libros_categorias (
    id_libro INT NOT NULL,
    id_categoria INT NOT NULL,
    PRIMARY KEY (id_libro, id_categoria),
    CONSTRAINT fk_lc_libro FOREIGN KEY (id_libro) REFERENCES libros (id_libro) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_lc_categoria FOREIGN KEY (id_categoria) REFERENCES categorias (id_categoria) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB;

-- ============================================================
-- Datos de prueba
-- ============================================================

INSERT INTO
    autores (
        nombre,
        apellidos,
        nacionalidad,
        fecha_nacimiento
    )
VALUES (
        'Gabriel',
        'García Márquez',
        'Colombiana',
        '1927-03-06'
    ),
    (
        'Isabel',
        'Allende',
        'Chilena',
        '1942-08-02'
    ),
    (
        'George',
        'Orwell',
        'Británica',
        '1903-06-25'
    ),
    (
        'Agatha',
        'Christie',
        'Británica',
        '1890-09-15'
    ),
    (
        'Haruki',
        'Murakami',
        'Japonesa',
        '1949-01-12'
    );

INSERT INTO
    libros (
        titulo,
        isbn,
        anio_publicacion,
        id_autor
    )
VALUES (
        'Cien años de soledad',
        '978-84-376-0494-7',
        1967,
        1
    ),
    (
        'El amor en los tiempos del cólera',
        '978-84-397-1893-4',
        1985,
        1
    ),
    (
        'La casa de los espíritus',
        '978-84-01-24211-9',
        1982,
        2
    ),
    (
        'Paula',
        '978-84-01-24212-6',
        1994,
        2
    ),
    (
        '1984',
        '978-0-452-28423-4',
        1949,
        3
    ),
    (
        'Rebelión en la granja',
        '978-0-452-28424-1',
        1945,
        3
    ),
    (
        'Asesinato en el Orient Express',
        '978-0-00-711931-2',
        1934,
        4
    ),
    (
        'Kafka en la orilla',
        '978-4-06-273315-2',
        2002,
        5
    );

INSERT INTO
    categorias (nombre, descripcion)
VALUES (
        'Realismo mágico',
        'Ficción con elementos fantásticos tratados como cotidianos'
    ),
    (
        'Distopía',
        'Ficción sobre sociedades futuras opresivas'
    ),
    (
        'Novela histórica',
        'Ficción ambientada en hechos o épocas históricas'
    ),
    (
        'Misterio',
        'Tramas centradas en la resolución de un enigma'
    ),
    (
        'Autobiografía',
        'Relato de la propia vida del autor'
    );

-- Un mismo libro puede pertenecer a varias categorías y viceversa (N-N)
INSERT INTO
    libros_categorias (id_libro, id_categoria)
VALUES (1, 1), -- Cien años de soledad -> Realismo mágico
    (1, 3), -- Cien años de soledad -> Novela histórica
    (2, 1), -- El amor en los tiempos del cólera -> Realismo mágico
    (3, 1), -- La casa de los espíritus -> Realismo mágico
    (4, 5), -- Paula -> Autobiografía
    (5, 2), -- 1984 -> Distopía
    (6, 2), -- Rebelión en la granja -> Distopía
    (7, 4), -- Asesinato en el Orient Express -> Misterio
    (8, 1);
-- Kafka en la orilla -> Realismo mágico