import sys
sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from graphviz_utils import render
from sebenta_style import DARK, MAGENTA, PINK, GREY

FILL = "#f4f0f6"

blocks = {
    "Formacao":     ("Formação de Grupos", "Participante", 2.6, 5.15, MAGENTA),
    "Comunicacao":  ("Comunicação", "Mensagem", 10.7, 5.15, PINK),
    "Coordenacao":  ("Coordenação", "Plano de Trabalho", 2.6, 1.1, DARK),
    "Cooperacao":   ("Cooperação", "Atividade", 10.7, 1.1, MAGENTA),
}

lines = [
    "digraph G {",
    '  labelloc="t"; fontsize=30; fontname="Helvetica-Bold"; '
    f'fontcolor="{DARK}"; label="Ontologia de Colaboração";',
    '  graph [layout=neato, overlap=false, margin=0.3];',
    '  node [shape=plaintext, fontname="Helvetica"];',
]

for name, (title, sub, x, y, color) in blocks.items():
    html = (f'<<TABLE BORDER="2" COLOR="{color}" CELLBORDER="0" '
            f'CELLPADDING="12" BGCOLOR="{FILL}">'
            f'<TR><TD><FONT COLOR="{DARK}" POINT-SIZE="19"><B>{title}</B></FONT></TD></TR>'
            f'<TR><TD><FONT COLOR="{color}" POINT-SIZE="15"><I>{sub}</I></FONT></TD></TR>'
            f'</TABLE>>')
    lines.append(f'  "{name}" [label={html}, pos="{x * 72},{y * 72}!"];')
    lines.append(f'  "{name}" -> "Colabo" [color="{GREY}", dir="none"];')

lines.append(f'  "Colabo" [label=<<FONT COLOR="white" POINT-SIZE="17"><B>COLABO-<BR/>RAÇÃO</B></FONT>>, '
             f'shape=circle, style=filled, fillcolor="{DARK}", fixedsize=true, width=1.2, '
             f'pos="{6.67 * 72},{3.1 * 72}!"];')

lines.append("}")
dot_src = "\n".join(lines)

render(dot_src, "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap04/slides/ontologia-colaboracao-slide.png",
       dpi=200, target_width_px=2666)
print("done")
