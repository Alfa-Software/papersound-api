# Papersound-api

Api desenvolvida em Python para a rede social Papersound.

## Instruções Básicas

  O projeto da API, seguirá o modelo MVC(MODEL VIEW CONTROLLER), o qual dividiremos nosso posjeto entre camadas de conexão e modelagem de dados,
camadas de validação e autenticação de  dados, e camada de visualização de dados, aqui uma imagem ordinária de como é a estrutura total da API:



<img src="https://raw.githubusercontent.com/diegoeis/tableless-static-images/master/2015/02/laravel-introducao.jpg">

Os controllers atuarão difinindo as rotas e quais dados devem estar vísiveis nessa rota quando o usuário  solicitar um GET,POST,PATCH ou DELETE,
ele que ficará responsavel de fazer o transporte de dados  da Base de dados para a camada de Visualização.

As models, será onde definiremos os tipos de dados  que irão estar presentes na nossa base de dados.

A view será a camada de renderização que ficará disponível ao usuário.

Tendo entendido  esses conceitos ,vamos  as instruções.

Para instalar o Django digite ```pip install Django==3.0.5``` para instalar a versão mais recente dele,pós ter instalado,crie uma pasta para seu projeto
e digite ```django-admin.py startproject<NomeDProjeto>```, isso fará com que o Django crie, o esqueleto da Api.

Tendo esta parte já feita, sugiro revisitar nossa wiki para aprender sobre o comportamento do Django.

Importante que  já tenha  noções de como se configura um projeto MVC e como funciona os padrões de requesição REST e também como funciona o protocolo HTTP

## Como está organizado o Projeto

> Ainda em Construção

## Comandos importantes:

```Manage.py makemigrations``` ===> Gera um arquivo migration a partir do arquivo Models.py<br/>
```Manage.py migrate``` ===> cria um banco de dados e insere os dados modelados dentro da migration no banco de dados via sql query<br/>
```Manage.py runserver```===> Inicia o servidor local da api
