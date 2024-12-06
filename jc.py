def calcular_juros_compostos(capital, taxa, tempo):
    """
    Calcula o montante com juros compostos.

    Args:
        capital (float): O capital inicial.
        taxa (float): A taxa de juros em porcentagem.
        tempo (float): O tempo em meses ou anos.

    Returns:
        float: O montante com juros compostos.
    """
    montante = capital * (1 + (taxa / 100)) ** tempo
    return montante

if __name__ == "__main__":
    print("Calculadora de Juros Compostos")
    capital = float(input("Digite o capital inicial: "))
    taxa = float(input("Digite a taxa de juros (%): "))
    tempo = float(input("Digite o tempo (meses ou anos): "))

    montante = calcular_juros_compostos(capital, taxa, tempo)
    juros = montante - capital

    print(f"Juros Compostos: R${juros:.2f}")
    print(f"Montante Final: R${montante:.2f}")
