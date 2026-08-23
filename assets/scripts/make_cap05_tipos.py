import sys
sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from graphviz_utils import render
from sebenta_style import DARK, MAGENTA, PINK, GREY, NOTE_COLOR

FILL = "#f4f0f6"


def node_line(name, label, hi=False, note=False):
    if hi:
        return f'  "{name}" [label="{label}", style="filled", fillcolor="{DARK}", fontcolor="white", color="{DARK}", fontname="Helvetica-Bold"];'
    if note:
        return f'  "{name}" [label="{label}", shape="plaintext", fontcolor="{NOTE_COLOR}", fontsize=12, fontname="Helvetica"];'
    return f'  "{name}" [label="{label}", style="filled", fillcolor="{FILL}", fontcolor="{DARK}", color="{GREY}"];'


lines = [
    "digraph G {",
    '  labelloc="t"; fontsize=26; fontname="Helvetica-Bold"; '
    f'fontcolor="{DARK}"; label="Sistemas de Comunicação, por Sincronismo";',
    '  graph [layout=dot, rankdir=TB, ranksep=0.55, nodesep=0.35, margin=0.3];',
    '  node [shape=box, style="rounded,filled", fontsize=14, '
    'fontname="Helvetica", margin="0.18,0.10"];',
    '  edge [color="' + GREY + '", arrowsize=0.6];',

    node_line("raiz", "Sistema de\\nComunicação", hi=True),

    node_line("sincrono", "Síncrono", note=False),
    node_line("assincrono", "Assíncrono", note=False),

    node_line("mensageiro", "Mensageiro"),
    node_line("batepapo", "Bate-papo"),
    node_line("conferencia", "Conferência"),
    node_line("correio", "Correio\\neletrónico"),
    node_line("discussao", "Discussão"),
    node_line("registo", "Registo de\\nmensagens"),

    node_line("ex_mensageiro", "WhatsApp, Messenger,\\nTelegram", note=True),
    node_line("ex_batepapo", "Discord, Slack", note=True),
    node_line("ex_conferencia", "Zoom, Teams", note=True),
    node_line("ex_correio", "Gmail, Outlook", note=True),
    node_line("ex_discussao", "Reddit, grupos\\ndo Facebook", note=True),
    node_line("ex_registo", "WordPress,\\nX, Instagram", note=True),

    f'  "raiz" -> "sincrono" [color="{MAGENTA}", penwidth=1.8];',
    f'  "raiz" -> "assincrono" [color="{PINK}", penwidth=1.8];',

    '  "sincrono" -> "mensageiro";',
    '  "sincrono" -> "batepapo";',
    '  "sincrono" -> "conferencia";',
    '  "assincrono" -> "correio";',
    '  "assincrono" -> "discussao";',
    '  "assincrono" -> "registo";',

    '  "mensageiro" -> "ex_mensageiro" [style=dashed, arrowhead=none];',
    '  "batepapo" -> "ex_batepapo" [style=dashed, arrowhead=none];',
    '  "conferencia" -> "ex_conferencia" [style=dashed, arrowhead=none];',
    '  "correio" -> "ex_correio" [style=dashed, arrowhead=none];',
    '  "discussao" -> "ex_discussao" [style=dashed, arrowhead=none];',
    '  "registo" -> "ex_registo" [style=dashed, arrowhead=none];',

    "}",
]
dot_src = "\n".join(lines)

render(dot_src, "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap05/tipos-sistemas.png",
       dpi=200, target_width_px=2200, engine="dot")
print("done")
