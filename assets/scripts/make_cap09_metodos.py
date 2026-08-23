import sys
sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from graphviz_utils import render
from sebenta_style import DARK, MAGENTA, PINK, GREY, NOTE_COLOR

blocks = [
    ("Jigsaw", "JIGSAW", "Cada um estuda uma\nparte e ensina\nos colegas", 2.0, 3.0, MAGENTA),
    ("Controversia", "CONTROVÉRSIA\nACADÉMICA", "Pares defendem\nposições opostas,\ndepois sintetizam", 6.67, 3.0, PINK),
    ("Investigacao", "INVESTIGAÇÃO\nEM GRUPO", "O grupo investiga\nautonomamente um\ntema comum", 11.3, 3.0, MAGENTA),
]

lines = [
    "digraph G {",
    '  labelloc="t"; fontsize=26; fontname="Helvetica-Bold"; '
    f'fontcolor="{DARK}"; label="Métodos de Aprendizagem Colaborativa";',
    '  graph [layout=neato, overlap=false, margin=0.3];',
    '  node [fontname="Helvetica"];',
]

for name, title, desc, x, y, color in blocks:
    title_html = title.replace("\n", "<BR/>")
    desc_html = desc.replace("\n", "<BR/>")
    html = (f'<<TABLE BORDER="0" CELLBORDER="0" CELLPADDING="10" BGCOLOR="{color}">'
            f'<TR><TD><FONT COLOR="white" POINT-SIZE="15" FACE="Helvetica-Bold"><B>{title_html}</B></FONT></TD></TR>'
            f'<TR><TD><FONT COLOR="white" POINT-SIZE="12" FACE="Helvetica">{desc_html}</FONT></TD></TR>'
            f'</TABLE>>')
    lines.append(f'  "{name}" [shape=plaintext, style="", margin="0", fontname="Helvetica", '
                 f'label={html}, pos="{x * 72},{y * 72}!"];')

lines.append("}")
dot_src = "\n".join(lines)

render(dot_src, "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap09/metodos-aprendizagem.png",
       dpi=200, target_width_px=2200)
print("done")
