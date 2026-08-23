import sys
sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from graphviz_utils import render
from sebenta_style import DARK, MAGENTA, GREY, NOTE_COLOR

FILL = "#f4f0f6"
HI_FILL = "#fbeaf7"


def cell(text, hi=False):
    bg = HI_FILL if hi else FILL
    border = f'BORDER="3" COLOR="{MAGENTA}"' if hi else f'BORDER="1" COLOR="{GREY}"'
    return (
        f'<TD BGCOLOR="{bg}" {border} CELLPADDING="18">'
        f'<FONT COLOR="{DARK}" POINT-SIZE="15">{text}</FONT>'
        f'</TD>'
    )


def header(text):
    return (f'<TD BORDER="0"><FONT COLOR="{DARK}" POINT-SIZE="16">'
            f'<B>{text}</B></FONT></TD>')


table = f"""<
<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="10">
<TR>
  <TD BORDER="0"></TD>
  {header("Mesmo tempo<BR/>(síncrono)")}
  {header("Tempo diferente<BR/>(assíncrono)")}
</TR>
<TR>
  {header("Mesmo local<BR/>(presencial)")}
  {cell("Conversa face a face", hi=True)}
  {cell("Notas Post-it ou quadro branco")}
</TR>
<TR>
  {header("Local diferente<BR/>(remoto)")}
  {cell("Mensageiro, chat,<BR/>áudio e videoconferência")}
  {cell("Correio eletrónico, lista,<BR/>fórum e Mapas de discussão,<BR/>blog e microblog")}
</TR>
</TABLE>>"""

dot_src = f"""digraph G {{
  labelloc="t"; fontsize=26; fontname="Helvetica-Bold"; fontcolor="{DARK}";
  label="Classificação Espaço-Tempo";
  graph [margin=0.3];
  node [shape=plaintext, fontname="Helvetica"];
  tabela [label={table}];
}}"""

render(dot_src, "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap05/espaco-tempo.png",
       dpi=200, target_width_px=2200, engine="dot")
print("done")
