"""
Utilitário partilhado para diagramas de grafo (nós + arestas rotuladas)
da Sebenta-PSC, gerados com Graphviz/neato em vez de matplotlib manual.

Chamamos a este método simplesmente "Graphviz" nas conversas do projeto
-- é a ferramenta real por trás (motor de layout "neato", com posições
fixas via pos="x,y!"). É o método preferido sempre que a figura é
essencialmente um grafo com nós e relações rotuladas (ontologias,
modelos conceptuais, diagramas de blocos), por dar layout preciso e
texto sempre legível, ao contrário de posicionar caixas à mão em
matplotlib. Para diagramas geométricos (gráficos de dados, redes
sociais desenhadas como grafo social real, etc.) continua a usar-se
sebenta_style.py + matplotlib.

Usa posições fixas (pos="x,y!") para controlar o layout, e a
paleta/tipografia da sebenta_style. Depois de gerado o PNG, o canvas é
sempre ajustado (com PADDING, nunca com escala) para a largura nativa
exata REFERENCE_WIDTH*dpi ou SLIDE_REFERENCE_WIDTH*dpi, seguindo a mesma
disciplina usada em todas as outras ilustrações.
"""

import subprocess
import sys
from PIL import Image

sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from sebenta_style import DARK, MAGENTA, PINK, GREY, NOTE_COLOR

FILL = "#f4f0f6"


def node_attrs(dashed=False, highlight=False, note=False):
    if note:
        return dict(shape="note", style="filled,dashed", fillcolor="white",
                    color=GREY, fontcolor=NOTE_COLOR, fontname="Helvetica",
                    fontsize=10.5)
    if highlight:
        return dict(style="filled", fillcolor=DARK, fontcolor="white",
                    color=DARK, fontname="Helvetica-Bold")
    return dict(style="filled,dashed" if dashed else "filled",
                fillcolor=FILL, color=GREY, fontcolor=DARK, fontname="Helvetica")


def build_dot(nodes, edges, node_font=15, edge_font=11.5):
    """
    nodes: dict name -> (label, x, y, dashed(bool), highlight(bool)[, note(bool)])
    edges: list of (src, dst, label, accent(bool))
    """
    lines = [
        "digraph G {",
        '  graph [layout=neato, overlap=false, splines=line, margin=0];',
        f'  node [shape=ellipse, fontsize={node_font}, fixedsize=false, '
        'width=1.0, height=0.6];',
        f'  edge [fontsize={edge_font}, fontname="Helvetica", arrowsize=0.7];',
    ]
    for name, spec in nodes.items():
        label, x, y, dashed, highlight = spec[:5]
        note = spec[5] if len(spec) > 5 else False
        attrs = node_attrs(dashed, highlight, note)
        attr_str = ", ".join(f'{k}="{v}"' for k, v in attrs.items())
        # pos é em pontos (72/in); as coordenadas dos scripts são em polegadas.
        lines.append(f'  "{name}" [label="{label}", pos="{x * 72},{y * 72}!", {attr_str}];')
    for src, dst, label, accent in edges:
        color = MAGENTA if accent else GREY
        lines.append(
            f'  "{src}" -> "{dst}" [label="{label}", color="{color}", '
            f'fontcolor="{NOTE_COLOR}"];'
        )
    lines.append("}")
    return "\n".join(lines)


def render(dot_src, out_path, dpi=200, target_width_px=None, extra_bottom_px=0,
           engine="neato"):
    proc = subprocess.run([engine, "-n2", "-Tpng", f"-Gdpi={dpi}"],
                           input=dot_src.encode(), capture_output=True, check=True)
    if proc.returncode != 0 or not proc.stdout:
        raise RuntimeError(proc.stderr.decode())
    with open(out_path, "wb") as f:
        f.write(proc.stdout)

    if target_width_px:
        raw = Image.open(out_path).convert("RGBA")
        flat = Image.new("RGBA", raw.size, "white")
        flat.paste(raw, (0, 0), raw)
        img = flat.convert("RGB")
        w, h = img.size
        new_w = max(w, target_width_px)
        new_h = h + extra_bottom_px
        canvas = Image.new("RGB", (new_w, new_h), "white")
        x = (new_w - w) // 2
        canvas.paste(img, (x, 0))
        canvas.save(out_path)
    return out_path
