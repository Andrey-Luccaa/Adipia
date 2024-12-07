import tkinter as tk

def alertas_e_sugestoes(janela_pai=None):
    # Interface para alertas e sugestões
    janela = tk.Tk()
    janela.title("Alertas e Sugestões")
    janela.geometry("500x300")
    janela.configure(bg="#e9f7ef")

    tk.Label(janela, text="Alertas e Sugestões", font=("Arial", 16, "bold"), bg="#e9f7ef", fg="#1b5e20").pack(pady=10)

    # Exemplo de alertas e sugestões
    alertas = [
        "Evite deixar aparelhos em modo stand-by.",
        "Substitua lâmpadas incandescentes por LED.",
        "Use eletrodomésticos durante horários de tarifa reduzida.",
        "Realize manutenção periódica em aparelhos antigos."
    ]

    for alerta in alertas:
        tk.Label(janela, text=f"- {alerta}", font=("Arial", 12), bg="#e9f7ef", fg="#388e3c", wraplength=450, justify="left").pack(anchor="w", padx=10)

    tk.Button(janela, text="Fechar", font=("Arial", 12), bg="#a5d6a7", fg="#1b5e20", command=janela.destroy).pack(pady=10)
