import numpy as numpy
import cmath
import pytest
import functions.hp_calc.py as hc


def hyp1():
    assert fc.hyp(-3, -4) > 0, "two negative should return a positive"


def hyp2():
    assert fc.hyp(3, -9) > 0, "one +ve an done -ve returns a positive"


def hyp3():
    assert fc.hyp(0, 0) == 0, "2 zeroes returns a zero"


def hyp4():
    assert fc.hyp(7, 2.5) == pytest.approx(
        7.43, 0.01
    ), "square roots of 2 floats returns a float with their added precision"


def hyp4():
    assert fc.hyp(np.infty, 0) == np.infty, "square root if infinity is infinity"


# def hyp5():
# assert fc.hyp((cmath.complex(0,1)),0)==, "square of a square root of i would return i"
