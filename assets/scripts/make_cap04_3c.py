import sys
sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from graphviz_utils import render
from sebenta_style import DARK, MAGENTA, PINK, GREY, NOTE_COLOR

nodes = {
    "Comunicacao":  ("COMUNICAÇÃO", 5.5, 5.0, MAGENTA),
    "Cooperacao":   ("COOPERAÇÃO", 2.0, 1.2, PINK),
    "Coordenacao":  ("COORDENAÇÃO", 9.0, 1.2, DARK),
}

lines = [
    "digraph G {",
    '  labelloc="t"; fontsize=26; fontname="Helvetica-Bold"; '
    f'fontcolor="{DARK}"; label="Modelo 3C de Colaboração";',
    '  graph [layout=neato, overlap=false, margin=0.25];',
    '  node [fontname="Helvetica-Bold", fontcolor=white, style=filled, '
    'shape=box, margin="0.28,0.16"];',
]

for name, (label, x, y, color) in nodes.items():
    lines.append(f'  "{name}" [label="{label}", pos="{x * 72},{y * 72}!", '
                  f'fillcolor="{color}", color="{color}"];')

lines.append(f'  "Colabo" [label="COLABO-\\nRAÇÃO", pos="{5.5 * 72},{2.5 * 72}!", '
             f'shape=circle, fixedsize=true, width=1.0, style=filled, '
             f'fillcolor="#f4f0f6", color="{GREY}", fontcolor="{DARK}", '
             f'fontname="Helvetica-Bold", fontsize=13];')

edges = [
    ("Comunicacao", "Cooperacao", "negoceiam compromissos"),
    ("Comunicacao", "Coordenacao", "demanda reorganização"),
    ("Cooperacao", "Coordenacao", "organiza tarefas e recursos"),
]
for a, b, label in edges:
    lines.append(
        f'  "{a}" -> "{b}" [dir="both", color="{GREY}", label="{label}", '
        f'fontsize=12.5, fontcolor="{NOTE_COLOR}", fontname="Helvetica"];'
    )

lines.append("}")
dot_src = "\n".join(lines)

render(dot_src, "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap04/modelo-3c.png",
       dpi=200, target_width_px=2200)
print("done")
