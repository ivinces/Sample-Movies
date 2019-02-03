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
	tipoplan_id int NOT NULL,
	FOREIGN KEY(tipoplan_id) REFERENCES movies_planes(id)
);

CREATE TABLE movies_registro(
	id serial NOT NULL PRIMARY KEY,
	cliente_id int,
	pelicula_id int,
	fecha date,
	hora time,
	calificacion int,
	FOREIGN KEY(cliente_id) REFERENCES movies_persona(id),
	FOREIGN KEY(pelicula_id) REFERENCES movies_pelicula(id)
);

SELECT * FROM movies_registro
SELECT * FROM movies_persona
SELECT * FROM movies_pelicula


create function listadopeliculas()
returns table(id int,titulo varchar,usuario varchar,calificacion int)
as $$
	SELECT movies_registro.id,movies_pelicula.titulo,movies_persona.nombre,calificacion FROM movies_registro,movies_persona,movies_pelicula WHERE movies_persona.id=movies_registro.cliente_id AND movies_pelicula.id=movies_registro.pelicula_id ORDER BY movies_registro.id
$$ language sql;

DROP FUNCTION listadopeliculas()
SELECT * FROM listadopeliculas()
SELECT titulo, usuario from listadopeliculas()
SELECT * FROM listadopeliculas()

--nuevos procedures

create function listadousuarios(identificador int)
returns table(id int)
as $$
SELECT mp.id FROM listadopeliculas() lp, movies_persona mp WHERE lp.usuario=mp.nombre AND lp.id=identificador
$$ language sql;

create function listadopelis(identificador int)
returns table(id int)
as $$
SELECT mp.id FROM listadopeliculas() lp, movies_pelicula mp WHERE lp.titulo=mp.titulo AND lp.id=identificador
$$ language sql;

create function listadousuariospelicula(identificador int)
returns table(id int, nombre varchar, apellido varchar)
as $$
SELECT mp.id, mp.nombre, mp.apellido FROM movies_persona mp, movies_registro mr WHERE mr.cliente_id=mp.id AND mr.pelicula_id=(SELECT id FROM movies_persona WHERE id=identificador)
$$ language sql;

create function listadousuariospelicula2(identificador int)
returns table(id int, nombre varchar, apellido varchar)
as $$
SELECT mp.id, mp.nombre, mp.apellido FROM movies_persona mp, movies_registro mr WHERE mr.cliente_id=mp.id AND mr.pelicula_id=(SELECT * FROM listadopelis(identificador))
$$ language sql;

create function listadopeliculausuarios(identificador int)
returns table(id int, titulo varchar)
as $$
SELECT mp.id, mp.titulo FROM movies_pelicula mp, movies_registro mr WHERE mr.pelicula_id=mp.id AND mr.cliente_id=(SELECT * FROM listadousuarios(identificador))
$$ language sql;

create function listadopeliculausuarios2(identificador int)
returns table(id int, titulo varchar)
as $$
SELECT mp.id, mp.titulo FROM movies_pelicula mp, movies_registro mr WHERE mr.pelicula_id=mp.id AND mr.cliente_id=(SELECT id FROM movies_pelicula WHERE id=identificador)
$$ language sql;

