import sys
sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from graphviz_utils import render
from sebenta_style import DARK, MAGENTA, PINK, GREY, NOTE_COLOR

FILL = "#f4f0f6"

blocks = [
    ("Identidade", "IDENTIDADE", "O avatar é\nreconhecível e\ndistinguível", 2.0, 4.6, MAGENTA),
    ("Interacao", "INTERAÇÃO", "O avatar\nfornece pistas\nde perceção", 6.67, 6.4, PINK),
    ("Presenca", "PRESENÇA", "Sensação\nilusória de\nnão mediação", 11.3, 4.6, MAGENTA),
]

lines = [
    "digraph G {",
    '  labelloc="t"; fontsize=26; fontname="Helvetica-Bold"; '
    f'fontcolor="{DARK}"; label="Identidade, Interação e Presença";',
    '  graph [layout=neato, overlap=false, margin=0.3];',
    '  node [fontname="Helvetica-Bold", fontcolor=white, style=filled, '
    'shape=box, margin="0.28,0.18"];',
]

for name, title, desc, x, y, color in blocks:
    desc_html = desc.replace("\n", "<BR/>")
    html = (f'<<TABLE BORDER="0" CELLBORDER="0" CELLPADDING="6" BGCOLOR="{color}">'
            f'<TR><TD><FONT COLOR="white" POINT-SIZE="16"><B>{title}</B></FONT></TD></TR>'
            f'<TR><TD><FONT COLOR="white" POINT-SIZE="12">{desc_html}</FONT></TD></TR>'
            f'</TABLE>>')
    lines.append(f'  "{name}" [shape=plaintext, style="", margin="0", '
                 f'label={html}, pos="{x * 72},{y * 72}!"];')
    lines.append(f'  "{name}" -> "Avatar" [color="{GREY}", dir="none"];')

lines.append(f'  "Avatar" [label=<<FONT COLOR="white" POINT-SIZE="15"><B>AVATAR<BR/>NO CVE</B></FONT>>, '
             f'shape=circle, style=filled, fillcolor="{DARK}", fixedsize=true, width=1.15, '
             f'pos="{6.67 * 72},{4.0 * 72}!"];')

lines.append("}")
dot_src = "\n".join(lines)

render(dot_src, "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap06/identidade-interacao-presenca.png",
       dpi=200, target_width_px=2200)
print("done")
