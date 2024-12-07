import tkinter as tk
from tkinter import ttk
import random

janela_analise = None  # Variável global para controlar a janela

def analise_eficiencia(janela_pai=None):
    global janela_analise
    # Verifica se a janela já está aberta ou foi fechada
    if janela_analise is None or not janela_analise.winfo_exists():  
        janela_analise = tk.Toplevel(janela_pai)  # Cria uma nova janela
        janela_analise.title("Análise de Eficiência")
        janela_analise.geometry("1280x720")
        janela_analise.configure(bg="#e9f7ef")

        # Centralizar janela
        largura, altura = 600, 400
        pos_x = (janela_pai.winfo_screenwidth() - largura) // 2
        pos_y = (janela_pai.winfo_screenheight() - altura) // 2
        janela_analise.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

        # Título da janela
        tk.Label(janela_analise, text="Análise de Eficiência", font=("Arial", 18, "bold"), bg="#e9f7ef", fg="#1b5e20").pack(pady=10)

        # Mensagem principal
        tk.Label(
            janela_analise,
            text="Sua eficiência energética está acima da média!",
            font=("Arial", 12),
            bg="#e9f7ef",
            fg="#388e3c"
        ).pack(pady=10)

        # Gráfico ilustrativo (simulação com barras de progresso)
        tk.Label(janela_analise, text="Consumo Atual vs. Consumo Ideal:", font=("Arial", 12), bg="#e9f7ef").pack(pady=10)

        # Barras de progresso
        frame_barras = tk.Frame(janela_analise, bg="#e9f7ef")
        frame_barras.pack(pady=10)

        tk.Label(frame_barras, text="Consumo Atual", font=("Arial", 10), bg="#e9f7ef").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        barra_atual = ttk.Progressbar(frame_barras, length=300, value=random.randint(50, 100))  # Valor randômico
        barra_atual.grid(row=0, column=1, padx=5)

        tk.Label(frame_barras, text="Consumo Ideal", font=("Arial", 10), bg="#e9f7ef").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        barra_ideal = ttk.Progressbar(frame_barras, length=300, value=80)  # Valor ideal fixo
        barra_ideal.grid(row=1, column=1, padx=5)

        # Dicas e melhorias
        tk.Label(janela_analise, text="Dicas para Melhorar:", font=("Arial", 14, "bold"), bg="#e9f7ef", fg="#1b5e20").pack(pady=10)
        dicas = [
            "🌱 Substitua lâmpadas incandescentes por LED.",
            "🌱 Evite deixar aparelhos em standby.",
            "🌱 Utilize eletrodomésticos com selo Procel A.",
            "🌱 Desligue luzes em ambientes desocupados.",
        ]
        for dica in dicas:
            tk.Label(janela_analise, text=dica, font=("Arial", 12), bg="#e9f7ef", fg="#388e3c").pack(anchor="w", padx=20)

        # Botão de fechar
        tk.Button(
            janela_analise,
            text="Fechar",
            font=("Arial", 12),
            bg="#a5d6a7",
            fg="#1b5e20",
            command=fechar_janela
        ).pack(pady=20)

        # Atribui o comando de fechar corretamente
        janela_analise.protocol("WM_DELETE_WINDOW", lambda: fechar_janela())

def fechar_janela():
    global janela_analise
    if janela_analise and janela_analise.winfo_exists():  # Verifica se a janela existe antes de destruir
        janela_analise.destroy()
        janela_analise = None  # Reseta a variável após fechar a janela
