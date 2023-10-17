-- creates a table second_table and add multiples rows
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
);

-- Add a row
INSERT INTO second_table (id, name, score) VALUES (1, "John", 10);
-- Add a row
INSERT INTO second_table (id, name, score) VALUES (2, "Alex", 3);
-- Add a row
INSERT INTO second_table (id, name, score) VALUES (3, "Bob", 14);
-- Add a row
INSERT INTO second_table (id, name, score) VALUES (4, "George", 8);
