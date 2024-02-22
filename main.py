#criando API em flask
from flask import Flask
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def home():
        return "Minha primeira API"
    
@app.route('/sentimento/<frase>')
def sentimento(frase):
    tb= TextBlob(frase)
    #tb_ingles = tb.translate(from_lang='pt', to='en')
    #polaridade = tb_ingles.sentiment.polarity
    polaridade = tb.sentiment.polarity
    return "Polaridade: {}".format(polaridade)
    
app.run(debug = True)