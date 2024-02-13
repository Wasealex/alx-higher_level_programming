-- Lists number of records that display the score and number of occurence
-- diplay grouped and in descending order
SELECT score, COUNT(1) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;
