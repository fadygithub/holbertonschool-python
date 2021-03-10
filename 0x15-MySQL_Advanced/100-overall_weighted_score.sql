-- Create the stored procedure
DELIMITER |
DROP PROCEDURE IF EXISTS ComputeOverallWeightedScoreForUser;
CREATE PROCEDURE ComputeOverallWeightedScoreForUser (IN user_id int)
BEGIN
UPDATE users AS usr SET usr.overall_score = (
SELECT SUM(s.score * w.weight) / SUM(w.weight)
FROM corrections AS s
LEFT JOIN projects AS w ON s.project_id = w.id
WHERE s.user_id = user_id
) WHERE usr.id = user_id;
END;
|
