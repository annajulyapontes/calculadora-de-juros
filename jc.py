# -*- coding: utf-8 -*-
def calcular_juros_compostos(principal, taxa, tempo):
    """
    Calcula o montante com juros compostos.
    :param principal: Valor principal (float)
    :param taxa: Taxa de juros em decimal (float)
    :param tempo: Tempo em anos (float)
    :return: Montante total (float)
    """
    return principal * (1 + taxa)**tempo

if __name__ == "__main__":
    principal = float(input("Digite o valor principal: "))
    taxa = float(input("Digite a taxa de juros (em decimal): "))
    tempo = float(input("Digite o tempo (em anos): "))

    montante = calcular_juros_compostos(principal, taxa, tempo)
    print(f"O montante com juros compostos é: R$ {montante:.2f}")
