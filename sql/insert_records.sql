-- Insert users
INSERT INTO Users (username, email) VALUES
('user51', 'user51@example.com'),
('user52', 'user52@example.com'),
('user53', 'user53@example.com'),
('user54', 'user54@example.com'),
('user55', 'user55@example.com'),
('user56', 'user56@example.com'),
('user57', 'user57@example.com'),
('user58', 'user58@example.com'),
('user59', 'user59@example.com'),
('user60', 'user60@example.com');

-- Insert posts
INSERT INTO Posts (user_id, title, content) VALUES
(51, 'Post by User51', 'Content of the post by User51'),
(52, 'Post by User52', 'Content of the post by User52'),
(53, 'Post by User53', 'Content of the post by User53'),
(54, 'Post by User54', 'Content of the post by User54'),
(55, 'Post by User55', 'Content of the post by User55'),
(56, 'Post by User56', 'Content of the post by User56'),
(57, 'Post by User57', 'Content of the post by User57'),
(58, 'Post by User58', 'Content of the post by User58'),
(59, 'Post by User59', 'Content of the post by User59'),
(60, 'Post by User60', 'Content of the post by User60');
