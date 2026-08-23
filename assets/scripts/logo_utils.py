"""
Biblioteca central de ícones/logótipos da Sebenta-PSC.

Estrutura de pastas (assets/images/icons/):
    historicos/   plataformas históricas/extintas (ICQ, MSN, Orkut, Friendster...)
    brands/       marcas/apps modernas (Simple Icons, ver fetch_simple_icon())
    tech/         ícones genéricos de computador/rede/cloud (servidores, routers...)
    _norm/        cache partilhada dos ícones já normalizados (recortados + em canvas
                   quadrado); indexada por "categoria__nome" para não colidir entre
                   pastas.

Regra de proveniência: todo o ícone usado na sebenta tem de ser verificado
visualmente antes de ser inserido numa figura (ver README das figuras).
"""

import os
import subprocess
import urllib.request

from PIL import Image

ICONS_ROOT = "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/icons"
HISTORICOS_DIR = os.path.join(ICONS_ROOT, "historicos")
BRANDS_DIR = os.path.join(ICONS_ROOT, "brands")
TECH_DIR = os.path.join(ICONS_ROOT, "tech")
NORM_DIR = os.path.join(ICONS_ROOT, "_norm")

os.makedirs(NORM_DIR, exist_ok=True)

CANVAS = 260
PAD = 18

_CATEGORY_DIRS = {
    "historicos": HISTORICOS_DIR,
    "brands": BRANDS_DIR,
    "tech": TECH_DIR,
}


def normalize(name, category="historicos", canvas=CANVAS, pad=PAD):
    """Devolve o caminho para o PNG normalizado (recortado ao conteúdo,
    escalado PROPORCIONALMENTE para caber num canvas quadrado com
    padding, e centrado). Resultado é cacheado em _norm/.

    IMPORTANTE: a rasterização de SVG usa apenas "-w" (nunca "-w" e "-h"
    em simultâneo) para que o rsvg-convert preserve o aspect-ratio nativo
    do ficheiro. Passar as duas dimensões ao mesmo tempo sem
    --keep-aspect-ratio esmaga/estica logótipos não-quadrados (ex.:
    wordmarks largos como o LinkedIn ou o Flickr, ~4:1) para caberem num
    quadrado 512x512 -- foi exactamente este bug que distorceu o LinkedIn
    na Figura 2.3 do Cap.2, corrigido nesta função.
    """
    out = os.path.join(NORM_DIR, f"{category}__{name}.png")
    if os.path.exists(out):
        return out

    src_dir = _CATEGORY_DIRS.get(category, category)
    svg = os.path.join(src_dir, name + ".svg")
    png = os.path.join(src_dir, name + ".png")

    src = None
    if os.path.exists(svg):
        raw = os.path.join(NORM_DIR, f"{category}__{name}_raw.png")
        subprocess.run(["rsvg-convert", "-w", "1024", "-o", raw, svg], check=True)
        src = raw
    elif os.path.exists(png):
        src = png
    else:
        return None

    img = Image.open(src).convert("RGBA")
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)

    target = canvas - 2 * pad
    w, h = img.size
    scale = target / max(w, h)
    img = img.resize((max(1, int(w * scale)), max(1, int(h * scale))), Image.LANCZOS)

    out_canvas = Image.new("RGBA", (canvas, canvas), (0, 0, 0, 0))
    x = (canvas - img.width) // 2
    y = (canvas - img.height) // 2
    out_canvas.paste(img, (x, y), img)
    out_canvas.save(out)
    return out


def fetch_simple_icon(slug, dest_name=None):
    """Descarrega um ícone de marca do Simple Icons (github.com/simple-icons)
    para assets/images/icons/brands/. `slug` é o nome usado pelo projecto
    (ver https://simpleicons.org, ex.: "linkedin", "docker", "kubernetes").
    NÃO substitui a verificação visual: confirmar sempre o resultado antes
    de o usar numa figura.
    """
    dest_name = dest_name or slug
    dest = os.path.join(BRANDS_DIR, dest_name + ".svg")
    if os.path.exists(dest):
        return dest
    url = f"https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/{slug}.svg"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as resp:
        data = resp.read()
    os.makedirs(BRANDS_DIR, exist_ok=True)
    with open(dest, "wb") as f:
        f.write(data)
    return dest
