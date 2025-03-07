-- Script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
-- First column called genre, second column called number_of_shows
-- Don't display a genre that doesn't have any shows linked
-- Results sorted in descending order by the number of shows linked
SELECT g.name AS genre, COUNT(s.show_id) AS number_of_shows
FROM tv_genres AS g
JOIN tv_show_genres AS s ON g.id = s.genre_id
GROUP BY g.name
ORDER BY number_of_shows DESC;
