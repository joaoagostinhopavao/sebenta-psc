import sys
sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from atividade_modelo import desenhar

# Mesmo esquema do slide_cap04_atividade.py, preenchido com uma situação
# concreta: a comissão que organiza a viagem de finalistas da turma.
CORPO = {
    "Artefactos": ["grupo de WhatsApp com sondagens", "folha de cálculo partilhada"],
    "Sujeito": ["comissão de 4 finalistas"],
    "Objeto": ["organização da viagem"],
    "Comunidade": ["os 40 finalistas da turma"],
    "Regras": ["decisões por votação", "máximo de 350 € por pessoa",
               "quota paga até 15 de março"],
    "Divisao": ["Ana: alojamento · Bruno: transporte",
                "Carla: pagamentos · Duarte: atividades"],
    "Resultado": ["viagem reservada", "e paga"],
}
POS = {
    "Artefactos": (6.7, 5.3), "Sujeito": (1.9, 2.8), "Objeto": (11.5, 2.8),
    "Resultado": (15.3, 2.8),
    "Regras": (1.9, 0.5), "Comunidade": (6.3, 0.5), "Divisao": (11.5, 0.5),
}
desenhar("slide",
         "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap04/slides/teoria-atividade-exemplo-slide.png",
         corpo=CORPO, pos=POS, tam=(24, 19))
print("done")
