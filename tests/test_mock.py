import pytest
from tests import mock


def test_obterDesconto(mocker):
    mocker.patch("tests.mock.retornarTaxaDesconto", return_value=0.50)
    resp = mock.obterDesconto(100)
    assert resp == 50


def taxaDescontoFalsa(multiplicador):
    return 0.25


def test_obterDescontoComSpyRetornoCustomizado(mocker):
    spy = mocker.patch("tests.mock.retornarTaxaDesconto",
                       side_effect=taxaDescontoFalsa)

    resultado = mock.obterDesconto(100)
    print(resultado)

    assert resultado == 75.0
    spy.assert_called_once()
    spy.assert_called_with(0.9)


# Integração, não unitário!
def test_calcularSomaComSpyIntegracao(mocker):
    spy = mocker.spy(mock, "retornarTaxaDesconto")
    resp = mock.obterDesconto(100)
    print(resp)

    assert resp == 91.0  # Retorno
    spy.assert_called_once()  # Comportamento
    # spy.assert_called_with(0.9)
