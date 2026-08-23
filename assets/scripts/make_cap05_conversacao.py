import sys
sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from graphviz_utils import render
from sebenta_style import DARK, MAGENTA, PINK, GREY, NOTE_COLOR

nodes = {
    "1": ("1", 0.8, 2.0, False),
    "2": ("2", 3.0, 2.0, False),
    "3": ("3", 5.4, 2.0, False),
    "4": ("4", 7.8, 2.0, False),
    "5": ("5", 10.0, 2.0, True),
    "6": ("Rejeitado", 3.0, 0.2, False),
}

lines = [
    "digraph G {",
    '  labelloc="t"; fontsize=26; fontname="Helvetica-Bold"; '
    f'fontcolor="{DARK}"; label="A Conversação para Ação";',
    '  graph [layout=neato, overlap=false, margin="0.3,0.3"];',
    '  node [shape=circle, fontsize=17, fontname="Helvetica-Bold", '
    'fixedsize=true, width=0.7];',
]

for name, (label, x, y, hi) in nodes.items():
    if hi:
        attrs = f'style="filled", fillcolor="{DARK}", fontcolor="white", color="{DARK}"'
    else:
        attrs = f'style="filled", fillcolor="#f4f0f6", fontcolor="{DARK}", color="{GREY}"'
    shape = "shape=box, fixedsize=false, width=0" if name == "6" else ""
    lines.append(f'  "{name}" [label="{label}", pos="{x * 72},{y * 72}!", {attrs}, {shape}];')

edges = [
    ("1", "2", "Solicita", True),
    ("2", "3", "Promete", True),
    ("3", "4", "Afirma", True),
    ("4", "5", "Declara", True),
    ("2", "6", "Rejeita", False),
]
for a, b, label, accent in edges:
    color = MAGENTA if accent else GREY
    lines.append(
        f'  "{a}" -> "{b}" [label="{label}", color="{color}", '
        f'fontcolor="{NOTE_COLOR}", fontsize=18, fontname="Helvetica"];'
    )

lines.append(f'  "Inicio" [shape=plaintext, label="Início", fontcolor="{NOTE_COLOR}", '
             f'fontsize=18, pos="{0.8*72},{2.9*72}!"];')
lines.append(f'  "Fim" [shape=plaintext, label="Concluído", fontcolor="{NOTE_COLOR}", '
             f'fontsize=18, pos="{9.3*72},{2.9*72}!"];')

lines.append("}")
dot_src = "\n".join(lines)

render(dot_src, "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap05/conversacao-acao.png",
       dpi=200, target_width_px=2200)
print("done")
