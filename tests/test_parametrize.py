import pytest
from tests import main


@pytest.mark.parametrize("valorA, valorB, result", [
    (1, 2, 3),
    (5, 7, 12),
    (-2, 2, 0),
    (3, 4, 7),
])
def test_somarParametrizada(valorA, valorB, result):
    resultado = main.somarValores(valorA, valorB)
    assert resultado == result
