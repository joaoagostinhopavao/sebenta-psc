import sys
sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from graphviz_utils import render
from sebenta_style import DARK, MAGENTA, PINK, GREY, NOTE_COLOR

FILL = "#f4f0f6"

blocks = {
    "Avatares": ("Avatares", "Objetos que<BR/>representam cada<BR/>participante", 2.2, 3.4, MAGENTA),
    "Interatividade": ("Interatividade", "O mundo responde<BR/>às ações dos<BR/>utilizadores", 8.8, 3.4, PINK),
}

lines = [
    "digraph G {",
    '  labelloc="t"; fontsize=26; fontname="Helvetica-Bold"; '
    f'fontcolor="{DARK}"; label="Elementos de um CVE";',
    '  graph [layout=neato, overlap=false, margin=0.3];',
    '  node [shape=plaintext, fontname="Helvetica"];',
]

for name, (title, sub, x, y, color) in blocks.items():
    html = (f'<<TABLE BORDER="2" COLOR="{color}" CELLBORDER="0" '
            f'CELLPADDING="12" BGCOLOR="{FILL}">'
            f'<TR><TD><FONT COLOR="{DARK}" POINT-SIZE="18"><B>{title}</B></FONT></TD></TR>'
            f'<TR><TD><FONT COLOR="{color}" POINT-SIZE="13">{sub}</FONT></TD></TR>'
            f'</TABLE>>')
    lines.append(f'  "{name}" [label={html}, pos="{x * 72},{y * 72}!"];')
    lines.append(f'  "{name}" -> "Mundo" [color="{GREY}", dir="both", arrowsize=0.7];')

lines.append(f'  "Mundo" [label=<<FONT COLOR="white" POINT-SIZE="17"><B>Mundo<BR/>Virtual</B></FONT>>, '
             f'shape=circle, style=filled, fillcolor="{DARK}", fixedsize=true, width=1.3, '
             f'pos="{5.5 * 72},{3.4 * 72}!"];')

lines.append("}")
dot_src = "\n".join(lines)

render(dot_src, "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap06/elementos-cve.png",
       dpi=200, target_width_px=2200)
print("done")
