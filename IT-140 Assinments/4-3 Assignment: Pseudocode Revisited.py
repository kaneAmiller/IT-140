START the higher/lower game

CREATE variable for lower bound

CREATE variable for upper bound

IMPORT the random module to generate random numbers

READ the seed_Val from the user to seed the random number generator

INITIALIZE the random number generator with the seed_Val using the random.seed() function

WHILE True:

    READ the lower and upper bounds of the game

    IF the lower bound is greater than the upper bound THEN:

        OUTPUT 'The lower bound must be less than the upper bound.'

    ELIF the upper bound is less than the lower bound THEN:

        OUTPUT 'The upper bound must be more than the lower bound.'

    ELSE:

        BREAK out of the loop

GENERATE a random number between the lower and upper bounds using the random.randint() function

SET the variable 'right_num' to the random number

WHILE TRUE

    INPUT the user's guess for the number

    READ the user's guess

    IF the user's guess is higher than the right number THEN:

        OUTPUT ' Nope, too high.'

    ELIF the user's guess is lower than the right number THEN:

        OUTPUT ' Nope, too low.'

    ELSE:

        OUTPUT 'You got it!'

        BREAK out of the loop

END the game