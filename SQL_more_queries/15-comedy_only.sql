-- Script that lists all Comedy shows in the database hbtn_0d_tvshows
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record displays the show title
-- Results are sorted in ascending order by the show title
SELECT s.title
FROM tv_shows AS s
JOIN tv_show_genres AS sg ON s.id = sg.show_id
JOIN tv_genres AS g ON sg.genre_id = g.id
WHERE g.name = 'Comedy'
ORDER BY s.title ASC;
