from flask import Flask
from flask_cors import CORS
from routes.simulate import simulate_bp
from routes.requests import requests_bp
from database import create_tables
import os
 
app = Flask(__name__)
CORS(app)

app.register_blueprint(simulate_bp)
app.register_blueprint(requests_bp)

if __name__ == "__main__":
    create_tables()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)