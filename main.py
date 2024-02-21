#criando API em flask
from flask import Flask
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def home():
        return "Minha primeira API"
    
#@app.route('/sentimentos/<frase>')
#def sentimentos(frase):
 #   tb= TextBlob(frase)
    #tb ingles = tb.translate(from_lang='pt, to+'en')
    
    
app.run(debug = True)