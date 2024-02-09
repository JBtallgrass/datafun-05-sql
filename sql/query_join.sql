-- INNER JOIN to fetch posts with user details
SELECT Users.username, Posts.title, Posts.published_at FROM Posts
INNER JOIN Users ON Posts.user_id = Users.user_id
ORDER BY Posts.published_at DESC;

-- LEFT JOIN to find all users and their posts (if any)
SELECT Users.username, Posts.title FROM Users
LEFT JOIN Posts ON Users.user_id = Posts.user_id;
