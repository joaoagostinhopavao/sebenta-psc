import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import subprocess, os
from PIL import Image

DARK = "#1f0a2e"
MAGENTA = "#9c1f8f"
PINK = "#e857b0"

LOGOS_DIR = "/private/tmp/claude-501/-Users-jpavao-Documents-1-PARA-2-Areas-Teaching-AI-Team/b50987a5-ddcb-4467-807f-46b6b9ed1177/scratchpad/logos"
NORM_DIR = os.path.join(LOGOS_DIR, "norm")
os.makedirs(NORM_DIR, exist_ok=True)

CANVAS = 260  # px, fixed square canvas for every icon
PAD = 18      # px padding inside canvas

def normalize(name):
    """Return path to a CANVASxCANVAS transparent PNG with the logo centered/fit."""
    out = os.path.join(NORM_DIR, name + ".png")
    svg = os.path.join(LOGOS_DIR, name + ".svg")
    png = os.path.join(LOGOS_DIR, name + ".png")
    src = None
    if os.path.exists(svg):
        raw = os.path.join(NORM_DIR, name + "_raw.png")
        subprocess.run(["rsvg-convert", "-w", "512", "-h", "512", "-o", raw, svg], check=True)
        src = raw
    elif os.path.exists(png):
        src = png
    else:
        return None
    img = Image.open(src).convert("RGBA")
    # trim fully transparent/white border
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
    target = CANVAS - 2 * PAD
    w, h = img.size
    scale = target / max(w, h)
    img = img.resize((max(1, int(w * scale)), max(1, int(h * scale))), Image.LANCZOS)
    canvas = Image.new("RGBA", (CANVAS, CANVAS), (0, 0, 0, 0))
    x = (CANVAS - img.width) // 2
    y = (CANVAS - img.height) // 2
    canvas.paste(img, (x, y), img)
    canvas.save(out)
    return out

gens = {
    "1.ª geração: comunicação pessoal": [("icq", "ICQ"), ("msn", "MSN Messenger")],
    "2.ª geração: redes de afinidade": [("orkut", "Orkut"), ("friendster", "Friendster"),
                                         ("myspace", "MySpace"), ("facebook", "Facebook"),
                                         ("linkedin", "LinkedIn")],
}

plt.rcParams.update({"font.family": "sans-serif", "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans"]})

fig, ax = plt.subplots(figsize=(14, 6), dpi=200)
ax.set_xlim(0, 14); ax.set_ylim(0, 6); ax.axis("off")

col_x = {0: 3.1, 1: 9.9}

for col, (title, apps) in enumerate(gens.items()):
    cx = col_x[col]
    ax.text(cx, 5.55, title, ha="center", va="top", fontsize=18, fontweight="bold", color=DARK)

    n = len(apps)
    gap = 1.85 if col == 0 else 1.55
    total_w = (n - 1) * gap
    start_x = cx - total_w / 2

    for i, (app, label) in enumerate(apps):
        x = start_x + i * gap
        y = 3.15
        norm_path = normalize(app)
        if norm_path:
            img = mpimg.imread(norm_path)
            imagebox = OffsetImage(img, zoom=0.36)
            ab = AnnotationBbox(imagebox, (x, y), frameon=False)
            ax.add_artist(ab)
        ax.text(x, y - 1.15, label, ha="center", va="top", fontsize=13, color=DARK)

    accent = MAGENTA if col == 0 else PINK
    ax.plot([cx - total_w/2 - 1.0, cx + total_w/2 + 1.0], [1.35, 1.35],
             color=accent, linewidth=3.5, solid_capstyle="round")

ax.plot([6.6, 6.6], [0.8, 5.35], color="#ddd0e0", linewidth=1.4, linestyle=(0, (4, 3)))
ax.annotate("", xy=(7.3, 3.15), xytext=(5.9, 3.15),
            arrowprops=dict(arrowstyle="-|>", color="#8a7c90", lw=1.8))

fig.suptitle("As Gerações de Redes Sociais na Web", fontsize=22, fontweight="bold",
             color=DARK, y=0.99)
fig.savefig("/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap02/geracoes-icones.png",
            facecolor="white", bbox_inches="tight", pad_inches=0.35)
print("done")
