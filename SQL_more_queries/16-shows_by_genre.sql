-- Script that lists all shows and all genres linked to that show from the database hbtn_0d_tvshows
-- If a show doesn't have a genre, display NULL in the genre column
-- Each record displays: tv_shows.title - tv_genres.name
-- Results are sorted in ascending order by the show title and genre name
SELECT s.title, g.name
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS sg ON s.id = sg.show_id
LEFT JOIN tv_genres AS g ON sg.genre_id = g.id
ORDER BY s.title, g.name ASC;
