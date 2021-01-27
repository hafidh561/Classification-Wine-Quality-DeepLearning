from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from model import predict_model

app = Flask(__name__)
api = Api(app)
CORS(app)

api_args = reqparse.RequestParser()
api_args.add_argument('fixed_acidity', type=float,
                      help='Fixed acidity (tartaric acid - g/dm3). Most acids involved with wine or fixed or nonvolatile (do not evaporate readily)', required=True)
api_args.add_argument('volatile_acidity', type=float,
                      help='Volatile acidity (acetic acid - g/dm3). The amount of acetic acid in wine, which at too high of levels can lead to an unpleasant, vinegar taste', required=True)
api_args.add_argument('citric_acid', type=float,
                      help='Citric acid (g/dm3). Found in small quantities, citric acid can add ‘freshness’ and flavor to wines', required=True)
api_args.add_argument('residual_sugar', type=float,
                      help='Residual sugar (g/dm3). The amount of sugar remaining after fermentation stops, it’s rare to find wines with less than 1 gram/liter and wines with greater than 45 grams/liter are considered sweet', required=True)
api_args.add_argument('chlorides', type=float,
                      help='Chlorides (sodium chloride - g/dm3). The amount of salt in the wine', required=True)
api_args.add_argument('free_sulfur_dioxide', type=float,
                      help='Free sulfur dioxide (mg/dm3). The free form of SO2 exists in equilibrium between molecular SO2 (as a dissolved gas) and bisulfite ion; it prevents microbial growth and the oxidation of wine', required=True)
api_args.add_argument('total_sulfur_dioxide', type=float,
                      help='Total sulfur dioxide (mg/dm3). Amount of free and bound forms of S02; in low concentrations, SO2 is mostly undetectable in wine, but at free SO2 concentrations over 50 ppm, SO2 becomes evident in the nose and taste of wine', required=True)
api_args.add_argument('density', type=float,
                      help='Density (g/cm3). The density of water is close to that of water depending on the percent alcohol and sugar content', required=True)
api_args.add_argument('ph', type=float,
                      help='pH. Describes how acidic or basic a wine is on a scale from 0 (very acidic) to 14 (very basic); most wines are between 3-4 on the pH scale', required=True)
api_args.add_argument('sulphates', type=float,
                      help='Sulphates (potassium sulphate - g/dm3). A wine additive which can contribute to sulfur dioxide gas (S02) levels, wich acts as an antimicrobial and antioxidant', required=True)
api_args.add_argument('alcohol', type=float,
                      help='Alcohol (% by volume). The percent alcohol content of the wine', required=True)


class Predict(Resource):
    def post(self):
        args = api_args.parse_args()
        predict = predict_model(
            args['fixed_acidity'],
            args['volatile_acidity'],
            args['citric_acid'],
            args['residual_sugar'],
            args['chlorides'],
            args['free_sulfur_dioxide'],
            args['total_sulfur_dioxide'],
            args['density'],
            args['ph'],
            args['sulphates'],
            args['alcohol'],
        )
        return {'predict': predict}, 201


api.add_resource(Predict, '/')

if __name__ == '__main__':
    app.run()
