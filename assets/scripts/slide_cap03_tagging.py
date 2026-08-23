import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch
import sys

sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from sebenta_style import (DARK, MAGENTA, PINK, GREY, NOTE_COLOR, apply_style,
                            SLIDE_NOTE_SIZE, SLIDE_NODE_LABEL_SIZE_HI, SLIDE_TITLE_SIZE,
                            SLIDE_REFERENCE_WIDTH)

apply_style()

COLUMN_HEADER_SIZE = SLIDE_TITLE_SIZE - 4
SUPTITLE_SIZE = SLIDE_TITLE_SIZE + 8
TAG_BASE_SIZE = SLIDE_NODE_LABEL_SIZE_HI + 4

W, H = SLIDE_REFERENCE_WIDTH, 6.0
fig, ax = plt.subplots(figsize=(W, H), dpi=200)
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.axis("off")

# --- Pessoas -----------------------------------------------------
people_y = [3.7, 2.6, 1.5]
for y in people_y:
    c = Circle((1.4, y), 0.4, facecolor=DARK, edgecolor="white", linewidth=1.8, zorder=3)
    ax.add_patch(c)
ax.text(1.4, 4.65, "Pessoas", ha="center", va="bottom", fontsize=COLUMN_HEADER_SIZE,
        fontweight="bold", color=DARK)
ax.text(1.4, 0.65, "cada uma classifica\nà sua maneira", ha="center", va="top", fontsize=SLIDE_NOTE_SIZE,
        color=NOTE_COLOR, style="italic")

# --- Etiquetas (tags) ---------------------------------------------
tags = ["ficção", "azul", "2024", "viagem", "praia"]
tag_positions = [(6.3, 4.0), (7.4, 3.3), (5.8, 2.9), (6.9, 2.0), (6.1, 1.4)]
tag_sizes = [TAG_BASE_SIZE, TAG_BASE_SIZE - 3, TAG_BASE_SIZE - 4, TAG_BASE_SIZE - 2, TAG_BASE_SIZE - 4]
for (x, y), txt, fs in zip(tag_positions, tags, tag_sizes):
    box = FancyBboxPatch((x - 0.05, y - 0.24), 0.1 + 0.21 * len(txt), 0.48,
                          boxstyle="round,pad=0.02,rounding_size=0.2",
                          facecolor=MAGENTA, edgecolor="none", zorder=3)
    ax.add_patch(box)
    ax.text(x + 0.05 + 0.105 * len(txt), y, txt, ha="center", va="center",
            fontsize=fs, color="white", fontweight="bold", zorder=4)
ax.text(6.6, 4.65, "Etiquetas (tags)", ha="center", va="bottom", fontsize=COLUMN_HEADER_SIZE,
        fontweight="bold", color=DARK)
ax.text(6.6, 0.65, "vocabulário livre,\nsem hierarquia prévia", ha="center", va="top", fontsize=SLIDE_NOTE_SIZE,
        color=NOTE_COLOR, style="italic")

# --- Objetos -------------------------------------------------------
obj_y = [3.7, 2.6, 1.5]
for y in obj_y:
    box = FancyBboxPatch((11.7, y - 0.35), 1.05, 0.7, boxstyle="round,pad=0.02,rounding_size=0.1",
                          facecolor=DARK, edgecolor="none", zorder=3)
    ax.add_patch(box)
ax.text(12.25, 4.65, "Objetos", ha="center", va="bottom", fontsize=COLUMN_HEADER_SIZE,
        fontweight="bold", color=DARK)
ax.text(12.25, 0.65, "documentos, fotos,\npublicações", ha="center", va="top", fontsize=SLIDE_NOTE_SIZE,
        color=NOTE_COLOR, style="italic")

# --- setas -----------------------------------------------------
arrow1 = FancyArrowPatch((1.95, 2.6), (5.15, 2.6), arrowstyle="-|>", mutation_scale=30,
                          color=GREY, linewidth=3.0, zorder=1, connectionstyle="arc3,rad=0")
arrow2 = FancyArrowPatch((8.55, 2.6), (11.55, 2.6), arrowstyle="-|>", mutation_scale=30,
                          color=GREY, linewidth=3.0, zorder=1, connectionstyle="arc3,rad=0")
ax.add_patch(arrow1)
ax.add_patch(arrow2)

fig.suptitle("O Processo de Marcação (Tagging)", fontsize=SUPTITLE_SIZE, fontweight="bold",
             color=DARK, y=0.99)
fig.tight_layout(rect=[0, 0.02, 1, 0.85])
fig.savefig("/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap03/slides/processo-tagging-slide.png",
            facecolor="white")
print("done")
