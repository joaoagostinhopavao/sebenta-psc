import sys
sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from graphviz_utils import node_attrs, render
from sebenta_style import DARK, MAGENTA, PINK, GREY, NOTE_COLOR

nodes = {
    "Artefactos": ("Artefactos", 5.5, 5.4, False, True),
    "Sujeito":    ("Sujeito", 2.3, 3.1, False, False),
    "Objeto":     ("Objeto", 8.2, 3.1, False, False),
    "Comunidade": ("Comunidade", 2.8, 0.9, False, False),
    "Regras":     ("Regras", 5.5, 0.6, False, False),
    "Divisao":    ("Divisão de\nTrabalho", 8.0, 0.9, False, False),
    "Resultado":  ("Resultado", 8.2, 4.5, False, False),
    "MediacaoInd": ("mediação individual", 5.5, 4.15, False, False),
    "MediacaoCol": ("mediação coletiva", 5.5, 1.85, False, False),
}
PLAIN = {"Resultado", "MediacaoInd", "MediacaoCol"}

lines = [
    "digraph G {",
    '  labelloc="t"; fontsize=26; fontname="Helvetica-Bold"; '
    f'fontcolor="{DARK}"; label="Modelo de Atividade";',
    '  graph [layout=neato, overlap=false, margin=0.25];',
    '  node [shape=ellipse, fontsize=15, fontname="Helvetica"];',
]

for name, (label, x, y, dashed, hi) in nodes.items():
    if name == "Resultado":
        attrs = dict(shape="plaintext", fontcolor=DARK, fontname="Helvetica-Bold", fontsize=15)
    elif name in ("MediacaoInd", "MediacaoCol"):
        attrs = dict(shape="plaintext", fontcolor=NOTE_COLOR, fontname="Helvetica-Oblique",
                     fontsize=13)
    else:
        attrs = node_attrs(dashed, hi)
    attr_str = ", ".join(f'{k}="{v}"' for k, v in attrs.items())
    lines.append(f'  "{name}" [label="{label}", pos="{x * 72},{y * 72}!", {attr_str}];')

# ligações estruturais (não direcionais em conteúdo, sem seta)
structural = [
    ("Sujeito", "Artefactos", MAGENTA),
    ("Artefactos", "Objeto", MAGENTA),
    ("Sujeito", "Comunidade", PINK),
    ("Divisao", "Objeto", PINK),
]
for a, b, color in structural:
    lines.append(f'  "{a}" -> "{b}" [dir="none", color="{color}", penwidth=2.2];')

# ligação direta (mais fraca), tracejada
lines.append(
    f'  "Sujeito" -> "Objeto" [dir="none", style="dashed", color="{GREY}", '
    f'label="ação direta (mais fraca)", fontsize=12, fontcolor="{NOTE_COLOR}", '
    f'fontname="Helvetica"];'
)
# ligações tracejadas da comunidade (mediação coletiva, subsidiária)
lines.append(f'  "Comunidade" -> "Regras" [dir="none", style="dashed", color="{GREY}"];')
lines.append(f'  "Regras" -> "Divisao" [dir="none", style="dashed", color="{GREY}"];')

# resultado, com seta real (é uma consequência, não uma mediação)
lines.append(f'  "Objeto" -> "Resultado" [color="{DARK}", penwidth=2.0, arrowsize=0.8];')

lines.append("}")
dot_src = "\n".join(lines)

render(dot_src, "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap04/teoria-atividade.png",
       dpi=200, target_width_px=2200)
print("done")
