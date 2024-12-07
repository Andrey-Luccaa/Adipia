import tkinter as tk

def informacoes_educacao(janela_pai=None):
    # Interface para Informações e Educação
    janela = tk.Toplevel(janela_pai)
    janela.title("Informações e Educação")
    janela.geometry("600x400")
    janela.configure(bg="#e9f7ef")

    tk.Label(janela, text="Informações e Educação Energética", font=("Arial", 16, "bold"), bg="#e9f7ef", fg="#1b5e20").pack(pady=10)

    info = """
    🌍 Dicas para economizar energia:
    - Use lâmpadas de LED, que consomem até 80% menos energia.
    - Evite abrir a porta da geladeira desnecessariamente.
    - Aproveite ao máximo a luz natural durante o dia.
    - Realize manutenção periódica em aparelhos para garantir eficiência.
    
    📊 Benefícios da economia de energia:
    - Redução nas contas de energia.
    - Menor impacto ambiental.
    - Maior durabilidade de equipamentos.

    Lembre-se: pequenas ações podem gerar grandes economias e ajudar o planeta!
    """

    texto = tk.Text(janela, wrap="word", font=("Arial", 12), bg="#e9f7ef", fg="#388e3c", bd=0)
    texto.insert("1.0", info)
    texto.config(state="disabled")  # Torna o texto apenas leitura
    texto.pack(padx=20, pady=10, fill="both", expand=True)

    tk.Button(janela, text="Fechar", font=("Arial", 12), bg="#a5d6a7", fg="#1b5e20", command=janela.destroy).pack(pady=10)
