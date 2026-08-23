import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

DARK = "#1f0a2e"
MAGENTA = "#9c1f8f"
PINK = "#e857b0"
GRID = "#e4dee6"

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans"],
    "text.color": DARK,
    "axes.edgecolor": DARK,
    "axes.labelcolor": DARK,
    "xtick.color": DARK,
    "ytick.color": DARK,
    "axes.facecolor": "white",
    "figure.facecolor": "white",
    "savefig.facecolor": "white",
})

# ---------------------------------------------------------------
# Chart 1: Alcance das plataformas em Portugal (jan. 2024)
# Fonte: DataReportalPortugal2024
# ---------------------------------------------------------------
platforms = ["Snapchat", "X (Twitter)", "Pinterest", "TikTok*", "Messenger",
             "LinkedIn", "Instagram", "Facebook", "YouTube"]
values = [10.1, 19.6, 24.6, 42.6, 46.4, 47.9, 56.7, 58.1, 72.6]

fig, ax = plt.subplots(figsize=(8.6, 5.4), dpi=200)
bars = ax.barh(platforms, values, color=MAGENTA, height=0.62, zorder=3)
bars[-1].set_color(DARK)  # destaque YouTube (topo)

ax.set_xlim(0, 84)
ax.set_xlabel("Alcance potencial de publicidade (% da população)", fontsize=13)
ax.xaxis.grid(True, color=GRID, zorder=0)
ax.set_axisbelow(True)
for spine in ["top", "right", "left"]:
    ax.spines[spine].set_visible(False)
ax.spines["bottom"].set_color(DARK)
ax.tick_params(left=False, labelsize=13)

for bar, v in zip(bars, values):
    ax.text(v + 1.6, bar.get_y() + bar.get_height() / 2, f"{v:.1f}%",
            va="center", ha="left", fontsize=12.5, color=DARK, fontweight="bold")

ax.set_title("Alcance das principais plataformas em Portugal (jan. 2024)",
             fontsize=15.5, fontweight="bold", color=DARK, pad=16, loc="left")
fig.text(0.02, 0.015, "* TikTok: alcance entre adultos (18+), restantes plataformas: % da população total.\nFonte: DataReportal / We Are Social / Meltwater, Digital 2024: Portugal.",
          fontsize=10, color="#5c4f60")
fig.tight_layout(rect=[0, 0.09, 1, 1])
fig.savefig("/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap02/pt-plataformas-2024.png")
plt.close(fig)

# ---------------------------------------------------------------
# Chart 2: Adoção da Internet e das redes sociais, Mundial vs Portugal (2024)
# Fonte: WeAreSocial2024 (mundial) e DataReportalPortugal2024 (Portugal)
# ---------------------------------------------------------------
categories = ["Mundial", "Portugal"]
internet = [66.2, 86.4]
social = [62.3, 72.6]

x = range(len(categories))
width = 0.32

fig, ax = plt.subplots(figsize=(7.2, 5.0), dpi=200)
b1 = ax.bar([i - width/2 for i in x], internet, width, label="Utilizadores de Internet",
            color=DARK, zorder=3)
b2 = ax.bar([i + width/2 for i in x], social, width, label="Utilizadores de redes sociais",
            color=PINK, zorder=3)

ax.set_ylim(0, 100)
ax.set_ylabel("% da população", fontsize=13)
ax.set_xticks(list(x))
ax.set_xticklabels(categories, fontsize=14)
ax.yaxis.grid(True, color=GRID, zorder=0)
ax.set_axisbelow(True)
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)
ax.tick_params(bottom=False, labelsize=13)

for bars in (b1, b2):
    for bar in bars:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, h + 1.8, f"{h:.1f}%",
                ha="center", va="bottom", fontsize=12.5, color=DARK, fontweight="bold")

ax.legend(frameon=False, fontsize=12, loc="upper left", bbox_to_anchor=(0, 1.16), ncol=1)
ax.set_title("Adoção da Internet e das redes sociais (2024)",
             fontsize=15.5, fontweight="bold", color=DARK, pad=52, loc="left")
fig.text(0.02, 0.015, "Fonte: We Are Social / Meltwater, Digital 2024 (mundial); DataReportal, Digital 2024: Portugal.",
          fontsize=10, color="#5c4f60")
fig.tight_layout(rect=[0, 0.06, 1, 1])
fig.savefig("/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap02/adocao-mundial-portugal-2024.png")
plt.close(fig)

print("done")
