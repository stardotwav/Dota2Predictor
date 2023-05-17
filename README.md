<img src="https://github.com/stardotwav/Dota2Predictor/blob/main/img/icone.png" width="50px" align="left" alt="Imagem de Estrela">
<h1>Dota 2 Predictor</h1>

#### 🔴 Definição de Problema
Nos últimos anos tem sido estudados diversos temas ligados ao desenvolvimento de jogos digitais, em que ao olharmos especificamente para os jogos digitais do gênero MOBA temas como o estudo da toxicidade dos jogadores, a montagem e execução das regras de punição, a falta de representatividade das mulheres e, os fatores que colaboram para o sucesso de uma equipe tem se destacado [[1]](https://www.sciencedirect.com/science/article/abs/pii/S1875952117300149).

Olhando especificamente para trabalhos que lidam com os fatores que colaboram para o sucesso de uma equipe durante as partidas temos que é apresentado que a cooperação e a interação sejam o principal fator de colaboração [[2]](https://dl.acm.org/doi/10.1145/2487788.2488147) sendo isso muito exibido em equipes profissionais, que participam de campeonatos de e-Sports, visto que os mesmos passam diversas horas em conjunto treinando para os campeonatos. Além disso, um tema explorado recentemente sobre jogos MOBA é a predição da vitória de um determinado time, em que diversas características como os heróis escolhidos para a partida são usadas como base determinar a vitória, ou derrota [[3]](https://repositorio.bambui.ifmg.edu.br/index.php/ec/article/view/78).

Unindo os dois temas apresentados anteriormente: a participação de times profissionais, e a predição da vitória dos times de jogos MOBA, este trabalho irá apresentar um modelo para realizar a predição da vitória, ou derrota, de partidas do jogo [Dota 2](https://www.dota2.com/home) em seu cenário competitivo. A escolha da predição de vitórias usando de dados de jogos competitivos se deu pelo fator de seus dados serem mais precisos, visto que ao extrair dados de partidas comuns na maioria dos casos algumas informações para a predição não estavam preenchidas.

#### 🟠 Coleta dos Dados
Para a extração dos dados foi realizada uma pesquisa dos sistemas de API disponibilizados pela empresa gestora do jogo Dota 2, em que foi encontrado a API [OpenDota](https://www.opendota.com/), que disponibiliza a URL de requisição dos dados da API, de forma a facilitar o acesso na linguagem Python, usada para o desenvolvimento do projeto, bastando utilizar da biblioteca [requests](https://requests.readthedocs.io/en/latest/) que irá fazer o pedido das requisições, e a biblioteca [json](https://docs.python.org/pt-br/3/library/json.html) para que possamos manipular os dados e os transformar em arquivo CSV.

É importante ressaltar que para a implantação do modelo foi desenvolvido no escopo do trabalho visa que novos dados possam ser inseridos a base de dados usada para a geração do modelo, dessa forma, sempre que pedido na interface desenvolvida novos dados são gerados, e inseridos no arquivo CSV gerado inicialmente, de forma a não constar duplicatas de partidas, visto que pode ocorrer a inserção de partidas listadas anteriormente caso não tenham sido realizadas novas partidas profissionais no intervalo de tempo entre as coletas dos dados. Sobre os dados armazenados no CSV usado como base para a geração do modelo, o mesmo possui as seguintes colunas, e seguintes descrições:

idMatch | teamWinner | pickRadiant1, pickDire1, .. | numTeamFights | barracksRadiant e barracksDire
:------: | :------: | :------: | :------: | :------: |
Inteiro que indica o número da partida extraída pela API | String que indica o valor que desejamos adivinhar na predição do modelo | Inteiro que indica o identificador do personagem selecionado por cada jogador retornado pela API | Número de batalhas ocorridas durante a partida com participação dos times de forma completa ou quase completa | Número de estruturas de barracas que não foram destruídas, sendo esse valor extraído como um valor de base 2 e convertido para binário | 

#### 🟡 Preparação dos Dados
Visto que os dados utilizados durante a classificação da porcentagem de vitória de um time são em sua maioria númerica não foi necessária nenhuma preparação mais complexa, em que como o usuário não seria capaz de indicar o id de cada personagem retornado pela API utilizada, neste caso foi gerado um arquivo CSV contendo o nome de cada personagem e seu identificador, de forma que ao o usuário digitar com espaços o nome de cada personagem, como por exemplo é apresentado abaixo, é feita uma verificação de busca simples para identificar de qual personagem se trata e realizar a inserção na lista de picks que mais tarde é convertida em um dataset para a predição.

```
Crystal Maiden, Axe, Lina, Dark Willow, Zeus
```

Dessa forma, foi feito um pequeno diagrama de demonstração de como os dados recebidos pelo usuário são tratados para análise, apresentado abaixo.

<img src="https://github.com/stardotwav/Dota2Predictor/blob/main/img/preparacaoDadosUsuario.png" alt="Diagrama de Apresentação do Processo de Tratamento dos Dados Enviados pelo Usuário">

Sobre os dados extraídos pela API eles possuem um fluxo de tratamento diferente, isso porque quase todos os dados utilizados da API vem na forma final utilizado na dataframe de geração do modelo, em que apenas o número de barracas foi passa um tratamento, em que o mesmo é necessário ser transformado em valores binários, e a partir disso são contabilizados o número de valores 1 e isso indica o número de barracas que estavam em pé no final da partida. Abaixo também é apresentado um diagrama do tratamento dos dados da API.

<img src="https://github.com/stardotwav/Dota2Predictor/blob/main/img/preparacaoDadosAPI.png" alt="Diagrama de Apresentação do Processo de Tratamento dos Dados Enviados pela API">

#### 🟢 Criação do Modelo
🚧 Em construção a escolha e criação do modelo.

#### 🔵 Implantação do Modelo
🚧 Em construção a forma de implantação do modelo.

#### 🟣 Disponibilidade da Implantação do Modelo
Para a construção da implantação do modelo foi utilizado da criação de um web service, dessa forma necessitando de um desenvolvimento web, em que foi utilizado pra criação dos templates no **front-end** HTML e CSS, sem a necessidade de frameworks. Visando um melhor desenvolvimento da interface desenvolvida os modelos utilizados foram inicialmente modelados por meio da ferramenta **Figma** que os modelos desenvolvidos podem ser acessados [aqui](https://www.figma.com/file/8m0BbtTDQEJImw8tZmLBG0/Design-Twitts-League-of-Legends?type=design&node-id=0%3A1&t=N5HS2oQEgtKDhGDi-1).

E para o **back-end** visando usar da linguagem Python, usada no desenvolvimento do modelo, e pensando na atualização constante do modelo foi utilizado do framework **[Flask](https://flask.palletsprojects.com/en/2.3.x/)**.

🚧 Em construção a implantação do modelo na AWS.