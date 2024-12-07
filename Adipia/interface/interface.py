from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QVBoxLayout

class App(QWidget):
    def __init__(self):
        super().__init__()

        # Configuração da janela
        self.setWindowTitle("Interface com PyQt5")
        self.setGeometry(250, 250, 500, 500)

        # Layout
        layout = QVBoxLayout()

        # Labels para exibir as opções
        self.label1 = QLabel("Escolha uma opção:", self)
        self.label2 = QLabel("1 - Comparar consumo", self)
        self.label3 = QLabel("2 - Histórico de Consumo", self)
        self.label4 = QLabel("3 - Análise de Eficiência", self)
        self.label5 = QLabel("4 - Cálculo de Custos", self)
        self.label6 = QLabel("5 - Alertas e Sugestões", self)
        self.label7 = QLabel("6 - Informações e Educação", self)
        self.label8 = QLabel("7 - Feedback e Suporte", self)

        # Adicionando as labels ao layout
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.addWidget(self.label3)
        layout.addWidget(self.label4)
        layout.addWidget(self.label5)
        layout.addWidget(self.label6)
        layout.addWidget(self.label7)
        layout.addWidget(self.label8)

        # Campo de entrada para o nome
        self.entry = QLineEdit(self)
        layout.addWidget(self.entry)

        # Botão para exibir a mensagem
        self.button = QPushButton("Exibir mensagem", self)
        self.button.clicked.connect(self.exibir_mensagem)
        layout.addWidget(self.button)

        # Label para mostrar a resposta
        self.result_label = QLabel("", self)
        layout.addWidget(self.result_label)

        # Definindo o layout da janela
        self.setLayout(layout)

    def exibir_mensagem(self):
        nome = self.entry.text()
        self.result_label.setText(f"Olá, {nome}")

# Inicia a aplicação PyQt
app = QApplication([])
window = App()
window.show()
app.exec_()
