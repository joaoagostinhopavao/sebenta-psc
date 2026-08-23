import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx
import math
import sys

sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from sebenta_style import (DARK, MAGENTA, PINK, GREY, NOTE_COLOR, apply_style,
                            SLIDE_TITLE_SIZE, SLIDE_NODE_LABEL_SIZE, SLIDE_NODE_LABEL_SIZE_HI,
                            SLIDE_NOTE_SIZE, SLIDE_NODE_RADIUS, SLIDE_NODE_RADIUS_HI,
                            SLIDE_REFERENCE_WIDTH)

apply_style()

def draw_graph(ax, edges, pos, highlight, node_font=SLIDE_NODE_LABEL_SIZE, hi_font=SLIDE_NODE_LABEL_SIZE_HI,
               r=SLIDE_NODE_RADIUS, hi_r=SLIDE_NODE_RADIUS_HI):
    for u, v in edges:
        hi = (u in highlight or v in highlight)
        color = PINK if hi else GREY
        lw = 4.6 if hi else 3.2
        ax.plot([pos[u][0], pos[v][0]], [pos[u][1], pos[v][1]], color=color, linewidth=lw,
                 zorder=1, solid_capstyle="round")
    for n, (x, y) in pos.items():
        is_hi = n in highlight
        rad = hi_r if is_hi else r
        color = MAGENTA if is_hi else DARK
        circle = plt.Circle((x, y), rad, facecolor=color, edgecolor="white", linewidth=2.2, zorder=3)
        ax.add_patch(circle)
        ax.text(x, y, n, ha="center", va="center", fontsize=hi_font if is_hi else node_font,
                color="white", fontweight="bold", zorder=4)

# Painel 1: GRAU -- estrela
leaves1 = ["L1", "L2", "L3", "L4", "L5", "L6"]
edges1 = [("H", leaf) for leaf in leaves1]
pos1 = {"H": (2.5, 1.1)}
R1 = 1.75
for i, leaf in enumerate(leaves1):
    ang = math.pi/2 + i * (2*math.pi/6)
    pos1[leaf] = (2.5 + R1*math.cos(ang), 1.1 + R1*math.sin(ang)*0.85)
highlight1 = {"H"}

# Painel 2: INTERMEDIAÇÃO -- ponte
edges2 = [("A","B"), ("A","C"), ("B","C"),
          ("D","E"), ("D","F"), ("E","F"),
          ("A","X"), ("X","D")]
pos2 = {
    "B": (0.3, 1.5), "C": (0.3, 0.3), "A": (1.4, 0.9),
    "X": (2.5, 0.9),
    "D": (3.6, 0.9), "E": (4.7, 1.5), "F": (4.7, 0.3),
}
highlight2 = {"X"}

# Painel 3: PROXIMIDADE -- cadeia
chain = ["A", "B", "C", "D", "E", "F", "G"]
edges3 = [(chain[i], chain[i+1]) for i in range(len(chain)-1)]
pos3 = {n: (0.3 + i*0.75, 1.1) for i, n in enumerate(chain)}
highlight3 = {"D"}

panels = [
    ("Grau", edges1, pos1, highlight1,
     "H liga-se diretamente a todos; os\nrestantes têm apenas uma ligação"),
    ("Intermediação", edges2, pos2, highlight2,
     "X está no único caminho entre os\ndois grupos, com poucas ligações diretas"),
    ("Proximidade", edges3, pos3, highlight3,
     "D está, em média, mais perto de\ntodos os outros nós da cadeia"),
]

fig, axes = plt.subplots(1, 3, figsize=(SLIDE_REFERENCE_WIDTH, 6.3), dpi=200)

xlims = [(0.3, 4.7), (-0.4, 5.0), (-0.3, 5.1)]
ylims = [(-1.05, 3.1), (-0.5, 2.15), (0.1, 2.1)]

for ax, (title, edges, pos, highlight, note), xlim, ylim in zip(axes, panels, xlims, ylims):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.axis("off")

    draw_graph(ax, edges, pos, highlight)

    ax.set_title(title, fontsize=SLIDE_TITLE_SIZE, fontweight="bold", color=DARK, pad=14,
                 loc="left", x=0.0)
    ax.text(0.0, -0.02, note, ha="left", va="top", fontsize=SLIDE_NOTE_SIZE, color=NOTE_COLOR,
            style="italic", transform=ax.transAxes)

fig.suptitle("Centralidade: três medidas", fontsize=SLIDE_TITLE_SIZE + 6, fontweight="bold",
             color=DARK, x=0.02, ha="left", y=0.98)
fig.tight_layout(rect=[0, 0, 1, 0.85], w_pad=2.5)
fig.savefig("/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap03/slides/centralidade-slide.png",
            facecolor="white")
print("done")
