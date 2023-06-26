<img src="https://github.com/stardotwav/Dota2Predictor/blob/main/img/icone.png" width="50px" align="left" alt="Imagem de Estrela">
<h1>Dota 2 Predictor</h1>

#### 🔴 Definição de Problema
Jogos do gênero *Multiplayer Online Battle Arena* (MOBA) tem se destacado nos últimos anos devido a sua popularidade e criação de campeonatos profissionais (eSports), e em conjunto a isso estudos sobre análise das partidas. O objetivo deste trabalho é a análise de dados de partidas profissionais do jogo *Defense of The Ancients 2* (Dota 2) para predição da chance de vitória de um determinado time utilizando do menor número de atributos possível, variando em 4 diferentes configurações dos atributos:

- Identificador de cada personagem selecionado por cada um dos times;
- Identificador de cada personagem selecionado por cada um dos times e a taxa de vitória do personagem escolhido;
- Identificador de cada personagem selecionado por cada um dos times e a medalha de cada um dos jogadores;
- Identificador de cada personagem selecionado por cada um dos times, a taxa de vitória do personagem escolhido e a medalha de cada um dos jogadores.

#### 🟠 Coleta dos Dados
Para realizar a previsão os dados foi utilizado de dados extraídos da API [OpenDota](https://www.opendota.com/) e com enriquecimento dos dados sobre a taxa de vitória de cada personagem usando da ferramenta [DotaBuff](https://pt.dotabuff.com). Na API Open Dota são disponibilizados a distinção no tipo das partidas, normais ou profissionais, dessa forma foram utilizados de dados de partidas profissionais, a fim de se obter um melhor balanceamento, visto que em partidas normais os jogadores possuem diversos níveis de conhecimento, além de que alguns jogadores privam o compartilhamento dos dados de sua conta, fazendo com não seja possível por exemplo identificar o personagem selecionado na partida. Como última etapa da coleta de dados, visto que a API citada anteriormente retorna apenas as últimas 100 partidas que um determinado personagem participou, indicando se naquela determinada partida o time do personagem perdeu ou venceu foi optado por salvar manualmente a taxa de vitórias de cada um dos personagens presentes no jogo usando da ferramenta DotaBuff, sendo importante ressaltar que a taxa de vitória varia de acordo com a medalha em que se está jogando, dessa forma sendo anotado a taxa de vitória na medalha em que os jogadores profissionais em sua maioria estão: Divino e Imortal. Ao final da extração dos dados foram extraídas informações de 1387 partidas profissionais de Dota 2.

É importante ressaltar que para a implantação do modelo foi desenvolvido no escopo do trabalho visa que novos dados possam ser inseridos a base de dados usada para a geração do modelo, dessa forma, sempre que pedido na interface desenvolvida novos dados são gerados, e inseridos no arquivo CSV gerado inicialmente, de forma a não constar duplicatas de partidas, visto que pode ocorrer a inserção de partidas listadas anteriormente caso não tenham sido realizadas novas partidas profissionais no intervalo de tempo entre as coletas dos dados.

Ao final, o *dataset* geral, que apenas varia na remoção de algumas colunas dependendo da abordagem analisada, obteve um total de 32 colunas, constando o número identificador da partida (removido durante as análises de predição), a coluna que identifica o time vencedor (*dire* ou *radiant*), e uma coluna para um dos personagens selecionados (10 ao todo) e respectivamente a taxa de vitória do mesmo e a medalha do jogador que estava utilizando deste personagem.


#### 🟡 Preparação dos Dados
Para realizar o treinamento dos modelos não foi necessária nenhuma preparação dos dados, ou seja, transformações e pré-processamento, isso porque todos os dados extraídos e enriquecidos na base de dados foram retornados em valores numéricos, dessa forma, sendo aceito em qualquer algoritmo de classificação. 

#### 🟢 Criação do Modelo
Para a escolha do modelo foram selecionados previamente alguns algoritmos apresentados na literatura para a classificação de resultados em partidas de jogos MOBA. Os algoritmos selecionados foram Logistic Regression, Random Forest, Decision Tree, K-Nearest Neighbors (KNN) e Naive Bayes. A partir dos algoritmos selecionados e das bases de dados foi realizada uma aplicação do algoritmo *cross validation* em todos os algoritmos para medir a precisão dos mesmos em relação a cada uma das bases de dados com diferentes atributos. É importante ressaltar que a aplicação do algoritmo utilizou de 30 iterações, em que as bases de dados foram separadas em treino e teste no formato 80\% treino e 20\% teste. Além disso, durante a validação usando da validaçãi cruzada em conjunto com o ajuste de parâmetros para a escolha do melhor algoritmo foi utilizado apenas da base de treino. Na Tabela abaixo é possível verificar os resultados obtidos de acurácia de cada modelo. 

Abordagem  | Logistic Regression | Decision Tree | Ramdom Forest | KNN | Naive Bayes | XGBoost
--------- | ------ | ------ | ------ | ------ | ------ | ------
(1) Personagem Selecionado | 54.6\% | 57.8\% | **60.5\%** | 57.8\% | 53.8\% | 57.9%
(2) Personagem Selecionado e Taxa de Vitória | 55.7\% | 62.5\% | **74.2\%** | 56.1\% | 54.9\% | 63.9%
(3) Personagem Selecionado e Medalha da Pessoa Jogadora | 53.7\% | 58.5\% | **61.2\%** | 56.1\% | 51.3\% | 56.4%
(4) Personagem Selecionado, Taxa de Vitória e Medalha da Pessoa Jogadora | 54.9\% | 63.5\% | **71.8\%** | 55.6\% | 52.8\% | 64.6%

Ao final, com as configurações feitas e todas as funções geradas, como apresentadas no arquivo de análise do algoritmo as mesmas foram inseridas em arquivos da linguagem Python, que foram incorporados ao back-end do sistema desenvolvido, visto que como foi desenvolvido no framework Flask, como será apresentado posteriormente a sua execução é similar a feita em arquivos do jupyter notebook.

#### 🔵 Implantação do Modelo
Em pose dos modelos selecionados foi realizada a implantação dos mesmos em uma aplicação *web*. A aplicação foi desenvolvida com o objetivo de ser utilizada por pessoas jogadoras e equipes de forma mais facilitada.

Para desenvolver a aplicação *web* foi desenvolvido inicialmente um modelo da interface exibida ao usuário, o \textit{front-end}, utilizando da ferramenta [Figma](https://www.figma.com). Após desenvolvido o modelo da interface foi utilizado da linguagem de marcação de hipertexto HTML, e da linguagem de estilo CSS para implementar o mesmo, não sendo necessário a utilização de nenhum *framework* adicional às linguagens.

Para que fosse realizado a predição de novos dados desconhecidos de forma similar ao feito nos experimentos na ferramenta Jupyter Notebook, foi realizado uma implementação *back-end* na aplicação *web* utilizado da linguagem Python, em específico do *framework* [Flask](https://flask.palletsprojects.com/en/2.3.x/). Foram desenvolvidas funções de treinamento do modelo, predição de dados desconhecidos, requisição de dados de novas partidas à API Open Dota, e exibição das interfaces desenvolvidas. Deve-se ressaltar que ao receber dados desconhecidos do usuário na aplicação é realizada uma transformação no nome de cada personagem, que com ajuda de um dicionário que tem como chave o nome de cada personagem, e como valor o seu número identificador. Além disso, no vetor de predição é inserida a informação da taxa de vitória de cada personagem, em que também é utilizado de um dicionário, onde sua chave é o número identificador do personagem, e o valor a taxa de vitória.

#### 🟣 Disponibilidade da Implantação do Modelo
Os modelos com melhores resultados foram implantados em uma aplicação *web*. Nas imagens abaixo podem ser visualizados as interfaces desenvolvidas.

<img src="https://github.com/stardotwav/Dota2Predictor/blob/main/img/telawebservice.png" alt="Captura de Tela Principal do Web Service">

<img src="https://github.com/stardotwav/Dota2Predictor/blob/main/img/atualizardadoswebservice.png" alt="Captura de Tela de Inserção de Novas Partidas na Base de Dados">

Para executar a interface, basta realizar a instalação do arquivo de [requirements.txt](https://github.com/stardotwav/Dota2Predictor/blob/main/web%20service/requirements.txt) em um ambiente virtual [venv](https://docs.python.org/pt-br/3/library/venv.html), e após isso realizar a execução do Flask.