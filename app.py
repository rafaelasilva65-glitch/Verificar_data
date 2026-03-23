from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)
@app.route('/')
def home():
    return "<h1>Hello, World!</h1>"

@app.route("/maior_menor/<n1>/<n2>")
#@app.route("/data/<data_entrada>")
def maior_menor(n1, n2):
    n1=int(n1)
    n2=int(n2)
    if n1 > n2:
        return f'N1{n1} é maior que N2{n2}'
        """dados =
         {
            'n1': n1,
            'n2': n2,
        }
        #return jsonfy()"""
    else:
        return f'N2{n2} é maior que n1{n1}'

@app.route('/verificar-data/<data_entrada>')
def verificar_data(data_entrada):
    data_convertida = (datetime.datetime.strptime(data_entrada, '%d-%m-%Y')).date()
    agora_now = (datetime.datetime.now()).date()
    agora_today = (datetime.datetime.today()).date()
    if data_convertida > agora_today:
        var_situacao = f'Futuro{data_convertida}'
    elif data_convertida < agora_now:
        var_situacao = f'Passado{data_convertida}'
    else:
         var_situacao = f'Presente{data_convertida}'

    dia = (data_convertida - agora_now).days
    ano =(data_convertida.year - agora_now.year)
    mes= ((data_convertida.month - agora_now.month)+(12 * ano))
    print(f'teste: {dia}')
    print(f'teste_mes: {mes}')
    print(f'teste_ano: {ano}')

    dados = {
        "situacao":var_situacao,
        "dias_diferença":abs(int(dia)),
        "meses_diferença":abs(mes),
        "ano_diferença": abs(ano)
    }

    return jsonify(dados),200



if __name__ == '__main__':
    app.run(debug=True, port=5003)
