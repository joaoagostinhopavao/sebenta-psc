import sys
sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from graphviz_utils import build_dot, render
from sebenta_style import DARK

nodes = {
    "Produto":      ("Produto", 1.3, 5.8, True, False),
    "Objetivos":    ("Objetivos", 4.0, 5.8, False, False),
    "Negociacao":   ("Negociação", 6.7, 5.8, True, False),
    "Compromisso":  ("Compromisso", 9.5, 5.8, False, False),
    "Atividade":    ("Atividade", 1.3, 3.9, True, False),
    "Grupo":        ("Grupo", 4.0, 3.9, False, False),
    "Crencas":      ("Crenças", 10.1, 3.9, False, False),
    "Participante": ("Participante", 5.9, 2.2, False, True),
    "Tarefas":      ("Tarefas", 1.3, 1.9, True, False),
    "Confianca":    ("Confiança", 10.1, 1.5, False, False),
    "Competencia":  ("Competência", 4.3, 0.3, False, False),
    "Motivacao":    ("Motivação", 6.9, 0.3, False, False),
}

edges = [
    ("Produto", "Objetivos", "É um", False),
    ("Negociacao", "Objetivos", "Define", False),
    ("Negociacao", "Compromisso", "Resulta em", False),
    ("Atividade", "Produto", "Gera", False),
    ("Grupo", "Objetivos", "Tem", False),
    ("Grupo", "Atividade", "Realiza", False),
    ("Participante", "Grupo", "É parte de", True),
    ("Participante", "Objetivos", "Tem", True),
    ("Participante", "Negociacao", "Participa em", True),
    ("Participante", "Compromisso", "Assume", True),
    ("Crencas", "Participante", "É atributo de", True),
    ("Confianca", "Participante", "É atributo de", True),
    ("Participante", "Tarefas", "Assume", True),
    ("Tarefas", "Atividade", "É parte de", False),
    ("Competencia", "Participante", "É atributo de", True),
    ("Participante", "Motivacao", "Tem", True),
]

dot_src = build_dot(nodes, edges)
dot_src = dot_src.replace(
    "digraph G {",
    'digraph G {\n  labelloc="t"; fontsize=26; fontname="Helvetica-Bold"; '
    f'fontcolor="{DARK}"; label="Ontologia sobre Formação de Grupos";'
)

render(dot_src, "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap04/ontologia-grupos.png",
       dpi=200, target_width_px=2200)
print("done")
