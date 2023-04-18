<img src="https://github.com/stardotwav/Dota2Predictor/blob/main/img/icone.png" width="30px" align="left" margim-top="10" alt="Imagem de Estrela">
<h1>Dota 2 Predictor</h1>

#### 🔴 Definição de Problema
Nos últimos anos tem sido estudados diversos temas ligados ao desenvolvimento de jogos digitais, em que ao olharmos especificamente para os jogos digitais do gênero MOBA temas como o estudo da toxicidade dos jogadores, a montagem e execução das regras de punição, a falta de representatividade das mulheres e, os fatores que colaboram para o sucesso de uma equipe tem se destacado [[1]](https://www.sciencedirect.com/science/article/abs/pii/S1875952117300149).

Olhando especificamente para trabalhos que lidam com os fatores que colaboram para o sucesso de uma equipe durante as partidas temos que é apresentado que a cooperação e a interação sejam o principal fator de colaboração [[2]](https://dl.acm.org/doi/10.1145/2487788.2488147) sendo isso muito exibido em equipes profissionais, que participam de campeonatos de e-Sports, visto que os mesmos passam diversas horas em conjunto treinando para os campeonatos. Além disso, um tema explorado recentemente sobre jogos MOBA é a predição da vitória de um determinado time, em que diversas características como os heróis escolhidos para a partida são usadas como base determinar a vitória, ou derrota [[3]](https://repositorio.bambui.ifmg.edu.br/index.php/ec/article/view/78).

Unindo os dois temas apresentados anteriormente: a participação de times profissionais, e a predição da vitória dos times de jogos MOBA, este trabalho irá apresentar um modelo para realizar a predição da vitória, ou derrota, de partidas do jogo [Dota 2](https://www.dota2.com/home) em seu cenário competitivo. A escolha da predição de vitórias usando de dados de jogos competitivos se deu pelo fator de seus dados serem mais precisos, visto que ao extrair dados de partidas comuns na maioria dos casos algumas informações para a predição não estavam preenchidas.

#### 🟠 Coleta dos Dados
Para a extração dos dados foi realizada uma pesquisa dos sistemas de API disponibilizados pela empresa gestora do jogo Dota 2, em que foi encontrado a API [OpenDota](https://www.opendota.com/), que disponibiliza a URL de requisição dos dados da API, de forma a facilitar o acesso na linguagem Python, usada para o desenvolvimento do projeto, bastando utilizar da biblioteca [requets](https://requests.readthedocs.io/en/latest/) que irá fazer o pedido das requisições, e a biblioteca [json](https://docs.python.org/pt-br/3/library/json.html) para que possamos manipular os dados e os transformar em arquivo CSV.

É importante ressaltar que para a implantação do modelo foi desenvolvido no escopo do trabalho visa que novos dados possam ser inseridos a base de dados usada para a geração do modelo, dessa forma, sempre que pedido na interface desenvolvida novos dados são gerados, e inseridos no arquivo CSV gerado inicialmente, de forma a não constar duplicatas de partidas, visto que pode ocorrer a inserção de partidas listadas anteriormente caso não tenham sido realizadas novas partidas profissionais no intervalo de tempo entre as coletas dos dados.

#### 🟡 Preparação dos Dados
🚧 Em construção a escolha da preparação dos dados.

#### 🟢 Criação do Modelo
🚧 Em construção a escolha e criação do modelo.

#### 🔵 Implantação do Modelo
🚧 Em construção a forma de implantação do modelo.

#### 🟣 Disponibilidade da Implantação do Modelo
🚧 Em construção a implantação do modelo.