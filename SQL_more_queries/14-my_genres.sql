-- Script that uses the hbtn_0d_tvshows database to list all genres of the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record displays the genre name
-- Results are sorted in ascending order by the genre name
SELECT g.name
FROM tv_genres AS g
JOIN tv_show_genres AS sg ON g.id = sg.genre_id
JOIN tv_shows AS s ON sg.show_id = s.id
WHERE s.title = 'Dexter'
ORDER BY g.name ASC;
