import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import sys

sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from sebenta_style import (DARK, MAGENTA, PINK, NOTE_COLOR, apply_style,
                            TITLE_SIZE, NODE_LABEL_SIZE, NODE_LABEL_SIZE_HI, NOTE_SIZE,
                            REFERENCE_WIDTH)

apply_style()


def node(ax, xy, label, color=DARK, r=0.17, fontsize=NODE_LABEL_SIZE, textcolor="white"):
    c = Circle(xy, r, facecolor=color, edgecolor="white", linewidth=1.6, zorder=4)
    ax.add_patch(c)
    if label:
        ax.text(xy[0], xy[1], label, ha="center", va="center", fontsize=fontsize,
                color=textcolor, zorder=5, fontweight="bold")


def edge(ax, p1, p2, color=MAGENTA, lw=2.2, alpha=1.0):
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=color, linewidth=lw,
             zorder=2, alpha=alpha, solid_capstyle="round")


fig, axes = plt.subplots(1, 2, figsize=(REFERENCE_WIDTH, 5.9), dpi=200)

# -----------------------------------------------------------------
# Painel 1: Grafo social (ligações explícitas entre pessoas)
# -----------------------------------------------------------------
ax = axes[0]
ax.set_xlim(0, 4); ax.set_ylim(-0.75, 4.35); ax.set_aspect("equal"); ax.axis("off")

people = {
    "A": (0.9, 3.1), "B": (2.3, 3.4), "C": (3.3, 2.6),
    "D": (0.7, 1.6), "E": (2.1, 1.8), "F": (3.2, 1.1), "G": (1.3, 0.5),
}
social_edges = [("A","B"),("B","C"),("A","D"),("B","E"),("D","E"),
                ("E","F"),("E","G"),("D","G")]
for u, v in social_edges:
    edge(ax, people[u], people[v], color=MAGENTA)
for name, xy in people.items():
    node(ax, xy, name, color=DARK, r=0.19, fontsize=NODE_LABEL_SIZE)

ax.set_title("Grafo social", fontsize=TITLE_SIZE, fontweight="bold", color=DARK, pad=14)
ax.text(2.0, -0.55, "ligações explícitas: quem segue quem,\nquem conhece quem",
        ha="center", va="top", fontsize=NOTE_SIZE, color=NOTE_COLOR)

# -----------------------------------------------------------------
# Painel 2: Grafo de interesses (agrupamento por semelhança de conteúdo)
# -----------------------------------------------------------------
ax = axes[1]
ax.set_xlim(0, 4); ax.set_ylim(-0.75, 4.35); ax.set_aspect("equal"); ax.axis("off")

interests = {
    "Desporto": (0.85, 3.15),
    "Culinária": (3.15, 3.15),
    "Tecnologia": (2.0, 0.55),
}
label_side = {"Desporto": "acima", "Culinária": "acima", "Tecnologia": "abaixo"}

users_by_interest = {
    "Desporto": [(0.35, 2.35), (1.35, 2.15), (0.5, 1.55)],
    "Culinária": [(2.65, 2.35), (3.65, 2.15), (3.35, 1.55)],
    "Tecnologia": [(1.35, 0.9), (2.65, 0.9), (2.0, 1.65)],
}

for topic, xy in interests.items():
    for uxy in users_by_interest[topic]:
        edge(ax, xy, uxy, color=PINK, lw=1.9, alpha=0.9)

for topic, xy in interests.items():
    node(ax, xy, "", color=DARK, r=0.22)
    if label_side[topic] == "acima":
        ax.text(xy[0], xy[1] + 0.4, topic, ha="center", va="bottom",
                fontsize=NODE_LABEL_SIZE_HI, color=DARK, fontweight="bold")
    else:
        ax.text(xy[0], xy[1] - 0.4, topic, ha="center", va="top",
                fontsize=NODE_LABEL_SIZE_HI, color=DARK, fontweight="bold")

for topic, pts in users_by_interest.items():
    for uxy in pts:
        node(ax, uxy, "", color=PINK, r=0.11)

ax.set_title("Grafo de interesses", fontsize=TITLE_SIZE, fontweight="bold", color=DARK, pad=14)
ax.text(2.0, -0.55, "agrupamento por comportamento:\nquem consome o quê",
        ha="center", va="top", fontsize=NOTE_SIZE, color=NOTE_COLOR)

fig.tight_layout(rect=[0, 0.02, 1, 1])
# Tela fixa (sem bbox_inches="tight"): garante largura nativa exata =
# REFERENCE_WIDTH * dpi, tal como as restantes ilustrações da sebenta.
fig.savefig("/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap02/grafo-social-vs-interesses.png",
            facecolor="white")
print("done")
