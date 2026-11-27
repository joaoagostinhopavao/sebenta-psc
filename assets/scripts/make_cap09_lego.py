"""Figura da analogia LEGO para a transmissão de conhecimento (Cap09).
Uso: make_cap09_lego.py [pt|en] [raiz_do_projeto]"""
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.append("/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from sebenta_style import DARK, MAGENTA, PINK, GREY, NOTE_COLOR, NODE_LABEL_SIZE, apply_style

LANG = sys.argv[1] if len(sys.argv) > 1 else "pt"
RAIZ = Path(sys.argv[2] if len(sys.argv) > 2 else "/Users/jpavao/QProjects/Sebenta-PSC")
T = {
    "pt": dict(
        paineis=[("Conhecimento", "de quem explica:\na ideia a transmitir"),
                 ("Informação", "as peças e o modo\ncomo encaixam"),
                 ("Conhecimento", "de quem aprende:\na ideia que montou")],
        verbos=["descreve", "monta"],
        volta="quem explica compara as duas construções e corrige",
        out=RAIZ / "assets/images/cap09/analogia-lego.png"),
    "en": dict(
        paineis=[("Knowledge", "of the explainer:\nthe idea to convey"),
                 ("Information", "the pieces and how\nthey fit together"),
                 ("Knowledge", "of the learner:\nthe idea they built")],
        verbos=["describes", "builds"],
        volta="the explainer compares both constructions and corrects",
        out=RAIZ / "en/assets/images/cap09/analogia-lego.png"),
}[LANG]

apply_style()
plt.rcParams["font.sans-serif"] = ["Arial", "DejaVu Sans"]  # a Helvetica do sistema não dá negrito
fig, ax = plt.subplots(figsize=(11, 5.2))
ax.set_xlim(0, 11)
ax.set_ylim(0, 5.2)
ax.set_aspect("equal")
ax.axis("off")
L, G, Y, H = 2.8, 1.25, 1.05, 4.05
xs = [0.04 + k * (L + G) for k in range(3)]
U, A = 0.52, 0.40
AZUL = GREY


def peca(x, y, pinos, cor, numero=None):
    for k in range(pinos):
        ax.add_patch(Rectangle((x + k * U + 0.12, y + A), U - 0.24, 0.09, facecolor=cor, edgecolor="none"))
    ax.add_patch(Rectangle((x, y), pinos * U, A, facecolor=cor, edgecolor="white", linewidth=1.2))
    if numero:
        ax.text(x + pinos * U / 2, y + A / 2, numero, ha="center", va="center",
                color=DARK if cor == AZUL else "white", fontsize=NODE_LABEL_SIZE - 2, fontweight="bold")


for k, (titulo, legenda) in enumerate(T["paineis"]):
    ax.add_patch(FancyBboxPatch((xs[k], Y), L, H, boxstyle="round,pad=0,rounding_size=0.18",
                                facecolor="#f4f0f6", edgecolor=GREY, linewidth=2))
    ax.text(xs[k] + L / 2, Y + H - 0.42, titulo, ha="center", va="center", color=DARK, fontweight="bold",
            fontsize=NODE_LABEL_SIZE + 1)
    ax.text(xs[k] + L / 2, Y + 0.55, legenda, ha="center", va="center", color=NOTE_COLOR,
            fontsize=NODE_LABEL_SIZE - 1, linespacing=1.25)

# construções: (fila, deslocamento em pinos, n.º de pinos, cor)
original = [(0, 0, 4, DARK), (1, 0, 2, MAGENTA), (1, 2, 2, PINK), (2, 1, 2, AZUL)]
remontada = original[:3] + [(2, 2, 2, AZUL)]
for k, modelo in ((0, original), (2, remontada)):
    x0 = xs[k] + (L - 4 * U) / 2
    for fila, desl, pinos, cor in modelo:
        peca(x0 + desl * U, Y + 1.35 + fila * A, pinos, cor)

# peças soltas, numeradas pela ordem de encaixe
x = xs[1]
peca(x + (L - 4 * U) / 2, Y + 2.52, 4, DARK, "1")
peca(x + 0.3, Y + 1.87, 2, MAGENTA, "2")
peca(x + L - 0.3 - 2 * U, Y + 1.87, 2, PINK, "3")
peca(x + (L - 2 * U) / 2, Y + 1.22, 2, AZUL, "4")

seta = dict(arrowstyle="-|>", color=MAGENTA, linewidth=2.5, mutation_scale=22, shrinkA=0, shrinkB=0)
for k in range(2):
    ax.annotate("", xy=(xs[k + 1] - 0.08, Y + H / 2), xytext=(xs[k] + L + 0.08, Y + H / 2), arrowprops=seta)
    ax.text(xs[k] + L + G / 2, Y + H / 2 + 0.14, T["verbos"][k], ha="center", va="bottom", color=MAGENTA,
            fontweight="bold", fontsize=NODE_LABEL_SIZE - 3)
c1, c3, yb = xs[0] + L / 2, xs[2] + L / 2, 0.55
ax.plot([c3, c3, c1], [Y - 0.03, yb, yb], color=MAGENTA, linewidth=2, linestyle="--")
ax.annotate("", xy=(c1, Y - 0.03), xytext=(c1, yb), arrowprops=dict(seta, linestyle="--", linewidth=2))
ax.text((c1 + c3) / 2, yb - 0.1, T["volta"], ha="center", va="top", color=NOTE_COLOR,
        fontsize=NODE_LABEL_SIZE - 1)
fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
T["out"].parent.mkdir(parents=True, exist_ok=True)
fig.savefig(T["out"], dpi=200)
print("done", LANG, T["out"])
