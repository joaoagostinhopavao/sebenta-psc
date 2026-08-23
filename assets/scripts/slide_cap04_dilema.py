import sys
sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from graphviz_utils import render
from sebenta_style import DARK, MAGENTA, GREY, NOTE_COLOR

FILL = "#f4f0f6"
HI_FILL = "#fbeaf7"


def cell(eu, cúmplice, hi=False):
    bg = HI_FILL if hi else FILL
    border = f'BORDER="4" COLOR="{MAGENTA}"' if hi else f'BORDER="1" COLOR="{GREY}"'
    return (
        f'<TD BGCOLOR="{bg}" {border} CELLPADDING="20">'
        f'<FONT COLOR="{DARK}" POINT-SIZE="22"><B>eu = {eu}</B></FONT><BR/><BR/>'
        f'<FONT COLOR="{NOTE_COLOR}" POINT-SIZE="17">cúmplice = {cúmplice}</FONT>'
        f'</TD>'
    )


def header(text):
    return (f'<TD BORDER="0"><FONT COLOR="{DARK}" POINT-SIZE="18">'
            f'<B>{text}</B></FONT></TD>')


table = f"""<
<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="12">
<TR>
  <TD BORDER="0"></TD>
  {header("O cúmplice fica<BR/>em silêncio")}
  {header("O cúmplice<BR/>confessa")}
</TR>
<TR>
  {header("Eu fico<BR/>em silêncio")}
  {cell("6 meses", "6 meses", hi=True)}
  {cell("10 anos", "livre")}
</TR>
<TR>
  {header("Eu<BR/>confesso")}
  {cell("livre", "10 anos")}
  {cell("6 anos", "6 anos")}
</TR>
</TABLE>>"""

dot_src = f"""digraph G {{
  labelloc="t"; fontsize=32; fontname="Helvetica-Bold"; fontcolor="{DARK}";
  label="O Dilema dos Prisioneiros";
  graph [margin=0.35];
  node [shape=plaintext, fontname="Helvetica"];
  tabela [label={table}];
}}"""

render(dot_src, "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap04/slides/dilema-prisioneiro-slide.png",
       dpi=200, target_width_px=2666, engine="dot")
print("done")
