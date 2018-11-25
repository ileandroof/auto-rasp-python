from flask import Flask, render_template, request
from automate import inicializaBoard, definePinoSaida, escrevePorta, definePinoEntrada

app = Flask(__name__)

inicializaBoard()
definePinoSaida(3)
definePinoSaida(5)
definePinoSaida(7)
definePinoSaida(11)
definePinoSaida(13)
definePinoSaida(15)

@app.route('/', methods=['GET'])
def index():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def submit():
    comando=request.form['comando']
    print(comando)
    
    if(comando == 'QUARTO1ON'):
        escrevePorta(3,1)
    if(comando == 'QUARTO1OFF'):
        escrevePorta(3,0)
    if(comando == 'QUARTO2ON'):
        escrevePorta(5,1)
    if(comando == 'QUARTO2OFF'):
        escrevePorta(5,0)
    if(comando == 'CORREDORON'):
        escrevePorta(7,1)
    if(comando == 'CORREDOROFF'):
        escrevePorta(7,0)
    if(comando == 'COZINHAON'):
        escrevePorta(11,1)
    if(comando == 'COZINHAOFF'):
        escrevePorta(11,0)
    if(comando == 'SALAON'):
        escrevePorta(13,1)
    if(comando == 'SALAOFF'):
        escrevePorta(13,0)
    if(comando == 'QUINTALON'):
        escrevePorta(15,1)
    if(comando == 'QUINTALOFF'):
        escrevePorta(15,0)
    if(comando == 'TODASON'):
        escrevePorta(3,1)
        escrevePorta(5,1)
        escrevePorta(7,1)
        escrevePorta(11,1)
        escrevePorta(13,1)
        escrevePorta(15,1)
    if(comando == 'TODASOFF'):
        escrevePorta(3,0)
        escrevePorta(5,0)
        escrevePorta(7,0)
        escrevePorta(11,0)
        escrevePorta(13,0)
        escrevePorta(15,0)
    if(comando == 'LAMPADAON'):
        definePinoSaida(19)
    if(comando == 'LAMPADAOFF'):
        definePinoEntrada(19)
       
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True, host='192.168.25.54')