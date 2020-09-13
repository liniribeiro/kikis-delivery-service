from flask_restful import Resource


class HealthCheckHandler(Resource):

    def get(self):
        return {}, 200

