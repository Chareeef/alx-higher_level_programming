-- list all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT title
FROM tv_shows s
WHERE title NOT IN (
		SELECT title
		FROM tv_shows s
		JOIN tv_show_genres sg
		 ON s.id = sg.show_id
		JOIN tv_genres g
		 ON g.id = sg.genre_id && name = 'Comedy'
		)
ORDER BY title
