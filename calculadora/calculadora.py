print("BEM-VINDO À CALCULADORA.")

print("\nSELECIONE A OPERAÇÃO QUE DESEJA REALIZAR.")
print("MULTIPLICAR        [ 1 ]")
print("DIVIDIR            [ 2 ]")
print("SOMAR              [ 3 ]")
print("SUBTRAIR           [ 4 ]")
print("FECHAR CALCULADORA [ 5 ]")

while True:
    opcao = int(input("\nOPÇÃO: "))
    if opcao == 5:
        print("CALCULADORA ENCERRADA.")
        break
    num1 = float(input("Insira o primeiro número: "))
    num2 = float(input("Insira o segundo número: "))
    if opcao == 1:
        operacao = num1 * num2
        print(f"O RESULTADO É: {operacao}")
    elif opcao == 2:
        operacao = num1 / num2
        print(f"O RESULTADO É: {operacao}")
    elif opcao == 3:
        operacao = num1 + num2
        print(f"O RESULTADO É: {operacao}")
    elif opcao == 4:
        operacao = num1 - num2
        print(f"O RESULTADO É: {operacao}")
    else:
        print("[ERRO] OPÇÃO INVALIDA.")