import math
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch

# Modelo de Tuckman (etapas de desenvolvimento de um grupo), redesenhado a
# partir do slide 17 do deck original "Sistemas Colaborativos" (Fuks et al.,
# 2011). Uso: slide_cap04_tuckman.py [slide|pt|en]
#   slide: paleta verde do deck da Aula 5
#   pt/en: paleta magenta da sebenta, figura do Cap04
import sys
MODE = sys.argv[1] if len(sys.argv) > 1 else "slide"
if MODE == "slide":
    GREEN = "#3d8a52"
    GREEN_DARK = "#1d5a32"
    INK = "#111111"
    GREY = "#6b6b6b"
    OUT = "assets/images/cap04/slides/tuckman-slide.png"
else:
    sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
    from sebenta_style import DARK, MAGENTA, NOTE_COLOR
    GREEN, GREEN_DARK, INK, GREY = MAGENTA, DARK, DARK, NOTE_COLOR
    OUT = ("assets/images/cap04/tuckman.png" if MODE == "pt"
           else "en/assets/images/cap04/tuckman.png")

plt.rcParams["font.family"] = "Arial"

W, H = 13.333, 5.25
fig = plt.figure(figsize=(W, H), dpi=200)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.axis("off")

STAGES_EN = [
    ("Forming", "", "Identifying\nshared goals", "Sense of\nbelonging", "converge"),
    ("Storming", "", "Defining the\nresponsibilities\nof each role", "Defining roles\nand leadership", "cross"),
    ("Norming", "", "Defining the\nwork process", "Strong\nleadership", "align"),
    ("Performing", "", "Productivity:\ncarrying out and\nimproving the process", "Less\nleadership", "parallel"),
    ("Adjourning", "", "End of the process", "End of the group", "diverge"),
]

STAGES = [
    ("Formação", "forming",
     "Identificação de\nmetas partilhadas", "Sentimento de\npertença", "converge"),
    ("Confrontação", "storming",
     "Definição das\nresponsabilidades\nde cada papel", "Definição de papéis\ne liderança", "cross"),
    ("Normatização", "norming",
     "Definição do\nprocesso de\ntrabalho", "Forte atuação\nda liderança", "align"),
    ("Atuação", "performing",
     "Produtividade:\nexecução e melhoria\ndo processo", "Menor atuação\nda liderança", "parallel"),
    ("Dissolução", "adjourning",
     "Fim do processo", "Fim do grupo", "diverge"),
]

if MODE == "en":
    STAGES = STAGES_EN

BW, BH = 1.95, 0.95
GAP = 0.38
X0 = 0.85
YB = 4.4
xs = [X0 + BW / 2 + i * (BW + GAP) for i in range(5)]


def arrow(p, q, color=GREEN_DARK, lw=2.6, ms=18):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=ms,
                                 color=color, lw=lw, zorder=2,
                                 shrinkA=0, shrinkB=0))


# início e fim (notação de processo: círculo fino e círculo grosso)
ax.add_patch(Circle((0.45, YB), 0.22, facecolor="white", edgecolor=INK, lw=2))
arrow((0.67, YB), (xs[0] - BW / 2, YB))
end_x = xs[-1] + BW / 2 + GAP + 0.05
ax.add_patch(Circle((end_x, YB), 0.22, facecolor="white", edgecolor=INK, lw=4.5))
arrow((xs[-1] + BW / 2, YB), (end_x - 0.22, YB))

for i, (name, en, l1, l2, icon) in enumerate(STAGES):
    x = xs[i]
    ax.add_patch(FancyBboxPatch((x - BW / 2, YB - BH / 2), BW, BH,
                                boxstyle="round,pad=0,rounding_size=0.12",
                                facecolor=GREEN if i < 4 else GREEN_DARK,
                                edgecolor="none", zorder=3))
    ax.text(x, YB + (0.13 if en else 0), name, ha="center", va="center", fontsize=19,
            fontweight="bold", color="white", zorder=4)
    ax.text(x, YB - 0.24, en, ha="center", va="center", fontsize=13,
            style="italic", color="white", zorder=4)
    if i < 4:
        arrow((x + BW / 2, YB), (xs[i + 1] - BW / 2, YB))

    # chaveta por baixo da caixa
    yt = YB - BH / 2 - 0.25
    ax.plot([x, x], [YB - BH / 2, yt], color=GREY, lw=1.2, ls=(0, (2, 2)))
    ax.plot([x - BW / 2 + 0.05, x + BW / 2 - 0.05], [yt, yt], color=GREY, lw=1.4)
    for xx in (x - BW / 2 + 0.05, x + BW / 2 - 0.05):
        ax.plot([xx, xx], [yt, yt - 0.12], color=GREY, lw=1.4)

    ax.text(x, yt - 0.2, l1, ha="center", va="top", fontsize=15, color=INK,
            linespacing=1.2)
    ax.text(x, 2.45, l2, ha="center", va="top", fontsize=15, color=GREEN_DARK,
            fontweight="bold", linespacing=1.2)

    # ícone: como se movem os membros do grupo
    cy = 1.0
    L = 0.42
    kw = dict(color=INK, lw=2.2, ms=14)
    if icon == "converge":
        for a in (0, 90, 180, 270):
            r = math.radians(a)
            arrow((x + L * 1.4 * math.cos(r), cy + L * 1.4 * math.sin(r)),
                  (x + 0.08 * math.cos(r), cy + 0.08 * math.sin(r)), **kw)
    elif icon == "diverge":
        for a in (0, 90, 180, 270):
            r = math.radians(a)
            arrow((x + 0.08 * math.cos(r), cy + 0.08 * math.sin(r)),
                  (x + L * 1.4 * math.cos(r), cy + L * 1.4 * math.sin(r)), **kw)
    elif icon == "cross":
        for (dx0, dy0, dx1, dy1) in [(-0.5, -0.4, 0.45, 0.4), (0.5, -0.4, -0.45, 0.45),
                                     (-0.3, 0.45, 0.35, -0.45), (-0.55, 0.05, 0.55, 0.1)]:
            arrow((x + dx0, cy + dy0), (x + dx1, cy + dy1), **kw)
    elif icon == "align":
        for k, ang in enumerate((52, 62, 70, 58)):
            r = math.radians(ang)
            bx = x - 0.45 + k * 0.22
            arrow((bx, cy - 0.42), (bx + 0.9 * math.cos(r), cy - 0.42 + 0.9 * math.sin(r)), **kw)
    elif icon == "parallel":
        r = math.radians(35)
        px, py = -math.sin(r), math.cos(r)
        for k in range(4):
            off = (k - 1.5) * 0.2
            bx = x - 0.45 * math.cos(r) + off * px
            by = cy - 0.45 * math.sin(r) + off * py
            arrow((bx, by), (bx + 0.9 * math.cos(r), by + 0.9 * math.sin(r)), **kw)

fig.savefig("/Users/jpavao/QProjects/Sebenta-PSC/" + OUT,
            facecolor="white")
print("done")
