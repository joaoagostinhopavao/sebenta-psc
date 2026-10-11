"""
Cap. 3: rede com peso, mensagens trocadas numa semana entre seis colegas.
A matriz (no texto) é direcional; o desenho junta os dois sentidos e mostra
o total de mensagens de cada par: a espessura da ligação é proporcional a
esse total. A ligação Carla-Duarte é o laço fraco que faz de ponte.

Gera assets/images/cap03/rede-mensagens.png
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx
import sys

sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from sebenta_style import (DARK, MAGENTA, PINK, GREY, apply_style,
                            NODE_LABEL_SIZE, NOTE_SIZE, REFERENCE_WIDTH)

apply_style()

NAMES = ["Ana", "Bruno", "Carla", "Duarte", "Eva", "Filipe"]
# MSG[i][j] = mensagens enviadas por NAMES[i] a NAMES[j]
MSG = [
    [0, 15, 9, 0, 0, 0],
    [14, 0, 11, 0, 0, 0],
    [8, 12, 0, 1, 0, 0],
    [0, 0, 2, 0, 10, 7],
    [0, 0, 0, 12, 0, 13],
    [0, 0, 0, 6, 11, 0],
]

D = nx.DiGraph()
for i, a in enumerate(NAMES):
    for j, b in enumerate(NAMES):
        if MSG[i][j]:
            D.add_edge(a, b, weight=MSG[i][j])

G = nx.Graph()
for u, v, w in D.edges(data="weight"):
    if G.has_edge(u, v):
        G[u][v]["weight"] += w
    else:
        G.add_edge(u, v, weight=w)

group1 = {"Ana", "Bruno", "Carla"}
pos = {
    "Ana": (0.75, 3.0), "Bruno": (0.75, 0.6), "Carla": (2.85, 1.8),
    "Duarte": (5.15, 1.8), "Eva": (7.25, 3.0), "Filipe": (7.25, 0.6),
}
R = 0.62

fig_w = REFERENCE_WIDTH
xlim, ylim = (0.0, 8.0), (-0.1, 3.7)
fig_h = fig_w * (ylim[1] - ylim[0]) / (xlim[1] - xlim[0])
fig = plt.figure(figsize=(fig_w, fig_h), dpi=200)
ax = fig.add_axes([0.0, 0.0, 1.0, 1.0])
ax.set_xlim(*xlim)
ax.set_ylim(*ylim)
ax.set_aspect("equal")
ax.axis("off")

for u, v, w in G.edges(data="weight"):
    (x1, y1), (x2, y2) = pos[u], pos[v]
    weak = w < 5
    color = MAGENTA if weak else GREY
    lw = 2.5 if weak else 1.5 + w * 0.42
    ax.plot([x1, x2], [y1, y2], color=color, linewidth=lw, zorder=1,
            solid_capstyle="round", linestyle=(0, (2, 1.5)) if weak else "-")
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    ax.text(mx, my, str(w), ha="center", va="center", fontsize=NOTE_SIZE,
            fontweight="bold", color=MAGENTA if weak else DARK, zorder=2,
            bbox=dict(boxstyle="round,pad=0.25", facecolor="white",
                      edgecolor=MAGENTA if weak else GREY, linewidth=1.5))

for v, (x, y) in pos.items():
    face = DARK if v in group1 else PINK
    ax.add_patch(plt.Circle((x, y), R, facecolor=face, edgecolor="white",
                            linewidth=2.2, zorder=3))
    ax.text(x, y, v, ha="center", va="center", fontsize=NODE_LABEL_SIZE,
            color="white", fontweight="bold", zorder=4)

out = "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap03/rede-mensagens.png"
fig.savefig(out, facecolor="white")

if __name__ == "__main__":
    for u, v, w in sorted(G.edges(data="weight"), key=lambda e: -e[2]):
        print(u, v, w)
    U = nx.Graph(G.edges())
    print("pontes:", list(nx.bridges(U)))
    print("arestas:", U.number_of_edges(), "densidade (não-dir.):", round(nx.density(U), 3))
    print("graus:", dict(U.degree()))
    from PIL import Image
    print("tamanho:", Image.open(out).size)
