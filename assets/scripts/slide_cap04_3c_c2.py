import math
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch

# Slide "3C vs. Comando e Controlo" da Aula 5, na paleta verde do deck
# (a mesma do slide_cap04_atividade_exemplo.py). Os mesmos cinco
# participantes organizados de duas maneiras.
GREEN = "#3d8a52"
GREEN_DARK = "#1d5a32"
GREEN_LIGHT = "#dfece9"
INK = "#111111"
GREY = "#8a8a8a"

plt.rcParams["font.family"] = "Arial"

W, H = 13.333, 5.98
fig = plt.figure(figsize=(W, H), dpi=200)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.axis("off")

PEOPLE = "ABCDE"
R = 0.36


def person(x, y, letter):
    ax.add_patch(Circle((x, y), R, facecolor="white", edgecolor=GREEN, lw=3, zorder=3))
    ax.text(x, y, letter, ha="center", va="center", fontsize=20, fontweight="bold",
            color=INK, zorder=4)


def box(x, y, w, h, text, fill, fg, edge):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                                boxstyle="round,pad=0,rounding_size=0.15",
                                facecolor=fill, edgecolor=edge, lw=3, zorder=3))
    ax.text(x, y, text, ha="center", va="center", fontsize=18, fontweight="bold",
            color=fg, zorder=4, linespacing=1.15)


def legend(x, y, items):
    for i, (head, rest) in enumerate(items):
        yy = y - i * 0.42
        ax.add_patch(Circle((x, yy), 0.07, color=GREEN, zorder=3))
        t = ax.text(x + 0.2, yy, head, ha="left", va="center", fontsize=16,
                    fontweight="bold", color=INK)
        fig.canvas.draw()
        bb = t.get_window_extent().transformed(ax.transData.inverted())
        ax.text(bb.x1 + 0.08, yy, rest, ha="left", va="center", fontsize=16, color=INK)


# ---- painel esquerdo: colaboração (3C) ----
cx, cy = 3.2, 3.25
ax.text(cx, 5.6, "Colaboração (Modelo 3C)", ha="center", va="center",
        fontsize=24, fontweight="bold", color=INK)
pts = []
for i, letter in enumerate(PEOPLE):
    a = math.pi / 2 + i * 2 * math.pi / 5
    pts.append((cx + 1.75 * math.cos(a), cy + 1.55 * math.sin(a), letter))
for i in range(5):
    x1, y1, _ = pts[i]
    x2, y2, _ = pts[(i + 1) % 5]
    ax.plot([x1, x2], [y1, y2], color=GREEN, lw=3, zorder=1)
for x, y, _ in pts:
    ax.plot([x, cx], [y, cy], color=GREEN, lw=2.2, ls=(0, (4, 3)), zorder=1)
box(cx, cy, 1.9, 0.75, "espaço\npartilhado", GREEN_LIGHT, GREEN_DARK, GREEN)
for x, y, letter in pts:
    person(x, y, letter)
legend(0.75, 1.0, [
    ("Comunicação:", "falam diretamente uns com os outros"),
    ("Coordenação:", "combinam entre si quem faz o quê"),
    ("Cooperação:", "produzem juntos no espaço partilhado"),
])

# divisória
ax.plot([6.67, 6.67], [0.35, 5.75], color="#cccccc", lw=1.5)

# ---- painel direito: comando e controlo ----
rx = 10.0
ax.text(rx, 5.6, "Comando e Controlo (C2)", ha="center", va="center",
        fontsize=24, fontweight="bold", color=INK)
box(rx, 4.55, 3.0, 0.75, "Autoridade central", GREEN_DARK, "white", GREEN_DARK)
ys = 2.25
xs = [rx - 2.4 + i * 1.2 for i in range(5)]
for x in xs:
    ax.add_patch(FancyArrowPatch((rx, 4.17), (x, ys + R + 0.04), arrowstyle="-|>",
                                 mutation_scale=22, color=GREEN, lw=3, zorder=2))
ax.text(rx + 1.5, 3.65, "ordens", ha="left", va="center", fontsize=16,
        style="italic", color=GREEN_DARK)
for x, letter in zip(xs, PEOPLE):
    person(x, ys, letter)
ax.annotate("", xy=(xs[0], ys - 0.55), xytext=(xs[-1], ys - 0.55),
            arrowprops=dict(arrowstyle="-", color=GREY, lw=1.5, ls=(0, (2, 3))))
ax.text(rx, ys - 0.78, "sem ligação entre executores", ha="center", va="center",
        fontsize=15, style="italic", color=GREY)
legend(7.45, 1.0, [
    ("Decide:", "a autoridade define todas as tarefas"),
    ("Supervisiona:", "controla diretamente cada executor"),
    ("Executa:", "cada um cumpre a sua parte, sem negociar"),
])

fig.savefig("/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap04/slides/3c-vs-c2-slide.png",
            facecolor="white")
print("done")
