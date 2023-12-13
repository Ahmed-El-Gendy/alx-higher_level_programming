-- lists all genres from hbtn_0d_tvshows and displays the number of shows
SELECT a.name AS genre, count(b.show_id) AS number_of_shows
FROM tv_show_genres b
LEFT JOIN tv_genres a
ON b.genre_id = a.id
GROUP BY b.genre_id
ORDER BY 2 DESC;
