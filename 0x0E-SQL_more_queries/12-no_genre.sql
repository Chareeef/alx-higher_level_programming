-- list all shows contained in hbtn_0d_tvshows with no genre linked
SELECT  s.title, sg.genre_id
FROM tv_shows s
LEFT JOIN tv_show_genres sg
ON s.id = sg.show_id
WHERE sg.genre_id IS NULL
ORDER BY s.title
