import tkinter as tk
import math

class DesenhoArea:
    def __init__(self, master):
        self.master = master
        master.title("Desenhar Área")

        self.canvas = tk.Canvas(master, width=400, height=300, borderwidth=2, relief="groove")
        self.canvas.pack(pady=10)

        self.ponto_inicial = None
        self.pontos = []
        self.linhas = []

        self.canvas.bind("<Button-1>", self.iniciar_desenho)
        self.canvas.bind("<B1-Motion>", self.desenhar)
        self.canvas.bind("<ButtonRelease-1>", self.finalizar_linha)

        self.label_medida = tk.Label(master, text="Medida: 0 metros")
        self.label_medida.pack()

        self.label_area = tk.Label(master, text="Área: 0 metros quadrados")
        self.label_area.pack()

        self.escala_pixels_metro = 100  # Exemplo: 100 pixels = 1 metro

    def iniciar_desenho(self, event):
        self.ponto_inicial = (event.x, event.y)
        self.pontos.append((event.x, event.y))

    def desenhar(self, event):
        if self.ponto_inicial:
            x1, y1 = self.ponto_inicial
            x2, y2 = event.x, event.y
            self.canvas.delete("linha_temporaria")
            self.canvas.create_line(x1, y1, x2, y2, tags="linha_temporaria")
            comprimento_pixels = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            comprimento_metros = comprimento_pixels / self.escala_pixels_metro
            self.label_medida.config(text=f"Medida: {comprimento_metros:.2f} metros")

    def finalizar_linha(self, event):
        if self.ponto_inicial:
            x1, y1 = self.ponto_inicial
            x2, y2 = event.x, event.y
            linha_id = self.canvas.create_line(x1, y1, x2, y2, tags="linha_desenhada")
            self.linhas.append(((x1, y1), (x2, y2)))
            self.ponto_inicial = (event.x, event.y) # Começar nova linha
            self.pontos.append((event.x, event.y))
            self.canvas.delete("linha_temporaria")
            self.label_medida.config(text="Medida: 0 metros") # Resetar medida temporária

    # Aqui você precisaria adicionar a lógica para calcular a área
    def calcular_area_poligono(pontos):
        n = len(pontos)
        if n < 3:
            return 0.0  # Não é um polígono

        area = 0.0
        for i in range(n):
            x1, y1 = pontos[i]
            x2, y2 = pontos[(i + 1) % n]  # Próximo ponto (wrap around para o último)
            area += (x1 * y2 - x2 * y1)

        return abs(area) / 2.0
    # com base nos pontos armazenados na lista 'self.pontos'.
    # Isso dependerá da forma desenhada.

root = tk.Tk()
app = DesenhoArea(root)
root.mainloop()