import tkinter as tk
from tkinter import messagebox
import pandas as pd

class Comparar:
    def __init__(self, master):
        self.master = master
        self.master.title("Comparação de Consumo")
        self.master.geometry("600x500")
        self.master.configure(bg="#e9f7ef")

        self.file_path = "Python/Adipia/planilha/consumo_aparelhos.xlsx"
        self.df = pd.read_excel(self.file_path)

        # Lista de aparelhos disponíveis
        self.aparelhos_disponiveis = self.df['Aparelho'].unique()

        self.criar_widgets()

    def criar_widgets(self):
        # Título
        tk.Label(self.master, text="Comparação de Consumo", font=("Arial", 16, "bold"), bg="#e9f7ef", fg="#1b5e20").pack(pady=10)

        # Lista de aparelhos disponíveis
        tk.Label(self.master, text="Selecione um aparelho:", font=("Arial", 12), bg="#e9f7ef", fg="#388e3c").pack()
        self.listbox_aparelhos = tk.Listbox(self.master, height=10, width=40)
        for aparelho in self.aparelhos_disponiveis:
            self.listbox_aparelhos.insert(tk.END, aparelho)
        self.listbox_aparelhos.pack(pady=10)

        # Entrada para potência
        tk.Label(self.master, text="Potência do aparelho (W):", font=("Arial", 12), bg="#e9f7ef", fg="#388e3c").pack()
        self.entry_potencia = tk.Entry(self.master, width=30)
        self.entry_potencia.pack(pady=5)

        # Entrada para tempo de uso
        tk.Label(self.master, text="Tempo de uso diário (h):", font=("Arial", 12), bg="#e9f7ef", fg="#388e3c").pack()
        self.entry_tempo = tk.Entry(self.master, width=30)
        self.entry_tempo.pack(pady=5)

        # Botão para calcular
        tk.Button(self.master, text="Calcular", font=("Arial", 12), bg="#a5d6a7", fg="#1b5e20", command=self.calcular_consumo).pack(pady=10)

        # Resultado
        self.result_text = tk.StringVar()
        self.result_label = tk.Label(self.master, textvariable=self.result_text, font=("Arial", 12), bg="#e9f7ef", fg="#1b5e20", wraplength=550, justify="left")
        self.result_label.pack(pady=10)

        # Botão para fechar
        tk.Button(self.master, text="Fechar", font=("Arial", 12), bg="#a5d6a7", fg="#1b5e20", command=self.master.destroy).pack(pady=10)

    def calcular_consumo(self):
        try:
            # Verificar se o usuário selecionou um aparelho
            selecionados = self.listbox_aparelhos.curselection()
            if not selecionados:
                messagebox.showerror("Erro", "Por favor, selecione um aparelho!")
                return

            # Obter aparelho selecionado
            aparelho_escolhido = self.listbox_aparelhos.get(selecionados[0])

            # Obter dados do usuário
            potencia_usuario = self.entry_potencia.get()
            horas_uso_usuario = self.entry_tempo.get()

            if not potencia_usuario or not horas_uso_usuario:
                messagebox.showerror("Erro", "Preencha todos os campos!")
                return

            potencia_usuario = float(potencia_usuario)
            horas_uso_usuario = float(horas_uso_usuario)

            # Cálculo do consumo do usuário
            consumo_usuario = (potencia_usuario * horas_uso_usuario * 30) / 1000

            # Filtrar os dados na planilha para o aparelho escolhido
            filtro = self.df[self.df['Aparelho'] == aparelho_escolhido].copy()

            # Calcular consumo mensal dos aparelhos da planilha
            filtro['Consumo Mensal (kWh)'] = (
                filtro['Potência (W)'] * filtro['Tempo de Uso Diário (h)'] * 30 / 1000
            )
            consumo_medio = filtro['Consumo Mensal (kWh)'].mean()

            # Comparar consumo do usuário com a média
            if consumo_usuario > consumo_medio * 1.2:
                aviso = "ALERTA: Seu consumo está muito alto em relação à média!"
            elif consumo_usuario < consumo_medio * 0.8:
                aviso = "INFORMAÇÃO: Seu consumo está muito baixo em relação à média!"
            else:
                aviso = "Seu consumo está dentro da média esperada."

            # Exibir os resultados
            resultado = (
                f"Consumo mensal estimado do seu aparelho: {consumo_usuario:.2f} kWh\n"
                f"Consumo médio dos aparelhos semelhantes: {consumo_medio:.2f} kWh\n\n{aviso}\n\n"
                f"Consumo dos aparelhos semelhantes na planilha:\n"
            )
            for _, row in filtro.iterrows():
                resultado += (
                    f"- Aparelho: {row['Aparelho']}, Potência: {row['Potência (W)']} W, "
                    f"Tempo de Uso Diário: {row['Tempo de Uso Diário (h)']} h, "
                    f"Consumo Mensal: {row['Consumo Mensal (kWh)']:.2f} kWh\n"
                )
            self.result_text.set(resultado)

        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos para potência e tempo de uso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Algo deu errado: {e}")

class ExibirResultado:
    def __init__(self, master, resultado):
        self.master = master
        self.master.title("Resultado da Comparação")
        self.master.geometry("600x400")
        self.master.configure(bg="#e9f7ef")

        # Exibir resultado
        self.result_text = tk.StringVar(value=resultado)
        result_label = tk.Label(self.master, textvariable=self.result_text, font=("Arial", 12), bg="#e9f7ef", fg="#1b5e20", wraplength=550, justify="left")
        result_label.pack(pady=20)

        # Botão para voltar
        tk.Button(self.master, text="Voltar", font=("Arial", 12), bg="#a5d6a7", fg="#1b5e20", command=self.master.destroy).pack(pady=10)


# Janela principal
janela_principal = tk.Tk()
janela_principal.withdraw()  # Oculta a janela principal inicialmente

# Instanciar a classe Comparar
comparar_app = Comparar(janela_principal)

# Quando o usuário clicar para calcular, exibir o resultado em uma nova janela
resultado_calculo = comparar_app.result_text.get()  # Obter o resultado
exibir_resultado_app = ExibirResultado(tk.Tk(), resultado_calculo)

# Iniciar a aplicação
janela_principal.mainloop()
