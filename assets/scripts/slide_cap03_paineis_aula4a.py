"""
Painéis verticais (2:3) para dois slides da Aula 4a, no lugar das imagens
de folksonomia:

- paineis-grafo-metricas-slide.png: do grafo de interesses ao grafo social
  e às métricas (slide "Do Grafo de Interesses às Métricas");
- paineis-pergunta-sociograma-slide.png: da pergunta à matriz e ao
  sociograma (slide "Análise de Redes Sociais (SNA)").

Gera os dois ficheiros em assets/images/cap03/slides/
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import networkx as nx
import math
import os
import sys

sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from sebenta_style import DARK, MAGENTA, PINK, GREY, NOTE_COLOR, apply_style

apply_style()
OUT = "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap03/slides"
W, H = 5.0, 7.5
LABEL = 22


def canvas():
    fig = plt.figure(figsize=(W, H), dpi=288)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 15)
    ax.set_aspect("equal")
    ax.axis("off")
    return fig, ax


def node(ax, x, y, r, label=None, color=DARK, size=17):
    ax.add_patch(plt.Circle((x, y), r, color=color, zorder=3))
    if label:
        ax.text(x, y, label, ha="center", va="center", color="white",
                fontsize=size, fontweight="bold", zorder=4)


def edge(ax, p, q, color=MAGENTA, lw=3.0, r1=0.0, r2=0.0, arrow=None):
    (x1, y1), (x2, y2) = p, q
    d = math.hypot(x2 - x1, y2 - y1)
    ux, uy = (x2 - x1) / d, (y2 - y1) / d
    a = (x1 + ux * r1, y1 + uy * r1)
    b = (x2 - ux * r2, y2 - uy * r2)
    if arrow:
        ax.add_patch(FancyArrowPatch(a, b, arrowstyle=arrow, mutation_scale=16,
                                     color=color, linewidth=lw, zorder=1))
    else:
        ax.plot([a[0], b[0]], [a[1], b[1]], color=color, linewidth=lw, zorder=1)


def down_arrow(ax, y_top, y_bottom):
    ax.add_patch(FancyArrowPatch((5, y_top), (5, y_bottom), arrowstyle="-|>",
                                 mutation_scale=28, color=GREY, linewidth=4))


def label(ax, y, text):
    ax.text(5, y, text, ha="center", va="center", fontsize=LABEL,
            color=DARK, fontweight="bold")


# ------------------------------------------------------------------
# 1. Grafo de interesses -> grafo social -> métricas
# ------------------------------------------------------------------
fig, ax = canvas()

label(ax, 14.4, "Grafo de interesses")
topic = (5, 12.3)
node(ax, *topic, 0.55)
for ang in (200, 245, 295, 340):
    p = (topic[0] + 2.0 * math.cos(math.radians(ang)) * 1.3,
         topic[1] + 1.6 * math.sin(math.radians(ang)) * 0.6 + 0.2)
    edge(ax, topic, p, color=PINK, lw=2.6)
    ax.add_patch(plt.Circle(p, 0.25, color=PINK, zorder=3))
ax.text(5, 13.35, "tema", ha="center", va="center", fontsize=15, color=NOTE_COLOR)

down_arrow(ax, 11.1, 10.4)

label(ax, 9.9, "Grafo social")
G = nx.Graph([("A", "B"), ("A", "D"), ("B", "C"), ("B", "E"), ("D", "E"),
              ("D", "G"), ("E", "G"), ("E", "F")])
pos = {"A": (2.6, 8.5), "B": (5.0, 8.9), "C": (7.5, 8.5), "D": (2.4, 6.6),
       "E": (5.2, 7.1), "F": (7.7, 6.3), "G": (3.9, 5.3)}
for u, v in G.edges():
    edge(ax, pos[u], pos[v])
bet = nx.betweenness_centrality(G)
for v, (x, y) in pos.items():
    node(ax, x, y, 0.42 if v != "E" else 0.55, v,
         color=MAGENTA if v == "E" else DARK, size=17 if v != "E" else 20)

down_arrow(ax, 4.75, 4.05)

label(ax, 3.55, "Métricas")
top = sorted(bet.items(), key=lambda kv: -kv[1])[:3]
for i, (v, val) in enumerate(top):
    y = 2.55 - i * 0.72
    ax.text(1.4, y, v, ha="center", va="center", fontsize=17, color=DARK, fontweight="bold")
    ax.add_patch(FancyBboxPatch((2.0, y - 0.22), 5.6 * val / top[0][1], 0.44,
                                boxstyle="round,pad=0,rounding_size=0.12",
                                color=MAGENTA if i == 0 else GREY, zorder=2))
    ax.text(2.0 + 5.6 * val / top[0][1] + 0.25, y, f"{val:.2f}".replace(".", ","),
            ha="left", va="center", fontsize=16, color=DARK)
ax.text(5, 0.45, "intermediação dos três primeiros", ha="center", va="center",
        fontsize=14, color=NOTE_COLOR)
print("intermediação:", {k: round(v, 2) for k, v in bet.items()})

fig.savefig(os.path.join(OUT, "paineis-grafo-metricas-slide.png"), facecolor="white")
plt.close(fig)

# ------------------------------------------------------------------
# 2. Pergunta -> matriz -> sociograma
# ------------------------------------------------------------------
fig, ax = canvas()
CH = {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "D"], "D": ["C", "E"], "E": ["D", "C"]}
N = list("ABCDE")

label(ax, 14.4, "Pergunta")
ax.add_patch(FancyBboxPatch((0.9, 11.85), 8.2, 2.0, boxstyle="round,pad=0,rounding_size=0.35",
                            facecolor="#f6e3f1", edgecolor=MAGENTA, linewidth=2.2))
ax.text(5, 12.85, "Com que dois colegas\ngostarias de trabalhar?", ha="center", va="center",
        fontsize=17, color=DARK, linespacing=1.3)

down_arrow(ax, 11.6, 10.95)

label(ax, 10.45, "Matriz")
cell, x0, y0 = 0.74, 3.35, 9.5
for j, c in enumerate(N):
    ax.text(x0 + (j + 0.5) * cell, y0 + 0.05, c, ha="center", va="bottom", fontsize=14,
            color=NOTE_COLOR, fontweight="bold")
for i, r in enumerate(N):
    yy = y0 - (i + 1) * cell
    ax.text(x0 - 0.35, yy + cell / 2, r, ha="center", va="center", fontsize=14,
            color=NOTE_COLOR, fontweight="bold")
    for j, c in enumerate(N):
        on = c in CH[r]
        ax.add_patch(plt.Rectangle((x0 + j * cell, yy), cell, cell, facecolor=MAGENTA if on else "white",
                                   edgecolor=GREY, linewidth=1.5))
        if on:
            ax.text(x0 + (j + 0.5) * cell, yy + cell / 2, "1", ha="center", va="center",
                    fontsize=14, color="white", fontweight="bold")

down_arrow(ax, 5.55, 4.85)

label(ax, 4.35, "Sociograma")
spos = {"A": (2.0, 3.0), "B": (1.6, 1.0), "C": (4.9, 2.0), "D": (7.4, 3.0), "E": (8.2, 1.0)}
indeg = {v: sum(v in CH[u] for u in N) for v in N}
rad = {v: 0.32 + 0.07 * indeg[v] for v in N}
done = set()
for u in N:
    for v in CH[u]:
        k = frozenset((u, v))
        if k in done:
            continue
        done.add(k)
        mutual = u in CH[v]
        edge(ax, spos[u], spos[v], color=MAGENTA if mutual else "#8c8094", lw=2.4,
             r1=rad[u] + 0.05, r2=rad[v] + 0.05, arrow="<|-|>" if mutual else "-|>")
for v in N:
    node(ax, *spos[v], rad[v], v, size=15)

fig.savefig(os.path.join(OUT, "paineis-pergunta-sociograma-slide.png"), facecolor="white")
plt.close(fig)
print("ok")
