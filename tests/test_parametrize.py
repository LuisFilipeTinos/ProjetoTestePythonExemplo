import pytest
from tests.main import somarValores


@pytest.mark.parametrize(
    "entrada, esperado",
    [
        ({"valor1": 100, "valor2": 20}, 120),
        ({"valor1": 50, "valor2": 5}, 55),
        ({"valor1": 80, "valor2": 40}, 120),
    ]
)
def test_somarValores(entrada, esperado):
    resultado = somarValores(entrada["valor1"], entrada["valor2"])
    assert resultado == esperado
