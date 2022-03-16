""" LOTEK game symulator """
import random


ALL_NUMBERS = list(range(1,50))
BETTING_PRICE = 3
DRAWS_PER_WEEK = 3


def draw_six_numbers(all_numbers):
    """draw 6 numbers

    Args:
        all_numbers list: list of all posible to draw numbers

    Returns:
        set: six random numbers six from ALL_NUMBERS>
    """
    return set(random.sample(all_numbers, k=6))


def draw_until_win(win_numbers):
    """Simulate drows until draws numbers ar same as win numbers

    Args:
        win_numbers set: set of numbers you have to draw to win the game

    Returns:
        _type_: _description_
    """
    counter = 0
    draw_numbers = set()
    while draw_numbers != win_numbers:
        draw_numbers = draw_six_numbers(ALL_NUMBERS)
        counter += 1
    return counter


def get_years(draws, draws_pre_week):
    """Count how meny years it will teka to take number of drows

    Args:
        draws int: number of drows
        draws_pre_week int: number of drows per week

    Returns:
        int: number of years to won the game
    """
    weeks = draws // draws_pre_week
    return weeks // 52


def print_summary(counter):
    """Print to console summary of gamne symulation

    Args:
        counter int: draws number to won the game
    """
    print(f'''You won after {counter} draws,
total cost was {counter * BETTING_PRICE} zł,
total time was over {get_years(counter, DRAWS_PER_WEEK)} years''')


def main():
    """ main module function """
    draws_to_won = draw_until_win(draw_six_numbers(ALL_NUMBERS))
    print_summary(draws_to_won)

if __name__ == '__main__':
    main()
