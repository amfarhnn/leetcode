SELECT DISTINCT f.email AS Email
FROM Person f
JOIN
(
SELECT email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1
) s
USING (email)
WHERE f.email = s.email