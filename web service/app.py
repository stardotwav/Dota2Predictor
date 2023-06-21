from flask import Flask, render_template, request
from modelo import modelagemPredicao
from data import gerarNovosDados

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/', methods=['GET', 'POST'])
def index():
    # variáveis auxiliares
    partidas = 0 
    precisaomedalha = 0
    precisaotaxavitoria = 0
    probabilidade = 0
    team = 'RADIANT'

    if request.method == 'POST':
        radiantheroes = request.form.get('radiantheroes')
        direheroes = request.form.get('direheroes')
        radiantmedals = request.form.get('radiantmedals')
        diremedals = request.form.get('diremedals')
        
        if radiantheroes and direheroes:
            # separando os heróis
            radiantheroes = radiantheroes.split(',')
            direheroes = direheroes.split(',')

            # separando as medalhas
            radiantmedals = radiantmedals.split(',')
            diremedals = diremedals.split(',')

            if len(radiantheroes) == 5 and len(direheroes) == 5 and len(radiantmedals) == 5 and len(diremedals) == 5:
                # enviando para trasnformação dos dados
                dados = modelagemPredicao.preprocessamentomedalha(radiantheroes, radiantmedals, direheroes, diremedals)
                print(dados)

                # predict do modelo
                team, probabilidade = modelagemPredicao.predicao(dados, 1)

            elif len(radiantheroes) == 5 and len(direheroes) == 5:
                # enviando para trasnformação dos dados
                dados = modelagemPredicao.preprocessamentotaxavitoria(radiantheroes, direheroes)
                print(dados)

                # predict do modelo
                team, probabilidade = modelagemPredicao.predicao(dados, 2)
    
    # precisão dos modelos
    precisaomedalha, precisaotaxavitoria, partidas = modelagemPredicao.precisaomodelos()

    # deixando valor da precisao em número inteiro
    precisaomedalha = int(precisaomedalha*100)
    precisaotaxavitoria = int(precisaotaxavitoria*100)

    # deixando a probabilidade em número inteiro
    probabilidade = int(probabilidade*100)

    # deixando texto maiusculo
    team = team.upper()

    # definindo cor para html de acordo com o time
    color = ''

    if team == 'RADIANT':
        color = '#64FF56'
    else:
        color = '#d84a4a'

    # renderizando modelo
    return render_template("index.html", partidas=partidas, precisaotaxavitoria=precisaotaxavitoria, precisaomedalha=precisaomedalha, chance=probabilidade, team=team, color=color)

@app.route('/atualizarDados')
def atualizarDados():
    # chamando função de inserção de novos dados
    gerarNovosDados.gerarNovosDadosPartidas()

    # renderizando modelo
    return render_template("atualizarDados.html")