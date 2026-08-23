import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch
import sys

sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from sebenta_style import (DARK, MAGENTA, PINK, GREY, NOTE_COLOR, apply_style,
                            NOTE_SIZE, NODE_LABEL_SIZE_HI, TITLE_SIZE, REFERENCE_WIDTH)

apply_style()

COLUMN_HEADER_SIZE = TITLE_SIZE - 4   # 26
SUPTITLE_SIZE = TITLE_SIZE + 6        # 36
TAG_BASE_SIZE = NODE_LABEL_SIZE_HI    # 23

W, H = REFERENCE_WIDTH, 5.5
fig, ax = plt.subplots(figsize=(W, H), dpi=200)
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.axis("off")

# --- Pessoas -----------------------------------------------------
people_y = [3.4, 2.4, 1.4]
for y in people_y:
    c = Circle((1.15, y), 0.34, facecolor=DARK, edgecolor="white", linewidth=1.6, zorder=3)
    ax.add_patch(c)
ax.text(1.15, 4.25, "Pessoas", ha="center", va="bottom", fontsize=COLUMN_HEADER_SIZE,
        fontweight="bold", color=DARK)
ax.text(1.15, 0.55, "cada uma classifica\nà sua maneira", ha="center", va="top", fontsize=NOTE_SIZE,
        color=NOTE_COLOR, style="italic")

# --- Etiquetas (tags) ---------------------------------------------
tags = ["ficção", "azul", "2024", "viagem", "praia"]
tag_positions = [(5.15, 3.65), (6.05, 3.05), (4.7, 2.65), (5.6, 1.85), (5.0, 1.3)]
tag_sizes = [TAG_BASE_SIZE, TAG_BASE_SIZE - 3, TAG_BASE_SIZE - 4, TAG_BASE_SIZE - 2, TAG_BASE_SIZE - 4]
for (x, y), txt, fs in zip(tag_positions, tags, tag_sizes):
    box = FancyBboxPatch((x - 0.03, y - 0.2), 0.06 + 0.175 * len(txt), 0.4,
                          boxstyle="round,pad=0.02,rounding_size=0.17",
                          facecolor=MAGENTA, edgecolor="none", zorder=3)
    ax.add_patch(box)
    ax.text(x + 0.03 + 0.0875 * len(txt), y, txt, ha="center", va="center",
            fontsize=fs, color="white", fontweight="bold", zorder=4)
ax.text(5.4, 4.25, "Etiquetas (tags)", ha="center", va="bottom", fontsize=COLUMN_HEADER_SIZE,
        fontweight="bold", color=DARK)
ax.text(5.4, 0.55, "vocabulário livre,\nsem hierarquia prévia", ha="center", va="top", fontsize=NOTE_SIZE,
        color=NOTE_COLOR, style="italic")

# --- Objetos -------------------------------------------------------
obj_y = [3.4, 2.4, 1.4]
for y in obj_y:
    box = FancyBboxPatch((9.65, y - 0.3), 0.9, 0.6, boxstyle="round,pad=0.02,rounding_size=0.09",
                          facecolor=DARK, edgecolor="none", zorder=3)
    ax.add_patch(box)
ax.text(10.1, 4.25, "Objetos", ha="center", va="bottom", fontsize=COLUMN_HEADER_SIZE,
        fontweight="bold", color=DARK)
ax.text(10.1, 0.55, "documentos, fotos,\npublicações", ha="center", va="top", fontsize=NOTE_SIZE,
        color=NOTE_COLOR, style="italic")

# --- setas -----------------------------------------------------
arrow1 = FancyArrowPatch((1.6, 2.4), (4.3, 2.4), arrowstyle="-|>", mutation_scale=24,
                          color=GREY, linewidth=2.4, zorder=1, connectionstyle="arc3,rad=0")
arrow2 = FancyArrowPatch((7.05, 2.4), (9.5, 2.4), arrowstyle="-|>", mutation_scale=24,
                          color=GREY, linewidth=2.4, zorder=1, connectionstyle="arc3,rad=0")
ax.add_patch(arrow1)
ax.add_patch(arrow2)

fig.suptitle("O Processo de Marcação (Tagging)", fontsize=SUPTITLE_SIZE, fontweight="bold",
             color=DARK, y=0.98)
fig.tight_layout(rect=[0, 0.02, 1, 0.86])
# Tela fixa (sem bbox_inches="tight"): garante largura nativa exata =
# REFERENCE_WIDTH * dpi.
fig.savefig("/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap03/processo-tagging.png",
            facecolor="white")
print("done")
