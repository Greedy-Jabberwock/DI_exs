-- Q1:
SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL );
---- MY ANSWER: 		3
---- CORRECT ANSWER:	0
----- P.S. Don't understand why. SELECT from SecondTab must give null. 
----- So the first part looks for me like from firstTab where id is not in [Null]. 
----- 5,6,7 not in Null...

-------------------------------------------------------------
-- Q2:
SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 );
---- MY ANSWER: 		3
---- CORRECT ANSWER:	2
----- P.S. As i see, Null is literally nothing, and it is not included in counter.
-------------------------------------------------------------
-- Q3:
SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab );
---- MY ANSWER: 		2
---- CORRECT ANSWER:	0 
----- P.S. Don't understand why. Just completely. SELECT id FROM SecondTab gives [5, null]
----- 6 and 7 not in [5, null]. So why?
-------------------------------------------------------------
-- Q4:
SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL );
---- MY ANSWER: 		2
---- CORRECT ANSWER:	2
-------------------------------------------------------------