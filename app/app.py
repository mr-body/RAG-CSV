from flask import Flask, render_template
from flask_cors import CORS
from route.morning import morning_bp

app = Flask(__name__)
CORS(app)  # Configura o CORS para permitir solicitações de qualquer origem

app.register_blueprint(morning_bp, url_prefix='/morning')

@app.route('/')
def index():
    return render_template('app.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
