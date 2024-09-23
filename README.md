  
  

<a  name="readme-top"></a>

  

  

# REST API CENTRO ESPORTIVO

  

  

<p  align="center">

  

<img  src="http://img.shields.io/static/v1?label=Python&message=3.12&color=red&style=for-the-badge&logo=Python"/>

  

<img  src="https://img.shields.io/static/v1?label=Django&message=framework&color=blue&style=for-the-badge&logo=Django"/>

  

<img  src="https://img.shields.io/static/v1?label=SQLite&message=database&color=blue&style=for-the-badge&logo=SQLite"/>

  

<img  src="http://img.shields.io/static/v1?label=STATUS&message=CONCLUIDO&color=GREEN&style=for-the-badge"/>

  

<img  src="http://img.shields.io/static/v1?label=TESTES&message=100%&color=GREEN&style=for-the-badge"/>

  

<img  src="http://img.shields.io/static/v1?label=License&message=EULA&color=green&style=for-the-badge"/>

  

  
  
  
  
  

| :sparkles: Nome | **REST-API CENTRO ESPORTIVO**

  

| :label: Tecnologias | Django, SQLite, JWT

  


  
  
  

  

![rest-api-imagem](https://github.com/thomazcm/rest-api-financeira/blob/master/github/rest-api.png#vitrinedev)

  

  

### Tópicos

  

  

:small_blue_diamond: [Descrição do projeto](#descrição-do-projeto)

  

  

:small_blue_diamond: [Acesso](#acesso)

  

  

:small_blue_diamond: [Funcionalidades](#funcionalidades)

  

  

:small_blue_diamond: [Pré-Requisitos e como Rodar o Servidor](#pré-requisitos)

  

  

:small_blue_diamond: [Tecnologias](#tecnologias)

  

  

:small_blue_diamond: [Autor](#autor)

  

  

## Descrição do projeto

  

  

<p  align="justify">

  

API RESTful desenvolvida para servir como camada de back-end de sistema de gerenciamento de dados para instituções esportivas.<br/>

  

API de demonstração desenvolvida em Python com o framework Django, utiliza um sistema de autenticação stateless e banco de dados SQLite.

  

</p>

  

  

## Acesso

  

A demonstração das funcionalidades da API podem ser acessadas [através do aplicativo web]() que utiliza os endpoints para seu funcionamento.

  

Caso queira rodar o servidor localmente [siga os passos listados aqui](#pré-requisitos).

  

## Funcionalidades

  

:heavy_check_mark: Cadastro de novos alunos.

  

  

:heavy_check_mark: Consulta, edição e exclusão de alunos já cadastrados

  

  

:heavy_check_mark: Cadastro de novas turmas

  

  

:heavy_check_mark: Consulta, edição e exclusão de turmas já cadastradas

  

  

:heavy_check_mark: Cadastro de novos atestados em nome de um aluno

  
  
  

:heavy_check_mark: Consulta, edição e exclusão de atestados já cadastrados

  
  
  

:heavy_check_mark: Cadastro de novas matrículas, relacionando um aluno a uma turma

  
  
  

:heavy_check_mark: Consulta, edição e exclusão de matrículas já cadastrados

:heavy_check_mark: Listar todas matrículas de uma turma

:heavy_check_mark: Listar todas matrículas de um aluno

  

### API REST

  

Os endpoints da API REST estão descritos abaixo.

  

#### Alunos

  

&nbsp;&nbsp;&nbsp;&nbsp;`GET` /alunos &nbsp;&nbsp;→&nbsp;&nbsp; Listar alunos<br/>

&nbsp;&nbsp;&nbsp;&nbsp;`POST` /alunos &nbsp;&nbsp;→ &nbsp;&nbsp;Criar aluno<br/>

&nbsp;&nbsp;&nbsp;&nbsp;`GET` /alunos/id &nbsp;&nbsp;→ &nbsp;&nbsp;Consultar um aluno<br/>

&nbsp;&nbsp;&nbsp;&nbsp;`PATCH` /alunos/id &nbsp;&nbsp;→ &nbsp;&nbsp;Editar um aluno<br/>

&nbsp;&nbsp;&nbsp;&nbsp;`DELETE` /alunos/id &nbsp;&nbsp;→ &nbsp;&nbsp;Apagar um aluno<br/>

  
  

#### Turmas

  

&nbsp;&nbsp;&nbsp;&nbsp;`GET` /turmas &nbsp;&nbsp;→ &nbsp;&nbsp;Listar turmas<br/>

&nbsp;&nbsp;&nbsp;&nbsp;`POST` /turmas &nbsp;&nbsp;→ &nbsp;&nbsp;Criar turma<br/>

&nbsp;&nbsp;&nbsp;&nbsp;`GET` /turmas/id &nbsp;&nbsp;→ &nbsp;&nbsp;Consultar uma turma<br/>

&nbsp;&nbsp;&nbsp;&nbsp;`PATCH` /turmas/id &nbsp;&nbsp;→ &nbsp;&nbsp;Editar uma turma<br/>

&nbsp;&nbsp;&nbsp;&nbsp;`DELETE` /turmas/id &nbsp;&nbsp;→ &nbsp;&nbsp;Apagar uma turma<br/>
  

#### Matrículas

  

&nbsp;&nbsp;&nbsp;&nbsp;`GET` /matriculas &nbsp;&nbsp;→ &nbsp;&nbsp;Listar matrículas<br/>

&nbsp;&nbsp;&nbsp;&nbsp;`POST` /matriculas &nbsp;&nbsp;→ &nbsp;&nbsp;Criar matrícula<br/>

&nbsp;&nbsp;&nbsp;&nbsp;`GET` /matriculas/id &nbsp;&nbsp;→ &nbsp;&nbsp;Consultar uma matrícula<br/>

&nbsp;&nbsp;&nbsp;&nbsp;`PATCH` /matriculas/id &nbsp;&nbsp;→ &nbsp;&nbsp;Editar um matrícula<br/>

&nbsp;&nbsp;&nbsp;&nbsp;`DELETE` /matriculas/id &nbsp;&nbsp;→ &nbsp;&nbsp;Apagar um matrícula<br/>

&nbsp;&nbsp;&nbsp;&nbsp;`GET` /turmas/id/matriculas &nbsp;&nbsp;→ &nbsp;&nbsp;Listar todas matrículas em uma turma<br/>

&nbsp;&nbsp;&nbsp;&nbsp;`GET` /alunos/id/matriculas &nbsp;&nbsp;→ &nbsp;&nbsp;Listar todas matrículas de um aluno<br/>
  

#### Atestado

  

&nbsp;&nbsp;&nbsp;&nbsp;`GET` /atestados &nbsp;&nbsp;→ &nbsp;&nbsp;Listar atestados<br/>

&nbsp;&nbsp;&nbsp;&nbsp;`POST` /atestados &nbsp;&nbsp;→ &nbsp;&nbsp;Criar atestado<br/>

&nbsp;&nbsp;&nbsp;&nbsp;`GET` /atestados/id &nbsp;&nbsp;→ &nbsp;&nbsp;Consultar um atestado<br/>

&nbsp;&nbsp;&nbsp;&nbsp;`PATCH` /atestados/id &nbsp;&nbsp;→ &nbsp;&nbsp;Editar um atestado<br/>

&nbsp;&nbsp;&nbsp;&nbsp;`DELETE` /atestados/id &nbsp;&nbsp;→ &nbsp;&nbsp;Apagar um atestados<br/>

  

<p  align="right">(<a  href="#readme-top">voltar para o início</a>)</p>

  

## Pré-Requisitos

  

Para rodar o servidor localmente você precisa ter instalado as seguintes ferramentas: [Python](https://www.python.org/downloads/) e [Git](https://git-scm.com/).

  

### Como rodar a aplicação

  

1. Clone este repositório:

  

```

git clone https://github.com/JulioCout/IAB-Backend-Demo

```

  

2. Crie um ambiente virtual:

  

```

python -m venv venv

```

  

3. Ative o ambiente virtual :

  

```

venv\Scripts\activate

```

  

4. Instale as dependências com o o ambiente virtual ativado:

  

```

pip install -r requirements.txt

```

  
  

6. Execute o comando:

  

```

python manage.py runserver

```

  

  

6. Por fim, o servidor inciará na porta:8000 - acesse as endpoints por :

  

```

http://127.0.0.1:8000

```

  

  

<p align="right">(<a href="#readme-top">voltar para o início</a>)</p>

  

  

## Tecnologias

  

As seguintes ferramentas foram usadas na construção do projeto:

  

  

#### Tecnologias

  

- [Python 3.12](https://www.python.org/) - Framework

  

- [Django 5.1](https://www.djangoproject.com/) - Framework

  

- [Django Rest Framework 3.15.2](https://www.django-rest-framework.org/) - Framework

  

  

  

#### Ferramentas

  

- [Postman](https://www.postman.com/) - Testes de API

  

- [VSCode](https://code.visualstudio.com/) - Editor de código

  

  

<p align="right">(<a href="#readme-top">voltar para o início</a>)</p>

  

  

## Licença

  

  

Este projeto esta sob a licença [MIT](./LICENSE). Consulte o arquivo LICENSE.md para mais informações.

  

  

<p align="right">(<a href="#readme-top">voltar para o início</a>)</p>

  

  

## Autor

  

<b>Julio Coutinho</b><br />

  

<img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/90656852?v=4" width="100px;" alt=""/><br />

  

Projeto desenvolvido por Julio Coutinho. Entre em contato!

  

  

[LinkedIn](https://www.linkedin.com/in/juliocscoutinho//)

  

[E-mail](mailto:contact@juliocoutinho.com)

  

<p align="right">(<a href="#readme-top">voltar para o início</a>)</p>
