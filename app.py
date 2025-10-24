from flask import Flask, render_template, jsonify
from firebase_admin import credentials, db, initialize_app
import firebase_admin

app = Flask(__name__)

# === CONFIGURAÇÃO DO FIREBASE ===
cred = credentials.Certificate("sismag-firebase-adminsdk-fbsvc-9c97b7bf6b.json")
initialize_app(cred, {
    'databaseURL': 'https://sismag-default-rtdb.firebaseio.com/'
})

# === ROTAS ===
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/monitoramento')
def monitoramento():
    return render_template('monitoramento.html')

@app.route('/alerta')
def alerta():
    return render_template('alerta.html')

@app.route('/dados')
def dados():
    ref = db.reference('/sensorMQ135')
    dados_sensor = ref.get()
    if not dados_sensor:
        dados_sensor = {"nivelGas": 0, "qualidade": "Sem dados"}
    return jsonify(dados_sensor)

if __name__ == '__main__':
    app.run(debug=True)
