-- Paso 1: crear la base de datos y la tabla Alumnos
CREATE DATABASE IF NOT EXISTS escuela
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE escuela;

CREATE TABLE IF NOT EXISTS alumnos (
  id        INT AUTO_INCREMENT PRIMARY KEY,
  matricula VARCHAR(20)  NOT NULL UNIQUE,
  nombre    VARCHAR(60)  NOT NULL,
  apellido  VARCHAR(60)  NOT NULL,
  edad      INT          NOT NULL,
  carrera   VARCHAR(80)  NOT NULL
);

-- Datos de ejemplo (opcional)
INSERT IGNORE INTO alumnos (matricula, nombre, apellido, edad, carrera) VALUES
  ('A001', 'Ana',    'Lopez',   20, 'Informatica'),
  ('A002', 'Carlos', 'Ramirez', 22, 'Contabilidad');
