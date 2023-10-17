-- display the average temperature (Fahrenheit) by city ordered by temperature (descending).

-- use hbtn_0c_0
USE hbtn_0c_0;
-- display the desired outpuy
SELECT city, AVG(value) AS avg_temp
	FROM temperatures
	GROUP BY city
	ORDER BY avg_temp DESC;
