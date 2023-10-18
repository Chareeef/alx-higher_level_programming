-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

SELECT g.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres g
JOIN tv_show_genres sg
ON g.id = sg.genre_id
GROUP BY g.name
ORDER BY number_of_shows DESC
