---- Fetching data ----

-- 1.Fetch all of the data from the table.
SELECT * FROM students;

-- 2.Fetch all of the students first_names and last_names.
--SELECT first_name, last_name FROM students;

-- 3.For the following questions, only fetch the first_names and last_names of the students.
---- 3.1.Fetch the student which id is equal to 2.
-- SELECT first_name, last_name FROM students
-- WHERE id = 2;

---- 3.2.Fetch the student whose last_name is Benichou AND first_name is Marc.
-- SELECT first_name, last_name FROM students
-- WHERE last_name = 'Benichou' AND first_name = 'Marc';

---- 3.3.Fetch the students whose last_names are Benichou OR first_names are Marc.
-- SELECT first_name, last_name FROM students
-- WHERE last_name = 'Benichou' OR first_name = 'Marc';

---- 3.4.Fetch the students whose first_names contain the letter a.
-- SELECT first_name, last_name FROM students
-- WHERE first_name LIKE '%a%';

---- 3.5.Fetch the students whose first_names start with the letter a.
-- SELECT first_name, last_name FROM students
-- WHERE first_name ILIKE 'a%';
--  or
-- WHERE first_name LIKE 'a%';

---- 3.6.Fetch the students whose first_names end with the letter a.
-- SELECT first_name, last_name FROM students
-- WHERE first_name LIKE '%a';

---- 3.7.Fetch the students whose second to last letter of their first_names are a (Example: Leah).
-- SELECT first_name, last_name FROM students
-- WHERE first_name LIKE '%a_';

-- 3.8.Fetch the students whose id’s are equal to 1 AND 3 .
-- SELECT first_name, last_name FROM students
-- WHERE id = 1 OR id = 3;

-- 4.Fetch the students whose birth_dates are equal to or come after 1/01/2000. (show all their info).
-- SELECT * FROM students
-- WHERE birth_date >= '1/01/2000';