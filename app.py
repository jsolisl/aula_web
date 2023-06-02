from flask import Flask,render_template

entradas=[{
    'titulo':'Primero Post do Blog',
    'texto':'Aqui vem o texto primero....'
    },

    {
    'titulo':'Segundo Post do Blog',
    'texto':'Aqui vem o texto segundo....'
    }
]

app=Flask(__name__)

@app.route('/')
def exibir_entradas():
    return render_template("exibir_entradas.html", entradas=entradas)