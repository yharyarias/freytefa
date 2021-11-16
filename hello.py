from flask import Flask

app = Flask(__name__) # Instancia de la aplicación Flask.
# Esto se hace porque Flask configura algunas rutas en segundo plano.
# Envia respuestas al usuario.

@app.route('/') # Convierte el valor de devolución de la función en una respuesta HTTP
def hello():
    return 'Hello, World!'

    



