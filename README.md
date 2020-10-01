# Projeto GamingTrack

O projeto **GamingTrack** será um web site desenvolvido na disciplina de *Engenharia de Software 2* com o objetivo de construir, nos alunos envolvidos no projeto, o aprendizado de algumas técnicas da engenharia de software.  
Neste site teremos uma espécie de rede social dedicada aos jogadores games eletrônicos que será dinâmica e de fácil integração com a API de alguns dos gerenciadores de games disponíveis no mercado.  
Nesse sentido, os jogadores terão acesso ao tempo de jogo e conquistas conseguidas em seus games favoritos reunidos em um só ambiente, facilitando, assim, o compartilhamento dessas conquistas com os amigos.  
Além disso, os jogadores poderão fazer resenha de jogos dando sua opinião, fazendo críticas ou elogios.
Os usuários poderão ver e comentar as resenhas dos outros jogadores.

## Tecnologias utilizadas no projeto

### Back-end

O back-end do projeto será desenvolvido na linguagem de programação [Python](www.python.org/) e utilizando o [Framework Django REST](www.django-rest-framework.org/) que é uma variação do [Framework Django](www.djangoproject.com/).  

![Arquitetura de funcionamento do Framework Django REST](docs/img/Django_REST.png)

* **Model**

A model é a representação dos objetos, permitindo obter informações do banco de dados sem conhecer a complexidade de tal. Essa camada contém tudo sobre os dados: como acessar, validar, comportamentos e relações entre dados.

* **View**

A view controla o fluxo de informações entre a model e o template. Essa camada utiliza lógica programada para decidir quais informações serão extraídas do banco de dados e quais serão transmitidas para exibição.

* **Serializer**

Os serializers permitem que dados complexos sejam convertidos em tipos de dados nativos do python, que podem ser renderizados facilmente em JSON, XML e outros tipos de conteúdo. No Django Rest, os serializers funcionam de forma semelhante às classes Form e ModelForm do Django.

* **URL**

O framework REST tem suporte para o roteamento automático de URL para o Django, e fornece uma forma simples, rápida e consistente de conectar sua lógica de visualização a um conjunto de URLs.

### Front-end

O front-end será desenvolvido utilizando a linguagem JavaScript com React consumindo a API criada.
Espera-se que tenhamos uma a página web bem organizada e compatível com os diversos navegadores que tenham suporte ao JavaScript.

### Banco de Dados

Este projeto usará o banco de dados relacional - SQL. Com isso esperamos dados fortemente íntegros.  
Com essa finalidade, será usado o SGBD PostgreSQL, um poderoso gerenciador de banco de dados relacional que tem ampla credibilidade no mercado. Ele é portável em alguns sistemas operacionais como Windows, MacOS e diversas distribuições Linux, além disso, dá suporte ao mapeamento objeto-relacional - ORM (sigla em inglês), podendo ser usado para trabalhar com linguagens orientadas a objetos sem problemas.

## Informações

* Descrição das Tarefas - [Plano de Iteração e Release](docs/release.md)
* Perspectivas do projeto - [Documento de Visão](docs/doc-visao.md)
* Descrição do [Modelo de Dados](docs/modelo_dados.md)

## Links Úteis

Principal tutorial utilizado <www.youtube.com/watch?v=f1R_bykXHGE>  
Tutorial do framework Django Rest <www.django-rest-framework.org/tutorial/quickstart>  
Página sobre Django <https://tutorial.djangogirls.org/pt>  
