# Documento com a Lista de User Stories.

Este documento descreve os User Stories criados a partir da Lista de Requisitos no [Documento de Visão](docs/doc-visao.md). Modelo de documento baseado nas características do processo easYProcess (YP).  

## Introdução

O presente documento tem como finalidade descrever como serão as interações de usuários com sistema GamingTrack, listando uma sequência lógica de passos afim de mostrar como os requisitos funcionais estão interagindo e gerando aglomerados maiores e que servirão como base para as entidades existente.  

## Lista de User Stories

### User Story US00 - Manter Usuário

|                    |      |
| ------------------ | ---- |
|**Descrição**| O sistema deve manter um cadastro de usuário que tem acesso ao via login e senha. <p> Um usuário tem os atributos name, id, email, username, password. O email será o login e ele pode registrar-se diretamente no sistema. Além disso o usuário poderá alterar alguns dados, como o e-mail ou a senha. |
|**Requisitos envolvidos**| RF001, RF002, RF003, RF004 |
|**Prioridade**| Essencial |
|**Estimativa**| -- |
|**Tempo Gasto (real):**| 10h |
|**Tamanho Funcional**| -- |

#### **Testes de Aceitação (TA00)**

| Código | Descrição |
| ------ | --------- |
|**TA00.01**| |
|**TA00.02**| |
|**TA00.03**| |
|**TA00.04**| |

### User Story US01 - Atribuir Permissão de Usuário

|                    |      |
| ------------------ | ---- |
|**Descrição**| O sistema deve permitir que usuários comuns virem usuários moderadores mediante promoção por um administrador, também será possível remover a permissão de moderador.<p> Para isso, algum adminitrador deve ser criado no banco de dados e este dará as primeiras permissões |
|**Requisitos envolvidos**| RF005, RF006 |
|**Prioridade**| Importante |
|**Estimativa**| -- |
|**Tempo Gasto (real):**| -- |
|**Tamanho Funcional**| -- |

### **Testes de Aceitação (TA01)**

| Código | Descrição |
| ------ | --------- |
|**TA01.01**| |
|**TA01.02**| |
|**TA01.03**| |
|**TA01.04**| |

### User Story US03 - Permitir a Publicação de Postagens

|                    |      |
| ------------------ | ---- |
|**Descrição**| O sistema deve permitir que um usuário cadastrado possa fazer publicações de comentários escritos, fotos, vídeos uma mistura de quaisquer desses. |
|**Requisitos envolvidos**| RF009 |
|**Prioridade**| Essencial |
|**Estimativa**| -- |
|**Tempo Gasto (real):**| -- |
|**Tamanho Funcional**| -- |

### **Testes de Aceitação (TA03)**

| Código | Descrição |
| ------ | --------- |
|**TA03.01**| |
|**TA03.02**| |
|**TA03.03**| |
|**TA03.04**| |

### Histórico de Revisões do Modelo

| Data | Versão | Descrição | Autor |
| :--: | :----: | --------- | ----- |
| 10/10/2020 | 1.0 | Documento inicial. | José Geraldo de Medeiros Júnior |  
| 14/10/2020 | 1.1 | Detalhamento do US00 - Manter Usuário e US01 - Atribuir Permissão de Usuário | José Geraldo de Medeiros Júnior |  

## Prioridade do User Story

Prioridade do User Story ou dos Requisitos: A prioridade dos requisitos é utilizada no gerenciamento do escopo das etapas do projeto e na definição das prioridades durante o desenvolvimento do sistema.  
**Essencial**: requisito sem o qual o sistema não entra em funcionamento. Requisitos essenciais são requisitos imprescindíveis para o funcionamento do sistema.  
**Importante**: requisito sem o qual o sistema entra em funcionamento, mas de forma não satisfatória. Requisitos importantes devem ser implantados o mais rápido possível, mas, se não forem, parte do sistema poderá ser implantada mesmo assim.  
**Desejável**: requisito que não compromete as funcionalidades básicas do sistema, isto é, o sistema pode funcionar de forma satisfatória sem ele. Requisitos desejáveis são requisitos que podem ser implantados por último, sem comprometer o funcionamento do sistema.  

## Estimativa do User Story

Há muitas formas de realizar uma estimativa de User Story, uma delas é usar o Story Point. Levison (2010) diz que existem várias interpretações para o que é um Story Point: "Story Points representam unidades de tempo obscuras." ou "Story Point é uma unidade relativa de medida usada por times Scrum. Isso é usado para mensurar a quantidade de esforço necessário para implementar uma história." ou "...um story point é uma junção da quantidade de esforço envolvido no desenvolvimento de uma feature, a complexidade desse desenvolvimento, o riso contido nele, e por aí vai." (Cohn, 2005).  

Uma boa estimativa considera dois pontos fundamentais: complexidade e esforço. De acordo com o dicionário:  

- Esforço é a intensificação das forças físicas, intelectuais ou morais para a realização de algum projeto ou tarefa.  
- Complexidade é a qualidade daquilo que possui múltiplos aspectos ou elementos cujas relações de interdependência são incompreensíveis.  

São definidos Níveis de 1 a 5 para o Esforço e Complexidade, determinando assim a dificuldade do User Story. Para saber mais leia o artigo de  (BARROS, 2018).  

## Tamanho Funcional
    
Análise de Ponto de Função é um método de medição do tamanho funcional de um software, com base em operações extraídas dos requisitos funcionais. A partir dessa medição inicial de tamanho, derivam-se outras medidas como, por exemplo, o tempo necessário para desenvolvimento, e uma estimativa inicial de custos. (<https://pt.wikipedia.org/wiki/M%C3%A9trica_de_software>)

## Referências

BARROS, Marcelo L. Esforço e Complexidade: quando tamanho realmente importa, Agile Momentum, 18/02/2018, Acessado em 22/02/2020. Link: <https://agilemomentum.wordpress.com/2018/02/18/esforco-e-complexidade-quando-tamanho-realmente-importa/>  
LEVISON, Mark. O que são os "Story Points"? Eles são necessários?. Traduzido por Felipe Torres, InfoQ, 2010. <https://www.infoq.com/br/news/2010/03/story-points/>  
COHN, Mike. Agile estimating and planning. Pearson Education, 2005.  
