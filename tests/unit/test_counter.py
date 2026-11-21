import pytest
from even_counter import even_number_counter

def test_negative_number():
    assert even_number_counter(x=[-1]) == {"parzyste": 0, "nieparzyste": 1}

def test_zero_number():
    assert even_number_counter(x=[0]) =={"parzyste": 1, "nieparzyste": 0}

def test_two_numbers():
    assert even_number_counter(x=[2, 1]) =={"parzyste": 1, "nieparzyste": 1}




