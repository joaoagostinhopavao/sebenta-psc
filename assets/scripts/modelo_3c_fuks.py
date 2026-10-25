import sys
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle

sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from sebenta_style import DARK, MAGENTA, NOTE_COLOR

# Modelo 3C de Colaboração redesenhado a partir da Figura 2.4 de Fuks et
# al. (2011): o ciclo comunicação -> coordenação -> cooperação ->
# comunicação, com a perceção ao centro, ligada às três dimensões.
# Uso: modelo_3c_fuks.py slide  ·  modelo_3c_fuks.py livro pt|en
ESTILO = sys.argv[1] if len(sys.argv) > 1 else "slide"
LANG = sys.argv[2] if len(sys.argv) > 2 else "pt"

COR = {
    "livro": dict(linha=DARK, caixa="#f4f0f6", borda=DARK, texto=DARK, acento=MAGENTA,
                  nota=NOTE_COLOR),
    "slide": dict(linha="#1d5a32", caixa="#dfece9", borda="#3d8a52", texto="#111111",
                  acento="#3d8a52", nota="#4a4a4a"),
}[ESTILO]

TXT = {
    "pt": dict(
        com="COMUNICAÇÃO", coord="COORDENAÇÃO", coop="COOPERAÇÃO", perc="PERCEÇÃO",
        com_n=("comum-ação", "tornar comum (conhecimento partilhado):\nnegociação e compromissos"),
        coord_n=("co-ordem-ação", "ordenar em conjunto:\npessoas, tarefas e recursos"),
        coop_n=("co-operar-ação", "operar em conjunto:\nespaço partilhado"),
        a1="gera compromissos\ngeridos pela", a2="organiza as tarefas para", a3="exige",
        leg=("Perceção", " = ter noção do que\nos outros estão a fazer (", "awareness", ")"),
    ),
    "en": dict(
        com="COMMUNICATION", coord="COORDINATION", coop="COOPERATION", perc="AWARENESS",
        com_n=("make common", "shared knowledge:\nnegotiation and commitments"),
        coord_n=("order together", "people, tasks\nand resources"),
        coop_n=("operate together", "shared workspace"),
        a1="generates commitments\nmanaged by", a2="organises the tasks for", a3="demands",
    ),
}["pt" if ESTILO == "slide" else LANG]

SAIDA = {
    "slide": "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap04/slides/modelo-3c-fuks-slide.png",
    "pt": "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap04/modelo-3c.png",
    "en": "/Users/jpavao/QProjects/Sebenta-PSC/en/assets/images/cap04/modelo-3c.png",
}["slide" if ESTILO == "slide" else LANG]

plt.rcParams["font.family"] = "Arial"
plt.rcParams.update({"mathtext.fontset": "custom", "mathtext.bf": "Arial:bold",
                     "mathtext.it": "Arial:italic", "mathtext.rm": "Arial"})
W, H = 13.333, 6.4
fig = plt.figure(figsize=(W, H), dpi=200)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.axis("off")

BW, BH = 3.0, 0.8
COM, COORD, COOP = (6.67, 4.55), (10.0, 1.75), (3.33, 1.75)


def caixa(c, texto):
    ax.add_patch(FancyBboxPatch((c[0] - BW / 2, c[1] - BH / 2), BW, BH,
                                boxstyle="round,pad=0,rounding_size=0.15",
                                fc=COR["caixa"], ec=COR["borda"], lw=2.6, zorder=3))
    ax.text(c[0], c[1], texto, ha="center", va="center", fontsize=21, fontweight="bold",
            color=COR["texto"], zorder=4)


def nota(x, y, par, va):
    titulo, resto = par
    if va == "top":
        ax.text(x, y, titulo, ha="center", va="top", fontsize=17, fontweight="bold",
                color=COR["acento"])
        ax.text(x, y - 0.36, resto, ha="center", va="top", fontsize=15,
                color=COR["nota"], linespacing=1.2)
    else:
        ax.text(x, y, resto, ha="center", va="bottom", fontsize=15,
                color=COR["nota"], linespacing=1.2)
        ax.text(x, y + 0.27 * (resto.count("\n") + 1) + 0.03, titulo, ha="center",
                va="bottom", fontsize=17, fontweight="bold", color=COR["acento"])


def seta(pts, rotulo=None, rx=0, ry=0, ha="left"):
    for p, q in zip(pts[:-2], pts[1:-1]):
        ax.plot([p[0], q[0]], [p[1], q[1]], color=COR["linha"], lw=2.4,
                solid_capstyle="butt")
    ax.add_patch(FancyArrowPatch(pts[-2], pts[-1], arrowstyle="-|>", mutation_scale=24,
                                 lw=2.4, color=COR["linha"], shrinkA=0, shrinkB=0))
    if rotulo:
        ax.text(rx, ry, rotulo, ha=ha, va="center", fontsize=15, style="italic",
                color=COR["texto"], linespacing=1.15)


caixa(COM, TXT["com"])
caixa(COORD, TXT["coord"])
caixa(COOP, TXT["coop"])
nota(COM[0], COM[1] + BH / 2 + 0.15, TXT["com_n"], "bottom")
nota(COORD[0], COORD[1] - BH / 2 - 0.15, TXT["coord_n"], "top")
nota(COOP[0], COOP[1] - BH / 2 - 0.15, TXT["coop_n"], "top")

# o ciclo: comunicação -> coordenação -> cooperação -> comunicação
seta([(COM[0] + BW / 2, COM[1]), (COORD[0], COM[1]), (COORD[0], COORD[1] + BH / 2)],
     TXT["a1"], COORD[0] + 0.15, (COM[1] + COORD[1]) / 2 + 0.3)
yb = COORD[1] - BH / 2 - 0.0
seta([(COORD[0] - BW / 2, COORD[1]), (COOP[0] + BW / 2, COOP[1])],
     TXT["a2"], (COOP[0] + COORD[0]) / 2, COORD[1] - 0.3, "center")
seta([(COOP[0], COOP[1] + BH / 2), (COOP[0], COM[1]), (COM[0] - BW / 2, COM[1])],
     TXT["a3"], COOP[0] - 0.15, (COM[1] + COOP[1]) / 2 + 0.3, "right")

# perceção ao centro: três participantes que se veem uns aos outros
G = (6.67, 2.95)
P = [(G[0] - 0.95, G[1] + 0.3), (G[0] + 0.95, G[1] + 0.3), (G[0], G[1] - 0.6)]
for a in range(3):
    for b in range(a + 1, 3):
        ax.plot([P[a][0], P[b][0]], [P[a][1], P[b][1]], color=COR["linha"], lw=1.2,
                alpha=0.5, zorder=1)


def boneco(x, y, s=0.27):
    ax.add_patch(Circle((x, y + s * 1.1), s * 0.42, fc="white", ec=COR["linha"], lw=1.8,
                        zorder=3))
    for (x0, y0), (x1, y1) in [((x, y + s * 0.68), (x, y - s * 0.3)),
                               ((x - s * 0.55, y + s * 0.35), (x + s * 0.55, y + s * 0.35)),
                               ((x, y - s * 0.3), (x - s * 0.45, y - s * 1.0)),
                               ((x, y - s * 0.3), (x + s * 0.45, y - s * 1.0))]:
        ax.plot([x0, x1], [y0, y1], color=COR["linha"], lw=1.8, zorder=3)


for x, y in P:
    boneco(x, y)
ax.text(G[0], G[1] + 0.05, TXT["perc"], ha="center", va="center", fontsize=16,
        fontweight="bold", color=COR["acento"], zorder=4,
        bbox=dict(fc="white", ec="none", pad=2))
for alvo, origem in [((COM[0], COM[1] - BH / 2), (G[0], G[1] + 0.32)),
                     ((COORD[0] - BW / 2 + 0.25, COORD[1] + BH / 2), (P[1][0] + 0.2, P[1][1] - 0.3)),
                     ((COOP[0] + BW / 2 - 0.25, COOP[1] + BH / 2), (P[0][0] - 0.2, P[0][1] - 0.3))]:
    ax.add_patch(FancyArrowPatch(origem, alvo, arrowstyle="<|-|>", mutation_scale=16,
                                 lw=1.6, color=COR["linha"], shrinkA=2, shrinkB=2))

# legenda da perceção (só em PT: em inglês o termo já é "awareness")
if "leg" in TXT:
    termo, meio, ing, fim = TXT["leg"]
    ax.text(G[0], 0.82, f"$\\bf{{{termo}}}${meio}$\\it{{{ing}}}${fim}", ha="center",
            va="center", fontsize=14, color=COR["nota"], linespacing=1.3)

fig.savefig(SAIDA, dpi=200, facecolor="white")
print("done", SAIDA)
