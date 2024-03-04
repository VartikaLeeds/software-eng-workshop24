import functions.calc as fc
import pytest


def test_negatives():
    assert fc.adivb(-10, -5) == 2, "two negatives return a postive"


def test_pos_neg():
    assert fc.adivb(-9, 3) < 0, "one +ve, 1 -ve reurns -ve"


def test_3():
    assert fc.adivb(35, 7) > 0, "2 positives should be positive"


def test_4():
    assert isinstance(fc.adivb(5, 10), float), "minor by larger should be float"


def test_5():
    # assert fc.type(adivb(5,10))== type(1.0)
    assert fc.adivb(5, 2) == 2.5, "5 divided by 2 should be 2.5"


def test_6():
    assert fc.adivb(10, 3) == pytest.approx(3.33, 0.01), "10 div by 3 is 3.33333"
