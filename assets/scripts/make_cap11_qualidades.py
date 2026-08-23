import sys
sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from graphviz_utils import render
from sebenta_style import DARK, MAGENTA, PINK, GREY, NOTE_COLOR

FILL = "#f4f0f6"

blocks = [
    ("Usabilidade", "USABILIDADE", "Fácil, eficiente e\nagradável de usar", 2.2, 5.15, MAGENTA),
    ("Sociabilidade", "SOCIABILIDADE", "Densidade das relações\nsociais no grupo", 8.8, 5.15, PINK),
    ("Comunicabilidade", "COMUNICABILIDADE", "Transmite as decisões\ndo projetista", 2.2, 1.1, DARK),
    ("Acessibilidade", "ACESSIBILIDADE", "Uso independente das\ncapacidades da pessoa", 8.8, 1.1, MAGENTA),
]

lines = [
    "digraph G {",
    '  labelloc="t"; fontsize=26; fontname="Helvetica-Bold"; '
    f'fontcolor="{DARK}"; label="Qualidades de Uso";',
    '  graph [layout=neato, overlap=false, margin=0.3];',
    '  node [fontname="Helvetica"];',
]

for name, title, desc, x, y, color in blocks:
    desc_html = desc.replace("\n", "<BR/>")
    html = (f'<<TABLE BORDER="2" COLOR="{color}" CELLBORDER="0" CELLPADDING="10" BGCOLOR="{FILL}">'
            f'<TR><TD><FONT COLOR="{DARK}" POINT-SIZE="16" FACE="Helvetica-Bold"><B>{title}</B></FONT></TD></TR>'
            f'<TR><TD><FONT COLOR="{color}" POINT-SIZE="12" FACE="Helvetica">{desc_html}</FONT></TD></TR>'
            f'</TABLE>>')
    lines.append(f'  "{name}" [shape=plaintext, style="", margin="0", fontname="Helvetica", '
                 f'label={html}, pos="{x * 72},{y * 72}!"];')
    lines.append(f'  "{name}" -> "Sistema" [color="{GREY}", dir="none"];')

lines.append(f'  "Sistema" [label=<<FONT COLOR="white" POINT-SIZE="12"><B>SISTEMA<BR/>COLABORATIVO</B></FONT>>, '
             f'shape=circle, style=filled, fillcolor="{DARK}", fixedsize=true, width=1.6, '
             f'pos="{5.5 * 72},{3.1 * 72}!"];')

lines.append("}")
dot_src = "\n".join(lines)

render(dot_src, "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap11/qualidades-uso.png",
       dpi=200, target_width_px=2200)
print("done")
