import sys
sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from graphviz_utils import node_attrs, render
from sebenta_style import DARK, MAGENTA, PINK, GREY, NOTE_COLOR

nodes = {
    "Repo":  ("Repositório\nCentral", 5.7, 3.0, False, True),
    "Dev1":  ("Programador 1", 1.3, 3.0, False, False),
    "Dev2":  ("Programador 2", 10.1, 3.0, False, False),
}

lines = [
    "digraph G {",
    '  labelloc="t"; fontsize=26; fontname="Helvetica-Bold"; '
    f'fontcolor="{DARK}"; label="Sistema de Controlo de Versão";',
    '  graph [layout=neato, overlap=false, margin=0.3];',
    '  node [shape=box, style="rounded,filled", fontsize=15, fontname="Helvetica"];',
]

for name, (label, x, y, dashed, hi) in nodes.items():
    attrs = node_attrs(dashed, hi)
    attr_str = ", ".join(f'{k}="{v}"' for k, v in attrs.items())
    lines.append(f'  "{name}" [label="{label}", pos="{x * 72},{y * 72}!", {attr_str}];')

edges = [
    ("Dev1", "Repo", "commit / push\npull / checkout", MAGENTA),
    ("Dev2", "Repo", "commit / push\npull / checkout", PINK),
]
for a, b, label, color in edges:
    label_html = label.replace("\n", "\\n")
    lines.append(
        f'  "{a}" -> "{b}" [dir="both", color="{color}", fontcolor="{NOTE_COLOR}", '
        f'fontsize=12, fontname="Helvetica", label="{label_html}"];'
    )

lines.append("}")
dot_src = "\n".join(lines)

render(dot_src, "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap08/controlo-versao.png",
       dpi=200, target_width_px=2200)
print("done")
