import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import itertools, math, sys

sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from sebenta_style import (DARK, MAGENTA, PINK, GREY, NOTE_COLOR, apply_style,
                            TITLE_SIZE, NODE_LABEL_SIZE, NODE_LABEL_SIZE_HI, NOTE_SIZE,
                            BIG_NUMBER_SIZE, NODE_RADIUS, NODE_RADIUS_HI, EDGE_WIDTH, EDGE_WIDTH_HI,
                            REFERENCE_WIDTH)

apply_style()

# Rede genérica de 5 nós: a densidade pode ser calculada para qualquer
# um deles. Usa-se o nó D como exemplo concreto em cada painel (mesma
# rede, mesmos pares possíveis; o que muda são as ligações ativas).
#
# Layout em coluna (3 linhas x 1), largura = REFERENCE_WIDTH, tal como a
# Figura 3.2. Pentágono à esquerda, número/nota à direita, para que a
# proporção largura/altura de cada painel preencha a largura total da
# figura (evita letterboxing + corte pelo bbox_inches="tight").

nodes = ["A", "B", "C", "D", "E"]
all_pairs = list(itertools.combinations(nodes, 2))  # 10 ligações possíveis na rede

CX, CY = -0.7, 0.0
pos = {}
R = 1.35
for i, n in enumerate(nodes):
    ang = math.pi/2 + i * (2*math.pi/5)
    pos[n] = (CX + R*math.cos(ang), CY + R*math.sin(ang))

panels = [
    ("Densidade baixa", [("A","B"), ("C","E"), ("B","D")]),
    ("Densidade média", [("A","B"), ("A","C"), ("A","E"), ("B","D"), ("C","D"), ("C","E")]),
    ("Densidade máxima", all_pairs),
]

fig, axes = plt.subplots(3, 1, figsize=(REFERENCE_WIDTH, 11.5), dpi=200)

for ax, (title, active) in zip(axes, panels):
    ax.set_xlim(-2.3, 3.6)
    ax.set_ylim(-1.65, 1.75)
    ax.set_aspect("equal")
    ax.axis("off")

    active_set = set(frozenset(e) for e in active)

    for u, v in all_pairs:
        if frozenset((u, v)) not in active_set:
            ax.plot([pos[u][0], pos[v][0]], [pos[u][1], pos[v][1]], color=GREY,
                     linewidth=EDGE_WIDTH * 0.75, linestyle=(0, (5, 4)), zorder=1)

    for u, v in active:
        ax.plot([pos[u][0], pos[v][0]], [pos[u][1], pos[v][1]], color=MAGENTA,
                 linewidth=EDGE_WIDTH_HI, solid_capstyle="round", zorder=2)

    for n in nodes:
        x, y = pos[n]
        is_d = (n == "D")
        r = NODE_RADIUS_HI if is_d else NODE_RADIUS
        color = MAGENTA if is_d else DARK
        circle = plt.Circle((x, y), r, facecolor=color, edgecolor="white", linewidth=2.2, zorder=3)
        ax.add_patch(circle)
        ax.text(x, y, n, ha="center", va="center",
                fontsize=NODE_LABEL_SIZE_HI if is_d else NODE_LABEL_SIZE,
                color="white", fontweight="bold", zorder=4)

    d_degree = sum(1 for u, v in active if "D" in (u, v))
    density_d = d_degree / 4  # D tem 4 ligações possíveis (n-1)

    ax.set_title(title, fontsize=TITLE_SIZE, fontweight="bold", color=DARK, pad=20, loc="left", x=0.0)
    ax.text(2.5, 0.25, f"{density_d:.2f}".replace(".", ","), ha="center", va="center",
            fontsize=BIG_NUMBER_SIZE, fontweight="bold", color=PINK)
    ax.text(2.5, -0.55, f"D tem {d_degree} das 4\nligações possíveis",
            ha="center", va="top", fontsize=NOTE_SIZE, color=NOTE_COLOR, style="italic")

fig.tight_layout(h_pad=4.5)
# NOTA: sem bbox_inches="tight" de propósito -- com aspect="equal" e um
# rácio largura/altura de dados que não preenche exatamente a caixa,
# "tight" corta para o conteúdo realmente desenhado e pode devolver uma
# imagem MAIS ESTREITA do que REFERENCE_WIDTH, o que desfaz a comparação
# de tamanho de letra com as outras figuras. Guardar a tela completa
# garante que a largura nativa é sempre REFERENCE_WIDTH * dpi.
fig.savefig("/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap03/densidade.png",
            facecolor="white")
print("done")
