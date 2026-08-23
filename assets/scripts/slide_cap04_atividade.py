import sys
sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from graphviz_utils import node_attrs, render
from sebenta_style import DARK, MAGENTA, PINK, GREY, NOTE_COLOR

nodes = {
    "Artefactos": ("Artefactos", 6.67, 5.5, False, True),
    "Sujeito":    ("Sujeito", 3.4, 3.1, False, False),
    "Objeto":     ("Objeto", 9.9, 3.1, False, False),
    "Comunidade": ("Comunidade", 4.0, 0.9, False, False),
    "Regras":     ("Regras", 6.67, 0.55, False, False),
    "Divisao":    ("Divisão de\nTrabalho", 9.6, 0.9, False, False),
    "Resultado":  ("Resultado", 9.9, 4.55, False, False),
    "MediacaoInd": ("mediação individual", 6.67, 4.2, False, False),
    "MediacaoCol": ("mediação coletiva", 6.67, 1.85, False, False),
}

lines = [
    "digraph G {",
    '  labelloc="t"; fontsize=30; fontname="Helvetica-Bold"; '
    f'fontcolor="{DARK}"; label="Modelo de Atividade";',
    '  graph [layout=neato, overlap=false, margin=0.3];',
    '  node [shape=ellipse, fontsize=17, fontname="Helvetica"];',
]

for name, (label, x, y, dashed, hi) in nodes.items():
    if name == "Resultado":
        attrs = dict(shape="plaintext", fontcolor=DARK, fontname="Helvetica-Bold", fontsize=17)
    elif name in ("MediacaoInd", "MediacaoCol"):
        attrs = dict(shape="plaintext", fontcolor=NOTE_COLOR, fontname="Helvetica-Oblique",
                     fontsize=15)
    else:
        attrs = node_attrs(dashed, hi)
    attr_str = ", ".join(f'{k}="{v}"' for k, v in attrs.items())
    lines.append(f'  "{name}" [label="{label}", pos="{x * 72},{y * 72}!", {attr_str}];')

structural = [
    ("Sujeito", "Artefactos", MAGENTA),
    ("Artefactos", "Objeto", MAGENTA),
    ("Sujeito", "Comunidade", PINK),
    ("Divisao", "Objeto", PINK),
]
for a, b, color in structural:
    lines.append(f'  "{a}" -> "{b}" [dir="none", color="{color}", penwidth=2.4];')

lines.append(
    f'  "Sujeito" -> "Objeto" [dir="none", style="dashed", color="{GREY}", '
    f'label="ação direta (mais fraca)", fontsize=14, fontcolor="{NOTE_COLOR}", '
    f'fontname="Helvetica"];'
)
lines.append(f'  "Comunidade" -> "Regras" [dir="none", style="dashed", color="{GREY}"];')
lines.append(f'  "Regras" -> "Divisao" [dir="none", style="dashed", color="{GREY}"];')

lines.append(f'  "Objeto" -> "Resultado" [color="{DARK}", penwidth=2.2, arrowsize=0.9];')

lines.append("}")
dot_src = "\n".join(lines)

render(dot_src, "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap04/slides/teoria-atividade-slide.png",
       dpi=200, target_width_px=2666)
print("done")
