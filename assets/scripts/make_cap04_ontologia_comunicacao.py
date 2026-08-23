import sys
sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from graphviz_utils import build_dot, render
from sebenta_style import DARK

nodes = {
    "Compromisso":   ("Compromisso", 1.3, 6.6, False, False),
    "Negociacao":    ("Negociação", 1.3, 5.0, False, False),
    "Objetivos":     ("Objetivos", 1.3, 3.5, True, False),

    "FormaEx":       ("Linguística\nSimbólica/Iconográfica\nLinguagem Corporal\nIndireta (pistas no ambiente)",
                       3.9, 7.4, False, False, True),
    "Forma":         ("Forma", 3.9, 5.9, False, False),

    "SistemaColab":  ("Sistema\nColaborativo", 6.6, 7.4, False, False),
    "MeioTransm":    ("Meio de\nTransmissão", 6.6, 5.9, False, False),
    "MeioEx":        ("Face a face\nTelefone\nPapel\nQuadro negro\nSistema computacional",
                       9.4, 7.4, False, False, True),

    "Sincronismo":   ("Síncronismo", 9.6, 5.9, False, False),
    "SincronismoEx": ("Síncrona\nAssíncrona", 9.6, 4.5, False, False, True),

    "Mensagem":      ("Mensagem", 5.8, 3.6, False, True),

    "Codificacao":   ("Codificação", 3.6, 2.0, False, False),
    "Interpretacao": ("Interpretação", 8.0, 2.0, False, False),

    "Emissor":       ("Emissor", 3.6, 0.4, False, False),
    "ProtocoloCom":  ("Protocolo de\nComunicação", 5.8, 0.4, False, False),
    "Receptor":      ("Receptor", 8.0, 0.4, False, False),

    "SensoComum":    ("Senso\nComum", 5.8, -1.1, False, False),
    "Participante":  ("Participante", 3.6, -1.1, True, False),
}

edges = [
    ("FormaEx", "Forma", "É um", False),
    ("MeioEx", "MeioTransm", "É um", False),
    ("SincronismoEx", "Sincronismo", "É um", False),
    ("SistemaColab", "MeioTransm", "É um", False),
    ("Sincronismo", "MeioTransm", "Determina", False),
    ("MeioTransm", "Forma", "Restringe", False),
    ("Negociacao", "Compromisso", "Resulta em", False),
    ("Negociacao", "Objetivos", "Define", False),
    ("Negociacao", "Mensagem", "É realizada por meio de", True),
    ("Mensagem", "Compromisso", "Estabelece", True),
    ("Forma", "Mensagem", "É atributo de", True),
    ("MeioTransm", "Mensagem", "É atributo de", True),
    ("Sincronismo", "Mensagem", "É atributo de", True),
    ("Codificacao", "Mensagem", "Gera", True),
    ("Mensagem", "Interpretacao", "Gera", True),
    ("Emissor", "Codificacao", "Gera", False),
    ("Emissor", "Mensagem", "Envia", True),
    ("Mensagem", "ProtocoloCom", "Segue", True),
    ("Receptor", "Mensagem", "Recebe", True),
    ("Receptor", "Interpretacao", "Gera", False),
    ("Emissor", "ProtocoloCom", "Usa", False),
    ("Receptor", "ProtocoloCom", "Usa", False),
    ("Emissor", "SensoComum", "Compartilha", False),
    ("Receptor", "SensoComum", "Compartilha", False),
    ("Emissor", "Participante", "É um", True),
    ("Receptor", "Participante", "É um", True),
    ("Participante", "Compromisso", "Assume", True),
]

dot_src = build_dot(nodes, edges)
dot_src = dot_src.replace(
    "digraph G {",
    'digraph G {\n  labelloc="t"; fontsize=26; fontname="Helvetica-Bold"; '
    f'fontcolor="{DARK}"; label="Ontologia sobre Comunicação";'
)

render(dot_src, "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap04/ontologia-comunicacao.png",
       dpi=200, target_width_px=2200)
print("done")
