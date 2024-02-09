-- Find users created after a certain date
SELECT * FROM Users WHERE created_at > '2023-01-01';

-- Find posts with titles containing 'Post'
SELECT * FROM Posts WHERE title LIKE '%Post%';
