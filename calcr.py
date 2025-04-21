def calcular(num1, num2, operacao):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        if num2 == 0:
            return "Erro: divisão por zero!"
        return num1 / num2
    else:
        return "Operação inválida."

def main():
    print("=== Calculadora Simples ===")
    try:
        num1 = float(input("Digite o primeiro número: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))
        resultado = calcular(num1, num2, operacao)
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Erro: entrada inválida. Use apenas números.")

if __name__ == "__main__":
    main()
