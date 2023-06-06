from sqlite3 import connect
from random import randint, choice





def GenerateWages(minimum: int = 7, maximum: int = 10, amount: int = 10) -> float:
    """
    This function takes two integers to provide a range to draw
    a random number greater than or equal to 7.  By taking advantage of
    Python's dynamic typecasting system we can format a string with this
    number, a decimal, and two more integers between 2 & 9 and 5 & 9
    respectively.

    These minimum limitations serve to impart realism on the simulation by
    locking us into a return value that is no less than 7.25; the federal
    minimum.
    """


    # Custom error for preventing under-paying an employee.
    class FedMinViolation: pass

    step_count = 0
    while step_count <= amount:
        if minimum < 7: raise FedMinViolation(
            "You can not pay an employee less than the Federal Minimum Wage."
        )
        else: dollar = str( randint(minimum, maximum) )

        # If the dollar value is the minimum, then alter the tens place so as not to go below 2.
        if dollar == 7: tens = str( randint(2, 9) )
        else:           tens = str( randint(0, 9) )

        # If we're riding the edge of minimum wage, the the ones can not go lower than 5.
        if tens == 2:   ones = str( randint(5, 9) )
        else:           ones = str( randint(0, 9) )

        yield float( f"{dollar}.{tens}{ones}" )

        step_count += 1



   

def GenerateIndividuals(amount: int = 10) -> str:
    """
    This function generates an `amount` of first and last names
    to combine in random ways to maintain a unique list of individuals
    to assign rates of pay to.

    To extend the use of the operation, a 'coinflip' is held that
    determines which list to pull from first.
    """


    first_names = [ "Karl", "Sandy", "Peter", "Kyle", "Zack",
                    "Jim", "Tim", "Sally", "Samantha", "Alicia",
                    "Karyl", "Carol", "Jimothy", "Kris", "Wilson" ]

    last_names = [ "Newton", "Dale", "Rogers", "McGathey", "Isaac",
                   "Dylan", "Wilson", "Hanks", "Todd", "McFarlane"  ]

    step_count = 0# For as long as 'step_count' 
    while step_count <= amount:

        if randint(0, 10) % 2 == 0: yield f"{choice(first_names)} {choice(last_names)}"
        else: yield f"{choice(last_names)} {choice(first_names)}"

        step_count += 1


def GenerateHours(amount: int = 10):
    return GenerateWages( minimum = 15, maximum = 72, amount = 10)


def CalculateOvertime(wage, hours):
    if hours > 40:
        overtime = hours - 40
        return round( float( (wage * 40) + ((wage * 1.5) * overtime) ), 2 )

    else: return round( float(wage * hours), 2)



people = [ person for person in GenerateIndividuals() ]
wages  = [ dollar for dollar in GenerateWages() ]
hours  = [ hour for hour in GenerateHours() ]


while len(people) > 0:
    person = people.pop()
    wage   = wages.pop()
    hour   = hours.pop()
    pay    = CalculateOvertime(wage, hour)

    print(f"{person}: ${wage}/hour: {hour} hours: ${pay} paycheck")
