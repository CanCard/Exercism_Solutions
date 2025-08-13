"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    elapsed_bake_time = EXPECTED_BAKE_TIME - elapsed_bake_time
    return elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """ This part is about the how many minutes you have to pass to cooking lasagna.
    :param number_of_layers: You can consider = your lasagna layers * 2 minutes.
    """
    number_of_layers = number_of_layers * 2
    return number_of_layers

def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    """This is the next step of our code but it's not complicated. We just combined 2 functions        that we used before. So that, I will not identify the parameters. But the task doesn't want to     this from us, I just noticed.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    number_of_layers = number_of_layers * 2
    return number_of_layers + elapsed_bake_time
    
