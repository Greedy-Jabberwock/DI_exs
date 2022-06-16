-- Creating tables

CREATE TABLE items(
	item_id SERIAL PRIMARY KEY,
	title VARCHAR(50) NOT NULL,
	price MONEY NOT NULL
);

CREATE TABLE customers(
	customer_id SERIAL PRIMARY KEY,
	first_name VARCHAR(32) NOT NULL,
	last_name VARCHAR (32) NOT NULL
);

