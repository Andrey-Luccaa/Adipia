import tkinter as tk
from tkinter import messagebox  # Importar o messagebox corretamente

def calculo_custos(janela_pai=None):
    def calcular():
        try:
            consumo_mensal = float(entry_consumo.get())
            tarifa = float(entry_tarifa.get())
            custo_total = consumo_mensal * tarifa
            result_text.set(f"Custo mensal estimado: R$ {custo_total:.2f}")
        except ValueError:
            messagebox.showerror("Erro", "Insira valores numéricos válidos.")

    # Criar uma janela Toplevel (nova janela) se janela_pai for passado
    janela = tk.Toplevel(janela_pai) if janela_pai else tk.Tk()  # Usar Toplevel se janela_pai for passado
    janela.title("Cálculo de Custos")
    janela.geometry("500x300")
    janela.configure(bg="#e9f7ef")

    # Adicionar componentes da janela
    tk.Label(janela, text="Cálculo de Custos de Energia", font=("Arial", 16, "bold"), bg="#e9f7ef", fg="#1b5e20").pack(pady=10)

    tk.Label(janela, text="Digite o consumo mensal (kWh):", font=("Arial", 12), bg="#e9f7ef", fg="#388e3c").pack()
    entry_consumo = tk.Entry(janela)
    entry_consumo.pack(pady=5)

    tk.Label(janela, text="Digite a tarifa de energia (R$/kWh):", font=("Arial", 12), bg="#e9f7ef", fg="#388e3c").pack()
    entry_tarifa = tk.Entry(janela)
    entry_tarifa.pack(pady=5)

    tk.Button(janela, text="Calcular", font=("Arial", 12), bg="#a5d6a7", fg="#1b5e20", command=calcular).pack(pady=10)

    result_text = tk.StringVar()
    tk.Label(janela, textvariable=result_text, font=("Arial", 12), bg="#e9f7ef", fg="#1b5e20").pack(pady=10)

    # Se a janela pai foi passada, o botão "Fechar" fecha apenas a janela de cálculo
    def fechar():
        janela.destroy()

    tk.Button(janela, text="Fechar", font=("Arial", 12), bg="#a5d6a7", fg="#1b5e20", command=fechar).pack(pady=10)

    janela.mainloop()

# Exemplo de como chamar a função:
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Janela Principal")
    root.geometry("500x300")

    def abrir_calculo_custos():
        calculo_custos(root)  # Passando 'root' como janela pai

    tk.Button(root, text="Abrir Cálculo de Custos", command=abrir_calculo_custos).pack(pady=20)

    root.mainloop()
