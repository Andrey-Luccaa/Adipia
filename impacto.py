import tkinter as tk
from tkinter import messagebox  # Importando para mostrar mensagens de erro

class ImpactoCicloVida:
    def __init__(self, master):
        self.master = master
        self.janela_impacto()  # Chama a função para criar a janela de entrada

    def janela_impacto(self):
        impacto_window = tk.Toplevel(self.master)
        impacto_window.title("Calcular Impacto Ambiental")
        impacto_window.geometry("600x400")
        impacto_window.configure(bg="#e9f7ef")

        # Labels e campos de entrada para o usuário
        tk.Label(impacto_window, text="Nome do Aparelho:", bg="#e9f7ef", fg="#1b5e20").pack(pady=5)
        aparelho_entry = tk.Entry(impacto_window, font=("Arial", 12))
        aparelho_entry.pack(pady=5)

        tk.Label(impacto_window, text="Potência média (W):", bg="#e9f7ef", fg="#1b5e20").pack(pady=5)
        potencia_entry = tk.Entry(impacto_window, font=("Arial", 12))
        potencia_entry.pack(pady=5)

        tk.Label(impacto_window, text="Horas de uso diário (h):", bg="#e9f7ef", fg="#1b5e20").pack(pady=5)
        horas_entry = tk.Entry(impacto_window, font=("Arial", 12))
        horas_entry.pack(pady=5)

        tk.Label(impacto_window, text="Vida útil (anos):", bg="#e9f7ef", fg="#1b5e20").pack(pady=5)
        vida_entry = tk.Entry(impacto_window, font=("Arial", 12))
        vida_entry.pack(pady=5)

        # Função para calcular o impacto
        def calcular_impacto():
            try:
                # Pegando os valores inseridos pelo usuário
                aparelho_escolhido = aparelho_entry.get()
                if aparelho_escolhido == "":
                    raise ValueError("Nome do aparelho é obrigatório!")
                
                potencia_media = float(potencia_entry.get())
                horas_uso_diario = float(horas_entry.get())
                vida_util = int(vida_entry.get())

                # Dados fictícios de impacto do ciclo de vida
                impacto_producao = 0.1  # Emissões de CO2 (kg CO2 por aparelho produzido)
                consumo_energia = 0.2  # Emissões de CO2 por kWh consumido

                # Calculando o impacto durante o uso
                consumo_energia_anual = (potencia_media * horas_uso_diario * 365) / 1000  # em kWh
                emissao_uso_anual = consumo_energia_anual * consumo_energia  # Emissões anuais de CO2

                # Calculando o impacto total do ciclo de vida
                emissao_total_vida_util = (impacto_producao + emissao_uso_anual) * vida_util

                # Exibindo o impacto do ciclo de vida
                resultado_impacto = (
                    f"Impacto Ambiental do Ciclo de Vida do {aparelho_escolhido}:\n\n"
                    f"Emissões de CO2 durante a produção: {impacto_producao:.2f} kg\n"
                    f"Emissões anuais durante o uso: {emissao_uso_anual:.2f} kg CO2 por ano\n"
                    f"Emissões totais ao longo da vida útil de {vida_util} anos: {emissao_total_vida_util:.2f} kg CO2\n"
                )

                # Criando uma nova janela para mostrar o resultado
                resultado_window = tk.Toplevel(impacto_window)
                resultado_window.title(f"Resultado do Impacto - {aparelho_escolhido}")
                resultado_window.geometry("500x300")
                resultado_window.configure(bg="#e9f7ef")

                label_impacto = tk.Label(resultado_window, text=resultado_impacto, font=("Arial", 12), bg="#e9f7ef", fg="#1b5e20", justify="left", wraplength=450)
                label_impacto.pack(pady=20)

                # Botão para fechar a janela
                btn_fechar = tk.Button(resultado_window, text="Fechar", font=("Arial", 12), bg="#a5d6a7", fg="#1b5e20", command=resultado_window.destroy)
                btn_fechar.pack(pady=10)

            except ValueError as e:
                # Caso o usuário insira um valor inválido ou deixe algum campo vazio
                messagebox.showerror("Erro", f"Erro ao calcular impacto: {e}")

        # Botão para calcular o impacto
        btn_calcular = tk.Button(impacto_window, text="Calcular Impacto", font=("Arial", 12), bg="#a5d6a7", fg="#1b5e20", command=calcular_impacto)
        btn_calcular.pack(pady=20)

        # Botão para fechar a janela de entrada
        btn_fechar_impacto = tk.Button(impacto_window, text="Fechar", font=("Arial", 12), bg="#a5d6a7", fg="#1b5e20", command=impacto_window.destroy)
        btn_fechar_impacto.pack(pady=10)