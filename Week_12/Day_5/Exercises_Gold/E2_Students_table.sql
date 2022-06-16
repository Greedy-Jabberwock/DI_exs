--------------------------- UPDATE ---------------------------
-- ‘Lea Benichou’ and ‘Marc Benichou’ are twins, they should have the same birth_dates. 
-- Update both their birth_dates to 02/11/1998.
UPDATE students 
SET birth_date = '02/11/1998'
WHERE last_name = 'Benichou' AND first_name IN ('Lea', 'Marc');

-- Change the last_name of David from ‘Grez’ to ‘Guez’.
UPDATE students
SET last_name = 'Guez'
WHERE first_name = 'David' AND last_name ILIKE '%g_ez%';


--------------------------- DELETE ---------------------------
-- Delete the student named ‘Lea Benichou’ from the table.
DELETE FROM students WHERE first_name = 'Lea' AND last_name = 'Benichou';


---------------------------  COUNT  --------------------------
-- Count how many students are in the table.
SELECT COUNT(*) as Total_students FROM students;

-- Count how many students were born after 1/01/2000.
SELECT COUNT(*) as after_2000 FROM students
WHERE birth_date > '1/01/2000';

----------------------- INSERT / ALTER -----------------------
-- Add a column to the student table called math_grade.
ALTER TABLE students 
ADD math_grade integer;

-- Add 80 to the student which id is 1. 
UPDATE students
SET math_grade = 80
WHERE id = 1;

-- Add 90 to the students which have ids of 2 or 4.
UPDATE students
SET math_grade = 90
WHERE id IN (2, 4);


-- Add 40 to the student which id is 6.
UPDATE students
SET math_grade = 40
WHERE id = 6;

-- Count how many students have a grade bigger than 83
SELECT * FROM students WHERE math_grade > 83;


-- Add another student named ‘Omer Simpson’ with the same birth_date as 
-- the one already in the table. Give him a grade of 70.
INSERT INTO students(first_name, last_name, birth_date, math_grade)
VALUES ('Omer', 'Simpson', '2010-12-03', 70);

-- Bonus: Count how many grades each student has.
SELECT DISTINCT CONCAT(first_name, ' ', last_name) as fullname, COUNT(math_grade) AS total_grades
FROM students
GROUP BY fullname;

----------------------------  SUM  ---------------------------