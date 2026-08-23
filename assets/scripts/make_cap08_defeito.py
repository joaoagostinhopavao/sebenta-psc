import sys
sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from graphviz_utils import render
from sebenta_style import DARK, MAGENTA, PINK, GREY, NOTE_COLOR

lines = [
    "digraph G {",
    '  labelloc="t"; fontsize=26; fontname="Helvetica-Bold"; '
    f'fontcolor="{DARK}"; label="Ciclo de Vida de um Defeito";',
    '  graph [layout=neato, overlap=false, margin=0.3];',
    '  node [fontname="Helvetica", fontsize=14];',
]

nodes = [
    ("registo", "box", "Registo\ndo Defeito", 1.2, 3.0, "#f4f0f6", DARK),
    ("correcao", "box", "Correção\ndo Defeito", 4.4, 3.0, "#f4f0f6", DARK),
    ("verificacao", "box", "Verificação\nda Correção", 7.6, 3.0, "#f4f0f6", DARK),
    ("decisao", "diamond", "Defeito\nresolvido?", 7.6, 0.9, "#fbeaf7", MAGENTA),
    ("fim", "box", "Fim", 10.6, 0.9, DARK, "white"),
]

for key, shape, label, x, y, fill, fontcolor in nodes:
    label_dot = label.replace("\n", "\\n")
    style = "filled,rounded" if shape == "box" else "filled"
    lines.append(f'  "{key}" [shape={shape}, style="{style}", fillcolor="{fill}", '
                 f'fontcolor="{fontcolor}", color="{GREY}", label="{label_dot}", '
                 f'fontname="Helvetica", pos="{x * 72},{y * 72}!"];')

edges = [
    ("registo", "correcao", "atribui", MAGENTA),
    ("correcao", "verificacao", "envia para teste", MAGENTA),
    ("verificacao", "decisao", "", GREY),
]
for a, b, label, color in edges:
    lines.append(f'  "{a}" -> "{b}" [color="{color}", fontcolor="{NOTE_COLOR}", '
                 f'fontsize=12, fontname="Helvetica", label="{label}"];')

lines.append(f'  "decisao" -> "fim" [color="{MAGENTA}", fontcolor="{NOTE_COLOR}", '
             f'fontsize=12, fontname="Helvetica", label="sim"];')
lines.append(f'  "decisao" -> "correcao" [color="{GREY}", fontcolor="{NOTE_COLOR}", '
             f'fontsize=12, fontname="Helvetica", label="não, reabre", '
             f'headport=s, tailport=w];')

lines.append("}")
dot_src = "\n".join(lines)

render(dot_src, "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap08/ciclo-defeito.png",
       dpi=200, target_width_px=2200)
print("done")
