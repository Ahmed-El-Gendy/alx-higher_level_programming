-- lists all shows contained in hbtn_0d_tvshows
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres tv_show_genres
RIGHT JOIN tv_shows tv_shows
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
