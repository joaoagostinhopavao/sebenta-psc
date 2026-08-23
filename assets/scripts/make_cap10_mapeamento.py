import sys
sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from graphviz_utils import render
from sebenta_style import DARK, MAGENTA, PINK, GREY, NOTE_COLOR

FILL = "#f4f0f6"

rows = [
    ("Comunicacao", "COMUNICAÇÃO", "Sistemas autonómicos,\nontologias", MAGENTA, 3.4),
    ("Coordenacao", "COORDENAÇÃO", "Sistemas especialistas,\nmultiagentes, mineração de dados", PINK, 2.1),
    ("Cooperacao", "COOPERAÇÃO", "Sistemas autonómicos,\nagentes inteligentes (robôs)", MAGENTA, 0.8),
]

lines = [
    "digraph G {",
    '  labelloc="t"; fontsize=26; fontname="Helvetica-Bold"; '
    f'fontcolor="{DARK}"; label="Técnicas de IA para o Modelo 3C";',
    '  graph [layout=neato, overlap=false, margin=0.3];',
    '  node [fontname="Helvetica"];',
]

label_w = 260
tech_w = 620

for key, label, tech, color, y in rows:
    label_html = (f'<<TABLE BORDER="0" CELLBORDER="0" CELLPADDING="10" BGCOLOR="{color}" WIDTH="{label_w}">'
                  f'<TR><TD><FONT COLOR="white" POINT-SIZE="15" FACE="Helvetica-Bold"><B>{label}</B></FONT></TD></TR>'
                  f'</TABLE>>')
    lines.append(f'  "{key}" [shape=plaintext, style="", margin="0", fontname="Helvetica", '
                 f'label={label_html}, pos="{1.8 * 72},{y * 72}!"];')

    tech_html = tech.replace("\n", "<BR/>")
    tech_box = (f'<<TABLE BORDER="1" COLOR="{GREY}" CELLBORDER="0" CELLPADDING="10" '
                f'BGCOLOR="{FILL}" WIDTH="{tech_w}">'
                f'<TR><TD><FONT COLOR="{DARK}" POINT-SIZE="13" FACE="Helvetica">{tech_html}</FONT></TD></TR>'
                f'</TABLE>>')
    lines.append(f'  "{key}_tech" [shape=plaintext, style="", margin="0", fontname="Helvetica", '
                 f'label={tech_box}, pos="{7.2 * 72},{y * 72}!"];')
    lines.append(f'  "{key}" -> "{key}_tech" [color="{GREY}", dir="none"];')

lines.append("}")
dot_src = "\n".join(lines)

render(dot_src, "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap10/mapeamento-ia-3c.png",
       dpi=200, target_width_px=2200)
print("done")
