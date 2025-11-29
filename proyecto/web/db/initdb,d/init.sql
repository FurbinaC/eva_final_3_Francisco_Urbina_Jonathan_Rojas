CREATE DATABASE IF NOT EXISTS contador_final;

USE contador_final;

CREATE TABLE log (
    id int auto_increment primary key,
    hora VARCHAR(50) NOT NULL,
    actividad VARCHAR(100) NOT NULL,
    estado VARCHAR(50) NOT NULL,
    imagen TEXT
);

INSERT INTO log VALUES (null, "9:48", "creacion estructura de contenedor docker", "completado", "<img src='/static/img/evidencias/estructura.png' width='200'>");

INSERT INTO log VALUES (null, "9:50", "estructura docker-compose", "completado", "<img src='/static/img/evidencias/docker-compose.png' width='200'>");

INSERT INTO log VALUES (null, "9:55", "estructura Dockerfile", "completado", "<img src='/static/img/evidencias/estructura.png' width='200'>");

INSERT INTO log VALUES (null, "10:10", "creacion estructura python", "completado", "<img src='/static/img/evidencias/estructura.png' width='200'>");

INSERT INTO log VALUES (null, "10:15", "creacion requirements.txt", "completado", "<img src='/static/img/evidencias/estructura.png' width='200'>");

INSERT INTO log VALUES (null, "10:30", "levantar contenedor", "completado", "<img src='/static/img/evidencias/Captura de pantalla 2025-11-29 104901.png' width='200'>");

INSERT INTO log VALUES (null, "10:40", "vista pagina con base de datos y la tabla", "completado", "<img src='/static/img/evidencias/Captura de pantalla 2025-11-29 105030.png' width='200'>");