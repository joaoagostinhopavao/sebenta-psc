"""
Sociograma da turma para impressão a preto e branco (folha de apoio da
Aula 4). As duas sub-redes distinguem-se pelo preenchimento (nós escuros e
nós claros com contorno) e as pontes por um traço mais grosso, sem depender
da cor.

Gera assets/images/cap03/handout/sociograma-turma-pb.png
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import networkx as nx
import math
import os
import sys

sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from sebenta_style import apply_style, NODE_LABEL_SIZE, EDGE_WIDTH, REFERENCE_WIDTH

apply_style()

BLACK = "#111111"
EDGE = "#8c8c8c"

# mesmas escolhas e posições de make_cap03_sociograma.py
ARCS = [("A", "B"), ("A", "C"), ("B", "A"), ("B", "C"), ("C", "A"), ("C", "B"),
        ("D", "A"), ("D", "C"), ("E", "C"), ("E", "F"), ("F", "E"), ("F", "G"),
        ("G", "F"), ("G", "H"), ("H", "F"), ("H", "G"), ("I", "A"), ("I", "D")]
pos = {
    "A": (1.4, 1.9), "B": (0.7, 3.7), "C": (3.2, 3.0), "D": (2.7, 0.5),
    "I": (0.0, 0.6), "E": (5.0, 3.0), "F": (6.8, 3.0), "G": (8.2, 4.0),
    "H": (8.2, 1.6),
}
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
    bridge = key in bridges
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="<|-|>" if mutual else "-|>",
                                 mutation_scale=30 if bridge else 26,
                                 color=BLACK if bridge else EDGE,
                                 linewidth=6.5 if bridge else EDGE_WIDTH, zorder=1))

for v, (x, y) in pos.items():
    dark = v in group1
    ax.add_patch(plt.Circle((x, y), radius(v), facecolor=BLACK if dark else "white",
                            edgecolor=BLACK, linewidth=3.2, zorder=3))
    ax.text(x, y, v, ha="center", va="center", fontsize=NODE_LABEL_SIZE + 4,
            color="white" if dark else BLACK, fontweight="bold", zorder=4)

out_dir = "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap03/handout"
os.makedirs(out_dir, exist_ok=True)
out = os.path.join(out_dir, "sociograma-turma-pb.png")
fig.savefig(out, facecolor="white")
print(out)
