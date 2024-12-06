def calcular_prestacao(valor_financiado, taxa_juros, tempo):
    """
    Calcula o valor das prestações em um financiamento.

    Args:
        valor_financiado (float): O valor total financiado.
        taxa_juros (float): A taxa de juros mensal em porcentagem.
        tempo (int): O prazo de pagamento em meses.

    Returns:
        float: O valor da prestação mensal.
    """
    taxa_mensal = taxa_juros / 100
    prestacao = (valor_financiado * taxa_mensal) / (1 - (1 + taxa_mensal) ** -tempo)
    return prestacao

if __name__ == "__main__":
    print("Simulação de Financiamento")
    valor_financiado = float(input("Digite o valor financiado: "))
    taxa_juros = float(input("Digite a taxa de juros mensal (%): "))
    tempo = int(input("Digite o prazo de pagamento (meses): "))

    prestacao = calcular_prestacao(valor_financiado, taxa_juros, tempo)
    valor_total = prestacao * tempo

    print(f"Valor da Prestação: R${prestacao:.2f}")
    print(f"Valor Total Pago: R${valor_total:.2f}")
    print(f"Juros Totais: R${valor_total - valor_financiado:.2f}")
