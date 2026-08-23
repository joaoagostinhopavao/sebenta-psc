import sys
sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from graphviz_utils import render
from sebenta_style import DARK, MAGENTA, PINK, GREY, NOTE_COLOR

FILL = "#f4f0f6"


def cell(text, hi=False):
    bg = "#fbeaf7" if hi else FILL
    border = f'BORDER="3" COLOR="{MAGENTA}"' if hi else f'BORDER="1" COLOR="{GREY}"'
    return (
        f'<TD BGCOLOR="{bg}" {border} CELLPADDING="18">'
        f'<FONT COLOR="{DARK}" POINT-SIZE="15">{text}</FONT>'
        f'</TD>'
    )


def header(text):
    return (f'<TD BORDER="0"><FONT COLOR="{DARK}" POINT-SIZE="17">'
            f'<B>{text}</B></FONT></TD>')


table = f"""<
<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="10">
<TR>
  {header("Computação Móvel")}
  {header("Computação Ubíqua")}
</TR>
<TR>
  {cell("Foco na mobilidade<BR/>do equipamento", hi=True)}
  {cell("Foco na disponibilização<BR/>contínua de serviços")}
</TR>
<TR>
  {cell("Um utilizador transporta<BR/>um ou poucos dispositivos", hi=True)}
  {cell("Inúmeros objetos do<BR/>quotidiano, com pouca<BR/>perceção do utilizador")}
</TR>
<TR>
  {cell("Exemplo: telemóvel,<BR/>tablet, portátil", hi=True)}
  {cell("Exemplo: casa inteligente,<BR/>sensores embutidos")}
</TR>
</TABLE>>"""

dot_src = f"""digraph G {{
  labelloc="t"; fontsize=26; fontname="Helvetica-Bold"; fontcolor="{DARK}";
  label="Computação Móvel vs. Computação Ubíqua";
  graph [margin=0.3];
  node [shape=plaintext, fontname="Helvetica"];
  tabela [label={table}];
}}"""

render(dot_src, "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap11/movel-vs-ubiqua.png",
       dpi=200, target_width_px=2200, engine="dot")
print("done")
