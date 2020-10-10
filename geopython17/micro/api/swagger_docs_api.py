from flask import current_app, jsonify
from flask_restful import Resource
from flask_swagger import swagger


class SwaggerDocsAPI(Resource):
    """
    Tsimple endpoint for flask-swagger to generate the API docs,
    https://github.com/gangverk/flask-swagger
    """

    def get(self):
        """ Generates YAML for swagger-ui """
    
        swag = swagger(current_app)
        swag['info']['title'] = "Dokka Assignment"
        swag['info']['description'] = "API endpoints for Dokka"
        swag['info']['version'] = "0.0.1"

        return jsonify(swag)
