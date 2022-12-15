from flask import Flask, request
from flask_restful import Api, Resource
import math

app = Flask(__name__)
api = Api(app)

class Karekok(Resource):
        def get(self,sayi):
                return {'Sayinin Karekoku' : math.sqrt(sayi)},200

api.add_resource(Karekok,'/kareKok/<int:sayi>')

app.run(host="0.0.0.0", port=5000)
app.run()