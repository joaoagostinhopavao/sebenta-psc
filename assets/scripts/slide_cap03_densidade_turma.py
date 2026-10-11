"""
Slide "Densidade" da Aula 4: sociograma da turma com o aluno A em destaque,
para acompanhar a conta da densidade de um nó. As setas que tocam em A
ficam a magenta (6 setas: 2 escolhas feitas, 4 recebidas) e os seus 4
contactos (B, C, D, I) ficam a escuro; os restantes alunos ficam a cinzento.

Gera assets/images/cap03/slides/sociograma-turma-densidade-slide.png
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
FOCUS = "A"
FADED = "#e9e2ec"
FADED_TEXT = "#8a7d90"

D = nx.DiGraph(ARCS)
contacts = set(D.predecessors(FOCUS)) | set(D.successors(FOCUS))


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
    hi = FOCUS in key
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="<|-|>" if mutual else "-|>",
                                 mutation_scale=26, color=MAGENTA if hi else GREY,
                                 linewidth=EDGE_WIDTH_HI if hi else EDGE_WIDTH,
                                 zorder=2 if hi else 1))

for v, (x, y) in pos.items():
    if v == FOCUS:
        face, txt = MAGENTA, "white"
    elif v in contacts:
        face, txt = DARK, "white"
    else:
        face, txt = FADED, FADED_TEXT
    ax.add_patch(plt.Circle((x, y), radius(v), facecolor=face, edgecolor="white",
                            linewidth=2.2, zorder=3))
    ax.text(x, y, v, ha="center", va="center", fontsize=NODE_LABEL_SIZE + 4,
            color=txt, fontweight="bold", zorder=4)

out = "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap03/slides/sociograma-turma-densidade-slide.png"
fig.savefig(out, facecolor="white")

if __name__ == "__main__":
    U = D.to_undirected()
    n = D.number_of_nodes()
    print("A: setas", D.in_degree(FOCUS) + D.out_degree(FOCUS), "entrada", D.in_degree(FOCUS),
          "saída", D.out_degree(FOCUS), "contactos", sorted(contacts),
          "densidade do nó", U.degree(FOCUS) / (n - 1))
    print("rede direcional:", D.number_of_edges(), "/", n * (n - 1), "=", nx.density(D))
    print("rede não-direcional:", U.number_of_edges(), "/", n * (n - 1) // 2, "=", round(nx.density(U), 3))
    for v in sorted(D):
        print(v, "contactos", U.degree(v), "setas", D.degree(v), "dens", round(U.degree(v) / (n - 1), 3))
