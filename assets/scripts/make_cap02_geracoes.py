import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import sys

sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from sebenta_style import (DARK, MAGENTA, PINK, apply_style, TITLE_SIZE, NODE_LABEL_SIZE_HI,
                            REFERENCE_WIDTH)
from logo_utils import normalize

apply_style()

gens = {
    "1.ª geração: comunicação pessoal": [("icq", "ICQ"), ("msn", "MSN Messenger")],
    "2.ª geração: redes de afinidade": [("orkut", "Orkut"), ("friendster", "Friendster"),
                                         ("myspace", "MySpace"), ("facebook", "Facebook"),
                                         ("linkedin", "LinkedIn")],
}

fig, ax = plt.subplots(figsize=(REFERENCE_WIDTH, 5.8), dpi=200)
ax.set_xlim(0, REFERENCE_WIDTH); ax.set_ylim(0, 5.0); ax.axis("off")

col_x = {0: 2.6, 1: 8.2}

for col, (title, apps) in enumerate(gens.items()):
    cx = col_x[col]
    ax.text(cx, 4.75, title, ha="center", va="top", fontsize=TITLE_SIZE * 0.63,
            fontweight="bold", color=DARK)

    n = len(apps)
    gap = 1.5 if col == 0 else 1.25
    total_w = (n - 1) * gap
    start_x = cx - total_w / 2

    for i, (app, label) in enumerate(apps):
        x = start_x + i * gap
        y = 2.75
        norm_path = normalize(app)
        if norm_path:
            img = mpimg.imread(norm_path)
            imagebox = OffsetImage(img, zoom=0.30)
            ab = AnnotationBbox(imagebox, (x, y), frameon=False)
            ax.add_artist(ab)
        ax.text(x, y - 0.95, label, ha="center", va="top", fontsize=NODE_LABEL_SIZE_HI * 0.6,
                color=DARK)

    accent = MAGENTA if col == 0 else PINK
    ax.plot([cx - total_w/2 - 0.8, cx + total_w/2 + 0.8], [1.15, 1.15],
             color=accent, linewidth=3.2, solid_capstyle="round")

ax.plot([5.4, 5.4], [0.6, 4.5], color="#ddd0e0", linewidth=1.3, linestyle=(0, (4, 3)))
ax.annotate("", xy=(5.95, 2.75), xytext=(4.85, 2.75),
            arrowprops=dict(arrowstyle="-|>", color="#8a7c90", lw=1.6))

fig.suptitle("As Gerações de Redes Sociais na Web", fontsize=TITLE_SIZE * 0.8, fontweight="bold",
             color=DARK, y=0.96)
fig.tight_layout(rect=[0, 0.02, 1, 0.85])
fig.savefig("/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap02/geracoes-icones.png",
            facecolor="white")
print("done")
