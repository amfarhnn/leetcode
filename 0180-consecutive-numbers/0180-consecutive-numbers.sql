SELECT DISTINCT num AS ConsecutiveNums
FROM
    (SELECT num,
    LAG(num, 1) OVER(ORDER BY id) as prev1,
    LAG(num, 2) OVER(ORDER BY id) as prev2
    FROM Logs
    ) t
WHERE num = prev1 and num = prev2