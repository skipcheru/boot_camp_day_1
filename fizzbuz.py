"""
Function checks if a number is divisible b 3, 5 or both
"""

def fizz_buzz(digit):
    # parameter passed should be integer only
    try:
        if isinstance(digit, int):
            if digit % 3 == 0 and digit % 5 != 0:
                return 'Fizz'
            elif digit % 5 == 0 and digit % 3 != 0:
                return 'Buzz'
            elif digit % 5 == 0 and digit % 3 == 0:
                return 'FizzBuzz'
            else:
                return digit
    except ValueError:
            return 'Integers only'  # raise exception here for non integers
