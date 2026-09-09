-- Base de datos 'matricula' y tabla 'alumno' del curso.
-- Importa este archivo desde phpMyAdmin para dejarla igual que en la guia.

CREATE DATABASE IF NOT EXISTS matricula
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

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

INSERT IGNORE INTO alumno
  (cod_alumno, pat_alu, mat_alu, nom_alu, edad_alu, sexo_alu, direc_alu, dist_alu, correo_alu)
VALUES
  ('ALU-001','SANTOS','MARTINEZ','JESSICA',59,'F','JR. LARRABURE Y UNANUE #299-204','JESUS MARIA','JSANTOS@MAIL.COM'),
  ('ALU-002','ROJAS','CASTRO','JOSE LUIS',21,'M','AV. PERU 2323','SAN MARTIN DE PORRAS','carlos4030@gmail.com'),
  ('ALU-004','BUENO','SOBERON','RAFAEL ALFONSO',14,'M','JR. AUGUSTO SALAZAR BONDI MZ J LT 20','SAN JUAN DE MIRAFLORES','rbueno@hotmail.com'),
  ('ALU-005','BUENO','SOBERON','ESTEFANIA ISABEL',12,'F','AUGUSTO SALAZAR BONDI MZ J LT 20 URB. MARIA AUXILIADORA','SAN JUAN DE MIRAFLORES','rbueno@hotmail.com'),
  ('ALU-012','BUENO','MARTINEZ','ALFONSO ALF',45,'M','JR. LARRABURE Y UNANUE 299','JESUS MARIA','ALF_BUENO@HOTMAIL.COM'),
  ('ALU-013','SOBERON','CARRERA','MARIA JESUS MILAGROS',55,'F','MZ. J LT. 20 URB MARIA AUXILIADORA','SJMIRAFLORES','MJSOBERON@MAIL.COM'),
  ('ALU-014','ECHEVARRIA','SANTOS','LUIS',32,'M','LOS SAUCES 123','SAN MIGUEL','MAIL@MAIL.COM'),
  ('ALU-015','SANTOS','MARTINEZ','FRANCISCO',64,'M','LARRA','JM','FRNA@MAIL.COM'),
  ('ALU-019','MIRANDA','MERCADO-MAYORISTA','RAUL',45,'M','NO LO SE','NO TE IMPORTA','MIRANDA@MAIL.COM');
