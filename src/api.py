from flask import Flask, Blueprint
from flask_restplus import Resource, Api
from src.wallet import api as wallet

app = Flask(__name__) # instantiate flask app
blueprint = Blueprint('api', __name__, url_prefix='/api') # set api location with a blueprint
api = Api(blueprint, doc='/docs/') # instantiate API, and pass docs location -- /api/docs
app.register_blueprint(blueprint) # register the main api blueprint

# add other nested api namespaces
api.add_namespace(wallet, path='/wallet')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5006, debug=True)