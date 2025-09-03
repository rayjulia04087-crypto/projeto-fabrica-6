
def somaImposto(taxaImposto: float, custo: float) -> float:
    """
    Retorna o custo acrescido do imposto sobre vendas.
    - taxaImposto: porcentagem do imposto (ex.: 17.5 para 17,5%)
    - custo: preço do item antes do imposto
    Levanta ValueError se algum valor for negativo.
    """
    if taxaImposto < 0:
        raise ValueError("taxaImposto não pode ser negativa.")
    if custo < 0:
        raise ValueError("custo não pode ser negativo.")
    return custo * (1 + taxaImposto / 100.0)


def ler_float(msg: str) -> float:
    """Lê um número real, aceitando vírgula ou ponto como separador decimal."""
    return float(input(msg).strip().replace(',', '.'))


def main() -> None:
    print("=== Cálculo de Preço com Imposto ===\n")
    taxa = ler_float("Digite a taxa de imposto (%): ")
    custo = ler_float("Digite o custo do item (antes do imposto): ")

    try:
        final = somaImposto(taxa, custo)
    except ValueError as e:
        print(f"Erro: {e}")
        return

    print(f"\nPreço final com imposto: R$ {final:.2f}")


if __name__ == "__main__":
    main()
