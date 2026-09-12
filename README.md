# Knowledge Repository — Computer Science & Data Analytics

Este repositório centraliza materiais, códigos, exercícios e projetos desenvolvidos ao longo da minha trajetória acadêmica e prática em **Ciência da Computação**, com foco complementar em **Data Analytics** e **Advisory/Consulting**.

O objetivo principal é servir como uma **base de conhecimento estruturada**, contendo conteúdos que são frequentemente revisitados para reforço conceitual, prática técnica e evolução contínua.

---

## Projetos em destaque

<p align="center">
  <img src="Bacharelado%20-%20Ci%C3%AAncia%20da%20Computa%C3%A7%C3%A3o%20IMPACTA/6%20Semestre/Computa%C3%A7%C3%A3o%20Gr%C3%A1fica%20e%20RA%20RV/Aula%207/mini-catalogo%203d.png" alt="Prévia de uma cena 3D desenvolvida no repositório" width="520">
</p>

| Projeto | Problema resolvido | Tecnologias | Como executar |
| --- | --- | --- | --- |
| [Análise de emissões brasileiras](<Bacharelado - Ciência da Computação IMPACTA/5 Semestre/Inteligência Computacional/projetofinal-testes/README.md>) | Explora emissões por período, gás e setor e transforma os dados em relatórios técnicos e executivos. | Python, pandas, Matplotlib, Jupyter | Consulte o [README do projeto](<Bacharelado - Ciência da Computação IMPACTA/5 Semestre/Inteligência Computacional/projetofinal-testes/README.md>) e execute `analisebase.ipynb`. |
| [Floyd-Warshall](<Bacharelado - Ciência da Computação IMPACTA/5 Semestre/Teoria dos Grafos/Algoritmo Floyd Warshall/README.md>) | Calcula caminhos mínimos entre todos os pares de vértices em grafos ponderados. | Python, NetworkX, Matplotlib | Instale `networkx` e `matplotlib`; abra `AtividadeAlgoritmoFloydWarshall.ipynb`. |
| [Galeria 3D](<Bacharelado - Ciência da Computação IMPACTA/6 Semestre/Computação Gráfica e RA RV/Aula 8/README.md>) | Demonstra instâncias de malha, transformações, câmera orbital e hierarquia pai-filho. | Python, Pygame | Instale `pygame` e execute `python aula8-galeria-3d.py`. |
| [Pipeline ETL](<Cursos Livres - Impacta/ETL na Prática - Como Trabalhar com Dados (online)/README.md>) | Exercita extração, transformação, carga e análise de dados em um pipeline completo. | Python, pandas, SQLite, Excel | Execute os notebooks na sequência `1. Extract` → `4. Projeto`. |

> Os projetos acima representam entregas que vale a pena explorar primeiro. Para o mapa completo do acervo, consulte o índice abaixo.

## Índice navegável

| Tema | Tecnologias | Conteúdo | Link |
| --- | --- | --- | --- |
| Fundamentos de programação | Python, C | Lógica, estruturas de dados, recursividade, TDD e análise de algoritmos | [1º e 2º semestres](<Bacharelado - Ciência da Computação IMPACTA/2 Semestre/README.md>) |
| Algoritmos e estruturas de dados | Java, Python | Estruturas lineares, exercícios e análise/projeto de algoritmos | [3º semestre](<Bacharelado - Ciência da Computação IMPACTA/3 Semestre/README.md>) |
| Orientação a objetos | Python, Java | Classes, objetos, coleções e exercícios práticos | [4º semestre](<Bacharelado - Ciência da Computação IMPACTA/4 Semestre/README.md>) |
| Dados e IA | Python, Jupyter, pandas | Análise exploratória, inteligência computacional e inferência estatística | [5º semestre](<Bacharelado - Ciência da Computação IMPACTA/5 Semestre/README.md>) · [6º semestre](<Bacharelado - Ciência da Computação IMPACTA/6 Semestre/README.md>) |
| Teoria dos grafos | Python, NetworkX | Floyd-Warshall, Edmonds-Karp e anotações de grafos | [Teoria dos Grafos](<Bacharelado - Ciência da Computação IMPACTA/5 Semestre/Teoria dos Grafos/README.md>) |
| Computação gráfica | Python, Pygame | Modelagem, transformações, câmeras e cenas 3D | [Computação Gráfica](<Bacharelado - Ciência da Computação IMPACTA/6 Semestre/Computação Gráfica e RA RV/README.md>) |
| Web | HTML, CSS, JavaScript | Interfaces, páginas institucionais e portfólios | [ETEC](<ETEC Informática para Internet ABH/README.md>) · [Projetos HTML/CSS](<Projetos HTML e CSS/README.md>) |
| ETL | Python, pandas, SQLite | Extração, transformação, carga e projeto de dados | [Curso ETL](<Cursos Livres - Impacta/ETL na Prática - Como Trabalhar com Dados (online)/README.md>) |
| Fundamentos em C | C | Exercícios desenvolvidos durante o CS50 | [CC50](CC50/README.md) |

## Manutenção do acervo

- Novos conteúdos seguem as [convenções de nomenclatura e de dados](docs/CONVENCOES.md).
- Datasets grandes, vídeos, instaladores e resultados gerados não devem entrar no Git; use a fonte de obtenção ou Git LFS quando o arquivo for indispensável.
- Os projetos em destaque documentam objetivo, dependências, execução e resultado.

### Clone no Windows

O acervo histórico contém alguns caminhos longos. Em Windows, faça o clone com suporte a caminhos longos habilitado:

```bash
git clone -c core.longpaths=true https://github.com/gblsun/knowledge-repo.git
```

## Objetivo

- Consolidar aprendizados acadêmicos e práticos
- Manter um histórico organizado da evolução técnica
- Servir como material de revisão rápida e confiável
- Apoiar desenvolvimento em:
  - Engenharia de Software
  - Data Analytics
  - Resolução de problemas (problem solving)
  - Lógica e algoritmos

---

## Estrutura do Repositório

O repositório está organizado em múltiplas pastas, cada uma representando diferentes contextos de aprendizado. Cada semestre e cada disciplina/curso possui um `README.md` próprio com um resumo do conteúdo abordado, e um `.gitignore` na raiz mantém o repositório livre de artefatos de build, cache e arquivos de IDE.

### Bacharelado - Ciência da Computação (IMPACTA)

Conteúdos organizados por semestre, refletindo a progressão acadêmica. Cada semestre e cada disciplina possui seu próprio `README.md` com um resumo do conteúdo abordado:
```
/Bacharelado - Ciência da Computação IMPACTA/
│
├── 1 Semestre/
│   └── Linguagem de Programação
├── 2 Semestre/
│   ├── Matemática para Computação
│   └── Técnicas de Programação
├── 3 Semestre/
│   ├── Algoritmos e Estrutura de Dados
│   └── Análise e Projeto de Algoritmos
├── 4 Semestre/
│   └── Linguagem Orientada a Objeto
├── 5 Semestre/
│   ├── Análise Exploratória de Dados
│   ├── Inteligência Computacional
│   ├── Paradigmas da Computação
│   └── Teoria dos Grafos
└── 6 Semestre/
    ├── Compiladores
    ├── Computação Gráfica e RA RV
    └── Inferência Estatística
```

Inclui:

- **1º-2º semestre:** lógica de programação, matemática para computação e técnicas de programação em Python (estruturas de dados sequenciais, conjuntos, dicionários, recursividade e memoização, tratamento de exceções, TDD, análise de eficiência de algoritmos, algoritmos de ordenação — bubble, selection, insertion, heap, merge, quick sort — e busca — linear, binária, quickselect)
- **3º semestre:** algoritmos e estruturas de dados em Java (com apoio de bibliografia de referência) e análise e projeto de algoritmos
- **4º semestre:** programação orientada a objetos em Java (classes, objetos, exercícios práticos)
- **5º semestre:** análise exploratória de dados (datasets Iris e Penguins, boxplots), inteligência computacional (projeto final), paradigmas da computação (paradigma imperativo em C e paradigma funcional em Elixir) e teoria dos grafos (algoritmos de Edmonds-Karp e Floyd-Warshall)
- **6º semestre:** compiladores, computação gráfica / realidade aumentada e virtual e inferência estatística (revisão de estatística univariada e bivariada)

---

### CC50 (Harvard CS50)

Exercícios e fundamentos da linguagem C desenvolvidos a partir do curso CS50, reforçando:

- Sintaxe e estrutura básica de programas em C
- Fundamentos de programação de baixo nível

---

### ETEC — Informática para Internet

Materiais do curso técnico, com foco em desenvolvimento web e fundamentos de TI. Cada disciplina/projeto possui seu próprio `README.md`:
```
/ETEC Informática para Internet ABH/
├── Programação e algoritmos
├── Gestão e conteúdo Web
├── Interfaces Web
├── Projetos com DreamWeaver
├── Projeto Menu
├── Projeto Cripto
├── Projeto Prático
└── site ti é aqui
```

Inclui:

- Programação e algoritmos em C (calculadoras, tabuada, IMC)
- HTML, CSS e fundamentos de front-end
- Estruturação de projetos web (portfólio de estilos artísticos, site institucional, projetos com Adobe DreamWeaver)
- Conceitos iniciais de sistemas e gestão de conteúdo web

---

### ☁️ Cursos Livres & Especializações

Conteúdos complementares voltados para mercado e prática:

#### ETL / Data

- Pipeline completo de Extração, Transformação e Carga de dados em Python (pandas, SQLite, Excel/HTML)
- Notebooks organizados por etapa: `1. Extract`, `2. Transform`, `3. Load` e `4. Projeto de Análise de Dados`
- Material de apoio com exercícios adicionais de extração, transformação e carregamento

#### Java Programmer (IMPACTA - My Way)

- Fundamentos da linguagem Java
- Tipos de dados, valores literais e variáveis
- Introdução à orientação a objetos

---

### Projetos HTML e CSS

Projetos iniciais de front-end, incluindo:

- Estruturação de páginas
- Estilização com CSS
- Projeto de portfólio pessoal
- Site institucional simples (Fundação Bradesco)

---

## Tecnologias e Ferramentas

- **Linguagens:** Python, Java, C, Elixir, HTML, CSS
- **Conceitos:** Algoritmos, Estruturas de Dados, OOP, Paradigmas de Programação, Teoria dos Grafos, Compiladores
- **Data:** ETL, análise exploratória de dados, SQLite, pandas, organização e persistência de dados
- **Ferramentas:** Git, Jupyter Notebook, ambientes acadêmicos

---

## Abordagem

Este repositório não é apenas um conjunto de códigos, mas sim um reflexo de:

- Aprendizado contínuo
- Iteração e melhoria constante
- Reforço de fundamentos
- Construção de base sólida para atuação em tecnologia e dados

---

## Autor

Gabriel Muchon Pavanelli
Estudante de Ciência da Computação
Interesses em **Tecnologia, Data Analytics e Advisory Consulting**

---

## Observação

Este repositório contém materiais acadêmicos e de estudo, podendo incluir códigos experimentais, versões intermediárias e exercícios em diferentes níveis de maturidade.
