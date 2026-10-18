import sys
sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from graphviz_utils import build_dot, render
from sebenta_style import DARK

nodes = {
    "Participante":     ("Participante", 5.2, 6.8, True, False),
    "AcoplamentoEx":     ("Individual\nPassagem de tarefas\nOrquestrado", 8.8, 6.3, False, False, True),

    "SistemaColab":      ("Sistema\nColaborativo", 1.3, 5.2, False, False),
    "Negociacao":        ("Negociação", 3.5, 5.2, True, False),
    "Papel":             ("Papel", 5.2, 5.2, False, False),
    "Acoplamento":       ("Acoplamento", 7.7, 5.2, True, False),

    "PoliticaEx":        ("Acesso a recursos\nControlo de concorrência\nVersionamento\nPrivacidade\nSegurança",
                           0.9, 3.5, False, False, True),
    "PlanoTrabalho":     ("Plano de\nTrabalho", 4.7, 3.3, False, True),
    "Atividade":         ("Atividade", 7.7, 3.3, True, False),

    "Politica":          ("Política", 1.3, 1.6, False, False),
    "Prazo":             ("Prazo", 4.0, 1.6, False, False),
    "Recurso":           ("Recurso", 7.7, 1.6, True, False),

    "Acompanhamento":    ("Acompanhamento", 1.3, 0.0, False, False),
    "Status":            ("Estado\n(completude)", 4.0, 0.0, False, False),
    "Tarefa":            ("Tarefa", 7.7, 0.0, True, False),
}

edges = [
    ("SistemaColab", "PlanoTrabalho", "Apoia", False),
    ("Negociacao", "PlanoTrabalho", "Estabelece", False),
    ("PlanoTrabalho", "Papel", "Define", True),
    ("PlanoTrabalho", "Acoplamento", "Define", True),
    ("Participante", "Papel", "Executa", False),
    ("AcoplamentoEx", "Acoplamento", "É um", False),
    ("Acoplamento", "Atividade", "É atributo de", False),
    ("Papel", "Tarefa", "É responsável por", False),
    ("PlanoTrabalho", "Atividade", "Organiza", True),
    ("PoliticaEx", "Politica", "É um", False),
    ("PlanoTrabalho", "Politica", "Define", True),
    ("PlanoTrabalho", "Prazo", "Define", True),
    ("PlanoTrabalho", "Recurso", "Aloca", True),
    ("PlanoTrabalho", "Tarefa", "Define", True),
    ("Acompanhamento", "Prazo", "Controla", False),
    ("Acompanhamento", "Status", "Controla", False),
    ("Prazo", "Tarefa", "É atributo de", False),
    ("Status", "Tarefa", "É atributo de", False),
    ("Tarefa", "Recurso", "Requer", False),
    ("Acompanhamento", "PlanoTrabalho", "Segue", True),
]

dot_src = build_dot(nodes, edges)
# o rótulo de Papel -> Tarefa passa para a direita do Papel, onde a linha começa
# (a meio da aresta confundia-se com as ligações do Plano de Trabalho)
import re
m = re.search(r'label="É responsável por", color="([^"]+)", fontcolor="([^"]+)"', dot_src)
dot_src = dot_src.replace(m.group(0), f'label="", color="{m.group(1)}"')
x1, y1 = map(float, re.search(r'"Papel" \[label="Papel", pos="([-\d.]+),([-\d.]+)!"', dot_src).groups())
x2, y2 = map(float, re.search(r'"Tarefa" \[label="Tarefa", pos="([-\d.]+),([-\d.]+)!"', dot_src).groups())
import graphviz_utils as _gu
dx, dy = (94, -4) if getattr(_gu, "SLIDE", False) else (70, -26)  # slide: à direita; livro: abaixo
lx, ly = x1 + dx, y1 + dy
k = dot_src.rindex("}")
dot_src = (dot_src[:k] + '  "RotuloResp" [shape=plaintext, style="", label="É responsável por", '
           f'fontsize=11.5 /*resp*/, fontname="Helvetica", fontcolor="{m.group(2)}", '
           f'pos="{lx},{ly}!"];\n' + dot_src[k:])
dot_src = dot_src.replace(
    "digraph G {",
    'digraph G {\n  labelloc="t"; fontsize=26; fontname="Helvetica-Bold"; '
    f'fontcolor="{DARK}"; label="Ontologia sobre Coordenação";'
)

render(dot_src, "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap04/ontologia-coordenacao.png",
       dpi=200, target_width_px=2200)
print("done")
