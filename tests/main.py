
valorReferencia = 2


def somarValores(valor1, valor2):
    return valor1 + valor2


def subtrairValores(valor1, valor2):
    return valor1 - valor2


def multiplicarValores(valor1, valor2):
    return valor1 * valor2


def dividirValores(valor1, valor2):
    return valor1 / valor2


def calcularAreaQuadrado(lado):
    return lado * lado

#-----

def retornarValorEspecifico(valor):
    # processamento...
    # processamento...
    return {
        "nome": "Luis Filipe",
        "valorFinal": valor,
        "statusOk": True
    }


def erroUsuarioNaoEncontrado():
    # processamento...
    # processamento...
    raise Exception("Usuário não encontrado!")


def erroSystemExit():
    raise SystemExit(1)
