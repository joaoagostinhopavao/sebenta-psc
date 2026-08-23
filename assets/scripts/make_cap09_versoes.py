import sys
sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from graphviz_utils import render
from sebenta_style import DARK, MAGENTA, PINK, GREY, NOTE_COLOR

lines = [
    "digraph G {",
    '  labelloc="t"; fontsize=26; fontname="Helvetica-Bold"; '
    f'fontcolor="{DARK}"; label="As Três Versões de um Episódio";',
    '  graph [layout=neato, overlap=false, margin=0.3];',
    '  node [fontname="Helvetica", fontsize=15];',
]

nodes = [
    ("real", "Versão\nReal", 1.2, 2.2, "dashed", GREY, DARK),
    ("conhecida", "Versão\nConhecida", 5.5, 2.2, "filled", "#f4f0f6", DARK),
    ("relatada", "Versão\nRelatada", 9.8, 2.2, "filled", MAGENTA, "white"),
]

for key, label, x, y, style, fill, fontcolor in nodes:
    label_dot = label.replace("\n", "\\n")
    style_str = f"{style},rounded" if "rounded" not in style else style
    lines.append(f'  "{key}" [shape=box, style="rounded,{style}", fillcolor="{fill}", '
                 f'fontcolor="{fontcolor}", color="{GREY}", label="{label_dot}", '
                 f'fontname="Helvetica", width=2.0, height=0.9, fixedsize=true, '
                 f'pos="{x * 72},{y * 72}!"];')

lines.append(f'  "real" -> "conhecida" [color="{GREY}", fontcolor="{NOTE_COLOR}", '
             f'fontsize=12, fontname="Helvetica", label="testemunha"];')
lines.append(f'  "conhecida" -> "relatada" [color="{MAGENTA}", fontcolor="{NOTE_COLOR}", '
             f'fontsize=12, fontname="Helvetica", label="relata\\n(com perdas)"];')
lines.append(f'  "relatada" -> "real" [color="{GREY}", style="dashed", fontcolor="{NOTE_COLOR}", '
             f'fontsize=11, fontname="Helvetica", label="aproxima-se, nunca coincide", '
             f'headport=s, tailport=s];')

lines.append("}")
dot_src = "\n".join(lines)

render(dot_src, "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap09/versoes-conhecimento.png",
       dpi=200, target_width_px=2200)
print("done")
