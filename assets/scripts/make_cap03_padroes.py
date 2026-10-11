"""
Cap. 3: três formas típicas de rede (estrela, cadeia, clique) com cinco nós,
lado a lado com a respetiva matriz de adjacência, para mostrar que cada
estrutura deixa um padrão reconhecível na matriz.

Gera assets/images/cap03/padroes-matriz.png
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import math
import sys

sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from sebenta_style import (DARK, MAGENTA, GREY, apply_style, TITLE_SIZE,
                            NODE_LABEL_SIZE, EDGE_WIDTH, REFERENCE_WIDTH)

apply_style()

N = ["1", "2", "3", "4", "5"]
CELL_ON = "#f6d9ec"

star = [("1", n) for n in N[1:]]
chain = [(N[i], N[i + 1]) for i in range(4)]
clique = [(N[i], N[j]) for i in range(5) for j in range(i + 1, 5)]

# posições dos grafos (unidades de dados do painel direito)
ring = {n: (1.6 + 1.25 * math.cos(math.pi / 2 + k * 2 * math.pi / 5),
            1.35 + 1.25 * math.sin(math.pi / 2 + k * 2 * math.pi / 5))
        for k, n in enumerate(N)}
star_pos = {"1": (1.6, 1.35)}
for k, n in enumerate(N[1:]):
    a = math.pi / 4 + k * math.pi / 2
    star_pos[n] = (1.6 + 1.4 * math.cos(a), 1.35 + 1.4 * math.sin(a))
chain_pos = {n: (0.0 + k * 0.8, 1.35) for k, n in enumerate(N)}

panels = [
    ("Estrela", star, star_pos),
    ("Cadeia", chain, chain_pos),
    ("Clique", clique, ring),
]

fig = plt.figure(figsize=(REFERENCE_WIDTH, 11.4), dpi=200)
row_h = 1.0 / 3
R = 0.31

for r, (title, edges, pos) in enumerate(panels):
    bottom = 1 - (r + 1) * row_h
    adj = {(u, v) for u, v in edges} | {(v, u) for u, v in edges}

    # título da linha
    fig.text(0.04, bottom + row_h - 0.008, title, ha="left", va="top",
             fontsize=TITLE_SIZE, fontweight="bold", color=DARK)

    # matriz
    axm = fig.add_axes([0.04, bottom + 0.01, 0.44, row_h - 0.075])
    axm.set_xlim(-0.9, 5.05)
    axm.set_ylim(5.05, -0.9)
    axm.set_aspect("equal")
    axm.axis("off")
    for k, n in enumerate(N):
        axm.text(k + 0.5, -0.45, n, ha="center", va="center",
                 fontsize=NODE_LABEL_SIZE, fontweight="bold", color=DARK)
        axm.text(-0.45, k + 0.5, n, ha="center", va="center",
                 fontsize=NODE_LABEL_SIZE, fontweight="bold", color=DARK)
    for i, a in enumerate(N):
        for j, b in enumerate(N):
            on = (a, b) in adj
            axm.add_patch(Rectangle((j, i), 1, 1, facecolor=CELL_ON if on else "white",
                                    edgecolor=GREY, linewidth=1.5))
            if on:
                axm.text(j + 0.5, i + 0.5, "1", ha="center", va="center",
                         fontsize=NODE_LABEL_SIZE, color=MAGENTA, fontweight="bold")

    # grafo
    axg = fig.add_axes([0.53, bottom + 0.01, 0.44, row_h - 0.075])
    axg.set_xlim(-0.2, 3.4)
    axg.set_ylim(-0.25, 2.95)
    axg.set_aspect("equal")
    axg.axis("off")
    for u, v in edges:
        axg.plot([pos[u][0], pos[v][0]], [pos[u][1], pos[v][1]], color=GREY,
                 linewidth=EDGE_WIDTH, zorder=1, solid_capstyle="round")
    for n, (x, y) in pos.items():
        axg.add_patch(plt.Circle((x, y), R, facecolor=DARK, edgecolor="white",
                                 linewidth=2.2, zorder=3, clip_on=False))
        axg.text(x, y, n, ha="center", va="center", fontsize=NODE_LABEL_SIZE,
                 color="white", fontweight="bold", zorder=4, clip_on=False)

out = "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap03/padroes-matriz.png"
fig.savefig(out, facecolor="white")

if __name__ == "__main__":
    from PIL import Image
    print("tamanho:", Image.open(out).size)
