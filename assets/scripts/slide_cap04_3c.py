import sys
sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from graphviz_utils import render
from sebenta_style import DARK, MAGENTA, PINK, GREY, NOTE_COLOR

nodes = {
    "Comunicacao":  ("COMUNICAÇÃO", 6.67, 5.0, MAGENTA),
    "Cooperacao":   ("COOPERAÇÃO", 2.3, 1.2, PINK),
    "Coordenacao":  ("COORDENAÇÃO", 11.0, 1.2, DARK),
}

lines = [
    "digraph G {",
    '  labelloc="t"; fontsize=30; fontname="Helvetica-Bold"; '
    f'fontcolor="{DARK}"; label="Modelo 3C de Colaboração";',
    '  graph [layout=neato, overlap=false, margin=0.3];',
    '  node [fontname="Helvetica-Bold", fontcolor=white, style=filled, '
    'shape=box, margin="0.32,0.2", fontsize=17];',
]

for name, (label, x, y, color) in nodes.items():
    lines.append(f'  "{name}" [label="{label}", pos="{x * 72},{y * 72}!", '
                  f'fillcolor="{color}", color="{color}"];')

lines.append(f'  "Colabo" [label="COLABO-\\nRAÇÃO", pos="{6.67 * 72},{2.5 * 72}!", '
             f'shape=circle, fixedsize=true, width=1.15, style=filled, '
             f'fillcolor="#f4f0f6", color="{GREY}", fontcolor="{DARK}", '
             f'fontname="Helvetica-Bold", fontsize=15];')

edges = [
    ("Comunicacao", "Cooperacao", "negoceiam compromissos"),
    ("Comunicacao", "Coordenacao", "demanda reorganização"),
    ("Cooperacao", "Coordenacao", "organiza tarefas e recursos"),
]
for a, b, label in edges:
    lines.append(
        f'  "{a}" -> "{b}" [dir="both", color="{GREY}", label="{label}", '
        f'fontsize=14, fontcolor="{NOTE_COLOR}", fontname="Helvetica"];'
    )

lines.append("}")
dot_src = "\n".join(lines)

render(dot_src, "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap04/slides/modelo-3c-slide.png",
       dpi=200, target_width_px=2666)
print("done")
