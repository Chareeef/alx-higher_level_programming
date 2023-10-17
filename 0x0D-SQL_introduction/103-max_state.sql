-- displays the max temperature of each state (ordered by State name)

-- use hbtn_0c_0
USE hbtn_0c_0;
-- display the desired output
SELECT state, MAX(value) AS max_temp
	FROM temperatures
	GROUP BY state
	ORDER BY state;
