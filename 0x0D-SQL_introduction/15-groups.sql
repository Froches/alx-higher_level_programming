-- Lists the number of records with same score in the table
USE hbtn_0c_0;

CREATE TEMPORARY TABLE IF NOT EXISTS temp_count AS
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score;

SELECT score, number
FROM temp_count
ORDER BY number DESC;

DROP TEMPORARY TABLE IF EXISTS temp_count;
