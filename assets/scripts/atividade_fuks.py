import sys
import matplotlib.pyplot as plt

sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from sebenta_style import DARK, MAGENTA, NOTE_COLOR

# Modelo de Atividade com exemplos de cada elemento e os quatro
# subtriângulos (produção, troca, distribuição, consumo), redesenhado a
# partir da Figura 2.3 de Fuks et al. (2011), que por sua vez adapta
# Engeström (1987). Acrescenta-se a correspondência com os 3C, que no
# original está só no texto.
# Uso: atividade_fuks.py livro pt|en  ·  atividade_fuks.py slide
ESTILO = sys.argv[1] if len(sys.argv) > 1 else "livro"
LANG = sys.argv[2] if len(sys.argv) > 2 else "pt"

COR = {
    "livro": dict(linha=DARK, titulo=DARK, sub=MAGENTA, nota=NOTE_COLOR),
    "slide": dict(linha="#1d5a32", titulo="#111111", sub="#3d8a52", nota="#4a4a4a"),
}[ESTILO]

TXT = {
    "pt": dict(
        A=("Artefactos", "sistema computacional, Internet,\ncomputador, técnica, método,\n"
                         "ferramenta, livro, caneta, etc."),
        S=("Sujeito", "utilizador,\ncliente,\naluno, etc."),
        O=("Objeto", "matéria-prima,\nconteúdo partilhado,\ndados, etc."),
        Res=("Resultado", "produto"),
        R=("Regras", "negociação, política,\nconhecimento partilhado,\n"
                     "protocolo de interação, etc."),
        C=("Comunidade", "utilizadores, clientes, gestores,\ncomunidade formal (organização),\n"
                         "comunidade de prática, etc."),
        D=("Divisão de\nTrabalho", "papéis, coordenação mútua,\n"
                                   "coordenação hierárquica (controlo)"),
        prod=("PRODUÇÃO", "(cooperação)"), troca=("TROCA", "(comunicação)"),
        dist=("DISTRIBUIÇÃO", "(coordenação)"), cons=("CONSUMO", ""),
        out="/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap04/teoria-atividade-fuks.png",
    ),
    "en": dict(
        A=("Artefacts", "computer system, Internet,\ncomputer, technique, method,\n"
                        "tool, book, pen, etc."),
        S=("Subject", "user,\nclient,\nstudent, etc."),
        O=("Object", "raw material,\nshared content,\ndata, etc."),
        Res=("Outcome", "product"),
        R=("Rules", "negotiation, policy,\nshared knowledge,\ninteraction protocol, etc."),
        C=("Community", "users, clients, managers,\nformal community (organisation),\n"
                        "community of practice, etc."),
        D=("Division of\nLabour", "roles, mutual coordination,\n"
                                  "hierarchical coordination (control)"),
        prod=("PRODUCTION", "(cooperation)"), troca=("EXCHANGE", "(communication)"),
        dist=("DISTRIBUTION", "(coordination)"), cons=("CONSUMPTION", ""),
        out="/Users/jpavao/QProjects/Sebenta-PSC/en/assets/images/cap04/teoria-atividade-fuks.png",
    ),
}["pt" if ESTILO == "slide" else LANG]
if ESTILO == "slide":
    TXT["out"] = ("/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap04/slides/"
                  "teoria-atividade-fuks-slide.png")

plt.rcParams["font.family"] = "Arial"
W, H = 13.333, 6.6
fig = plt.figure(figsize=(W, H), dpi=200)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.axis("off")

T, N, SUB = 21, 14.5, 13.5  # tamanhos: elemento, notas, subtriângulos

# triângulo grande; Sujeito, Objeto e Comunidade nos pontos médios dos lados
A = (6.0, 5.55)
R = (3.15, 1.55)
D = (8.85, 1.55)
S = ((A[0] + R[0]) / 2, (A[1] + R[1]) / 2)
O = ((A[0] + D[0]) / 2, (A[1] + D[1]) / 2)
C = ((R[0] + D[0]) / 2, R[1])
G = ((A[0] + R[0] + D[0]) / 3, (A[1] + R[1] + D[1]) / 3)


def seg(p, q, **kw):
    ax.plot([p[0], q[0]], [p[1], q[1]], solid_capstyle="round", **kw)


for p, q in [(A, R), (R, D), (D, A), (S, O), (O, C), (C, S)]:
    seg(p, q, color=COR["linha"], lw=2.4)
for p, q in [(A, C), (S, D), (O, R)]:  # as três medianas, a tracejado
    seg(p, q, color=COR["linha"], lw=1.2, ls=(0, (5, 4)), alpha=0.55)


def sub(x, y, chave):
    nome, c3 = TXT[chave]
    ax.text(x, y, nome, ha="center", va="center", fontsize=SUB, fontweight="bold",
            color=COR["sub"], bbox=dict(fc="white", ec="none", pad=1.5))
    if c3:
        ax.text(x, y - 0.27, c3, ha="center", va="center", fontsize=SUB - 1.5,
                color=COR["sub"], style="italic", bbox=dict(fc="white", ec="none", pad=1))


sub(A[0], (A[1] + S[1]) / 2 - 0.15, "prod")
sub((R[0] + C[0]) / 2 + 0.3, R[1] + 0.5, "troca")
sub((D[0] + C[0]) / 2 - 0.3, D[1] + 0.5, "dist")
sub(G[0], G[1] - 0.05, "cons")


def elemento(x, y, chave, ha, nx, ny, nha, nva="center"):
    nome, nota = TXT[chave]
    ax.text(x, y, nome, ha=ha, va="center", fontsize=T, fontweight="bold",
            color=COR["titulo"], linespacing=1.0)
    ax.text(nx, ny, nota, ha=nha, va=nva, fontsize=N, style="italic",
            color=COR["nota"], linespacing=1.2)


elemento(A[0], A[1] + 0.38, "A", "center", A[0] + 1.05, A[1] + 0.35, "left")
elemento(S[0] - 0.15, S[1], "S", "right", S[0] - 1.45, S[1], "right")
elemento(O[0] + 0.15, O[1], "O", "left", O[0] + 0.2, O[1] + 0.95, "left")
elemento(R[0] - 0.1, R[1] - 0.38, "R", "center", R[0] - 0.1, R[1] - 0.7, "center", "top")
elemento(C[0], C[1] - 0.38, "C", "center", C[0], C[1] - 0.7, "center", "top")
elemento(D[0] + 0.45, D[1] - 0.45, "D", "center", D[0] + 0.45, D[1] - 0.95, "center", "top")

# Objeto -> Resultado
x0 = O[0] + 1.3
ax.annotate("", xy=(x0 + 0.75, O[1]), xytext=(x0, O[1]),
            arrowprops=dict(arrowstyle="-|>", lw=3, color=COR["linha"], mutation_scale=24))
ax.text(x0 + 0.9, O[1], TXT["Res"][0], ha="left", va="center", fontsize=T,
        fontweight="bold", color=COR["titulo"])
ax.text(x0 + 0.9, O[1] - 0.42, TXT["Res"][1], ha="left", va="center", fontsize=N,
        style="italic", color=COR["nota"])

fig.savefig(TXT["out"], dpi=200, facecolor="white")
print("done", TXT["out"])
