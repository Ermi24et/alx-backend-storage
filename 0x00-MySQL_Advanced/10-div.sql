-- SQL script that creates a function SafeDiv that divides and returns
-- the first by the second number or returns 0 if the second num is 0
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
RETURN if(b = 0, 0, a / b);