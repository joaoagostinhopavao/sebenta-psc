"""
Cap. 3: segundo exemplo de matriz de adjacência, uma rede de seguidores
entre seis contas (P a U) de uma plataforma como o Instagram ou o X.
Ao contrário da turma, cada conta segue quantas quiser, por isso o grau de
saída varia e a matriz não é simétrica.

Gera:
- assets/images/cap03/sociograma-seguidores.png (livro)
- assets/images/cap03/slides/matriz-seguidores-slide.png (deck da Aula 4)

Convenções visuais:
- tamanho do nó proporcional ao grau de entrada (número de seguidores)
- seta dupla a magenta = seguimento recíproco; seta simples a cinza = não retribuído
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle
import networkx as nx
import math
import sys

sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from sebenta_style import (DARK, MAGENTA, GREY, apply_style,
                            NODE_LABEL_SIZE, EDGE_WIDTH, EDGE_WIDTH_HI,
                            REFERENCE_WIDTH)

apply_style()

NODES = ["P", "Q", "R", "S", "T", "U"]
ARCS = [("P", "Q"), ("Q", "P"), ("Q", "R"), ("R", "P"), ("R", "S"),
        ("S", "P"), ("S", "R"), ("T", "P"), ("U", "P"), ("U", "T")]

D = nx.DiGraph()
D.add_nodes_from(NODES)
D.add_edges_from(ARCS)

pos = {
    "P": (3.5, 1.9), "Q": (0.7, 3.4), "R": (6.3, 3.4),
    "S": (6.3, 0.4), "T": (0.7, 0.4), "U": (3.5, -0.2),
}


def radius(v):
    return 0.30 + 0.05 * D.in_degree(v)


# ------------------------------------------------------------------
# Sociograma (livro)
# ------------------------------------------------------------------
fig_w = REFERENCE_WIDTH
xlim, ylim = (-0.05, 7.05), (-0.65, 4.0)
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
    color = MAGENTA if mutual else GREY
    lw = EDGE_WIDTH_HI if mutual else EDGE_WIDTH
    style = "<|-|>" if mutual else "-|>"
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle=style, mutation_scale=26,
                                 color=color, linewidth=lw, zorder=1))

for v, (x, y) in pos.items():
    ax.add_patch(plt.Circle((x, y), radius(v), facecolor=DARK, edgecolor="white",
                            linewidth=2.2, zorder=3))
    ax.text(x, y, v, ha="center", va="center", fontsize=NODE_LABEL_SIZE + 4,
            color="white", fontweight="bold", zorder=4)

out = "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap03/sociograma-seguidores.png"
fig.savefig(out, facecolor="white")
plt.close(fig)

# ------------------------------------------------------------------
# Matriz de adjacência como imagem (slide), no mesmo aspeto da tabela
# da turma usada no deck
# ------------------------------------------------------------------
HEADER_BG = "#f6d9ec"
LINE = "#d9d9de"
TEXT = "#3a3a46"

rows = NODES + ["Seguidores"]
cols = ["Segue ↓ / Seguido →"] + NODES + ["Segue"]
col_w = [4.0] + [0.85] * len(NODES) + [1.35]
row_h = 0.78
W = sum(col_w)
H = row_h * (len(rows) + 1)

plt.rcParams["font.sans-serif"] = ["Arial", "DejaVu Sans"]
fig = plt.figure(figsize=(W, H), dpi=200)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W)
ax.set_ylim(H, 0)
ax.axis("off")

xs = [sum(col_w[:i]) for i in range(len(col_w))]
centers = [x + w / 2 for x, w in zip(xs, col_w)]

ax.add_patch(Rectangle((0, 0), W, row_h, facecolor=HEADER_BG, edgecolor="none"))
ax.plot([0, W], [row_h, row_h], color="#b9a9b8", linewidth=2)
for c, label in zip(centers, cols):
    ax.text(c, row_h / 2, label, ha="center", va="center", fontsize=24,
            fontweight="bold", color=TEXT)

for i, r in enumerate(rows):
    y = row_h * (i + 1)
    yc = y + row_h / 2
    ax.plot([0, W], [y + row_h, y + row_h], color=LINE, linewidth=1.5)
    total = r == "Seguidores"
    ax.text(centers[0], yc, r, ha="center", va="center", fontsize=24,
            fontweight="bold", color=TEXT)
    for j, c in enumerate(NODES):
        if total:
            val = str(D.in_degree(c))
        else:
            val = "1" if D.has_edge(r, c) else ""
        ax.text(centers[j + 1], yc, val, ha="center", va="center", fontsize=24,
                fontweight="bold" if total else "normal", color=TEXT)
    if not total:
        ax.text(centers[-1], yc, str(D.out_degree(r)), ha="center", va="center",
                fontsize=24, fontweight="bold", color=TEXT)

out_m = "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap03/slides/matriz-seguidores-slide.png"
fig.savefig(out_m, facecolor="white")
plt.close(fig)

if __name__ == "__main__":
    U = D.to_undirected()
    print("arcos:", D.number_of_edges())
    print("densidade rede (dirigida):", round(nx.density(D), 3))
    print("reciprocidade:", round(nx.reciprocity(D), 3))
    print("pares recíprocos:", sorted({tuple(sorted((u, v))) for u, v in D.edges if D.has_edge(v, u)}))
    for v in NODES:
        print(v, "entrada", D.in_degree(v), "saída", D.out_degree(v))
    from PIL import Image
    print("tamanho:", Image.open(out).size, Image.open(out_m).size)
