import sys
sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from atividade_modelo import desenhar

# Modelo de Atividade de Engeström para o livro (paleta magenta).
# Versão do deck: slide_cap04_atividade.py.
POS = {
    "Artefactos": (4.7, 4.6), "Sujeito": (1.3, 2.5), "Objeto": (8.1, 2.5),
    "Resultado": (10.2, 2.5),
    "Regras": (1.3, 0.4), "Comunidade": (4.7, 0.4), "Divisao": (8.1, 0.4),
}
desenhar("livro", "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap04/teoria-atividade.png",
         lang="pt", pos=POS, tam=(17, 14))
desenhar("livro", "/Users/jpavao/QProjects/Sebenta-PSC/en/assets/images/cap04/teoria-atividade.png",
         lang="en", pos=POS, tam=(17, 14))
print("done")
