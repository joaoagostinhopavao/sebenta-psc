"""
Figura 3.x: sociograma da turma fictícia usada no exemplo trabalhado do
Cap. 3 (pergunta sociométrica "Com que dois colegas gostarias de fazer o
próximo trabalho de grupo?"). As métricas citadas no texto são calculadas
com networkx a partir destas mesmas escolhas (ver bloco final).

Convenções visuais:
- tamanho do nó proporcional ao grau de entrada (popularidade)
- cor do nó = sub-rede (comunidade) a que pertence
- ligações a magenta = pontes (cuja remoção desliga a rede)
- seta dupla = escolha recíproca; seta simples = escolha não retribuída
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import networkx as nx
import math
import sys

sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from sebenta_style import (DARK, MAGENTA, PINK, GREY, NOTE_COLOR, apply_style,
                            NODE_LABEL_SIZE, NOTE_SIZE, EDGE_WIDTH, EDGE_WIDTH_HI,
                            REFERENCE_WIDTH)

apply_style()

ARCS = [("A", "B"), ("A", "C"), ("B", "A"), ("B", "C"), ("C", "A"), ("C", "B"),
        ("D", "A"), ("D", "C"), ("E", "C"), ("E", "F"), ("F", "E"), ("F", "G"),
        ("G", "F"), ("G", "H"), ("H", "F"), ("H", "G"), ("I", "A"), ("I", "D")]

D = nx.DiGraph(ARCS)
U = D.to_undirected()
bridges = {frozenset(e) for e in nx.bridges(U)}
group1 = {"A", "B", "C", "D", "I"}

pos = {
    "A": (1.4, 1.9), "B": (0.7, 3.7), "C": (3.2, 3.0), "D": (2.7, 0.5),
    "I": (0.0, 0.6), "E": (5.0, 3.0), "F": (6.8, 3.0), "G": (8.2, 4.0),
    "H": (8.2, 1.6),
}


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
    is_bridge = key in bridges
    color = MAGENTA if is_bridge else GREY
    lw = EDGE_WIDTH_HI if is_bridge else EDGE_WIDTH
    style = "<|-|>" if mutual else "-|>"
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle=style, mutation_scale=26,
                                 color=color, linewidth=lw, zorder=1))

for v, (x, y) in pos.items():
    face = DARK if v in group1 else PINK
    ax.add_patch(plt.Circle((x, y), radius(v), facecolor=face, edgecolor="white",
                            linewidth=2.2, zorder=3))
    ax.text(x, y, v, ha="center", va="center", fontsize=NODE_LABEL_SIZE + 4,
            color="white", fontweight="bold", zorder=4)


out = "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap03/sociograma-turma.png"
fig.savefig(out, facecolor="white")

if __name__ == "__main__":
    n = D.number_of_nodes()
    print("densidade rede (dirigida):", nx.density(D))
    print("reciprocidade:", nx.reciprocity(D))
    print("diâmetro:", nx.diameter(U), "caminho médio:", nx.average_shortest_path_length(U))
    print("pontes:", sorted(tuple(sorted(b)) for b in bridges))
    bt = nx.betweenness_centrality(U)
    cl = nx.closeness_centrality(U)
    ev = nx.eigenvector_centrality(U, max_iter=1000)
    cc = nx.clustering(U)
    for v in sorted(D):
        print(v, D.in_degree(v), D.out_degree(v), U.degree(v), round(U.degree(v) / (n - 1), 2),
              round(bt[v], 2), round(cl[v], 2), round(ev[v], 2), round(cc[v], 2))
    from PIL import Image
    print("tamanho:", Image.open(out).size)
