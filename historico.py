import tkinter as tk

def exibir_historico():
    # Interface para histórico
    janela = tk.Tk()
    janela.title("Histórico de Consumo")
    janela.geometry("500x300")
    janela.configure(bg="#e9f7ef")

    tk.Label(janela, text="Histórico de Consumo", font=("Arial", 16, "bold"), bg="#e9f7ef", fg="#1b5e20").pack(pady=10)

    # Simulando dados de histórico
    historico = [
        "Janeiro: 120 kWh",
        "Fevereiro: 100 kWh",
        "Março: 110 kWh",
        "Abril: 130 kWh"
    ]

    for item in historico:
        tk.Label(janela, text=item, font=("Arial", 12), bg="#e9f7ef", fg="#388e3c").pack()

    tk.Button(janela, text="Fechar", font=("Arial", 12), bg="#a5d6a7", fg="#1b5e20", command=janela.destroy).pack(pady=10)

    janela.mainloop()
