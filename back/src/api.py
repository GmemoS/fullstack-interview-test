from flask import Flask
from flask_restful import Api

from config import CustomConfig
from resources.branch import Branch
from resources.branches import Branches
from resources.branch_commits import BranchCommits
from resources.commit import Commit

app = Flask(__name__)
app.config.from_object(CustomConfig)
CustomConfig.init_app(app)
api = Api(app)

api.add_resource(Branches, '/api/v1/branches', '/api/v1/branches/')

api.add_resource(
    Branch,
    '/api/v1/branch/<string:name>',
    '/api/v1/branch/<string:name>/',
)

api.add_resource(
    BranchCommits,
    '/api/v1/branch/<string:name>/commits',
    '/api/v1/branch/<string:name>/commits/',
)

api.add_resource(
    Commit,
    '/api/v1/commit/<string:hexsha>',
    '/api/v1/commit/<string:hexsha>/',
)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
