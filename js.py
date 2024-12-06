def calcular_juros_simples(capital, taxa, tempo):
    """
    Calcula o juros simples.

    Args:
        capital (float): O capital inicial.
        taxa (float): A taxa de juros em porcentagem.
        tempo (float): O tempo em meses.

    Returns:
        float: O valor do juros simples.
    """
    juros = capital * (taxa / 100) * tempo
    return juros

if __name__ == "__main__":
    print("Calculadora de Juros Simples")
    capital = float(input("Digite o capital inicial: "))
    taxa = float(input("Digite a taxa de juros (%): "))
    tempo = float(input("Digite o tempo (meses): "))

    juros = calcular_juros_simples(capital, taxa, tempo)
    montante = capital + juros

    print(f"Juros Simples: R${juros:.2f}")
    print(f"Montante Final: R${montante:.2f}")
