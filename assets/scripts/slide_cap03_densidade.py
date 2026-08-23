import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import itertools, math, sys

sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from sebenta_style import (DARK, MAGENTA, PINK, GREY, NOTE_COLOR, apply_style,
                            SLIDE_TITLE_SIZE, SLIDE_NODE_LABEL_SIZE, SLIDE_NODE_LABEL_SIZE_HI,
                            SLIDE_NOTE_SIZE, SLIDE_BIG_NUMBER_SIZE, SLIDE_NODE_RADIUS,
                            SLIDE_NODE_RADIUS_HI, SLIDE_EDGE_WIDTH, SLIDE_EDGE_WIDTH_HI,
                            SLIDE_REFERENCE_WIDTH)

apply_style()

nodes = ["A", "B", "C", "D", "E"]
all_pairs = list(itertools.combinations(nodes, 2))

pos = {}
R = 1.5
for i, n in enumerate(nodes):
    ang = math.pi/2 + i * (2*math.pi/5)
    pos[n] = (R*math.cos(ang), R*math.sin(ang))

panels = [
    ("Densidade baixa", [("A","B"), ("C","E"), ("B","D")]),
    ("Densidade média", [("A","B"), ("A","C"), ("A","E"), ("B","D"), ("C","D"), ("C","E")]),
    ("Densidade máxima", all_pairs),
]

fig, axes = plt.subplots(1, 3, figsize=(SLIDE_REFERENCE_WIDTH, 6.4), dpi=200)

for ax, (title, active) in zip(axes, panels):
    ax.set_xlim(-2.0, 2.0)
    ax.set_ylim(-2.5, 1.95)
    ax.set_aspect("equal")
    ax.axis("off")

    active_set = set(frozenset(e) for e in active)

    for u, v in all_pairs:
        if frozenset((u, v)) not in active_set:
            ax.plot([pos[u][0], pos[v][0]], [pos[u][1], pos[v][1]], color=GREY,
                     linewidth=SLIDE_EDGE_WIDTH * 0.7, linestyle=(0, (5, 4)), zorder=1)

    for u, v in active:
        ax.plot([pos[u][0], pos[v][0]], [pos[u][1], pos[v][1]], color=MAGENTA,
                 linewidth=SLIDE_EDGE_WIDTH_HI, solid_capstyle="round", zorder=2)

    for n in nodes:
        x, y = pos[n]
        is_d = (n == "D")
        r = SLIDE_NODE_RADIUS_HI if is_d else SLIDE_NODE_RADIUS
        color = MAGENTA if is_d else DARK
        circle = plt.Circle((x, y), r, facecolor=color, edgecolor="white", linewidth=2.2, zorder=3)
        ax.add_patch(circle)
        ax.text(x, y, n, ha="center", va="center",
                fontsize=SLIDE_NODE_LABEL_SIZE_HI if is_d else SLIDE_NODE_LABEL_SIZE,
                color="white", fontweight="bold", zorder=4)

    d_degree = sum(1 for u, v in active if "D" in (u, v))
    density_d = d_degree / 4

    ax.set_title(title, fontsize=SLIDE_TITLE_SIZE, fontweight="bold", color=DARK, pad=16)
    ax.text(0, -1.95, f"{density_d:.2f}".replace(".", ","), ha="center", va="center",
            fontsize=SLIDE_BIG_NUMBER_SIZE, fontweight="bold", color=PINK)
    ax.text(0, -2.35, f"D tem {d_degree} das 4 ligações possíveis",
            ha="center", va="top", fontsize=SLIDE_NOTE_SIZE, color=NOTE_COLOR, style="italic")

fig.tight_layout(w_pad=3.0)
fig.savefig("/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap03/slides/densidade-slide.png",
            facecolor="white")
print("done")
