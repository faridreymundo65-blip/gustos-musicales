-- Estructura de la tabla 'alumno' dentro de la base de datos 'matricula'.
-- La tabla ya existe en tu servidor; este archivo sirve de referencia
-- y para recrearla si hiciera falta.

USE matricula;

CREATE TABLE IF NOT EXISTS alumno (
  cod_alumno VARCHAR(10)  NOT NULL PRIMARY KEY,   -- ALU-001, ALU-002, ...
  pat_alu    VARCHAR(50)  NOT NULL,               -- apellido paterno
  mat_alu    VARCHAR(50)  NOT NULL,               -- apellido materno
  nom_alu    VARCHAR(60)  NOT NULL,               -- nombres
  edad_alu   INT          NOT NULL,
  sexo_alu   CHAR(1)      NOT NULL,               -- M / F
  direc_alu  VARCHAR(120),
  dist_alu   VARCHAR(60),                         -- distrito
  correo_alu VARCHAR(80)
);
