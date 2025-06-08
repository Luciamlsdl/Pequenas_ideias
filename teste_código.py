def saudar(detalhes):
   # Compare a lista 'detalhes' com os padrões abaixo:
   match detalhes:
      # CASO 1: Se a lista tiver EXATAMENTE dois elementos.
      # O primeiro elemento é o 'horario', o segundo é o 'nome'.
      case [horario, nome]:
         # Retorne uma saudação única.
         return f'Bom {horario} {nome}!'

      # CASO 2: Se a lista tiver DOIS OU MAIS elementos.
      # O primeiro elemento é o 'horario'.
      # O '*' significa que TODOS os elementos restantes (depois do primeiro)
      # serão coletados em uma nova lista chamada 'nomes'.
      case [horario, *nomes]:
         mensagem = '' # Inicialize uma string vazia para a mensagem.
         # Para cada 'nome' na lista de 'nomes':
         for nome_atual in nomes:
            # Adicione uma saudação para o 'nome_atual' à mensagem, seguida de uma nova linha.
            mensagem += f'Bom {horario} {nome_atual}!\n'
         return mensagem # Retorne a mensagem completa com todas as saudações.

# Exemplos de uso da função 'saudar':
print(saudar(["Dia", "Pedro"]))
# Saída esperada: Bom Dia Pedro!

print(saudar(["Tarde","Convidado"]))
# Saída esperada: Bom Tarde Convidado!

print(saudar(["Noite", "Ana", "Bruno", "Carla"]))
# Saída esperada:
# Bom Noite Ana!
# Bom Noite Bruno!
# Bom Noite Carla!