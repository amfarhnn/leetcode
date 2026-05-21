SELECT id
FROM
(SELECT id, recordDate, temperature,
    LAG(recordDate, 1) OVER(ORDER BY recordDate) AS prev_recordDate,
    LAG(temperature, 1) OVER(ORDER BY recordDate) AS prev_temperature
FROM Weather
) t
WHERE temperature > prev_temperature
AND DATEDIFF(recordDate, prev_recordDate) = 1;