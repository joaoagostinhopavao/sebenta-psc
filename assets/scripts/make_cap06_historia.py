import sys
sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from graphviz_utils import render
from sebenta_style import DARK, MAGENTA, PINK, GREY, NOTE_COLOR

FILL = "#f4f0f6"

events = [
    ("maze", "1974", "Maze War", "Primeiro CVE<BR/>registado (NASA)", MAGENTA),
    ("simnet", "1983", "SIMNET", "Treino militar<BR/>simulado (DoD)", PINK),
    ("sl_wow", "2003 a 2004", "Second Life<BR/>e World of Warcraft", "Os mais<BR/>bem-sucedidos", MAGENTA),
    ("atual", "2010s a 2020s", "VRChat, Horizon<BR/>Worlds, Roblox", "Mundos sociais<BR/>com RV nativa", PINK),
]

lines = [
    "digraph G {",
    '  labelloc="t"; fontsize=26; fontname="Helvetica-Bold"; '
    f'fontcolor="{DARK}"; label="Linha do Tempo dos CVEs";',
    '  graph [layout=neato, overlap=false, margin=0.3];',
    '  node [shape=plaintext, fontname="Helvetica"];',
]

xs = [1.6, 4.5, 7.4, 10.3]
y_line = 2.6

for (key, year, title, desc, color), x in zip(events, xs):
    lines.append(f'  "dot_{key}" [shape=circle, style=filled, fillcolor="{color}", '
                 f'color="{color}", fixedsize=true, width=0.22, label="", pos="{x*72},{y_line*72}!"];')
    lines.append(f'  "year_{key}" [label=<<FONT COLOR="{color}" POINT-SIZE="15"><B>{year}</B></FONT>>, '
                 f'pos="{x*72},{(y_line+0.55)*72}!"];')
    html = (f'<<TABLE BORDER="0" CELLBORDER="0" CELLPADDING="4">'
            f'<TR><TD><FONT COLOR="{DARK}" POINT-SIZE="14"><B>{title}</B></FONT></TD></TR>'
            f'<TR><TD><FONT COLOR="{NOTE_COLOR}" POINT-SIZE="11">{desc}</FONT></TD></TR>'
            f'</TABLE>>')
    lines.append(f'  "label_{key}" [label={html}, pos="{x*72},{(y_line-0.9)*72}!"];')

lines.append(f'  "axis" [shape=plaintext, label="", pos="{5.95*72},{y_line*72}!"];')
lines.append(f'  "line0" [shape=point, width=0.01, pos="{(xs[0]-0.5)*72},{y_line*72}!"];')
lines.append(f'  "line1" [shape=point, width=0.01, pos="{(xs[-1]+0.5)*72},{y_line*72}!"];')
lines.append(f'  "line0" -> "line1" [dir="none", color="{GREY}", penwidth=2.2];')

lines.append("}")
dot_src = "\n".join(lines)

render(dot_src, "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap06/historia-cves.png",
       dpi=200, target_width_px=2200)
print("done")
