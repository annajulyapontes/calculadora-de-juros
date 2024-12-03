# -*- coding: utf-8 -*-
def calcular_parcela(valor, taxa, meses):
    """
    Calcula o valor da parcela em um financiamento.
    :param valor: Valor total do financiamento (float)
    :param taxa: Taxa de juros mensal em decimal (float)
    :param meses: Número de parcelas (int)
    :return: Valor da parcela (float)
    """
    fator = (1 + taxa)**meses
    return valor * (taxa * fator) / (fator - 1)

if __name__ == "__main__":
    valor = float(input("Digite o valor do financiamento: "))
    taxa = float(input("Digite a taxa de juros mensal (em decimal): "))
    meses = int(input("Digite o número de parcelas: "))

    parcela = calcular_parcela(valor, taxa, meses)
    print(f"O valor da parcela é: R$ {parcela:.2f}")
