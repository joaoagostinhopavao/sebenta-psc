import sys
sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from atividade_modelo import desenhar

# Versão para o livro do exemplo da viagem de finalistas (Modelo de
# Atividade preenchido). O slide usa a paleta verde do deck:
# slide_cap04_atividade_exemplo.py. Uso: make_cap04_atividade_exemplo.py [pt|en]
LANG = sys.argv[1] if len(sys.argv) > 1 else "pt"

CORPO = {
    "pt": {
        "Artefactos": ["grupo de WhatsApp com sondagens", "folha de cálculo partilhada"],
        "Sujeito": ["comissão de 4 finalistas"],
        "Objeto": ["organização da viagem"],
        "Comunidade": ["os 40 finalistas da turma"],
        "Regras": ["decisões por votação", "máximo de 350 € por pessoa",
                   "quota paga até 15 de março"],
        "Divisao": ["Ana: alojamento · Bruno: transporte",
                    "Carla: pagamentos · Duarte: atividades"],
        "Resultado": ["viagem reservada", "e paga"],
    },
    "en": {
        "Artefactos": ["WhatsApp group with polls", "shared spreadsheet"],
        "Sujeito": ["committee of 4", "final-year students"],
        "Objeto": ["organising the trip"],
        "Comunidade": ["the 40 final-year students"],
        "Regras": ["decisions by vote", "at most €350 per person",
                   "fee paid by 15 March"],
        "Divisao": ["Ana: accommodation · Bruno: transport",
                    "Carla: payments · Duarte: activities"],
        "Resultado": ["trip booked", "and paid for"],
    },
}[LANG]

POS = {
    "Artefactos": (5.3, 4.9), "Sujeito": (1.6, 2.7), "Objeto": (9.0, 2.7),
    "Resultado": (11.9, 2.7),
    "Regras": (1.6, 0.5), "Comunidade": (5.3, 0.5), "Divisao": (9.0, 0.5),
}
SAIDA = {"pt": "assets/images/cap04/teoria-atividade-exemplo.png",
         "en": "en/assets/images/cap04/teoria-atividade-exemplo.png"}[LANG]
desenhar("livro", "/Users/jpavao/QProjects/Sebenta-PSC/" + SAIDA, lang=LANG,
         corpo=CORPO, pos=POS, tam=(16, 13))
print("done", LANG)
