-- list all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
SELECT title, name
FROM tv_shows s
LEFT JOIN tv_show_genres sg
  ON s.id = sg.show_id
LEFT JOIN tv_genres g
  ON g.id = sg.genre_id
ORDER BY title, name
