import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle
import sys

sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from sebenta_style import (DARK, MAGENTA, PINK, GREY, NOTE_COLOR, apply_style,
                            TITLE_SIZE, NODE_LABEL_SIZE_HI, NOTE_SIZE, REFERENCE_WIDTH)

apply_style()

panels = [
    ("Sem relação", "none", "A e B não têm ligação"),
    ("Não-direcional", "undirected", "ex.: amizade no Facebook"),
    ("Direcional", "directed", "ex.: seguir no Instagram ou no X"),
    ("Direcional mútuo", "mutual", "A segue B e B segue A"),
]

# Grelha 2x2 (em vez de 1x4) para que a largura total da figura fique
# igual a REFERENCE_WIDTH -- ver sebenta_style.scale_for para o porquê.
fig, axes = plt.subplots(2, 2, figsize=(REFERENCE_WIDTH, 8.4), dpi=200)
axes = axes.flatten()

R = 0.46
XA, XB = 1.1, 3.9
Y = 1.5

def node(ax, x, label):
    c = Circle((x, Y), R, facecolor=DARK, edgecolor="white", linewidth=1.8, zorder=3)
    ax.add_patch(c)
    ax.text(x, Y, label, ha="center", va="center", fontsize=NODE_LABEL_SIZE_HI, color="white",
            fontweight="bold", zorder=4)

for ax, (title, kind, note) in zip(axes, panels):
    ax.set_xlim(0, 5.0)
    ax.set_ylim(0, 3.3)
    ax.set_aspect("equal")
    ax.axis("off")

    if kind == "none":
        pass
    elif kind == "undirected":
        ax.plot([XA + R, XB - R], [Y, Y], color=MAGENTA, linewidth=3.4, solid_capstyle="round", zorder=1)
    elif kind == "directed":
        arrow = FancyArrowPatch((XA + R, Y), (XB - R, Y), arrowstyle="-|>",
                                 mutation_scale=30, color=MAGENTA, linewidth=3.4, zorder=1)
        ax.add_patch(arrow)
    elif kind == "mutual":
        arrow1 = FancyArrowPatch((XA + R, Y + 0.17), (XB - R, Y + 0.17), arrowstyle="-|>",
                                  mutation_scale=27, color=MAGENTA, linewidth=3.0, zorder=1)
        arrow2 = FancyArrowPatch((XB - R, Y - 0.17), (XA + R, Y - 0.17), arrowstyle="-|>",
                                  mutation_scale=27, color=PINK, linewidth=3.0, zorder=1)
        ax.add_patch(arrow1)
        ax.add_patch(arrow2)

    node(ax, XA, "A")
    node(ax, XB, "B")

    ax.set_title(title, fontsize=TITLE_SIZE, fontweight="bold", color=DARK, pad=18)
    ax.text(2.5, 0.55, note, ha="center", va="top", fontsize=NOTE_SIZE, color=NOTE_COLOR, style="italic")

fig.tight_layout(h_pad=3.0, w_pad=2.0)
# Tela fixa (sem bbox_inches="tight"): garante largura nativa exata =
# REFERENCE_WIDTH * dpi, sem cortes dependentes do rácio de aspeto.
fig.savefig("/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap03/tipos-relacao.png",
            facecolor="white")
print("done")
