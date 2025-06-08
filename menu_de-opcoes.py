from InquirerPy import prompt

pergunta = [
{
"type": "list",
"message": "Qual seu conhecimento em Python?",
"choices": ["Iniciante", "Intermediário", "Avançado"],
}
]    

resultado = prompt(pergunta)