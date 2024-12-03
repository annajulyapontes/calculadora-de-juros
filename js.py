# -*- coding: utf-8 -*-

def calcular_juros_simples(principal, taxa, tempo):
    return principal * taxa * tempo

if __name__ == "__main__":
    principal = float(input("Digite o valor principal: "))
    taxa = float(input("Digite a taxa de juros (em decimal): "))
    tempo = float(input("Digite o tempo (em anos): "))

    juros = calcular_juros_simples(principal, taxa, tempo)
    print(f"O juros simples é: R$ {juros:.2f}")