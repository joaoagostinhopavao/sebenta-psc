import copy
import sys
from pptx import Presentation
from pptx.util import Emu

# Aula 5: o slide "Aplicação à Sala de Aula" (redundante depois da Viagem
# de Finalistas) passa a ser a ponte "Da Atividade aos 3C". Reaproveita o
# cabeçalho, três ícones e os estilos de texto do próprio slide.
# Só com o deck fechado.
DECK = sys.argv[1]

LINHAS = [  # (ícone, título, corpo)
    ("Image 3", "Troca  =  Comunicação",
     "As discussões e as sondagens no grupo de WhatsApp: a turma negoceia e assume "
     "compromissos (máximo de 350 € por pessoa)."),
    ("Image 4", "Distribuição  =  Coordenação",
     "A divisão de trabalho (Ana trata do alojamento, Bruno do transporte…) e os "
     "prazos (quota paga até 15 de março)."),
    ("Image 2", "Produção  =  Cooperação",
     "O trabalho feito em conjunto no espaço partilhado: a folha de cálculo dos "
     "pagamentos e as reservas."),
]
NOTAS = (
    "• Ponte entre os dois modelos: três das quatro partes da atividade em sociedade (slide 9) "
    "são as três dimensões do Modelo 3C: produção = cooperação, distribuição = coordenação, "
    "troca = comunicação (Fuks et al., 2011)\n\n"
    "• A Teoria da Atividade descreve a estrutura da atividade (quem, sobre quê, com que "
    "ferramentas, com que regras); o Modelo 3C descreve a dinâmica da colaboração\n\n"
    "• Ler a viagem pelos 3C com a turma, linha a linha\n\n"
    "• Terminar com o imprevisto do hotel: a cooperação exige nova comunicação, que exige "
    "coordenação; é o ciclo do slide seguinte"
)

p = Presentation(DECK)
slide = next(s for s in p.slides
             if any(sh.has_text_frame and sh.text_frame.text == "Aplicação à Sala de Aula"
                    for sh in s.shapes))
sh = {s.name: s for s in slide.shapes}

sh["Text 1"].text_frame.paragraphs[0].runs[0].text = "MODELO 3C"
sh["Text 2"].text_frame.paragraphs[0].runs[0].text = "Da Atividade aos 3C"
sh["Text 3"].text_frame.paragraphs[0].runs[0].text = (
    "Três das quatro partes da atividade são as três dimensões do Modelo 3C. "
    "Na viagem de finalistas:")
sh["Text 3"].width = Emu(10868745)

titulos, corpos = ["Text 4", "Text 6", "Text 8"], ["Text 5", "Text 7", "Text 9"]
topo, passo = 2713732, 900000
for i, (icone, titulo, corpo) in enumerate(LINHAS):
    y = topo + i * passo
    sh[icone].left, sh[icone].top = Emu(661475), Emu(y)
    t, c = sh[titulos[i]], sh[corpos[i]]
    t.left, t.top, t.width = Emu(1198830), Emu(y + 56852), Emu(10331390)
    c.left, c.top, c.width, c.height = Emu(1198830), Emu(y + 414536), Emu(10331390), Emu(264616)
    t.text_frame.paragraphs[0].runs[0].text = titulo
    c.text_frame.paragraphs[0].runs[0].text = corpo

for nome in ["Image 0", "Image 1", "Image 5", "Text 10", "Text 11", "Text 12", "Text 13",
             "Text 14", "Text 15"]:
    sh[nome]._element.getparent().remove(sh[nome]._element)

# remate: o imprevisto que leva ao ciclo do slide seguinte
el = copy.deepcopy(sh["Text 3"]._element)
slide.shapes._spTree.append(el)
fim = slide.shapes[-1]
fim.top, fim.height = Emu(topo + 3 * passo + 120000), Emu(560000)
par = fim.text_frame.paragraphs[0]
r1 = par.runs[0]
r1.text = "E se o hotel cancelar? "
r1.font.bold = True
r2 = copy.deepcopy(r1._r)
r1._r.addnext(r2)
par.runs[1].text = ("A comissão volta ao WhatsApp para decidir (comunicação) e a Ana "
                    "reorganiza o alojamento (coordenação): os 3C formam um ciclo.")
par.runs[1].font.bold = False
fim.text_frame.word_wrap = True

slide.notes_slide.notes_text_frame.text = NOTAS
p.save(DECK)
print("ok", p.slides.index(slide) + 1)
