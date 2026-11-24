import pytest

from odd_even import odd_even_check

@pytest.fixture
def liczby():
    return [1, 2, 3, 4, 5]

def test_odd_even_check(liczby):
    assert odd_even_check(liczby) == {"even":2, "odd":3}

def test_is_highest_five(liczby):
    assert max(liczby) == 5

def test_num_of_elements(liczby):
    assert len(liczby) == 5

@pytest.mark.parametrize ("dane, oczekiwane", [([], {"even":0,"odd":0}),
                                               ([-1, -2, -3, -4], {"even":2,"odd":2}),
                                               ([0], {"even":1,"odd":0}),
                                               ([123124312], {"even":1,"odd":0})], ids=["empty list", "only negative numbers", "only zero", "one big number"])
def test_parametric_odd_even(dane, oczekiwane):
    assert odd_even_check(dane) == oczekiwane


@pytest.mark.parametrize("dodatkowe, oczekiwane", [
    ([], {"even":2, "odd":3}),
    ([0, 0, 0, 0], {"even":6, "odd":3}),
    ([1, 3, 5, 7], {"even":2, "odd":7}),
    ([1, 1, 0, 0], {"even":4, "odd":5}),
    ], ids=["pusta", "same_zera", "same_nieparzyste", "mieszanka"])
def test_baza_plus_dodatkowe(liczby, dodatkowe, oczekiwane):
    assert odd_even_check(liczby+dodatkowe) == oczekiwane