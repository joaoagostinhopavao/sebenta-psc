import sys
sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from graphviz_utils import render
from sebenta_style import DARK, MAGENTA, PINK, GREY, NOTE_COLOR

levels = [
    ("n1", "1", "Prestação de\nServiços", PINK),
    ("n2", "2", "Coleta de\nOpinião Pública", "#c25aa8"),
    ("n3", "3", "Prestação de\nContas", "#a3399a"),
    ("n4", "4", "Democracia\nDeliberativa", MAGENTA),
    ("n5", "5", "Democracia\nDireta", DARK),
]

lines = [
    "digraph G {",
    '  labelloc="t"; fontsize=26; fontname="Helvetica-Bold"; '
    f'fontcolor="{DARK}"; label="Níveis de Participação Democrática";',
    '  graph [layout=neato, overlap=false, margin=0.3];',
    '  node [shape=plaintext, fontname="Helvetica"];',
]

x = 5.5
y0 = 0.7
step = 1.15
widths = [520, 450, 380, 310, 240]

for i, ((key, num, label, color), w) in enumerate(zip(levels, widths)):
    y = y0 + i * step
    label_html = label.replace("\n", "<BR/>")
    html = (f'<<TABLE BORDER="0" CELLBORDER="0" CELLPADDING="8" BGCOLOR="{color}" WIDTH="{w}">'
            f'<TR><TD WIDTH="30"><FONT COLOR="white" POINT-SIZE="16"><B>{num}</B></FONT></TD>'
            f'<TD><FONT COLOR="white" POINT-SIZE="14"><B>{label_html}</B></FONT></TD></TR>'
            f'</TABLE>>')
    lines.append(f'  "{key}" [shape=plaintext, style="", margin="0", label={html}, '
                 f'pos="{x * 72},{y * 72}!"];')
    if i > 0:
        prev_key = levels[i - 1][0]
        lines.append(f'  "{prev_key}" -> "{key}" [color="{GREY}", arrowsize=0.6];')

lines.append("}")
dot_src = "\n".join(lines)

render(dot_src, "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap07/niveis-participacao.png",
       dpi=200, target_width_px=2200)
print("done")
