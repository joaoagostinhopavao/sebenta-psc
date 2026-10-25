import sys
from pptx import Presentation

# Aula 5: "O Modelo de Atividade em Pormenor" passa para depois do exemplo
# da Viagem de Finalistas, logo antes da ponte "Da Atividade à
# Colaboração", que usa as suas quatro partes. Acerta as notas que
# dependiam da ordem. Depois correr numerar_slides.py. Só com o deck fechado.
DECK = sys.argv[1]


def titulo(s):
    return [sh.text_frame.text for sh in s.shapes if sh.has_text_frame]


p = Presentation(DECK)
slides = list(p.slides)
pormenor = next(s for s in slides if "O Modelo de Atividade em Pormenor" in titulo(s))
preenchido = next(s for s in slides if "Exemplo: o Modelo Preenchido" in titulo(s))
ponte = next(s for s in slides if "Da Atividade à Colaboração" in titulo(s))

lst = p.slides._sldIdLst
ids = list(lst)
el = ids[slides.index(pormenor)]
lst.remove(el)
lst.insert(list(p.slides).index(preenchido) + 1, el)

tf = pormenor.notes_slide.notes_text_frame
tf.text = (tf.text
           .replace("• Este esquema mostra o mesmo modelo do slide anterior, agora com exemplos de cada elemento",
                    "• Depois da viagem, o mesmo modelo com exemplos gerais de cada elemento e as quatro partes de uma atividade em sociedade")
           .replace("• A seguir, aplicar o modelo a uma situação concreta: a viagem de finalistas",
                    "• A seguir, ver estas partes na viagem de finalistas"))
tf = ponte.notes_slide.notes_text_frame
tf.text = tf.text.replace("(slide 9)", "(slide anterior)")

p.save(DECK)
print("Pormenor agora é o slide", list(p.slides).index(pormenor) + 1)
