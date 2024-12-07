import tkinter as tk

def feedback_e_suporte():
    def enviar_feedback():
        mensagem = entry_feedback.get("1.0", tk.END).strip()
        if mensagem:
            tk.messagebox.showinfo("Obrigado", "Seu feedback foi enviado com sucesso!")
            entry_feedback.delete("1.0", tk.END)
        else:
            tk.messagebox.showerror("Erro", "Por favor, insira uma mensagem de feedback.")

    # Interface para feedback e suporte
    janela = tk.Tk()
    janela.title("Feedback e Suporte")
    janela.geometry("500x400")
    janela.configure(bg="#e9f7ef")

    tk.Label(janela, text="Feedback e Suporte", font=("Arial", 16, "bold"), bg="#e9f7ef", fg="#1b5e20").pack(pady=10)

    tk.Label(janela, text="Digite seu feedback ou dúvida:", font=("Arial", 12), bg="#e9f7ef", fg="#388e3c").pack()
    entry_feedback = tk.Text(janela, height=10, width=50)
    entry_feedback.pack(pady=10)

    tk.Button(janela, text="Enviar", font=("Arial", 12), bg="#a5d6a7", fg="#1b5e20", command=enviar_feedback).pack(pady=10)

    tk.Button(janela, text="Fechar", font=("Arial", 12), bg="#a5d6a7", fg="#1b5e20", command=janela.destroy).pack(pady=10)

    janela.mainloop()
