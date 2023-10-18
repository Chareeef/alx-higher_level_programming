-- Use the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT g.name
FROM tv_genres g
JOIN tv_show_genres sg
  ON sg.genre_id = g.id
JOIN tv_shows s
  ON s.id = sg.show_id AND s.title = "Dexter"
ORDER BY g.name
