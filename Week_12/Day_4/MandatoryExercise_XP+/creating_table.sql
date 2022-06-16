---- Creating table 'students' ----
CREATE TABLE students(
	id SERIAL PRIMARY KEY,
	first_name VARCHAR (32) NOT NULL,
	last_name VARCHAR (32) NOT NULL,
	birth_date DATE NOT NULL
);

