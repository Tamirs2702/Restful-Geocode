from flask_restful import Resource


class HelloAPI(Resource):

    def get(self):
        """
        Greets GeoPython conf
        ---
        tags:
          - getAddresses
        produces:
          - application/json
        responses:
            200:
                description: Says hello
            500:
                description: Internal Server Error
        """
        return {"hello": "GeoPython 17"}, 200


class getResult(Resource):

    def get(self, num1: int, num2: int):
        """
        Here you can Upload csv files
        ---
        tags:
          - getResult Api
        produces:
          - application/json
        parameters:

        responses:
            200:
                description: Answer provided
            500:
                description: Internal Server Error
        """
        return {"answer": num1 * num2}, 200
