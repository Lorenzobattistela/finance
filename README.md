# Finance 

## O que é o projeto?
Esse projeto foi criado com a intenção de facilitar a visualização das minhas finanças pessoais. 
Isso foi feito de maneira que é possível inserir, deletar e editar investimentos, e um relatório de todos os investimentos é mostrado no formato HTML.
O HTML é construído automaticamente e a página mostrada para o usuário.

## Stack do projeto
O projeto foi construído utilizando Python, que interage com a base de dados, constrói o HTML e insere os dados que pegou da base de dados.
A base de dados é feita utilizando Sqlite3, já que a complexidade de inserção de dados é baixa.
O front utiliza HTML + CSS (para mostrar o relatório).

## Estrutura
Os arquivos estão divididos em: `api.py`, que fornece as funções utilizadas para pegar o preço em tempo real de uma ação. `browser.py` 
que tem função de abrir o arquivo HTML quando a opção de abrir relatório é escolhida. `helpers.py` que contém as funções que ajudam a regra de negócio a acontecer, ou seja: queries de base de dados, inserção de colunas e linhas no HTML, pegar dados estáticos, etc. `report.py` contém as funções específicas de construção do relatório em html. O arquivo `app.py` utiliza todos os outros para integrar as funcionalidades, isolando a parte bruta do código da regra de negócio.


