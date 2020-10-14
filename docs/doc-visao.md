# Documento de Visão

Documento de Visão do projeto GamingTrack, construído a partir do **Modelo BSI - Doc 001 - Documento de Visão** que pode ser encontrado no link:   
<https://docs.google.com/document/d/1DPBcyGHgflmz5RDsZQ2X8KVBPoEF5PdAz9BBNFyLa6A/edit?usp=sharing>

## Equipe e Definição de Papéis

Membro     |     Papel   |   E-mail   |
---------  | ----------- | ---------- |
Geraldo    | Analista, Desenvolvedor | geraldo_sjs@hotmail.com
Paulo      | Gerente, Analista, Desenvolvedor | paulovmedeiros@outlook.com
Pedro      | Analista, Desenvolvedor | pedrojonassm@gmail.com

&nbsp;

### Matriz de Competências

Membro     |     Competências   |
---------  | ----------- |
Geraldo    | Desenvolvedor Java Script, VueJS, Python, Python-Django, C, C#, Java, Eclipse, Matemática, Latex. |
Paulo      | Front-end (HTML, CSS, JS), UI, UX, Design Gráfico, etc. |
Pedro      | Desenvolvedor Java, Python, C, Eclipse, Visual Studio, Matemática, etc. |

&nbsp;

## Perfis dos Usuários

O sistema será utilizado por diversos perfis de usuário, sendo eles:

Perfil        | Descrição   |
---------     | ----------- |
Administrador | Usuário que possui todas as permissões de acesso. Pode realizar os cadastros base, utilizar todas as funções de CRUD e moderação no sistema.
Moderador     | Usuário que possui acesso às permissões de acesso para moderar as postagens e conteúdo no sistema, além das funções acessíveis a usuários.
Usuário       | Usuário comum que possui acesso ao cadastro no site e possui permissão para publicar e interagir com outros usuários no site.  

&nbsp;

## Lista de Requisitos Funcionais

| Requisito | Descrição   | Ator |
| --------- | ----------- | :--: |
| RF001 - Realizar o autocadastro para utilizar o sistema. | O usuário poderá se autocadastrar para utilizar o sistema. | Usuário |
| RF002 - Fazeer auto-atualização de seus dados | O usuário poderá atualizar seus prórpios dados| Usuário |
| RF003 - Auto-apagar conta | O usuário poderá se apagar do sistema | Usuário |
| RF004 - Visualizar seus dados | O usuário poderá visualizar seus dados retidos pelo sistema, incluindo dados do último acessos | Usuário |
| RF005 - Atribuir permissão de *moderador*| O usuário poderá ser promovido a *moderador* | Administrador - Moderado |
| RF006 - Remover permissão de *moderador* | O usuário poderá ser despromovido de *moderador* para usuário | Administrador - Moderado - Usuário |
| RF007 - Permitir a criação de resenhas sobre jogos | O usuário poderá publicar conteúdo sobre jogos específicos como avaliações escritas, vídeos e imagens | Usuário |
| RF008 - Permitir a criação de comentários em resenhas sobre jogos | O usuário poderá fazer comentários nas resenhas de outros usuários | Usuário |
| RF009 - Permitir a criação de postagens | O usuário poderá publicar conteúdo diversos sobre jogos ou afins, incluindo ou não fotos e vídeos | Usuário |
| RF010 - Permitir a criação de comentários em postagens | O usuário poderá fazer comentários nas postagens de outros usuários | Usuário |
| RF011 - Permitir a remoção de resenhas sobre jogos | O usuário poderá remover seus conteúdos publicados sobre jogos específicos. Caso haja algum comentário na resenha, esta regra será ignorada | Usuário |
| RF012 - Permitir a excluão de comentários em resenhas sobre jogos | O usuário poderá remover seus comentários feitos em resenhas de outros usuários | Usuário |
| RF013 - Permitir a exclusão de postagens | O usuário poderá excluir suas publicações de conteúdo diversos sobre jogos ou afins. Caso haja algum comentário na postagem, esta regra será ignorada | Usuário |
| RF014 - Permitir a excluão de comentários em postagens | O usuário poderá remover seus comentários feitos em postagens| Usuário |
| RF015 - Moderação de conteúdo publicado. | Os moderadores do sistema devem ter acesso às postagem dos usuários e ter a opção de moderar o conteúdo, advertindo usuários que façam publicações ofensivas | Moderador |
| RF016 - Permitir a exclusão publicações de usuários | O moderador poderá excluir qualquer publicação de usuário que seja ilegal/ofensiva ou infrija as regras do site | Administrador |
| RF017 - Conectar usuários através de convites de amizade. | O usuário pode se conectar a outros usuários através de convites de amizade. Amigos adicionados estarão disponíveis numa lista de amigos.  | Usuário |
| RF018 - Recusar convites de amizade | O usuário pode recusar convites de amizade | Usuário |
| RF019 - Remover amizade | O usuário pode remover a amizade com outros usuário a qualquer momento | Usuário |
| RF020 - Consultar amigos | O usuário poderá consultar seus amigos e exibir uma lista | Usuário |
| RF021 - Gostar de uma postagem | O usuário pode clicar no símbolo de gostar para dar reputação à postagem | Usuário |
| RF022 - Visualizar páginas de jogos | O sistema deverá acessar páginas de jogos a partir da conexão com APIs externas do IGDB e Steam | Administrador |
| RF023 - Manter páginas de jogos | O sistema deverá reter em banco de dados informações de jogos que receberam um resenha | Administrador |

&nbsp;

## Lista de Requisitos Não-Funcionais

| Requisito | Descrição |
| --------- | --------- |
| RNF001 - Respossibilidade | Deve abrir perfeitamento no *Mozilla FireFox* e *Chrome* em  em diversos tamanhos de tela |
| RNF002 - Conexões com APIs externas | O sistema deve buscar informações de um jogo acessado em no máximo 2 segundos |

&nbsp;

## Riscos

Tabela com o mapeamento dos riscos do projeto, as possíveis soluções e os responsáveis.

| Data | Risco | Prioridade | Responsável | Status | Providência/Solução |
| :--: | ----- | ---------- | ----------- | ------ | ------------------- |
| 15/10/2020 | Não aprendizado das ferramentas utilizadas pelos componentes do grupo | Alta | Todos | Vigente | Reforçar estudos sobre as ferramentas e aulas com a integrante que conhece a ferramenta |
| 15/10/2020 | Divisão de tarefas mal sucedida | Baixa | Gerente | Vigente | Acompanhar de perto o desenvolvimento de cada membro da equipe |
| 01/11/2020 | Implementação de protótipo com as tecnologias | Alto | Todos | Resolvido | Encontrar tutorial com a maioria da tecnologia e implementar um caso base do sistema |

&nbsp;

### Referências

Documentação da SteamAPI. Disponível em: <https://developer.valvesoftware.com/wiki/Steam_Web_API>
Documentação da API IGDB. Disponível em: <https://api-docs.igdb.com/#about>  
Modelo de Documento de Visão do BSI. Disponível em: <https://docs.google.com/document/d/1DPBcyGHgflmz5RDsZQ2X8KVBPoEF5PdAz9BBNFyLa6A/edit>
Modelo de Documento de Modelos do BSI. Disponível em: <https://docs.google.com/document/d/1cddfSCpBtTjmDLxsFND9BM6m9hQZSTPAwHrNYXif98/edit>
