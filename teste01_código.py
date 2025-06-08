def saudar(detalhes):
    match detalhes:
        case [horario, nome]:
            return f"Bom {horario} {nome}!"
        
        case [horario, *nomes]:
            mensagem = ""

            for nome_atual in nomes:
                mensagem += f"Bom {horario} {nome_atual}!\n"
            return mensagem


print(saudar(["Dia", "Pedro"]))
print(saudar(["Tarde", "Convidado"]))
print(saudar(["Noite", "Ana", "Bruno", "Carla"]))
