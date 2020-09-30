# Documento de Visão

Documento de Visão do projeto GamingTrack, construído a partir do **Modelo BSI - Doc 001 - Documento de Visão** que pode ser encontrado no
link: https://docs.google.com/document/d/1DPBcyGHgflmz5RDsZQ2X8KVBPoEF5PdAz9BBNFyLa6A/edit?usp=sharing

## Equipe e Definição de Papéis

Membro     |     Papel   |   E-mail   |
---------  | ----------- | ---------- |
Geraldo    | Desenvolvedor, Testador  | geraldo_sjs@hotmail.com
Paulo      | Gerente, Desenvolvedor | paulovmedeiros@outlook.com
Pedro      | Analista, Desenvolvedor | pedrojonassm@gmail.com

### Matriz de Competências

Membro     |     Competências   |
---------  | ----------- |
Geraldo    | Desenvolvedor Java Script, VueJS, Python, Python-Django, C, C#, Java, Eclipse, Matemática, Latex. |
Paulo      | Front-end (HTML, CSS, JS), UI, UX, Design Gráfico, etc. |
Pedro      | Desenvolvedor Java, Python, C, Eclipse, Visual Studio, Matemática, etc. |

## Perfis dos Usuários

O sistema será utilizado por diversos perfis de usuário, sendo eles:

Perfil        | Descrição   |
---------     | ----------- |
Administrador | Usuário que possui todas as permissões de acesso. Pode realizar os cadastros base, utilizar todas as funções de CRUD e moderação no sistema.
Moderador     | Usuário que possui acesso às permissões de acesso para moderar as postagens e conteúdo no sistema, além das funções acessíveis a usuários.
Usuário       | Usuário comum que possui acesso ao cadastro no site e possui permissão para publicar e interagir com outros usuários no site.

## Lista de Requisitos Funcionais

Requisito                                 | Descrição   | Ator |
---------                                 | ----------- | ---------- |
RF001 - Realizar o cadastro para utilizar o sistema.     | O usuário pode se cadastrar para utilizar o sistema. | Usuário |
RF002 - Permitir a criação de resenhas, comentários e postagem de conteúdo sobre jogos. | O usuário pode publicar conteúdo sobre jogos específicos, como resenhas, vídeos e fotos. | Usuário |
RF003 - Conectar usuários através de convites de amizade. | O usuário pode se conectar a outros usuários através de convites de usuário. Amigos adicionados estarão disponíveis numa lista de amigos.  | Usuário |
RF004 - Moderação de conteúdo publicado. | Os moderadores do sistema devem ter acesso às postagem dos usuários e ter a opção de moderar o conteúdo, eliminando e advertendo usuários que façam publicações ofensivas. | Administrador |
RF005 - Manter páginas de jogos | O sistema deverá possuir páginas que apresentem os dados dos jogos. Estas informações serão obtidas a partir da conexão com APIs externas do IGDB e Steam. | Administrador |

## Lista de Requisitos Não-Funcionais

Requisito                                 | Descrição   |
---------                                 | ----------- |
RNF001 - Deve ser acessível via navegador | Deve abrir perfeitamento no Firefox e no Chrome. |
RNF002 - Conexões com APIs externas | O sistema deve estar conectados às APIs da Steam e do IGDB para acessar informações sobre os jogos. |

## Riscos

Tabela com o mapeamento dos riscos do projeto, as possíveis soluções e os responsáveis.

Data | Risco | Prioridade | Responsável | Status | Providência/Solução |
------ | ------ | ------ | ------ | ------ | ------ |
15/10/2020 | Não aprendizado das ferramentas utilizadas pelos componentes do grupo | Alta | Todos | Vigente | Reforçar estudos sobre as ferramentas e aulas com a integrante que conhece a ferramenta |
15/10/2020 | Divisão de tarefas mal sucedida | Baixa | Gerente | Vigente | Acompanhar de perto o desenvolvimento de cada membro da equipe |
01/10/2020 | Implementação de protótipo com as tecnologias | Alto | Todos | Resolvido | Encontrar tutorial com a maioria da tecnologia e implementar um caso base do sistema |

### Referências