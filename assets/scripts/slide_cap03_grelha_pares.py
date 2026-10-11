"""
Grelha de pares da intermediação para o aluno E (rede da turma): linhas e
colunas com os 8 colegas sem E, só a metade de cima preenchida com 1, ½ ou
0, e a soma de cada linha à direita.

Gera assets/images/cap03/slides/grelha-pares-E-slide.png
"""
import itertools
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx

sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from sebenta_style import DARK, MAGENTA, GREY, NOTE_COLOR, apply_style

apply_style()

ARCS = [("A", "B"), ("A", "C"), ("B", "A"), ("B", "C"), ("C", "A"), ("C", "B"),
        ("D", "A"), ("D", "C"), ("E", "C"), ("E", "F"), ("F", "E"), ("F", "G"),
        ("G", "F"), ("G", "H"), ("H", "F"), ("H", "G"), ("I", "A"), ("I", "D")]
U = nx.DiGraph(ARCS).to_undirected()
V = "E"
others = [x for x in sorted(U) if x != V]
g = {}
for s, t in itertools.combinations(others, 2):
    paths = list(nx.all_shortest_paths(U, s, t))
    g[(s, t)] = sum(V in p[1:-1] for p in paths) / len(paths)

n = len(others)
fig = plt.figure(figsize=(6.2, 5.6), dpi=250)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(-1.1, n + 1.6)
ax.set_ylim(-1.3, n + 1.0)
ax.set_aspect("equal")
ax.axis("off")


def cell(i, j, face, text=None, color=DARK, bold=False):
    y = n - 1 - i
    ax.add_patch(plt.Rectangle((j, y), 1, 1, facecolor=face, edgecolor="#b9b0bf", linewidth=1.2))
    if text is not None:
        ax.text(j + 0.5, y + 0.5, text, ha="center", va="center", fontsize=17,
                color=color, fontweight="bold" if bold else "normal")


for k, c in enumerate(others):
    ax.text(k + 0.5, n + 0.4, c, ha="center", va="center", fontsize=17, color=DARK, fontweight="bold")
    ax.text(-0.5, n - 1 - k + 0.5, c, ha="center", va="center", fontsize=17, color=DARK, fontweight="bold")

for i, r in enumerate(others):
    row = 0
    for j, c in enumerate(others):
        if j < i:
            cell(i, j, "#efedf1")
        elif j == i:
            cell(i, j, GREY)
        else:
            v = g[(r, c)]
            row += v
            txt = {0: "0", 1: "1", 0.5: "½"}[v]
            if v:
                cell(i, j, "#f3c6e4", txt, color=MAGENTA, bold=True)
            else:
                cell(i, j, "white", txt, color="#9a90a0")
    if i < n - 1:
        ax.text(n + 0.75, n - 1 - i + 0.5, f"{row:g}", ha="center", va="center",
                fontsize=16, color=NOTE_COLOR)

ax.text(n + 0.75, n + 0.4, "soma", ha="center", va="center", fontsize=13, color=NOTE_COLOR)
total = sum(g.values())
ax.text(n / 2, -0.7, f"Intermediação: {total:g} ÷ 28 ≈ {total / 28:.2f}".replace(".", ","),
        ha="center", va="center", fontsize=18, color=DARK, fontweight="bold")

out = "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap03/slides/grelha-pares-E-slide.png"
fig.savefig(out, facecolor="white")
print(out, total)
