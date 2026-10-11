"""
Slide "Centralidade de Intermediação" da Aula 4: sociograma da turma com o
aluno E em destaque. E tem só 2 contactos, mas as ligações C-E e E-F (a
magenta) são as únicas pontes entre as duas sub-redes, por isso todos os
caminhos mais curtos entre {A, B, C, D, I} e {F, G, H} passam por E.

Gera assets/images/cap03/slides/sociograma-turma-intermediacao-slide.png
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import networkx as nx
import math
import sys

sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from sebenta_style import (DARK, MAGENTA, PINK, GREY, apply_style,
                            NODE_LABEL_SIZE, EDGE_WIDTH, EDGE_WIDTH_HI,
                            REFERENCE_WIDTH)

apply_style()

# mesmas escolhas e posições de make_cap03_sociograma.py
ARCS = [("A", "B"), ("A", "C"), ("B", "A"), ("B", "C"), ("C", "A"), ("C", "B"),
        ("D", "A"), ("D", "C"), ("E", "C"), ("E", "F"), ("F", "E"), ("F", "G"),
        ("G", "F"), ("G", "H"), ("H", "F"), ("H", "G"), ("I", "A"), ("I", "D")]
pos = {
    "A": (1.4, 1.9), "B": (0.7, 3.7), "C": (3.2, 3.0), "D": (2.7, 0.5),
    "I": (0.0, 0.6), "E": (5.0, 3.0), "F": (6.8, 3.0), "G": (8.2, 4.0),
    "H": (8.2, 1.6),
}
FOCUS = "E"
group1 = {"A", "B", "C", "D", "I"}

D = nx.DiGraph(ARCS)
U = D.to_undirected()
bridges = {frozenset(e) for e in nx.bridges(U)}


def radius(v):
    return 0.30 + 0.05 * D.in_degree(v)


fig_w = REFERENCE_WIDTH
xlim, ylim = (-0.45, 8.75), (0.0, 4.55)
fig_h = fig_w * (ylim[1] - ylim[0]) / (xlim[1] - xlim[0])
fig = plt.figure(figsize=(fig_w, fig_h), dpi=200)
ax = fig.add_axes([0.0, 0.0, 1.0, 1.0])
ax.set_xlim(*xlim)
ax.set_ylim(*ylim)
ax.set_aspect("equal")
ax.axis("off")

done = set()
for u, v in ARCS:
    key = frozenset((u, v))
    if key in done:
        continue
    done.add(key)
    mutual = D.has_edge(v, u)
    (x1, y1), (x2, y2) = pos[u], pos[v]
    d = math.hypot(x2 - x1, y2 - y1)
    ux, uy = (x2 - x1) / d, (y2 - y1) / d
    ru, rv = radius(u) + 0.06, radius(v) + 0.06
    start = (x1 + ux * ru, y1 + uy * ru)
    end = (x2 - ux * rv, y2 - uy * rv)
    hi = key in bridges
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="<|-|>" if mutual else "-|>",
                                 mutation_scale=26, color=MAGENTA if hi else GREY,
                                 linewidth=EDGE_WIDTH_HI if hi else EDGE_WIDTH,
                                 zorder=2 if hi else 1))

for v, (x, y) in pos.items():
    if v == FOCUS:
        face = MAGENTA
    elif v in group1:
        face = DARK
    else:
        face = PINK
    ax.add_patch(plt.Circle((x, y), radius(v), facecolor=face, edgecolor="white",
                            linewidth=2.2, zorder=3))
    ax.text(x, y, v, ha="center", va="center", fontsize=NODE_LABEL_SIZE + 4,
            color="white", fontweight="bold", zorder=4)

out = "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap03/slides/sociograma-turma-intermediacao-slide.png"
fig.savefig(out, facecolor="white")

if __name__ == "__main__":
    n = U.number_of_nodes()
    raw = nx.betweenness_centrality(U, normalized=False)
    norm = nx.betweenness_centrality(U)
    print("pares sem o nó:", (n - 1) * (n - 2) // 2)
    for v in sorted(U):
        print(v, "contactos", U.degree(v), "pares", raw[v], "intermediação", round(norm[v], 3))
    print("pontes:", sorted(tuple(sorted(b)) for b in bridges))
