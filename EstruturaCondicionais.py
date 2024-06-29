def calcular_reajuste(salario_atual):
    inflacao = 0.038

    if salario_atual <= 280.00:
        percentual_aumento = 0.20
    elif 280.00 < salario_atual <= 700.00:
        percentual_aumento = 0.15
    elif 700.00 < salario_atual <= 1500.00:
        percentual_aumento = 0.10
    else:
        percentual_aumento = 0.05

    valor_aumento = salario_atual * percentual_aumento
    novo_salario = salario_atual + valor_aumento
    aumento_real = valor_aumento - (novo_salario * inflacao)

    return salario_atual, percentual_aumento, valor_aumento, novo_salario, aumento_real

def main():
    salario_atual = float(input("Digite o salário atual do colaborador: R$ "))
    salario_antigo, percentual_aumento, valor_aumento, novo_salario, aumento_real = calcular_reajuste(salario_atual)

    print(f"Salário antes do reajuste: R$ {salario_antigo:.2f}")
    print(f"Percentual de aumento aplicado: {percentual_aumento * 100:.0f}%")
    print(f"Valor do aumento: R$ {valor_aumento:.2f}")
    print(f"Novo salário, após o aumento: R$ {novo_salario:.2f}")
    print(f"Valor do aumento real, descontado a inflação: R$ {aumento_real:.2f}")

if __name__ == "__main__":
    main()