import sys
sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from graphviz_utils import render

# Paleta verde do deck da Aula 5 (slide 8, imagem "Modelo de Atividade")
GREEN = "#3d8a52"
GREEN_DARK = "#1d5a32"
INK = "#111111"
BOLD = "Helvetica Neue Condensed Bold"
REG = "Helvetica Neue"

# Mesmo esquema do slide_cap04_atividade.py, preenchido com uma situação
# concreta: a comissão que organiza a viagem de finalistas da turma.
nodes = {
    "Artefactos": ("Artefactos",
                   ["grupo de WhatsApp com sondagens", "folha de cálculo partilhada"],
                   6.67, 5.6, True),
    "Sujeito":    ("Sujeito", ["comissão de 4 finalistas"], 1.85, 3.1, False),
    "Objeto":     ("Objeto", ["organização da viagem"], 11.5, 3.1, False),
    "Comunidade": ("Comunidade", ["os 40 finalistas da turma"], 1.85, 0.75, False),
    "Regras":     ("Regras",
                   ["decisões por votação", "máximo de 350 € por pessoa",
                    "quota paga até 15 de março"],
                   6.67, 0.3, False),
    "Divisao":    ("Divisão de Trabalho",
                   ["Ana: alojamento · Bruno: transporte",
                    "Carla: pagamentos · Duarte: atividades"],
                   11.5, 0.75, False),
}

lines = [
    "digraph G {",
    '  graph [layout=neato, overlap=false, margin=0.25];',
    '  node [shape=box, style="rounded,filled", margin="0.22,0.12"];',
]

for name, (title, body, x, y, hi) in nodes.items():
    fg = "white" if hi else INK
    fill = GREEN if hi else "white"
    rows = "".join(f'<BR/><FONT POINT-SIZE="20">{t}</FONT>' for t in body)
    label = (f'<<FONT FACE="{BOLD}" POINT-SIZE="25" COLOR="{fg}">{title}</FONT>'
             f'<FONT FACE="{REG}" COLOR="{fg}">{rows}</FONT>>')
    border = GREEN
    lines.append(f'  "{name}" [label={label}, pos="{x * 72},{y * 72}!", '
                 f'fillcolor="{fill}", color="{border}", penwidth=2.6];')

lines.append(
    f'  "Resultado" [shape=plaintext, style="", pos="{11.5 * 72},{5.0 * 72}!", '
    f'label=<<FONT FACE="{BOLD}" POINT-SIZE="25" COLOR="{INK}">Resultado</FONT>'
    f'<BR/><FONT FACE="{REG}" POINT-SIZE="20" COLOR="{INK}">viagem reservada e paga</FONT>>];'
)

lines.append(f'  "Sujeito" -> "Artefactos" [color="{GREEN}", penwidth=4, arrowsize=1.1];')
lines.append(f'  "Objeto" -> "Artefactos" [color="{GREEN}", penwidth=4, arrowsize=1.1];')
lines.append(f'  "Sujeito" -> "Comunidade" [dir="none", color="{GREEN_DARK}", penwidth=4];')
lines.append(f'  "Divisao" -> "Objeto" [dir="none", color="{GREEN}", penwidth=4];')

lines.append(f'  "Sujeito" -> "Objeto" [dir="none", style="dashed", color="{GREEN}", penwidth=3];')
lines.append(f'  "Comunidade" -> "Regras" [dir="none", style="dashed", color="{GREEN}", penwidth=3];')
lines.append(f'  "Regras" -> "Divisao" [dir="none", style="dashed", color="{GREEN}", penwidth=3];')
lines.append(f'  "Objeto" -> "Resultado" [color="{GREEN_DARK}", penwidth=4, arrowsize=1.1];')

lines.append("}")
dot_src = "\n".join(lines)

render(dot_src,
       "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap04/slides/teoria-atividade-exemplo-slide.png",
       dpi=200, target_width_px=2666)
print("done")
