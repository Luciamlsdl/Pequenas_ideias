class PisoLaminado:

    def __init__(self, nome_cliente, cidade, ambiente, largura, comprimento, modelo_piso, quantidade_porta):
        self.nome_cliente = nome_cliente
        self.cidade = cidade
        self.ambiente = ambiente
        self.largura = largura
        self.comprimento = comprimento
        self.modelo_piso = modelo_piso
        self.quantidade_porta = quantidade_porta

    def calcular_area(self):
        return self.largura * self.comprimento
    
    def calcular_material(self):
        area = self.calcular_area()
        if self.modelo_piso == 'Eucafloor':
            if self.ambiente == 'carvalho':
                qtde_cx = area / 2.2
            elif self.ambiente == 'ipê':
                qtde_cx = area / 2.3
            elif self.ambiente == 'jacarandá':
                qtde_cx = area / 2.4
            elif self.ambiente == 'peroba':
                qtde_cx = area / 2.5
            else:
                return 'Ambiente inválido'
        elif self.modelo_piso == 'Durafloor':
            if self.ambiente == 'carvalho':
                qtde_cx = area / 2.1
            elif self.ambiente == 'ipê':
                qtde_cx = area / 2.2
            elif self.ambiente == 'jacarandá':
                qtde_cx = area / 2.3
            elif self.ambiente == 'peroba':
                qtde_cx = area / 2.4
            else:
                return 'Ambiente inválido'
        elif self.modelo_piso == 'Espaçofloor':
            if self.ambiente == 'carvalho':
                qtde_cx = area / 2.3
            elif self.ambiente == 'ipê':
                qtde_cx = area / 2.4
            elif self.ambiente == 'jacarandá':
                qtde_cx = area / 2.5
            elif self.ambiente == 'peroba':
                qtde_cx = area / 2.6
            else:
                return 'Ambiente inválido'
        else:
            return 'Modelo de piso não encontrado'
        
        return f'Quantidade de caixas: {qtde_cx:.2f}'
        
    def calcular_manta(self):
        area = self.calcular_area()
        if self.modelo_piso == 'Eucafloor':
            return area * 1.1
        elif self.modelo_piso == 'Durafloor':
            return area * 1.2
        elif self.modelo_piso == 'Espaçofloor':
            return area * 1.3
        else:
            return 'Modelo de piso não encontrado'
        
    def calcular_rodape(self):
        area = self.calcular_area()
        if self.modelo_piso == 'Eucafloor':
            return area * 0.2
        elif self.modelo_piso == 'Durafloor':
            return area * 0.3
        elif self.modelo_piso == 'Espaçofloor':
            return area * 0.4
        else:
            return 'Modelo de piso não encontrado'
        
    def calcular_porta(self):
        return self.quantidade_porta * 0.8
    
    def calcular_valor(self):
        area = self.calcular_area()
        if self.modelo_piso == 'carvalho':
            return area * 50
        elif self.modelo_piso == 'ipê':
            return area * 60
        elif self.modelo_piso == 'jacarandá':
            return area * 70
        elif self.modelo_piso == 'peroba':
            return area * 80
        else:
            return 'Modelo de piso não encontrado'

    def __str__(self):
        return f'Cliente: {self.nome_cliente}\nCidade: {self.cidade}\nAmbiente: {self.ambiente}\nLargura: {self.largura}m\nComprimento: {self.comprimento}m\nModelo do piso: {self.modelo_piso}\nÁrea: {self.calcular_area()}m²\nValor: R${self.calcular_valor()}\nQuantidade de portas: {self.quantidade_porta}'

nome_cliente = str(input('Digite o nome do cliente: ')).strip().capitalize()
cidade = str(input('Digite a cidade: ')).strip().capitalize()
ambiente = str(input('Digite o ambiente: ')).strip().capitalize()
largura = float(input('Digite a largura do ambiente em metros: '))
comprimento = float(input('Digite o comprimento do ambiente em metros: '))
modelo_piso = str(input('Digite o modelo do piso: ')).strip().capitalize()
quantidade_porta = int(input('Digite a quantidade de portas: '))

piso = PisoLaminado(nome_cliente, cidade, ambiente, largura, comprimento, modelo_piso, quantidade_porta)
print(piso)
print(piso.calcular_material())
print(f'Quantidade de mantas: {piso.calcular_manta()}')
print(f'Quantidade de rodapés: {piso.calcular_rodape()}')
print(f'Quantidade de portas: {piso.calcular_porta()}')
print(f'Valor total: R${piso.calcular_valor()}')
