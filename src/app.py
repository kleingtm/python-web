from flask import Flask, Blueprint
from flask_restplus import Resource, Api

app = Flask(__name__)
blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint, doc='/doc/')

app.register_blueprint(blueprint)
assert url_for('api.doc') == '/api/doc/'

@app.route('/')
@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)