-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that
-- computes and store the average weighted score for a student
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN usr_id INT)
BEGIN
        SET @avrg = (SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight)
                     AS avrg FROM projects
                     JOIN corrections ON corrections.project_id = projects.id
                     WHERE user_id = usr_id
                     );
        UPDATE users SET average_score = @avrg WHERE id = usr_id;
END //
DELIMITER;