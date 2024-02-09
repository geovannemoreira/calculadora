def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        if num2 != 0:  # Verifica se o divisor não é zero
            return num1 / num2
        else:
            return "Erro: Divisão por zero"
    else:
        return "Erro: Operação inválida"

while True:
    try:
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))
        operacao = int(input("Escolha a operação (1 - Soma, 2 - Subtração, 3 - Multiplicação, 4 - Divisão): "))

        resultado = calculadora(numero1, numero2, operacao)
        print("O resultado da operação é:", resultado)
    except ValueError:
        print("Erro: Entrada inválida. Por favor, insira apenas dados que foram pedidos.")
    except Exception as e:
        print("Erro:", e)

    continuar = input("Deseja continuar? (S/N): ")
    if continuar.upper() != 'S':
        break