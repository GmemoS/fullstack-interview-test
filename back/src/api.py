from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from config import CustomConfig
from resources.branches import Branches
from resources.commits import Commits

app = Flask(__name__)
app.config.from_object(CustomConfig)
CustomConfig.init_app(app)
api = Api(app)
CORS(app)

api.add_resource(Branches, '/api/v1/branches', '/api/v1/branches/')

api.add_resource(Commits, '/api/v1/commits', '/api/v1/commits/')

if __name__ == '__main__':
    app.run(host="0.0.0.0")
