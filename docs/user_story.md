# Documento com a Lista de User Stories.

Este documento descreve os User Stories criados a partir da Lista de Requisitos no [Documento de Visão](docs/doc-visao.md). Modelo de documento baseado nas características do processo eas*YP*rocess (**YP**).  

## Introdução

O presente documento tem como finalidade descrever como serão as interações de usuários com sistema GamingTrack, listando uma sequência lógica de passos afim de mostrar como os requisitos funcionais estão interagindo e gerando aglomerados maiores e que servirão como base para as entidades existente.  

## Lista de User Stories

### User Story US00 - Manter Usuário

|                    |      |
| ------------------ | ---- |
|**Descrição**| O sistema deve manter um cadastro de usuário que tem acesso ao via login e senha. <p> Um usuário tem os atributos name, id, email, username, password. O email será o login e ele pode registrar-se diretamente no sistema. Além disso o usuário poderá alterar alguns dados, como o e-mail ou a senha. |
|**Requisitos envolvidos**| RF001, RF002, RF003, RF004 |
|**Prioridade**| Essencial |
|**Estimativa**| 6h |
|**Tempo Gasto (real):**| 4h |
|**Tamanho Funcional**| -- |

**********

### User Story US01 - Atribuir Permissão de Usuário

|                    |      |
| ------------------ | ---- |
|**Descrição**| O sistema deve permitir que usuários comuns virem usuários moderadores mediante promoção por um administrador, também será possível remover a permissão de moderador.<p> Para isso, algum adminitrador deve ser criado no banco de dados e este dará as primeiras permissões |
|**Requisitos envolvidos**| RF005, RF006 |
|**Prioridade**| Importante |
|**Estimativa**| 5h |
|**Tempo Gasto (real):**| 6h |
|**Tamanho Funcional**| -- |

**********

### User Story US02 - Conectar com APIs Externas

|                    |      |
| ------------------ | ---- |
|**Descrição**| O sistema deverrá se conectar a APIs externas com a finalidade de prover dados acerca de games diversos e, consequentemente, alimentar o banco de dados com informações relevantes sobre tais games. <p> Além disso, os usuários dependem dessa conexão para poderem fazer reviews dos seus games favoritos. |
|**Requisitos envolvidos**| RF022 |
|**Prioridade**| Importante |
|**Estimativa**| 3h |
|**Tempo Gasto (real):**| -- |
|**Tamanho Funcional**| -- |

**********

### User Story US03 - Manter Postagens

|                    |      |
| ------------------ | ---- |
|**Descrição**| O sistema deve permitir que um usuário cadastrado possa fazer publicações de comentários escritos, fotos, vídeos uma mistura de quaisquer desses. Além de apagá-los, editá-los e pesquisar por eles |
|**Requisitos envolvidos**| RF009, RF013, RF015, RF021, RF025 |
|**Prioridade**| Essencial |
|**Estimativa**| 3h |
|**Tempo Gasto (real):**| 2h |
|**Tamanho Funcional**| -- |

**********

### User Story US04 - Atribuir poderes

|                    |      |
| ------------------ | ---- |
|**Descrição**| O sistema deve permitir que um usuário com nível mínimo 3 possa deletar outro usuário, um post de outro usuário, etc. com um nível de poder menor que o seu. |
|**Requisitos envolvidos**| RF015, RF016 |
|**Prioridade**| Desejável |
|**Estimativa**| 5h |
|**Tempo Gasto (real):**| 4h |
|**Tamanho Funcional**| -- |

**********

### User Story US05 - Manter Resenhas

|                    |      |
| ------------------ | ---- |
|**Descrição**| O sistema deve permitir que um usuário cadastrado possa fazer publicações de resenhas escritos, fotos, vídeos ou uma mistura de quaisquer desses. |
|**Requisitos envolvidos**| RF007, RF011, RF015, RF026 |
|**Prioridade**| Essencial |
|**Estimativa**| 5h |
|**Tempo Gasto (real):**| -- |
|**Tamanho Funcional**| -- |

**********

### User Story US06 - Manter Comentários de Postagens

|                    |      |
| ------------------ | ---- |
|**Descrição**| O sistema devera permitir que o usuário faça comentários em Postagens |
|**Requisitos envolvidos**| RF008, RF010, RF012, RF014, RF015, RF027 |
|**Prioridade**| Importante |
|**Estimativa**| 5h |
|**Tempo Gasto (real):**| 4h |
|**Tamanho Funcional**| -- |

**********

### Histórico de Revisões do Modelo

| Data | Versão | Descrição | Autor |
| :--: | :----: | --------- | ----- |
| 10/10/2020 | 1.0 | Documento inicial. | José Geraldo de Medeiros Júnior |  
| 14/10/2020 | 1.1 | Detalhamento do US00 - Manter Usuário; US01 - Atribuir Permissão de Usuário; US03 - Fazer um post. | José Geraldo de Medeiros Júnior |  
| 22/10/2020 | 1.2 | Detalhamento da US02 - Conectar com APIs externas; US04 - Fazer uma review de um game. | José Geraldo de Medeiros Júnior |
| 24/10/2020 | 1.3 | Detalhamento da US04 - Permitir a Modificação de Postagens; US06 - Permitir a pesquisa; US07 - Atrubuir poderes.| Pedro Jonas da Silva Medeiros |
| 14/11/2020 | 1.4 | Detalhamento da US06 - Manter Comentários; US07 agora é US04; US04 e US06 deletados; modificação de nome dos US US03 e US05 para, respectivamente, Manter Postagens e Manter Resenhas; alterado detalhamento de US03 e US05. | Pedro Jonas da Silva Medeiros |


**********

## Prioridade do User Story

Prioridade do User Story ou dos Requisitos: A prioridade dos requisitos é utilizada no gerenciamento do escopo das etapas do projeto e na definição das prioridades durante o desenvolvimento do sistema.  
**Essencial**: requisito sem o qual o sistema não entra em funcionamento. Requisitos essenciais são requisitos imprescindíveis para o funcionamento do sistema.  
**Importante**: requisito sem o qual o sistema entra em funcionamento, mas de forma não satisfatória. Requisitos importantes devem ser implantados o mais rápido possível, mas, se não forem, parte do sistema poderá ser implantada mesmo assim.  
**Desejável**: requisito que não compromete as funcionalidades básicas do sistema, isto é, o sistema pode funcionar de forma satisfatória sem ele. Requisitos desejáveis são requisitos que podem ser implantados por último, sem comprometer o funcionamento do sistema.  

**********

## Estimativa do User Story

Há muitas formas de realizar uma estimativa de User Story, uma delas é usar o Story Point. Levison (2010) diz que existem várias interpretações para o que é um Story Point: "Story Points representam unidades de tempo obscuras." ou "Story Point é uma unidade relativa de medida usada por times Scrum. Isso é usado para mensurar a quantidade de esforço necessário para implementar uma história." ou "...um story point é uma junção da quantidade de esforço envolvido no desenvolvimento de uma feature, a complexidade desse desenvolvimento, o riso contido nele, e por aí vai." (Cohn, 2005).  

Uma boa estimativa considera dois pontos fundamentais: complexidade e esforço. De acordo com o dicionário:  

- Esforço é a intensificação das forças físicas, intelectuais ou morais para a realização de algum projeto ou tarefa.  
- Complexidade é a qualidade daquilo que possui múltiplos aspectos ou elementos cujas relações de interdependência são incompreensíveis.  

São definidos Níveis de 1 a 5 para o Esforço e Complexidade, determinando assim a dificuldade do User Story. Para saber mais leia o artigo de  (BARROS, 2018).  

**********

## Tamanho Funcional
  
Análise de Ponto de Função é um método de medição do tamanho funcional de um software, com base em operações extraídas dos requisitos funcionais. A partir dessa medição inicial de tamanho, derivam-se outras medidas como, por exemplo, o tempo necessário para desenvolvimento, e uma estimativa inicial de custos. (<https://pt.wikipedia.org/wiki/M%C3%A9trica_de_software>)

**********

## Referências

BARROS, Marcelo L. Esforço e Complexidade: quando tamanho realmente importa, Agile Momentum, 18/02/2018, Acessado em 22/02/2020. Link: <https://agilemomentum.wordpress.com/2018/02/18/esforco-e-complexidade-quando-tamanho-realmente-importa/>  
LEVISON, Mark. O que são os "Story Points"? Eles são necessários?. Traduzido por Felipe Torres, InfoQ, 2010. <https://www.infoq.com/br/news/2010/03/story-points/>  
COHN, Mike. Agile estimating and planning. Pearson Education, 2005.  
