"""Figura das três versões de um episódio (Cap09).
Uso: make_cap09_versoes.py [pt|en] [raiz_do_projeto]"""
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.append("/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from sebenta_style import DARK, MAGENTA, GREY, NOTE_COLOR, NODE_LABEL_SIZE, apply_style

LANG = sys.argv[1] if len(sys.argv) > 1 else "pt"
RAIZ = Path(sys.argv[2] if len(sys.argv) > 2 else "/Users/jpavao/QProjects/Sebenta-PSC")
T = {
    "pt": dict(
        caixas=[("Versão real", "o que de facto\naconteceu"),
                ("Versão conhecida", "na memória de\nquem testemunhou"),
                ("Versão relatada", "o relato\nescrito")],
        setas=["testemunha", "escreve,\ncom perdas"],
        volta="aproxima-se, mas nunca coincide",
        out=RAIZ / "assets/images/cap09/versoes-conhecimento.png"),
    "en": dict(
        caixas=[("Real version", "what actually\nhappened"),
                ("Known version", "in the memory of\nthe witness"),
                ("Reported version", "the written\naccount")],
        setas=["witnesses", "writes,\nwith losses"],
        volta="approaches, but never coincides",
        out=RAIZ / "en/assets/images/cap09/versoes-conhecimento.png"),
}[LANG]

apply_style()
plt.rcParams["font.sans-serif"] = ["Arial", "DejaVu Sans"]  # a Helvetica do sistema não dá negrito
fig, ax = plt.subplots(figsize=(11, 3.4))
ax.set_xlim(0, 11)
ax.set_ylim(0, 3.4)
ax.axis("off")
L, G, Y, H = 2.65, 1.45, 1.25, 2.0
xs = [0.075 + k * (L + G) for k in range(3)]
estilos = [dict(facecolor="white", edgecolor=MAGENTA, linestyle="--", linewidth=2),
           dict(facecolor="#f4f0f6", edgecolor=GREY, linewidth=2),
           dict(facecolor=MAGENTA, edgecolor=MAGENTA, linewidth=2)]
for k, ((titulo, desc), estilo) in enumerate(zip(T["caixas"], estilos)):
    cor = "white" if k == 2 else DARK
    ax.add_patch(FancyBboxPatch((xs[k], Y), L, H, boxstyle="round,pad=0,rounding_size=0.18", **estilo))
    ax.text(xs[k] + L / 2, Y + H - 0.5, titulo, ha="center", va="center", color=cor, fontweight="bold",
            fontsize=NODE_LABEL_SIZE)
    ax.text(xs[k] + L / 2, Y + 0.65, desc, ha="center", va="center", color=cor, fontsize=NODE_LABEL_SIZE - 2,
            linespacing=1.3)
seta = dict(arrowstyle="-|>", color=MAGENTA, linewidth=2.5, mutation_scale=22, shrinkA=0, shrinkB=0)
for k, rotulo in enumerate(T["setas"]):
    xa, xb = xs[k] + L + 0.05, xs[k + 1] - 0.05
    ax.annotate("", xy=(xb, Y + H / 2), xytext=(xa, Y + H / 2), arrowprops=seta)
    ax.text((xa + xb) / 2, Y + H / 2 + 0.12, rotulo, ha="center", va="bottom", color=NOTE_COLOR,
            fontsize=NODE_LABEL_SIZE - 3, linespacing=1.2)
c1, c3, yb = xs[0] + L / 2, xs[2] + L / 2, 0.65
ax.plot([c3, c3, c1], [Y - 0.03, yb, yb], color=MAGENTA, linewidth=2, linestyle="--")
ax.annotate("", xy=(c1, Y - 0.03), xytext=(c1, yb),
            arrowprops=dict(seta, linestyle="--", linewidth=2))
ax.text((c1 + c3) / 2, yb - 0.12, T["volta"], ha="center", va="top", color=NOTE_COLOR,
        fontsize=NODE_LABEL_SIZE - 1)
fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
T["out"].parent.mkdir(parents=True, exist_ok=True)
fig.savefig(T["out"], dpi=200)
print("done", LANG, T["out"])
