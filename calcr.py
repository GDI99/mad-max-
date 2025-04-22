"""Módulo com uma calculadora simples."""

def calcular(num1, num2, operacao):
    """Realiza a operação matemática informada entre dois números."""
    if operacao == "+":
        return num1 + num2
    if operacao == "-":
        return num1 - num2
    if operacao == "*":
        return num1 * num2
    if operacao == "/":
        if num2 == 0:
            return "Erro: divisão por zero!"
        return num1 / num2
    return "Operação inválida."

def main():
    """Função principal que executa a calculadora."""
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
