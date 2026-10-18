import sys
sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from graphviz_utils import FILL, render
from sebenta_style import DARK, MAGENTA, PINK, GREY

# Versão para o livro do exemplo da viagem de finalistas (Modelo de
# Atividade preenchido). O slide usa a paleta verde do deck:
# slide_cap04_atividade_exemplo.py. Uso: make_cap04_atividade_exemplo.py [pt|en]
LANG = sys.argv[1] if len(sys.argv) > 1 else "pt"

TXT = {
    "pt": {
        "Artefactos": ("Artefactos", ["grupo de WhatsApp com sondagens",
                                      "folha de cálculo partilhada"]),
        "Sujeito": ("Sujeito", ["comissão de 4 finalistas"]),
        "Objeto": ("Objeto", ["organização da viagem"]),
        "Comunidade": ("Comunidade", ["os 40 finalistas da turma"]),
        "Regras": ("Regras", ["decisões por votação", "máximo de 350 € por pessoa",
                              "quota paga até 15 de março"]),
        "Divisao": ("Divisão de Trabalho", ["Ana: alojamento · Bruno: transporte",
                                            "Carla: pagamentos · Duarte: atividades"]),
        "Resultado": ("Resultado", ["viagem reservada e paga"]),
        "out": "assets/images/cap04/teoria-atividade-exemplo.png",
    },
    "en": {
        "Artefactos": ("Artefacts", ["WhatsApp group with polls",
                                     "shared spreadsheet"]),
        "Sujeito": ("Subject", ["committee of 4 final-year students"]),
        "Objeto": ("Object", ["organising the trip"]),
        "Comunidade": ("Community", ["the 40 final-year students"]),
        "Regras": ("Rules", ["decisions by vote", "at most €350 per person",
                             "fee paid by 15 March"]),
        "Divisao": ("Division of Labour", ["Ana: accommodation · Bruno: transport",
                                           "Carla: payments · Duarte: activities"]),
        "Resultado": ("Outcome", ["trip booked and paid for"]),
        "out": "en/assets/images/cap04/teoria-atividade-exemplo.png",
    },
}[LANG]

pos = {
    "Artefactos": (5.5, 5.5), "Sujeito": (1.7, 3.1), "Objeto": (9.3, 3.1),
    "Comunidade": (1.7, 0.75), "Regras": (5.5, 0.3), "Divisao": (9.3, 0.75),
}

lines = [
    "digraph G {",
    '  graph [layout=neato, overlap=false, margin=0.2];',
    '  node [shape=box, style="rounded,filled", margin="0.18,0.10"];',
]

for name, (x, y) in pos.items():
    title, body = TXT[name]
    hi = name == "Artefactos"
    fg = "white" if hi else DARK
    rows = "".join(f'<BR/><FONT POINT-SIZE="14">{t}</FONT>' for t in body)
    label = (f'<<FONT FACE="Helvetica-Bold" POINT-SIZE="16" COLOR="{fg}">{title}</FONT>'
             f'<FONT FACE="Helvetica" COLOR="{fg}">{rows}</FONT>>')
    lines.append(f'  "{name}" [label={label}, pos="{x * 72},{y * 72}!", '
                 f'fillcolor="{DARK if hi else FILL}", color="{DARK if hi else GREY}", '
                 f'penwidth=1.4];')

rt, rb = TXT["Resultado"]
lines.append(
    f'  "Resultado" [shape=plaintext, style="", pos="{9.3 * 72},{4.85 * 72}!", '
    f'label=<<FONT FACE="Helvetica-Bold" POINT-SIZE="16" COLOR="{MAGENTA}">{rt}</FONT>'
    f'<BR/><FONT FACE="Helvetica" POINT-SIZE="14" COLOR="{DARK}">{rb[0]}</FONT>>];'
)

for a, b, color in [("Sujeito", "Artefactos", MAGENTA), ("Artefactos", "Objeto", MAGENTA),
                    ("Sujeito", "Comunidade", PINK), ("Divisao", "Objeto", PINK)]:
    lines.append(f'  "{a}" -> "{b}" [dir="none", color="{color}", penwidth=2.2];')
for a, b in [("Sujeito", "Objeto"), ("Comunidade", "Regras"), ("Regras", "Divisao")]:
    lines.append(f'  "{a}" -> "{b}" [dir="none", style="dashed", color="{GREY}"];')
lines.append(f'  "Objeto" -> "Resultado" [color="{DARK}", penwidth=2.0, arrowsize=0.8];')
lines.append("}")

render("\n".join(lines),
       "/Users/jpavao/QProjects/Sebenta-PSC/" + TXT["out"],
       dpi=200, target_width_px=2200)
print("done", LANG)
