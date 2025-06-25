from tests.main import erroUsuarioNaoEncontrado, calcularAreaQuadrado, erroSystemExit
import pytest


def test_erroUsuarioNaoEncontrado():
    try:
        erroUsuarioNaoEncontrado()
    except Exception as exception:
        print(exception)
        assert str(exception) == "Usuário não encontrado!"


def test_erroSystemExit():
    with pytest.raises(SystemExit):
        erroSystemExit()


def test_erroComPytest():
    with pytest.raises(Exception) as info_erro:
        erroUsuarioNaoEncontrado()

    assert str(info_erro.value) == "Usuário não encontrado!"


# def test_erroComPytestSemExcecao():
#    with pytest.raises(Exception):
#        calcularAreaQuadrado(3)
