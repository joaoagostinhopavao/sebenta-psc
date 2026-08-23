import sys
sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from graphviz_utils import render
from sebenta_style import DARK, MAGENTA, PINK, GREY

FILL = "#f4f0f6"

blocks = {
    "Formacao":     ("Formação de Grupos", "Participante", 2.2, 5.15, MAGENTA),
    "Comunicacao":  ("Comunicação", "Mensagem", 8.8, 5.15, PINK),
    "Coordenacao":  ("Coordenação", "Plano de Trabalho", 2.2, 1.1, DARK),
    "Cooperacao":   ("Cooperação", "Atividade", 8.8, 1.1, MAGENTA),
}

lines = [
    "digraph G {",
    '  labelloc="t"; fontsize=26; fontname="Helvetica-Bold"; '
    f'fontcolor="{DARK}"; label="Ontologia de Colaboração";',
    '  graph [layout=neato, overlap=false, margin=0.3];',
    '  node [shape=plaintext, fontname="Helvetica"];',
]

for name, (title, sub, x, y, color) in blocks.items():
    html = (f'<<TABLE BORDER="2" COLOR="{color}" CELLBORDER="0" '
            f'CELLPADDING="10" BGCOLOR="{FILL}">'
            f'<TR><TD><FONT COLOR="{DARK}" POINT-SIZE="16"><B>{title}</B></FONT></TD></TR>'
            f'<TR><TD><FONT COLOR="{color}" POINT-SIZE="13"><I>{sub}</I></FONT></TD></TR>'
            f'</TABLE>>')
    lines.append(f'  "{name}" [label={html}, pos="{x * 72},{y * 72}!"];')
    lines.append(f'  "{name}" -> "Colabo" [color="{GREY}", dir="none"];')

lines.append(f'  "Colabo" [label=<<FONT COLOR="white" POINT-SIZE="15"><B>COLABO-<BR/>RAÇÃO</B></FONT>>, '
             f'shape=circle, style=filled, fillcolor="{DARK}", fixedsize=true, width=1.05, '
             f'pos="{5.5 * 72},{3.1 * 72}!"];')

lines.append("}")
dot_src = "\n".join(lines)

render(dot_src, "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap04/ontologia-colaboracao.png",
       dpi=200, target_width_px=2200)
print("done")
