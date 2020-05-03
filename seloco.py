from flask import Flask, render_template
app = Flask(__name__)



comidas = ['Refrigerante','Pizza','Suco','Salgado','Lanche']
precos = ['4.50' , '2.50' , '24.90', '5.50', '18.50']
@app.route('/')
def index():
    return render_template(
        'index.html',
        title='Início',
        comidas = comidas
        
        
        )
@app.route('/com/<int:id>')
def comida(id):
    nome = comidas[id]
    preco = precos[id]
    return f'Nome: {nome}  -  Preço: {preco}'


if __name__ == '__main__':
    app.run()
