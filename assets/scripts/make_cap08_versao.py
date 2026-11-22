"""Figura do controlo de versão com Git e GitHub (Cap08).
Uso: make_cap08_versao.py [pt|en]"""
import sys
sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from graphviz_utils import node_attrs, render
from sebenta_style import DARK, MAGENTA, PINK, NOTE_COLOR

LANG = sys.argv[1] if len(sys.argv) > 1 else "pt"
T = {
    "pt": dict(titulo="Controlo de Versão com Git e GitHub", repo="GitHub\\n(repositório remoto)",
               dev="Programador {n}\\ncópia local completa\\ncom o histórico",
               aresta="push: envia\\npull: recebe",
               out="/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap08/controlo-versao.png"),
    "en": dict(titulo="Version Control with Git and GitHub", repo="GitHub\\n(remote repository)",
               dev="Programmer {n}\\nfull local copy\\nwith the whole history",
               aresta="push: sends\\npull: receives",
               out="/Users/jpavao/QProjects/Sebenta-PSC/en/assets/images/cap08/controlo-versao.png"),
}[LANG]

nodes = {
    "Repo": (T["repo"], 5.7, 4.0, False, True),
    "Dev1": (T["dev"].format(n=1), 1.9, 0.9, False, False),
    "Dev2": (T["dev"].format(n=2), 9.5, 0.9, False, False),
}

lines = [
    "digraph G {",
    '  labelloc="t"; fontsize=26; fontname="Helvetica-Bold"; '
    f'fontcolor="{DARK}"; label="{T["titulo"]}\\n ";',
    '  graph [layout=neato, overlap=false, margin=0.3];',
    '  node [shape=box, style="rounded,filled", fontsize=15, fontname="Helvetica"];',
]
for name, (label, x, y, dashed, hi) in nodes.items():
    attrs = node_attrs(dashed, hi)
    attr_str = ", ".join(f'{k}="{v}"' for k, v in attrs.items())
    lines.append(f'  "{name}" [label="{label}", pos="{x * 72},{y * 72}!", {attr_str}];')
for dev, color in (("Dev1", MAGENTA), ("Dev2", PINK)):
    lines.append(
        f'  "{dev}" -> "Repo" [dir="both", color="{color}", fontcolor="{NOTE_COLOR}", '
        f'fontsize=13, fontname="Helvetica", label="{T["aresta"]}"];'
    )
lines.append("}")
render("\n".join(lines), T["out"], dpi=200, target_width_px=2200)
print("done", LANG)
