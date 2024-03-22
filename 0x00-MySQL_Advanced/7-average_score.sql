-- SQL script that creates a stored procedure ComputeAverageScoreForUser that
-- computes and store the average score for a student.
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN usr_id INT)
BEGIN
        SET @avrg = (SELECT AVG(score) AS avrg FROM corrections WHERE user_id = usr_id);
        UPDATE users SET average_score = @avrg WHERE id = usr_id;
END //
DELIMITER;