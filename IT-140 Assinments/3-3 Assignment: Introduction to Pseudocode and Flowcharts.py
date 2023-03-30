INPUT number of hours worked
DECLARE weekly pay, overtime pay, and overtime hours as variables

IF the number of hours worked is <= 40:
    THEN weekly pay = number of hours worked * 20;
ELSE:
    Overtime hours = number of hours worked – 40;
    Overtime pay = overtime hours * 30;
    Weekly pay = (40 * 20) + overtime pay;

PRINT weekly paycheck amount
