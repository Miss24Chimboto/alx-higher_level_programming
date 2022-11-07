-- Script that lists all records of the table second_table of the database hbtn_0c_0
-- Records should be listed by descending score
-- Add new data to the table
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
