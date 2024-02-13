-- list best score that has >= 10 scores
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
