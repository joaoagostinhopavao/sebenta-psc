"""Modelo de Atividade de Engeström (1987), em Graphviz/neato.

Segue a figura original (Engeström, 1987, p. 78): Artefactos em cima,
Sujeito à esquerda, Objeto à direita com a seta larga para o Resultado e,
na base, Regras, Comunidade e Divisão de Trabalho. Todas as ligações são
bidirecionais; o triângulo de cima (Sujeito, Artefactos, Objeto) fica em
destaque. Usado pelos scripts make_cap04_atividade*.py (livro, magenta) e
slide_cap04_atividade*.py (deck da Aula 5, verde).
"""
import sys
sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from graphviz_utils import FILL, render
from sebenta_style import DARK, MAGENTA, PINK, GREY

PALETAS = {
    "livro": dict(forte=MAGENTA, fraca=PINK, texto=DARK, destaque=DARK,
                  fundo=FILL, borda=GREY, bold="Helvetica-Bold", reg="Helvetica",
                  largura=2200, pen=(2.6, 1.6), seta=0.9),
    "slide": dict(forte="#3d8a52", fraca="#8fb89a", texto="#111111",
                  destaque="#1d5a32", fundo="white", borda="#3d8a52",
                  bold="Helvetica Neue Condensed Bold", reg="Helvetica Neue",
                  largura=1, pen=(4.2, 2.6), seta=1.1),
}

NOMES = {
    "pt": {"Artefactos": "Artefactos", "Sujeito": "Sujeito", "Objeto": "Objeto",
           "Regras": "Regras", "Comunidade": "Comunidade",
           "Divisao": "Divisão de Trabalho", "Resultado": "Resultado"},
    "en": {"Artefactos": "Artefacts", "Sujeito": "Subject", "Objeto": "Object",
           "Regras": "Rules", "Comunidade": "Community",
           "Divisao": "Division of Labour", "Resultado": "Outcome"},
}

# triângulo de cima: a ação do sujeito sobre o objeto, mediada por artefactos
LIGACOES_FORTES = [("Sujeito", "Artefactos"), ("Artefactos", "Objeto"),
                   ("Sujeito", "Objeto")]
# dimensão coletiva: base e ligações cruzadas do triângulo de triângulos
LIGACOES_FRACAS = [("Regras", "Comunidade"), ("Comunidade", "Divisao"),
                   ("Sujeito", "Regras"), ("Sujeito", "Comunidade"),
                   ("Sujeito", "Divisao"), ("Objeto", "Regras"),
                   ("Objeto", "Comunidade"), ("Objeto", "Divisao"),
                   ("Artefactos", "Comunidade")]


def desenhar(estilo, saida, lang="pt", corpo=None, pos=None, tam=(16, 14)):
    """corpo: dict nó -> linhas de exemplo (versão preenchida) ou None."""
    p = PALETAS[estilo]
    nomes = NOMES[lang]
    corpo = corpo or {}
    t_titulo, t_corpo = tam
    linhas = [
        "digraph G {",
        '  graph [layout=neato, overlap=false, splines=line, margin=0.25];',
        '  node [shape=box, style="rounded,filled", margin="0.20,0.10"];',
    ]
    for no, (x, y) in pos.items():
        if no == "Resultado":
            continue
        hi = no == "Artefactos"
        fg = "white" if hi else p["texto"]
        rows = "".join(f'<BR/><FONT POINT-SIZE="{t_corpo}">{t}</FONT>'
                       for t in corpo.get(no, []))
        label = (f'<<FONT FACE="{p["bold"]}" POINT-SIZE="{t_titulo}" COLOR="{fg}">'
                 f'{nomes[no]}</FONT>'
                 + (f'<FONT FACE="{p["reg"]}" COLOR="{fg}">{rows}</FONT>' if rows else '')
                 + '>')
        linhas.append(
            f'  "{no}" [label={label}, pos="{x * 72},{y * 72}!", '
            f'fillcolor="{p["destaque"] if hi else p["fundo"]}", '
            f'color="{p["destaque"] if hi else p["borda"]}", penwidth=1.8];')

    x, y = pos["Resultado"]
    rows = "".join(f'<BR/><FONT FACE="{p["reg"]}" POINT-SIZE="{t_corpo}" '
                   f'COLOR="{p["texto"]}">{t}</FONT>' for t in corpo.get("Resultado", []))
    linhas.append(
        f'  "Resultado" [shape=plaintext, style="", pos="{x * 72},{y * 72}!", '
        f'label=<<FONT FACE="{p["bold"]}" POINT-SIZE="{t_titulo}" '
        f'COLOR="{p["texto"]}">{nomes["Resultado"]}</FONT>{rows}>];')

    forte, fraca = p["pen"]
    for a, b in LIGACOES_FORTES:
        linhas.append(f'  "{a}" -> "{b}" [dir=both, color="{p["forte"]}", '
                      f'penwidth={forte}, arrowsize={p["seta"]}];')
    for a, b in LIGACOES_FRACAS:
        linhas.append(f'  "{a}" -> "{b}" [dir=both, color="{p["fraca"]}", '
                      f'penwidth={fraca}, arrowsize={p["seta"] * 0.8}];')
    # seta larga do original: o objeto transforma-se no resultado
    linhas.append(f'  "Objeto" -> "Resultado" [color="{p["destaque"]}", '
                  f'penwidth={forte * 2.2}, arrowhead=empty, arrowsize={p["seta"] * 1.1}];')
    linhas.append("}")
    render("\n".join(linhas), saida, dpi=200, target_width_px=p["largura"])
