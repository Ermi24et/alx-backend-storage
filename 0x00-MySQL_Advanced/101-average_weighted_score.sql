-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that
-- computes and the store the average weighted score for all students
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users AS usr,
        (SELECT usr.id, SUM(score * weight) / SUM(weight) AS wght_avg
        FROM users AS usr
        JOIN corrections AS crn ON usr.id=crn.user_id
        JOIN projects AS prj ON crn.project_id=prj.id
        GROUP BY usr.id)
    AS Usr
    SET usr.average_score = Usr.wght_avg
    WHERE usr.id=Usr.id;
END //
DELIMITER;