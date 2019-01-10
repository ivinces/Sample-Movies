CREATE TABLE movies_planes(
	id serial NOT NULL PRIMARY KEY,
	tipoplan varchar(30),
	valor int
);

CREATE TABLE movies_persona(
	id serial NOT NULL PRIMARY KEY,
	nombre varchar(30),
	apellido varchar(30),
	fecha_nacimiento date,
	ciudad varchar(60),
	paisnac varchar(30),
	tipoplan_id int NOT NULL,
	FOREIGN KEY(tipoplan_id) REFERENCES movies_planes(id)
);

CREATE TABLE movies_pelicula(
	id serial NOT NULL PRIMARY KEY,
	titulo varchar(50),
	director varchar(50),
	reparto varchar(300),
	calificacion int,
	tipoplan_id int NOT NULL,
	FOREIGN KEY(tipoplan_id) REFERENCES movies_planes(id)
);

CREATE TABLE movies_registro(
	id serial NOT NULL PRIMARY KEY,
	cliente_id int,
	pelicula_id int,
	fecha date,
	hora time,
	FOREIGN KEY(cliente_id) REFERENCES movies_persona(id),
	FOREIGN KEY(pelicula_id) REFERENCES movies_pelicula(id)
);

DROP TABLE movies_planes;
Drop Table movies_persona, movies_planes, movies_pelicula, movies_registro;
ALTER TABLE Planes RENAME movies_planes;

SELECT * FROM movies_pelicula;

SELECT id,titulo,director,reparto,calificacion FROM movies_pelicula ORDER BY calificacion DESC FETCH FIRST 10 ROWS ONLY;

CREATE PROCEDURE pelistop()
LANGUAGE SQL
AS $$
SELECT id,titulo,director,reparto,calificacion FROM movies_pelicula ORDER BY calificacion DESC FETCH FIRST 10 ROWS ONLY
$$;


create function pelistop()
returns table(id int,titulo varchar,director varchar,reparto varchar,calificacion int)
as $$
  SELECT id,titulo,director,reparto,calificacion FROM movies_pelicula ORDER BY calificacion DESC FETCH FIRST 10 ROWS ONLY
$$ language sql;

SELECT * FROM pelistop();

SELECT movies_pelicula.id,titulo,director,reparto,calificacion,count(*) FROM movies_registro,movies_pelicula WHERE movies_pelicula.id=movies_registro.pelicula_id group by movies_pelicula.id  ORDER BY count DESC FETCH FIRST 10 ROWS ONLY

SELECT movies_pelicula.id,titulo,director,reparto,calificacion FROM movies_registro,movies_pelicula WHERE movies_pelicula.id=movies_registro.pelicula_id group by movies_pelicula.id  ORDER BY count(*) DESC FETCH FIRST 10 ROWS ONLY

create function pelisvistas()
returns table(id int,titulo varchar,director varchar,reparto varchar,calificacion int)
as $$
	SELECT movies_pelicula.id,titulo,director,reparto,calificacion FROM movies_registro,movies_pelicula WHERE movies_pelicula.id=movies_registro.pelicula_id group by movies_pelicula.id  ORDER BY count(*) DESC FETCH FIRST 10 ROWS ONLY
$$ language sql;

SELECT * FROM pelisvistas();

create function pelisvistas2()
returns table(id int,titulo varchar,director varchar,reparto varchar,calificacion int,repetidas bigint)
as $$
	SELECT movies_pelicula.id,titulo,director,reparto,calificacion, count(*) FROM movies_registro,movies_pelicula WHERE movies_pelicula.id=movies_registro.pelicula_id group by movies_pelicula.id  ORDER BY count DESC FETCH FIRST 10 ROWS ONLY
$$ language sql;

SELECT * FROM pelisvistas2();
