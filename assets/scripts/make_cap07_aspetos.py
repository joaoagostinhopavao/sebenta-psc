import sys
sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from graphviz_utils import render
from sebenta_style import DARK, MAGENTA, PINK, GREY, NOTE_COLOR

blocks = [
    ("Colaboracao", "COLABORAÇÃO", "Comunicação,<BR/>coordenação e<BR/>cooperação", 2.0, 4.6, MAGENTA),
    ("Transparencia", "TRANSPARÊNCIA", "Acesso, qualidade<BR/>e auditabilidade<BR/>da informação", 6.67, 6.4, PINK),
    ("Memoria", "MEMÓRIA", "Registo e<BR/>recuperação da<BR/>discussão", 11.3, 4.6, MAGENTA),
]

lines = [
    "digraph G {",
    '  labelloc="t"; fontsize=26; fontname="Helvetica-Bold"; '
    f'fontcolor="{DARK}"; label="Aspetos para a Democracia Eletrónica";',
    '  graph [layout=neato, overlap=false, margin=0.3];',
    '  node [fontname="Helvetica"];',
]

for name, title, desc, x, y, color in blocks:
    html = (f'<<TABLE BORDER="0" CELLBORDER="0" CELLPADDING="8" BGCOLOR="{color}">'
            f'<TR><TD><FONT COLOR="white" POINT-SIZE="16"><B>{title}</B></FONT></TD></TR>'
            f'<TR><TD><FONT COLOR="white" POINT-SIZE="12">{desc}</FONT></TD></TR>'
            f'</TABLE>>')
    lines.append(f'  "{name}" [shape=plaintext, style="", margin="0", label={html}, '
                 f'pos="{x * 72},{y * 72}!"];')
    lines.append(f'  "{name}" -> "Democracia" [color="{GREY}", dir="none"];')

lines.append(f'  "Democracia" [label=<<FONT COLOR="white" POINT-SIZE="12"><B>DEMOCRACIA<BR/>ELETRÓNICA</B></FONT>>, '
             f'shape=circle, style=filled, fillcolor="{DARK}", fixedsize=true, width=1.55, '
             f'pos="{6.67 * 72},{4.0 * 72}!"];')

lines.append("}")
dot_src = "\n".join(lines)

render(dot_src, "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap07/aspetos-democracia.png",
       dpi=200, target_width_px=2200)
print("done")
