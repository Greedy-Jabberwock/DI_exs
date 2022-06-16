SELECT purchase_id, CONCAT(customers.first_name, ' ', customers.last_name) as customer, 
		items.title, quantity_purchased FROM purchases
INNER JOIN customers
ON purchases.customer_id = customers.customer_id
INNER JOIN items
ON purchases.item_id = items.item_id;