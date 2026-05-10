from flask import Flask
from flask_cors import CORS
from routes.simulate import simulate_bp
from routes.requests import requests_bp
from models import create_tables

app = Flask(__name__)
CORS(app)

app.register_blueprint(simulate_bp)
app.register_blueprint(requests_bp)

if __name__ == "__main__":
    create_tables()
    app.run(debug=True)