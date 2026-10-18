import re
import runpy
import sys
sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
import graphviz_utils as gu

# Versões para slide (Aula 5) das quatro ontologias do Cap04
# (make_cap04_ontologia_{grupos,comunicacao,coordenacao,cooperacao}.py):
# paleta verde do deck, sem título interno (o slide já o tem), posições
# esticadas na horizontal para caberem a toda a largura do slide, e termos
# em PT-PT. Uso: slide_cap04_ontologias.py [nome ...]
GREEN = "#3d8a52"
GREEN_DARK = "#1d5a32"
GREEN_SOFT = "#a9c8b2"
FILL = "#eef5f0"
INK = "#111111"
NOTE = "#4a4a4a"

# largura e altura alvo (polegadas) do espaço ocupado pelos centros dos nós
TARGET = {"grupos": (11.0, 4.5), "comunicacao": (11.6, 5.6),
          "coordenacao": (11.4, 4.8), "cooperacao": (11.6, 5.4)}

PTPT = [("Compartilhamento", "Partilha"), ("Compartilhado", "Partilhado"),
        ("Compartilha", "Partilha"), ("Artefato", "Artefacto"),
        ("Co-localizado", "Colocalizado"), ("Repasse de tarefas", "Passagem de tarefas"),
        ("Apóia", "Apoia"), ("Síncronismo", "Sincronismo"), ("Status", "Estado")]


def node_attrs(dashed=False, highlight=False, note=False):
    if note:
        return dict(shape="note", style="filled,dashed", fillcolor="white",
                    color=GREEN_SOFT, fontcolor=NOTE, fontname="Helvetica",
                    fontsize=12)
    if highlight:
        return dict(style="filled", fillcolor=GREEN_DARK, fontcolor="white",
                    color=GREEN_DARK, fontname="Helvetica-Bold")
    return dict(style="filled,dashed" if dashed else "filled",
                fillcolor=FILL, color=GREEN, fontcolor=INK, fontname="Helvetica")


gu.node_attrs = node_attrs
gu.MAGENTA, gu.GREY, gu.NOTE_COLOR = GREEN, GREEN_SOFT, NOTE
_build = gu.build_dot
_render = gu.render


def run(name):
    tw, th = TARGET[name]

    def build_dot(nodes, edges, node_font=15, edge_font=11.5):
        xs = [v[1] for v in nodes.values()]
        ys = [v[2] for v in nodes.values()]
        sx = tw / (max(xs) - min(xs))
        sy = th / (max(ys) - min(ys))
        scaled = {k: (v[0], (v[1] - min(xs)) * sx, (v[2] - min(ys)) * sy) + tuple(v[3:])
                  for k, v in nodes.items()}
        return _build(scaled, edges, node_font=17, edge_font=13.5)

    def render(dot_src, out_path, dpi=200, target_width_px=None, **kw):
        dot_src = re.sub(r'\n  labelloc="t";[^\n]*', "", dot_src)
        for a, b in PTPT:
            dot_src = dot_src.replace(a, b)
        out = f"/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap04/slides/ontologia-{name}-slide.png"
        return _render(dot_src, out, dpi=dpi)

    gu.build_dot, gu.render = build_dot, render
    runpy.run_path(f"/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts/make_cap04_ontologia_{name}.py")


for name in (sys.argv[1:] or TARGET):
    run(name)
