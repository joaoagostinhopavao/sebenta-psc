# Sebenta PSC — Plataformas Sociais e Cooperativas

Projecto Quarto para a sebenta da UC de Plataformas Sociais e Cooperativas,
Licenciatura em Comunicação e Multimédia, UTAD.

## Estrutura

```
Sebenta-PSC/
├── _quarto.yml          # Configuração do projecto (PT)
├── index.qmd            # Prefácio
├── capitulos/
│   ├── cap01.qmd        # Sociedade em Rede e Ciberespaço
│   ├── cap02.qmd        # Redes Sociais: Fundamentos e Dados Estatísticos
│   └── ...              # cap03.qmd … cap11.qmd
├── assets/
│   ├── css/custom.css   # Estilos personalizados
│   ├── images/          # Imagens e figuras (uma pasta por capítulo, heroes/, capa/)
│   └── cover.tex          # Capa PDF (imagem única já desenhada)
├── en/                    # Versão em inglês (projecto Quarto próprio, HTML + PDF)
│   ├── _quarto.yml
│   ├── index.qmd
│   ├── capitulos/         # cap01.qmd … cap11.qmd, em inglês (completo)
│   └── assets/             # Cópia própria de css/images/cover.tex (ver nota abaixo)
└── referencias.bib      # Bibliografia
```

## Renderização

```bash
# Versão portuguesa — livro completo (HTML + PDF)
quarto render

# Versão inglesa — HTML + PDF
quarto render en/

# Preview com hot reload (cada versão tem de ser aberta em separado)
quarto preview
quarto preview en/
```

A versão em inglês (`en/`) segue o mesmo padrão já usado nas outras
sebentas bilingues deste autor (ASW, IM, DAW1): projecto Quarto irmão, com
`output-dir: ../docs/en`. O botão de mudança de idioma fica na barra
lateral, ao lado do toggle claro/escuro (`book.sidebar.tools`), em ambas
as versões.

**Nota sobre o CSS e as imagens da versão inglesa:** os caminhos usados em
`en/` resolvem-se à raiz do *site* do próprio subprojecto (`docs/en/`), não
à pasta principal. Por isso existem cópias próprias em
`en/assets/css/custom.css` e `en/assets/images/` — sempre que o CSS
principal ou uma imagem forem alterados na pasta principal, replicar
também aqui.

**Nota sobre a capa da versão inglesa:** tal como na Sebenta-DAW1 (e ao
contrário da ASW/IM), a capa é uma imagem única já desenhada
(`assets/images/capa/*.jpg`), não gerada em TikZ. A versão inglesa
reutiliza a mesma imagem em português por agora — não existe fonte
editável para lhe mudar só o texto.

**Nota sobre os diagramas dos capítulos:** as ~34 figuras dos capítulos
(cap02-cap11) têm texto em português desenhado na própria imagem, e
mantêm-se em português também na versão inglesa por agora — só a prosa e
as legendas foram traduzidas. Se for necessário traduzi-las, seguir a
mesma técnica já usada na Sebenta-ASW (recriar cada diagrama com
`matplotlib`, mesma paleta, só o texto em inglês).

## Estado

Projecto criado em 2026-08-18. **Todos os 11 capítulos têm conteúdo real,
em português e em inglês.**

## Autores

João Pavão — UTAD, 2026 (componente teórica, autor dos capítulos)

Diana Carvalho — UTAD (componente prática)
