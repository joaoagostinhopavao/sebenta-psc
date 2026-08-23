import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import numpy as np
import sys

sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from sebenta_style import DARK, MAGENTA, NOTE_COLOR, apply_style, TITLE_SIZE, REFERENCE_WIDTH

apply_style()

rng = np.random.default_rng(7)

fig, ax = plt.subplots(figsize=(REFERENCE_WIDTH, 6.4), dpi=200)
ax.set_xlim(0, REFERENCE_WIDTH); ax.set_ylim(0, 5.8); ax.axis("off")

fig.suptitle("O Dilema do Prisioneiro", fontsize=TITLE_SIZE * 0.75, fontweight="bold",
             color=DARK, y=0.96)

# --- figura (Open Peeps, recolorida + listrada) — atrás das barras ---
img = mpimg.imread("/private/tmp/claude-501/-Users-jpavao-Documents-1-PARA-2-Areas-Teaching-AI-Team/"
                    "b50987a5-ddcb-4467-807f-46b6b9ed1177/scratchpad/illustration_test/peep_man3_striped.png")
imagebox = OffsetImage(img, zoom=0.30)
ab = AnnotationBbox(imagebox, (5.3, 2.55), frameon=False, zorder=2)
ax.add_artist(ab)

# --- célula: barras verticais tipo esboço à mão (jitter em cada segmento), à frente ---
bar_x = np.linspace(3.4, 7.2, 6)
for x in bar_x:
    ys = np.linspace(0.5, 4.9, 14)
    xs = x + rng.normal(0, 0.02, size=ys.shape)
    xs[0] = x; xs[-1] = x
    ax.plot(xs, ys, color=DARK, linewidth=2.8, solid_capstyle="round", zorder=4, alpha=0.92)

# travessas horizontais
for y in (0.55, 4.85):
    xs = np.linspace(3.2, 7.4, 10)
    ys_line = y + rng.normal(0, 0.02, size=xs.shape)
    ax.plot(xs, ys_line, color=DARK, linewidth=3.4, solid_capstyle="round", zorder=4, alpha=0.92)

# balão de pensamento
ax.text(2.0, 4.6, "Confessar…\nou ficar\nem silêncio?", ha="center", va="center",
        fontsize=13, color=NOTE_COLOR, style="italic",
        bbox=dict(boxstyle="round,pad=0.5", facecolor="white", edgecolor=NOTE_COLOR, linewidth=1.2))
for r, dx, dy in [(0.10, 1.1, -0.55), (0.06, 1.35, -0.8), (0.035, 1.55, -1.0)]:
    ax.add_patch(plt.Circle((2.0 + dx, 4.6 + dy), r, facecolor="white",
                             edgecolor=NOTE_COLOR, linewidth=1.0, zorder=4))

fig.tight_layout(rect=[0, 0.02, 1, 0.90])
fig.savefig("/private/tmp/claude-501/-Users-jpavao-Documents-1-PARA-2-Areas-Teaching-AI-Team/"
            "b50987a5-ddcb-4467-807f-46b6b9ed1177/scratchpad/illustration_test/teste-dilema-cena.png",
            facecolor="white")
print("done")
