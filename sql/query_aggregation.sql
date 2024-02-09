-- Count the number of posts by each user
SELECT user_id, COUNT(*) AS post_count FROM Posts GROUP BY user_id;

-- Calculate the average number of posts per user
SELECT AVG(post_count) AS avg_posts_per_user FROM (SELECT COUNT(*) AS post_count FROM Posts GROUP BY user_id);
