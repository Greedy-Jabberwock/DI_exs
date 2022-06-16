-- Fetching items table. --

---- All the items
SELECT * FROM items;

---- All the items with a price above 80 (80 not included).
-- SELECT * FROM items WHERE price > money(80);

---- All the items with a price below 300. (300 included)
-- SELECT * FROM items WHERE price <= money(300);

-- Fetching customers table. --

---- All customers whose last name is ‘Smith’ (What will be your outcome?).
-- SELECT * FROM customers WHERE last_name = 'Smith';

---- All customers whose last name is ‘Jones’.
-- SELECT * FROM customers WHERE last_name = 'Jones';

---- All customers whose firstname is not ‘Scott’.
-- SELECT * FROM customers WHERE first_name <> 'Scott';