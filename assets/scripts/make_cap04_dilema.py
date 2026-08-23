import sys
sys.path.insert(0, "/Users/jpavao/QProjects/Sebenta-PSC/assets/scripts")
from graphviz_utils import render
from sebenta_style import DARK, MAGENTA, GREY, NOTE_COLOR

FILL = "#f4f0f6"
HI_FILL = "#fbeaf7"


def cell(eu, cúmplice, hi=False):
    bg = HI_FILL if hi else FILL
    border = f'BORDER="3" COLOR="{MAGENTA}"' if hi else f'BORDER="1" COLOR="{GREY}"'
    return (
        f'<TD BGCOLOR="{bg}" {border} CELLPADDING="16">'
        f'<FONT COLOR="{DARK}" POINT-SIZE="18"><B>eu = {eu}</B></FONT><BR/><BR/>'
        f'<FONT COLOR="{NOTE_COLOR}" POINT-SIZE="14">cúmplice = {cúmplice}</FONT>'
        f'</TD>'
    )


def header(text):
    return (f'<TD BORDER="0"><FONT COLOR="{DARK}" POINT-SIZE="15">'
            f'<B>{text}</B></FONT></TD>')


table = f"""<
<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="10">
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
  labelloc="t"; fontsize=26; fontname="Helvetica-Bold"; fontcolor="{DARK}";
  label="O Dilema dos Prisioneiros";
  graph [margin=0.3];
  node [shape=plaintext, fontname="Helvetica"];
  tabela [label={table}];
}}"""

render(dot_src, "/Users/jpavao/QProjects/Sebenta-PSC/assets/images/cap04/dilema-prisioneiro.png",
       dpi=200, target_width_px=2200, engine="dot")
print("done")
