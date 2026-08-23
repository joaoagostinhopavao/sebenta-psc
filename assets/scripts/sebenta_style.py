"""
Estilo visual partilhado para todas as ilustrações da Sebenta-PSC
(matplotlib). Qualquer script novo de ilustração deve importar destas
constantes em vez de escolher tamanhos/cores à parte — isto existe
precisamente para não ser preciso pedir "aumenta a fonte" de cada vez.

Uso típico:

    import sys
    sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
    from sebenta_style import DARK, MAGENTA, PINK, GREY, apply_style, \
        TITLE_SIZE, NODE_LABEL_SIZE, NODE_LABEL_SIZE_HI, NOTE_SIZE

    apply_style()  # configura a fonte por omissão do matplotlib

Exceção conhecida: nuvens de etiquetas (tag clouds), onde a variação de
tamanho de letra é o próprio conteúdo (codifica frequência) — nesse caso
não se aplicam TITLE_SIZE/NODE_LABEL_SIZE da mesma forma.
"""

import matplotlib.pyplot as plt

# --- paleta ---------------------------------------------------------
DARK = "#1f0a2e"      # violeta muito escuro — texto, nós normais
MAGENTA = "#9c1f8f"   # magenta — acento principal, nós/ligações em destaque
PINK = "#e857b0"      # rosa vibrante — acento secundário
GREY = "#c9bccf"      # cinza-lilás — ligações/elementos não destacados
NOTE_COLOR = "#5c4f60"  # cinza-arroxeado — texto de apoio/notas

# --- tamanhos de fonte (mínimos — nunca ir abaixo disto) ------------
# Calibrados em 2026-08-20 a partir da Figura 3.2 (centralidade), que o
# professor validou como referência de tamanho correto.
TITLE_SIZE = 30          # título de cada painel/figura
NODE_LABEL_SIZE = 19     # letra dentro de um nó normal
NODE_LABEL_SIZE_HI = 23  # letra dentro de um nó em destaque (maior)
NOTE_SIZE = 20           # legenda/nota de apoio por baixo de um painel
BIG_NUMBER_SIZE = 56     # número "herói" (estatística em destaque)

# --- espessuras/raios de referência ---------------------------------
NODE_RADIUS = 0.27
NODE_RADIUS_HI = 0.36
EDGE_WIDTH = 3.0
EDGE_WIDTH_HI = 4.4

# --- largura de referência para onde os tamanhos acima foram calibrados
# (Figura 3.2, centralidade.py: fig.subplots(3, 1, figsize=(11, ...))).
REFERENCE_WIDTH = 11.0


def scale_for(fig_width):
    """
    Fator de correção OBRIGATÓRIO para qualquer figura com largura
    diferente de REFERENCE_WIDTH.

    O motivo: o Quarto/browser redimensiona todas as imagens à mesma
    largura de coluna. Se uma figura tiver um canvas nativo mais largo
    (ex.: vários painéis lado a lado), o MESMO fontsize em pontos fica
    proporcionalmente mais pequeno depois desse redimensionamento — não
    chega usar as constantes TITLE_SIZE/NOTE_SIZE/etc. tal e qual; têm de
    ser multiplicadas por este fator.

    Uso:
        SCALE = scale_for(19)  # largura do fig, em polegadas
        ax.set_title(t, fontsize=TITLE_SIZE * SCALE, ...)
        ax.plot(..., linewidth=EDGE_WIDTH * SCALE)

    Nota: o raio dos nós (NODE_RADIUS/NODE_RADIUS_HI) está em unidades de
    dados, não em pontos — escala automaticamente com a largura da figura
    e NÃO deve ser multiplicado por este fator (senão fica em dobro).
    """
    return fig_width / REFERENCE_WIDTH


def apply_style():
    """Configura a fonte por omissão do matplotlib para todas as figuras."""
    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans"],
    })


# ============================================================
# VERSÃO PARA SLIDES (Gamma/PowerPoint, 16:9, anfiteatro)
# ============================================================
# As figuras do livro são pensadas para uma coluna de texto estreita.
# Os slides são um contentor muito mais largo (ecrã 16:9 quase inteiro)
# E têm de ser lidos à distância, num anfiteatro — por isso usam a sua
# própria largura de referência E constantes de letra maiores, não só a
# mesma REFERENCE_WIDTH renormalizada.
#
# SLIDE_REFERENCE_WIDTH = 13.333in corresponde à largura de um slide
# 16:9 standard (ex.: PowerPoint widescreen), assumindo que a ilustração
# ocupa perto da largura total do slide (como nos slides dedicados de
# imagem que já reservámos no Gamma). Se uma imagem for inserida mais
# pequena que isso dentro do slide, ainda assim fica legível — só deixa
# de estar "no limite" da escala calibrada.

SLIDE_REFERENCE_WIDTH = 13.333

# NOTA (2026-08-20): a primeira tentativa usou tamanhos "anfiteatro"
# (título 40pt) para 3-4 painéis lado a lado neste canvas -- resultou em
# texto sobreposto, porque cada painel tem, na prática, MENOS largura
# (13.33/4=3.33in) do que um único painel do livro (11in). O professor
# escolheu manter a comparação toda num único slide, com letra mais
# modesta em vez de a máxima -- estes valores são esse compromisso.
# Calibrados para grelhas de 3-4 painéis lado a lado; se um layout novo
# tiver MENOS painéis (ou for vertical), pode voltar a usar valores mais
# próximos de SLIDE_TITLE_SIZE cheio.
SLIDE_TITLE_SIZE = 24
SLIDE_NODE_LABEL_SIZE = 16
SLIDE_NODE_LABEL_SIZE_HI = 19
SLIDE_NOTE_SIZE = 16
SLIDE_BIG_NUMBER_SIZE = 44

SLIDE_NODE_RADIUS = 0.27
SLIDE_NODE_RADIUS_HI = 0.36
SLIDE_EDGE_WIDTH = 3.0
SLIDE_EDGE_WIDTH_HI = 4.2


def scale_for_slide(fig_width):
    """Equivalente a scale_for(), mas contra SLIDE_REFERENCE_WIDTH."""
    return fig_width / SLIDE_REFERENCE_WIDTH
