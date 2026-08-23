import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

DARK = "#1f0a2e"
MAGENTA = "#9c1f8f"
PINK = "#e857b0"
MID = "#6b3d68"

plt.rcParams.update({"font.family": "sans-serif", "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans"]})

# (texto, x, y, fontsize, cor, peso)
words = [
    ("folksonomia", 5.0, 3.1, 58, DARK, "bold"),
    ("hashtag", 2.0, 4.3, 34, MAGENTA, "bold"),
    ("etiquetas", 8.1, 4.2, 32, MAGENTA, "bold"),
    ("redes sociais", 5.0, 5.0, 26, MID, "bold"),
    ("tagging", 1.5, 2.4, 24, PINK, "bold"),
    ("classificação", 8.4, 2.3, 22, PINK, "bold"),
    ("comunidade", 2.6, 1.2, 18, MID, "normal"),
    ("colaborativa", 7.3, 1.1, 18, MID, "normal"),
    ("interesses", 4.2, 0.55, 15, DARK, "normal"),
    ("partilha", 6.3, 0.55, 15, DARK, "normal"),
    ("popular", 0.7, 3.4, 14, MID, "normal"),
    ("conteúdo", 9.3, 3.5, 14, MID, "normal"),
    ("algoritmo", 1.1, 5.3, 12, "#9a8a97", "normal"),
    ("viral", 8.9, 5.4, 12, "#9a8a97", "normal"),
    ("tendência", 3.3, 5.7, 11, "#9a8a97", "normal"),
    ("perfil", 6.7, 5.7, 11, "#9a8a97", "normal"),
    ("moda", 0.3, 1.0, 10, "#9a8a97", "normal"),
    ("memes", 9.5, 0.9, 10, "#9a8a97", "normal"),
]

fig, ax = plt.subplots(figsize=(10, 6.2), dpi=200)
ax.set_xlim(0, 10)
ax.set_ylim(0, 6.2)
ax.axis("off")

for txt, x, y, fs, color, weight in words:
    ax.text(x, y, txt, ha="center", va="center", fontsize=fs, color=color,
            fontweight=weight, family="sans-serif")

fig.tight_layout(pad=0.4)
fig.savefig("/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap03/nuvem-etiquetas.png",
            facecolor="white", bbox_inches="tight", pad_inches=0.3)
print("done")
