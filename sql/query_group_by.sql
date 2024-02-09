-- Count posts by user
SELECT Users.username, COUNT(Posts.post_id) AS post_count FROM Users
JOIN Posts ON Users.user_id = Posts.user_id
GROUP BY Users.user_id;
