def retornarTaxaDesconto(multiplicador):
    return 0.10 * multiplicador


def obterDesconto(preco: float):
    taxa = retornarTaxaDesconto(0.9)
    return preco - (preco * taxa)
