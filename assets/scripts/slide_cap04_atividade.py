import sys
sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from atividade_modelo import desenhar

# Modelo de Atividade de Engeström para o deck da Aula 5 (paleta verde,
# slide "Como se Realiza uma Atividade Mediada?"). Versão do livro:
# make_cap04_atividade.py. Troca no deck: deck_aula5_atividade.py.
POS = {
    "Artefactos": (4.7, 5.0), "Sujeito": (1.3, 2.7), "Objeto": (8.1, 2.7),
    "Resultado": (10.4, 2.7),
    "Regras": (1.3, 0.4), "Comunidade": (4.7, 0.4), "Divisao": (8.1, 0.4),
}
desenhar("slide",
         "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap04/slides/teoria-atividade-slide.png",
         pos=POS, tam=(26, 20))
print("done")
