#criando API em flask
from flask import Flask
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression



app = Flask(__name__)

df = pd.read_csv("Casas - casas.csv")

colunas = ['tamanho' , 'preco']
df = df[colunas]
df.head()

x = df.drop('preco', axis = 1)
y = df ['preco']

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3)

modelo = LinearRegression()
modelo.fit(x_train,y_train)

modelo.intercept_

@app.route('/')
def home():
        return "Home"
    
@app.route('/casas/<int:tamanho>')
def casas(tamanho):
    preco = modelo.predict([[tamanho]])
    return str(preco)
    
app.run(debug = True)