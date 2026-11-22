"""Figura do ciclo de vida de um defeito (Cap08), segundo a figura 8.3 de Souza et al. (2011).
Uso: make_cap08_defeito.py [pt|en]"""
import sys
sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from graphviz_utils import render
from sebenta_style import DARK, MAGENTA, GREY, NOTE_COLOR

LANG = sys.argv[1] if len(sys.argv) > 1 else "pt"
T = {
    "pt": dict(titulo="Ciclo de Vida de um Defeito",
               registo="Registo\\n(testador ou utilizador)", analise="Análise e atribuição\\n(engenheiro de software)",
               correcao="Correção\\n(programador)", verificacao="Verificação\\n(equipa de teste)",
               negociacao="Negociação do fecho\\n(gestor de testes e líder técnico)\\nResolvido?",
               fechado="Defeito fechado", sim="sim", nao="não: o defeito é reaberto",
               out="/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap08/ciclo-defeito.png"),
    "en": dict(titulo="The Lifecycle of a Defect",
               registo="Reporting\\n(tester or user)", analise="Analysis and assignment\\n(software engineer)",
               correcao="Fix\\n(programmer)", verificacao="Verification\\n(test team)",
               negociacao="Closure negotiation\\n(test manager and technical lead)\\nResolved?",
               fechado="Defect closed", sim="yes", nao="no: the defect is reopened",
               out="/Users/jpavao/QProjects/Sebenta-PSC/en/assets/images/cap08/ciclo-defeito.png"),
}[LANG]

lines = [
    "digraph G {",
    '  labelloc="t"; fontsize=26; fontname="Helvetica-Bold"; '
    f'fontcolor="{DARK}"; label="{T["titulo"]}\\n ";',
    '  graph [layout=neato, overlap=false, margin=0.3];',
    '  node [fontname="Helvetica", fontsize=14];',
]
nodes = [
    ("registo", "registo", 1.6, 3.6, "#f4f0f6", DARK),
    ("analise", "analise", 5.2, 3.6, "#f4f0f6", DARK),
    ("correcao", "correcao", 8.8, 3.6, "#f4f0f6", DARK),
    ("verificacao", "verificacao", 12.4, 3.6, "#f4f0f6", DARK),
    ("negociacao", "negociacao", 12.4, 1.1, "#fbeaf7", MAGENTA),
    ("fechado", "fechado", 8.8, 1.1, DARK, "white"),
]
for key, campo, x, y, fill, fontcolor in nodes:
    lines.append(f'  "{key}" [shape=box, style="filled,rounded", fillcolor="{fill}", '
                 f'fontcolor="{fontcolor}", color="{GREY}", label="{T[campo]}", '
                 f'pos="{x * 72},{y * 72}!"];')
for a, b in (("registo", "analise"), ("analise", "correcao"), ("correcao", "verificacao"),
             ("verificacao", "negociacao")):
    lines.append(f'  "{a}" -> "{b}" [color="{MAGENTA}"];')
lines.append(f'  "negociacao" -> "fechado" [color="{MAGENTA}", fontcolor="{NOTE_COLOR}", '
             f'fontsize=13, fontname="Helvetica", label="{T["sim"]}"];')
lines.append(f'  "negociacao" -> "correcao" [color="{GREY}", fontcolor="{NOTE_COLOR}", '
             f'fontsize=13, fontname="Helvetica", label="{T["nao"]}"];')
lines.append("}")
render("\n".join(lines), T["out"], dpi=200, target_width_px=2200)
print("done", LANG)
