-- Script that lists all shows that have at least one genre linked
-- Each record displays: tv_shows.title - tv_show_genres.genre_id
-- Results are sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT s.title, g.genre_id
FROM tv_shows AS s
JOIN tv_show_genres AS g ON s.id = g.show_id
ORDER BY s.title, g.genre_id ASC;
