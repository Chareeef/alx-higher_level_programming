-- lists all genres from hbtn_0d_tvshows_rate by their rating
SELECT name, SUM(rate) AS rating
FROM tv_shows s
JOIN tv_show_ratings sr
ON s.id = sr.show_id
JOIN tv_show_genres sg
ON s.id = sg.show_id
JOIN tv_genres g
ON g.id = sg.genre_id
GROUP BY name
ORDER BY rating DESC
