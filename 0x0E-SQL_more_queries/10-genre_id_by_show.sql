-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked

SELECT DISTINCT tv_shows.title, tv_show_genres.genre_id
FROM hbtn_0d_tvshows.tv_shows
JOIN hbtn_0d_tvshows.tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
