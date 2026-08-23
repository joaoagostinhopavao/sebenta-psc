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

cols = [
    ("Partilha", [("flickr", "Flickr"), ("youtube", "YouTube")]),
    ("Profissional", [("linkedin", "LinkedIn")]),
    ("Plataforma", [("ning", "Ning")]),
    ("Entretenimento", [("myspace", "MySpace"), ("hi5", "hi5")]),
]

fig, ax = plt.subplots(figsize=(SLIDE_REFERENCE_WIDTH, 6.6), dpi=200)
ax.set_xlim(0, SLIDE_REFERENCE_WIDTH); ax.set_ylim(0, 5.0); ax.axis("off")

col_x = {0: 1.75, 1: 5.05, 2: 8.35, 3: 11.6}
accents = [MAGENTA, PINK, MAGENTA, PINK]

for col, (title, apps) in enumerate(cols):
    cx = col_x[col]
    ax.text(cx, 4.75, title, ha="center", va="top", fontsize=SLIDE_TITLE_SIZE * 0.7,
            fontweight="bold", color=DARK)

    n = len(apps)
    gap = 1.35
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
        ax.text(x, y - 1.0, label, ha="center", va="top", fontsize=SLIDE_NODE_LABEL_SIZE_HI * 0.65,
                color=DARK)

    accent = accents[col]
    half = max(total_w / 2 + 0.75, 1.15)
    ax.plot([cx - half, cx + half], [1.15, 1.15],
             color=accent, linewidth=3.2, solid_capstyle="round")

fig.suptitle("Finalidades das Redes Sociais", fontsize=SLIDE_TITLE_SIZE, fontweight="bold",
             color=DARK, y=0.96)
fig.tight_layout(rect=[0, 0.02, 1, 0.84])
fig.savefig("/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap02/slides/finalidades-icones-slide.png",
            facecolor="white")
print("done")
