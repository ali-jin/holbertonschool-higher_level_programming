-- script that lists all the tables of a database in your MySQL server
SELECT table_name
FROM INFORMATION_SCHEMA.TABLES
WHERE table_type = 'BASE TABLE'
