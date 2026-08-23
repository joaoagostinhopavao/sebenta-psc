import sys
sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from graphviz_utils import build_dot, render
from sebenta_style import DARK

nodes = {
    "DistribGeoEx":      ("Co-localizado\nRemoto", 0.4, 6.6, False, False, True),
    "DistribGeo":        ("Distribuição\nGeográfica", 2.4, 6.0, False, False),
    "Grupo":             ("Grupo", 5.4, 6.0, True, False),
    "SistemaColab":      ("Sistema\nColaborativo", 9.2, 6.0, False, False),

    "Acoplamento":       ("Acoplamento", 0.9, 4.2, True, False),
    "Atividade":         ("Atividade", 2.9, 4.2, False, True),
    "EspacoCompart":     ("Espaço\nCompartilhado", 9.2, 4.2, False, False),

    "Participante":      ("Participante", 0.9, 2.6, True, False),
    "Objetivo":          ("Objetivo", 5.0, 2.6, True, False),
    "Produto":           ("Produto", 6.8, 2.6, False, False),

    "Prazo":             ("Prazo", 0.9, 1.0, True, False),
    "Tarefa":            ("Tarefa", 2.9, 1.0, False, False),
    "Artefato":          ("Artefato", 6.8, 1.0, False, False),

    "Status":            ("Status\n(completude)", 0.9, -0.6, True, False),
    "CompartilhamentoEx": ("Individual\nCompartilhado", 2.9, -2.1, False, False, True),
    "Compartilhamento":  ("Compartilhamento", 2.9, -0.6, False, False),
    "Recurso":           ("Recurso", 6.8, -0.6, False, False),
    "RecursoEx":         ("Quadro Negro\nNotas\nTelefone\nPapel\nLápis", 6.8, -2.2, False, False, True),
}

edges = [
    ("DistribGeoEx", "DistribGeo", "É um", False),
    ("DistribGeo", "Atividade", "É atributo de", True),
    ("Grupo", "Atividade", "Realiza", True),
    ("Grupo", "EspacoCompart", "Interage através de", False),
    ("SistemaColab", "EspacoCompart", "É um", False),
    ("Acoplamento", "Atividade", "É atributo de", True),
    ("Atividade", "EspacoCompart", "É realizada em", True),
    ("Atividade", "Produto", "Gera", True),
    ("Produto", "Objetivo", "É um", False),
    ("Produto", "EspacoCompart", "É produzido em", False),
    ("Artefato", "Produto", "É parte de", False),
    ("Participante", "Tarefa", "Realiza", False),
    ("Prazo", "Tarefa", "É atributo de", False),
    ("Status", "Tarefa", "É atributo de", False),
    ("CompartilhamentoEx", "Compartilhamento", "É um", False),
    ("Compartilhamento", "Tarefa", "É atributo de", False),
    ("Tarefa", "Atividade", "É parte de", True),
    ("Tarefa", "Artefato", "Gera", False),
    ("Tarefa", "Recurso", "Requer", False),
    ("RecursoEx", "Recurso", "É um", False),
    ("Recurso", "EspacoCompart", "É parte de", False),
]

dot_src = build_dot(nodes, edges)
dot_src = dot_src.replace(
    "digraph G {",
    'digraph G {\n  labelloc="t"; fontsize=26; fontname="Helvetica-Bold"; '
    f'fontcolor="{DARK}"; label="Ontologia sobre Cooperação";'
)

render(dot_src, "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap04/ontologia-cooperacao.png",
       dpi=200, target_width_px=2200)
print("done")
