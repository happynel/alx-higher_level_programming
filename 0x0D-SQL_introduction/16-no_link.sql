-- List all records
-- list all record of the second_table
-- Do not list rows with NULL column
SELECT score, name FROM 'second table' WHERE NAME IS NOT NULL ORDER BY score desc;
