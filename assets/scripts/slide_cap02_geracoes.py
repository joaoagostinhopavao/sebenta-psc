import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import sys

sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from sebenta_style import (DARK, MAGENTA, PINK, apply_style, SLIDE_TITLE_SIZE,
                            SLIDE_NODE_LABEL_SIZE_HI, SLIDE_REFERENCE_WIDTH)
from logo_utils import normalize

apply_style()


gens = {
    "1.ª geração: comunicação pessoal": [("icq", "ICQ"), ("msn", "MSN Messenger")],
    "2.ª geração: redes de afinidade": [("orkut", "Orkut"), ("friendster", "Friendster"),
                                         ("myspace", "MySpace"), ("facebook", "Facebook"),
                                         ("linkedin", "LinkedIn")],
}

fig, ax = plt.subplots(figsize=(SLIDE_REFERENCE_WIDTH, 6.2), dpi=200)
ax.set_xlim(0, SLIDE_REFERENCE_WIDTH); ax.set_ylim(0, 5.0); ax.axis("off")

col_x = {0: 3.0, 1: 9.8}

for col, (title, apps) in enumerate(gens.items()):
    cx = col_x[col]
    ax.text(cx, 4.75, title, ha="center", va="top", fontsize=SLIDE_TITLE_SIZE * 0.85,
            fontweight="bold", color=DARK)

    n = len(apps)
    gap = 1.6 if col == 0 else 1.35
    total_w = (n - 1) * gap
    start_x = cx - total_w / 2

    for i, (app, label) in enumerate(apps):
        x = start_x + i * gap
        y = 2.75
        norm_path = normalize(app)
        if norm_path:
            img = mpimg.imread(norm_path)
            imagebox = OffsetImage(img, zoom=0.32)
            ab = AnnotationBbox(imagebox, (x, y), frameon=False)
            ax.add_artist(ab)
        ax.text(x, y - 1.0, label, ha="center", va="top", fontsize=SLIDE_NODE_LABEL_SIZE_HI * 0.75,
                color=DARK)

    accent = MAGENTA if col == 0 else PINK
    ax.plot([cx - total_w/2 - 0.85, cx + total_w/2 + 0.85], [1.15, 1.15],
             color=accent, linewidth=3.4, solid_capstyle="round")

ax.plot([6.4, 6.4], [0.6, 4.5], color="#ddd0e0", linewidth=1.4, linestyle=(0, (4, 3)))
ax.annotate("", xy=(7.0, 2.75), xytext=(5.8, 2.75),
            arrowprops=dict(arrowstyle="-|>", color="#8a7c90", lw=1.8))

fig.suptitle("As Gerações de Redes Sociais na Web", fontsize=SLIDE_TITLE_SIZE, fontweight="bold",
             color=DARK, y=0.98)
fig.tight_layout(rect=[0, 0.02, 1, 0.82])
fig.savefig("/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap02/slides/geracoes-icones-slide.png",
            facecolor="white")
print("done")
