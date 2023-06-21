import pandas as pd
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score
from sklearn.model_selection import train_test_split

# criando uma máscara para gerar posições aleatórias
# da separação de dados de treino e teste
def separacaoModelo(dataset, target):
    X = dataset.drop(target, axis=1)
    Y = dataset[target]
    xTrain, xTest, yTrain, yTest = train_test_split(X, Y, test_size=0.2, random_state=42)
    
    return xTrain, xTest, yTrain, yTest
    
def precisaomodelos():
    dadosmedalha = pd.read_csv('dadosmedalhataxavitoria.csv')
    dadosmedalha = dadosmedalha.drop_duplicates()
    dadosmedalha = dadosmedalha.drop(columns=['Unnamed: 0', 'id'])
    dadosmedalha['winner'] = dadosmedalha['winner'].apply(lambda item: 1 if item == 'radiant' else 0)

    dadostaxavitoria = pd.read_csv('dadosmedalhataxavitoria.csv')
    dadostaxavitoria = dadostaxavitoria.drop_duplicates()
    dadostaxavitoria = dadostaxavitoria.drop(columns=['Unnamed: 0', 'id', 'rank1', 'rank2', 'rank3', 
                                                    'rank4', 'rank5', 'rank6', 'rank7', 'rank8', 
                                                    'rank9', 'rank10'])
    dadostaxavitoria['winner'] = dadostaxavitoria['winner'].apply(lambda item: 1 if item == 'radiant' else 0)

    # número de partidas
    partidas = dadosmedalha[dadosmedalha.columns[0]].count()
    # treino e teste
    xTrain, xTest, yTrain, yTest = separacaoModelo(dadosmedalha, 'winner')
    # predição
    modelo = RandomForestClassifier(bootstrap=False, criterion='gini', max_depth=None, min_samples_split=2, n_estimators=100, random_state=42)
    modelo.fit(xTrain, yTrain)
    pred = modelo.predict(xTest)
    precisaomedalha = precision_score(yTest, pred)

    # treino e teste
    xTrain, xTest, yTrain, yTest = separacaoModelo(dadostaxavitoria, 'winner')
    # predição
    modelo = RandomForestClassifier(bootstrap=False, criterion='gini', max_depth=None, min_samples_split=4, n_estimators=200, random_state=42)
    modelo.fit(xTrain, yTrain)
    pred = modelo.predict(xTest)
    precisaotaxavitoria = precision_score(yTest, pred)

    return precisaomedalha, precisaotaxavitoria, partidas
    
def preprocessamentomedalha(radiantheroes, radiantmedals, direheroes, diremedals):
    f = open('dadosheroistaxavitoria.csv','r')
    heroes = pd.read_csv(f)
    heroes = heroes.drop(columns=['Unnamed: 0'])
    valores = heroes['id'].values
    taxavitoria = heroes['taxavitoria'].values
    heroes = heroes['nome'].values
    f.close()
    dados = []

    for i in range(len(heroes)):
        heroes[i] = heroes[i].replace(' ', '')

    for i in range(len(radiantheroes)):
        radiantheroes[i] = radiantheroes[i].replace(' ', '')
        for j in range(len(heroes)):
            if radiantheroes[i] == heroes[j]:
                dados.append(int(valores[j]))
                dados.append(taxavitoria[j])
                dados.append(radiantmedals[i])
                break

    for i in range(len(direheroes)):
        direheroes[i] = direheroes[i].replace(' ', '')
        for j in range(len(heroes)):
            if direheroes[i] == heroes[j]:
                dados.append(int(valores[j]))
                dados.append(taxavitoria[j])
                dados.append(diremedals[i])
                break

    return dados

def preprocessamentotaxavitoria(radiantheroes, direheroes):
    f = open('dadosheroistaxavitoria.csv','r')
    heroes = pd.read_csv(f)
    heroes = heroes.drop(columns=['Unnamed: 0'])
    valores = heroes['id'].values
    taxavitoria = heroes['taxavitoria'].values
    heroes = heroes['nome'].values
    f.close()
    dados = []

    for i in range(len(heroes)):
        heroes[i] = heroes[i].replace(' ', '')

    for i in range(len(radiantheroes)):
        radiantheroes[i] = radiantheroes[i].replace(' ', '')
        for j in range(len(heroes)):
            if radiantheroes[i] == heroes[j]:
                dados.append(int(valores[j]))
                dados.append(taxavitoria[j])
                break

    for i in range(len(direheroes)):
        direheroes[i] = direheroes[i].replace(' ', '')
        for j in range(len(heroes)):
            if direheroes[i] == heroes[j]:
                dados.append(int(valores[j]))
                dados.append(taxavitoria[j])
                break

    return dados

def predicao(vetor, tipo):
    if tipo == 1:
        dados = pd.read_csv('dadosmedalhataxavitoria.csv')
        dados = dados.drop(columns=['Unnamed: 0', 'id'])
        dados = dados.drop_duplicates()

        # treino e teste
        xTrain, xTest, yTrain, yTest = separacaoModelo(dados, 'winner')
        # predição
        modelo = RandomForestClassifier(bootstrap=False, criterion='gini', max_depth=None, min_samples_split=2, n_estimators=100, random_state=42)
        modelo.fit(xTrain, yTrain)

        partida = []
        partida.append(0)
        partida[0] = vetor
        time = modelo.predict(partida)[0]
        probabilidade = 0

        if time == 'dire': 
            probabilidade = modelo.predict_proba(partida)[0][0]
        else:
            probabilidade = modelo.predict_proba(partida)[0][1]

        return time, probabilidade
    
    else:
        dados = pd.read_csv('dadosmedalhataxavitoria.csv')
        dados = dados.drop(columns=['Unnamed: 0', 'id', 'rank1', 'rank2', 'rank3', 
                                    'rank4', 'rank5', 'rank6', 'rank7', 'rank8', 'rank9', 'rank10'])
        dados = dados.drop_duplicates()

        # treino e teste
        xTrain, xTest, yTrain, yTest = separacaoModelo(dados, 'winner')
        # predição
        modelo = RandomForestClassifier(bootstrap=False, criterion='gini', max_depth=None, min_samples_split=4, n_estimators=200, random_state=42)
        modelo.fit(xTrain, yTrain)

        partida = []
        partida.append(0)
        partida[0] = vetor
        time = modelo.predict(partida)[0]
        probabilidade = 0

        if time == 'dire': 
            probabilidade = modelo.predict_proba(partida)[0][0]
        else:
            probabilidade = modelo.predict_proba(partida)[0][1]

        print(probabilidade)
        return time, probabilidade