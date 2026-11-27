"""Figura dos três métodos de aprendizagem colaborativa (Cap09).
Uso: make_cap09_metodos.py [pt|en] [raiz_do_projeto]"""
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.append("/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from sebenta_style import DARK, MAGENTA, PINK, NODE_LABEL_SIZE, apply_style

LANG = sys.argv[1] if len(sys.argv) > 1 else "pt"
RAIZ = Path(sys.argv[2] if len(sys.argv) > 2 else "/Users/jpavao/QProjects/Sebenta-PSC")
T = {
    "pt": dict(
        cartoes=[("Jigsaw", "Cada pessoa estuda\numa parte e\nensina as outras"),
                 ("Controvérsia\nAcadémica", "Pares defendem\nposições opostas\ne depois sintetizam"),
                 ("Investigação\nem Grupo", "O grupo planeia,\nreparte tarefas,\ndiscute o que cada\num encontra e\nconclui em conjunto")],
        out=RAIZ / "assets/images/cap09/metodos-aprendizagem.png"),
    "en": dict(
        cartoes=[("Jigsaw", "Each person studies\none part and\nteaches the others"),
                 ("Academic\nControversy", "Pairs defend\nopposing positions\nand then synthesise"),
                 ("Group\nInvestigation", "The group plans,\nshares out tasks,\ndiscusses what each\none finds and\nconcludes together")],
        out=RAIZ / "en/assets/images/cap09/metodos-aprendizagem.png"),
}[LANG]

apply_style()
plt.rcParams["font.sans-serif"] = ["Arial", "DejaVu Sans"]  # a Helvetica do sistema não dá negrito
fig, ax = plt.subplots(figsize=(11, 3.8))
ax.set_xlim(0, 11)
ax.set_ylim(0, 3.8)
ax.axis("off")
for k, ((titulo, desc), cor) in enumerate(zip(T["cartoes"], (MAGENTA, DARK, MAGENTA))):
    x = 0.1 + k * 3.65
    ax.add_patch(FancyBboxPatch((x, 0.1), 3.5, 3.6, boxstyle="round,pad=0,rounding_size=0.18",
                                linewidth=0, facecolor=cor))
    ax.text(x + 1.75, 3.08, titulo, ha="center", va="center", color="white", fontweight="bold",
            fontsize=NODE_LABEL_SIZE + 3, linespacing=1.15)
    ax.plot([x + 0.5, x + 3.0], [2.42, 2.42], color=PINK, linewidth=2.5)
    ax.text(x + 1.75, 2.18, desc, ha="center", va="top", color="white", fontsize=NODE_LABEL_SIZE - 1,
            linespacing=1.3)
fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
T["out"].parent.mkdir(parents=True, exist_ok=True)
fig.savefig(T["out"], dpi=200)
print("done", LANG, T["out"])
