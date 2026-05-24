# Write your MySQL query statement below
SELECT player_id, event_date AS first_login
FROM (
    SELECT *,
    ROW_NUMBER() OVER(PARTITION BY player_id ORDER BY event_date) AS rank_date
    FROM Activity
) t
WHERE rank_date = 1