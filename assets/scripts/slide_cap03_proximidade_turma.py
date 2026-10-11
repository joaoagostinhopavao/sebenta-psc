"""
Slide "Centralidade de Proximidade" da Aula 4: sociograma da turma com o
aluno C em destaque e, junto de cada colega, a sua distância a C (número de
passos no caminho mais curto, ignorando o sentido das setas). A soma das
distâncias dá a proximidade de C: 8 / 14 ≈ 0,57.

Gera assets/images/cap03/slides/sociograma-turma-proximidade-slide.png
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import networkx as nx
import math
import sys

sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from sebenta_style import (DARK, MAGENTA, GREY, apply_style,
                            NODE_LABEL_SIZE, EDGE_WIDTH, REFERENCE_WIDTH)

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
FOCUS = "C"
# posição do selo com a distância, relativa ao centro do nó
BADGE = {
    "A": (-0.55, 0.45), "B": (0.55, 0.3), "D": (0.55, 0.3), "I": (-0.1, 0.65),
    "E": (0.0, -0.62), "F": (0.0, -0.72), "G": (-0.62, 0.2), "H": (-0.62, -0.2),
}

D = nx.DiGraph(ARCS)
U = D.to_undirected()
dist = nx.single_source_shortest_path_length(U, FOCUS)


def radius(v):
    return 0.30 + 0.05 * D.in_degree(v)


fig_w = REFERENCE_WIDTH
xlim, ylim = (-0.45, 8.75), (-0.15, 4.55)
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
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="<|-|>" if mutual else "-|>",
                                 mutation_scale=26, color=GREY, linewidth=EDGE_WIDTH,
                                 zorder=1))

for v, (x, y) in pos.items():
    ax.add_patch(plt.Circle((x, y), radius(v), facecolor=MAGENTA if v == FOCUS else DARK,
                            edgecolor="white", linewidth=2.2, zorder=3))
    ax.text(x, y, v, ha="center", va="center", fontsize=NODE_LABEL_SIZE + 4,
            color="white", fontweight="bold", zorder=4)
    if v != FOCUS:
        bx, by = BADGE[v]
        ax.text(x + bx, y + by, str(dist[v]), ha="center", va="center",
                fontsize=NODE_LABEL_SIZE + 2, fontweight="bold", color=MAGENTA, zorder=5,
                bbox=dict(boxstyle="circle,pad=0.25", facecolor="white",
                          edgecolor=MAGENTA, linewidth=2.2))

out = "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap03/slides/sociograma-turma-proximidade-slide.png"
fig.savefig(out, facecolor="white")

if __name__ == "__main__":
    n = U.number_of_nodes()
    print("distâncias a C:", dict(sorted(dist.items())), "soma", sum(dist.values()))
    cl = nx.closeness_centrality(U)
    for v in sorted(U):
        s = sum(nx.single_source_shortest_path_length(U, v).values())
        print(v, "contactos", U.degree(v), "soma", s, "proximidade", round(cl[v], 3))
