# Análise de emissões brasileiras

Projeto de análise exploratória de emissões de gases do efeito estufa no Brasil, organizado para produzir uma visão técnica e um relatório executivo.

## Tecnologias

Python, pandas, Matplotlib, Jupyter e openpyxl.

## Problema abordado

Transformar dados de emissões em análises por período, gás e setor, com visualizações que apoiem uma leitura técnica e executiva.

## Como executar

1. Crie e ative um ambiente virtual.
2. Instale `pandas`, `matplotlib`, `openpyxl`, `nbformat` e `nbconvert`.
3. Obtenha o dataset na fonte oficial do SEEG e salve-o como `br_seeg_emissoes_brasil.xlsx` neste diretório.
4. Abra e execute `analisebase.ipynb` em ordem.

Os relatórios HTML versionados permitem consultar o resultado sem executar o notebook:

- [Relatório executivo](Relatorio_Executivo_Emissoes.html)
- [Relatório técnico](Relatorio_Analise_Emissoes.html)

## Resultado e aprendizados

O notebook gera visualizações comparativas e um relatório executivo exportável. O foco foi combinar limpeza de dados, análise estatística e comunicação de resultados.

## Dados

Os dados são grandes e não devem ser adicionados em novas versões do repositório. Registre sempre a fonte, a data de obtenção e a licença do dataset usado.
