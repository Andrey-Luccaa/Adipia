import os
import comparar  # Importa o módulo comparar.py

def menu():
    while True:
        print("==========================================================================================")
        print("Escolha uma opção: ")
        print()
        print("1 - Comparar consumo")
        print("2 - Histórico de Consumo")
        print("3 - Análise de Eficiência")
        print("4 - Cálculo de Custos")
        print("5 - Alertas e Sugestões")
        print("6 - Informações e Educação")
        print("7 - Feedback e Suporte")
        print("==========================================================================================")

        # Captura a entrada do usuário
        opcao = int(input("Digite o número da opção desejada: "))

        # Verifica a opção escolhida
        if opcao == 1:
            print("Você escolheu: Comparar consumo")
            comparar.comparar_consumo()  # Chama a função de comparação de consumo

            # Pergunta ao usuário se ele deseja continuar comparando
            continuar = input("\nDeseja comparar o consumo de outro aparelho? (s/n): ").strip().lower()
            if continuar != 's':
                print("\nSaindo do programa...")
                break  # Sai do loop se o usuário não quiser continuar comparando
        elif opcao == 2:
            print("Saindo do programa...")
            break  # Sai do loop
        else:
            print("Opção inválida! Tente novamente.")

# Chama o menu
menu()
