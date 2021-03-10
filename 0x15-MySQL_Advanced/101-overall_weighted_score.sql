-- Create the stored procedure
DELIMITER |
DROP PROCEDURE IF EXISTS ComputeOverallWeightedScoreForUsers;
CREATE PROCEDURE ComputeOverallWeightedScoreForUsers ()
BEGIN
UPDATE users AS usr SET usr.overall_score = (
SELECT SUM(s.score * w.weight) / SUM(w.weight)
FROM corrections AS s
LEFT JOIN projects AS w ON s.project_id = w.id
WHERE s.user_id = usr.id
);
END;
|
