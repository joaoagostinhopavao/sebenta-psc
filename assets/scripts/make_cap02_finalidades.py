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

cols = [
    ("Partilha", [("flickr", "Flickr"), ("youtube", "YouTube")]),
    ("Profissional", [("linkedin", "LinkedIn")]),
    ("Plataforma", [("ning", "Ning")]),
    ("Entretenimento", [("myspace", "MySpace"), ("hi5", "hi5")]),
]

fig, ax = plt.subplots(figsize=(REFERENCE_WIDTH, 6.0), dpi=200)
ax.set_xlim(0, REFERENCE_WIDTH); ax.set_ylim(0, 5.0); ax.axis("off")

col_x = {0: 1.35, 1: 4.15, 2: 6.85, 3: 9.55}
accents = [MAGENTA, PINK, MAGENTA, PINK]

for col, (title, apps) in enumerate(cols):
    cx = col_x[col]
    ax.text(cx, 4.75, title, ha="center", va="top", fontsize=TITLE_SIZE * 0.6,
            fontweight="bold", color=DARK)

    n = len(apps)
    gap = 1.15
    total_w = (n - 1) * gap
    start_x = cx - total_w / 2

    for i, (app, label) in enumerate(apps):
        x = start_x + i * gap
        y = 2.75
        norm_path = normalize(app)
        if norm_path:
            img = mpimg.imread(norm_path)
            imagebox = OffsetImage(img, zoom=0.26)
            ab = AnnotationBbox(imagebox, (x, y), frameon=False)
            ax.add_artist(ab)
        ax.text(x, y - 0.95, label, ha="center", va="top", fontsize=NODE_LABEL_SIZE_HI * 0.55,
                color=DARK)

    accent = accents[col]
    half = max(total_w / 2 + 0.65, 1.0)
    ax.plot([cx - half, cx + half], [1.15, 1.15],
             color=accent, linewidth=3.0, solid_capstyle="round")

fig.suptitle("Finalidades das Redes Sociais", fontsize=TITLE_SIZE * 0.8, fontweight="bold",
             color=DARK, y=0.96)
fig.tight_layout(rect=[0, 0.02, 1, 0.84])
fig.savefig("/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap02/finalidades-icones.png",
            facecolor="white")
print("done")
