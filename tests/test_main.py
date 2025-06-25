import tests.main as main
from tests.main import valorReferencia


def test_somarValores():
    valorFinal = main.somarValores(valorReferencia, valorReferencia)
    assert valorFinal == 4


def test_subtrairValores():
    valorFinal = main.subtrairValores(valorReferencia, valorReferencia)
    assert valorFinal == 0


def test_multiplicarValores():
    valorFinal = main.multiplicarValores(valorReferencia, valorReferencia)
    assert valorFinal == 4


def test_dividirValores():
    valorFinal = main.dividirValores(valorReferencia, valorReferencia)
    assert valorFinal == 1


def test_calcularAreaQuadrado():
    valorFinal = main.calcularAreaQuadrado(valorReferencia)
    assert valorFinal == 4
    assert isinstance(valorFinal, int)


def test_retornarValorEspecifico():
    info = main.retornarValorEspecifico(valorReferencia)
    assert "valorFinal" in info
    assert info["nome"] == "Luis Filipe"
    assert "tipo" not in info
    assert info["statusOk"]
    assert isinstance(info["statusOk"], bool)
