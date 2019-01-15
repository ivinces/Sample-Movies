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

create function pelisvistas2()
returns table(id int,titulo varchar,director varchar,reparto varchar,calificacion int,repetidas bigint)
as $$
	SELECT movies_pelicula.id,titulo,director,reparto,calificacion, count(*) FROM movies_registro,movies_pelicula WHERE movies_pelicula.id=movies_registro.pelicula_id group by movies_pelicula.id  ORDER BY count DESC FETCH FIRST 10 ROWS ONLY
$$ language sql;

SELECT * FROM pelisvistas2();

create function listadopeliculas()
returns table(id int,titulo varchar,usuario varchar,calificacion int)
as $$
	SELECT movies_pelicula.id,titulo,movies_persona.nombre,calificacion FROM movies_registro,movies_persona,movies_pelicula WHERE movies_pelicula.id=movies_registro.pelicula_id AND movies_persona.id=movies_registro.cliente_id
$$ language sql;


