# Write your MySQL query statement below

SELECT author_id as id FROM Views 
WHERE author_id = viewer_id
GROUP BY author_id
ORDER BY author_id ASC;

-- SELECT author_id as id FROM Views 
-- WHERE (
--     SELECT count(viewer_id) AS Viewcount FROM Views
--     HAVING Viewcount >= 1 AND author_id = viewer_id
--     )
-- GROUP BY author_id
-- ORDER BY author_id ASC;
