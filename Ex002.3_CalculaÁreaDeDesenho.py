import tkinter as tk
from tkinter import filedialog, messagebox
import math

class DesenhoArea:
    def __init__(self, master):
        self.master = master
        master.title("Desenhar Área")

        self.canvas = tk.Canvas(master, width=400, height=300, borderwidth=2, relief="groove")
        self.canvas.pack(pady=10, padx=10)

        self.ponto_inicial = None
        self.pontos = []
        self.linhas_ids = []  # Para rastrear as linhas desenhadas no canvas

        self.canvas.bind("<Button-1>", self.iniciar_desenho)
        self.canvas.bind("<B1-Motion>", self.desenhar)
        self.canvas.bind("<ButtonRelease-1>", self.finalizar_linha)

        self.label_medida = tk.Label(master, text="Medida: 0 metros")
        self.label_medida.pack(pady=5)

        self.label_area = tk.Label(master, text="Área: 0 metros quadrados")
        self.label_area.pack(pady=5)

        self.escala_pixels_metro = 100  # Exemplo: 100 pixels = 1 metro

        # Frame para os botões
        button_frame = tk.Frame(master)
        button_frame.pack(pady=10)

        self.btn_novo = tk.Button(button_frame, text="Novo Cálculo", command=self.novo_calculo)
        self.btn_novo.pack(side=tk.LEFT, padx=5)

        self.btn_salvar = tk.Button(button_frame, text="Salvar", command=self.salvar)
        self.btn_salvar.pack(side=tk.LEFT, padx=5)

        self.btn_apagar = tk.Button(button_frame, text="Apagar", command=self.apagar)
        self.btn_apagar.pack(side=tk.LEFT, padx=5)

        self.btn_fechar = tk.Button(button_frame, text="Fechar", command=master.quit)
        self.btn_fechar.pack(side=tk.LEFT, padx=5)

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
            self.linhas_ids.append(linha_id)
            self.ponto_inicial = (event.x, event.y) # Começar nova linha
            self.pontos.append((event.x, event.y))
            self.canvas.delete("linha_temporaria")
            self.label_medida.config(text="Medida: 0 metros") # Resetar medida temporária
            self.atualizar_area() # Chamar a função para calcular e exibir a área

    def calcular_area_poligono(self, pontos):
        n = len(pontos)
        if n < 3:
            return 0.0

        area_pixels_quadrados = 0.0
        for i in range(n):
            x1, y1 = pontos[i]
            x2, y2 = pontos[(i + 1) % n]
            area_pixels_quadrados += (x1 * y2 - x2 * y1)

        return abs(area_pixels_quadrados) / 2.0

    def atualizar_area(self):
        area_pixels = self.calcular_area_poligono(self.pontos)
        area_metros_quadrados = area_pixels / (self.escala_pixels_metro ** 2)
        self.label_area.config(text=f"Área: {area_metros_quadrados:.2f} metros quadrados")

    def novo_calculo(self):
        self.canvas.delete("all")  # Apaga todos os desenhos do canvas
        self.pontos = []
        self.linhas_ids = []
        self.ponto_inicial = None
        self.label_medida.config(text="Medida: 0 metros")
        self.label_area.config(text="Área: 0 metros quadrados")

    def apagar(self):
        if self.linhas_ids:
            ultimo_linha_id = self.linhas_ids.pop()
            self.canvas.delete(ultimo_linha_id)
            if self.pontos:
                self.pontos.pop()
            self.atualizar_area()
            if not self.pontos:
                self.label_medida.config(text="Medida: 0 metros")
                self.label_area.config(text="Área: 0 metros quadrados")
            elif len(self.pontos) > 1:
                x1, y1 = self.pontos[-2]
                x2, y2 = self.pontos[-1]
                comprimento_pixels = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                comprimento_metros = comprimento_pixels / self.escala_pixels_metro
                self.label_medida.config(text=f"Medida: {comprimento_metros:.2f} metros")
            else:
                self.label_medida.config(text="Medida: 0 metros")


    def salvar(self):
        if not self.pontos:
            messagebox.showinfo("Salvar", "Nenhum desenho para salvar.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                               filetypes=[("Arquivo de Texto", "*.txt"), ("Todos os Arquivos", "*.*")])
        if file_path:
            try:
                with open(file_path, "w") as f:
                    f.write("Pontos do Desenho (x, y):\n")
                    for ponto in self.pontos:
                        f.write(f"{ponto[0]}, {ponto[1]}\n")
                    area_pixels = self.calcular_area_poligono(self.pontos)
                    area_metros_quadrados = area_pixels / (self.escala_pixels_metro ** 2)
                    f.write(f"\nÁrea Calculada: {area_metros_quadrados:.2f} metros quadrados\n")
                messagebox.showinfo("Salvar", f"Desenho e cálculo salvos em: {file_path}")
            except Exception as e:
                messagebox.showerror("Erro ao Salvar", f"Ocorreu um erro ao salvar o arquivo: {e}")

root = tk.Tk()
app = DesenhoArea(root)
root.mainloop()