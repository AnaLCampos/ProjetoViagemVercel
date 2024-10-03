from flask import Flask, render_template, request, redirect

class cadviagens:
    def __init__(self, idviagens,nomedestino,pais,atracao,customedio,classificacao):
        self.idviagens = idviagens
        self.nomedestino=nomedestino
        self.pais= pais
        self.atracao= atracao
        self.customedio= customedio
        self.classificacao= classificacao

lista = []

app = Flask(__name__)



@app.route('/')
def cadastro():
    return render_template('Cadastro.html',Titulo='CADASTROS DE VIAGENS')

@app.route('/criar', methods=['POST'])
def criar():
    idviagens = request.form['ID-Viagens']
    nomedestino = request.form['Nome']
    pais = request.form['Pais']
    atracao = request.form['Atracao']
    customedio = request.form['CustoMedio']
    classificacao = request.form['Classificacao']
    obj = cadviagens(idviagens,nomedestino,pais,atracao,customedio,classificacao)
    lista.append(obj)
    return redirect('/viagens')

@app.route('/viagens')
def viagens():
    return render_template('Viagens.html', Titulo='VIAGENS', ListaViagens=lista)

@app.route('/excluir/<idviagens>', methods=['GET', 'DELETE'])
def excluir(idviagens):
    for i, viagens in enumerate(lista):
        if viagens.idviagens == idviagens:
            lista.pop(i)
            break
    return redirect('/viagens')

@app.route('/editar/<idviagens>', methods=['GET'])
def editar(idviagens):
    for i, viagens in enumerate(lista):
        if viagens.idviagens == idviagens:
            return render_template('Editar.html', Titulo='Editar Viagens', Viagens=viagens)


@app.route('/alterar', methods=['PUT', 'POST'])
def alterar():
    id = request.form['ID-Viagens']
    for i, viagens in enumerate(lista):
        if viagens.idviagens == id:
            viagens.nomedestino = request.form['Nome']
            viagens.pais = request.form['Pais']
            viagens.atracao = request.form['Atracao']
            viagens.customedio = request.form['CustoMedio']
            viagens.classificacao = request.form['Classificacao']
        return redirect('/viagens')

if __name__ == '__main__':
    app.run()
