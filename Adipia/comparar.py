import pandas as pd

def comparar_consumo():
    # Caminho do arquivo Excel
    file_path = "planilha/consumo_aparelhos.xlsx"

    # Ler a planilha
    df = pd.read_excel(file_path)

    # Obter lista única de aparelhos disponíveis
    aparelhos_disponiveis = df['Aparelho'].unique()

    # Exibir as opções numeradas de aparelhos
    print("\nAPARELHOS DISPONÍVEIS PARA COMPARAÇÃO:")
    for i, aparelho in enumerate(aparelhos_disponiveis, start=1):
        print(f"{i} - {aparelho}")

    # Entrada do usuário: escolha do aparelho
    print("\nCOMPARAÇÃO DE CONSUMO\n")
    opcao = int(input("Escolha o número correspondente ao aparelho: "))

    # Validar entrada do usuário
    if 1 <= opcao <= len(aparelhos_disponiveis):
        aparelho_escolhido = aparelhos_disponiveis[opcao - 1]
        print(f"\nVocê escolheu: {aparelho_escolhido}")

        # Filtrar os dados na planilha para o aparelho escolhido
        filtro = df[df['Aparelho'] == aparelho_escolhido].copy()

        # Entrada do usuário: potência e horas de uso
        potencia_usuario = float(input("Digite a potência do seu aparelho em watts (W): "))
        horas_uso_usuario = float(input("Digite o número de horas de uso por dia: "))

        # Cálculo do consumo mensal do usuário
        consumo_usuario = (potencia_usuario * horas_uso_usuario * 30) / 1000

        # Calcular o consumo mensal dos aparelhos da planilha
        filtro.loc[:, 'Consumo Mensal (kWh)'] = (
            filtro['Potência (W)'] * filtro['Tempo de Uso Diário (h)'] * 30 / 1000
        )

        # Obter média de consumo dos aparelhos semelhantes
        consumo_medio = filtro['Consumo Mensal (kWh)'].mean()

        # Comparar consumo do usuário com a média
        if consumo_usuario > consumo_medio * 1.2:  # 20% acima da média
            aviso = "ALERTA: Seu consumo está muito alto em relação à média!"
        elif consumo_usuario < consumo_medio * 0.8:  # 20% abaixo da média
            aviso = "INFORMAÇÃO: Seu consumo está muito baixo em relação à média!"
        else:
            aviso = "Seu consumo está dentro da média esperada."

        # Exibir resultados
        print(f"\nConsumo mensal estimado do seu aparelho: {consumo_usuario:.2f} kWh")
        print(f"\nConsumo médio dos aparelhos semelhantes: {consumo_medio:.2f} kWh")
        print(aviso)

        print("\nConsumo dos aparelhos semelhantes na planilha:")
        print(filtro[['Aparelho', 'Potência (W)', 'Tempo de Uso Diário (h)', 'Consumo Mensal (kWh)']])
    else:
        print("\nOpção inválida. Por favor, escolha um número válido.")
