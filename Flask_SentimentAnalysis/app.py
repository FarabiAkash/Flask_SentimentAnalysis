from flask import Flask, request
from flask_restful import Resource, Api

from setfit import SetFitModel

app = Flask(__name__)
api = Api(app)



class SentimentAnalysis(Resource):

    def post(self):
        sentiment = ''
        
        try:
            data = request.json
            text = data['text']
            print(text)
        except Exception as e:
            print("An exception occurred. Error: "+str(e))
            return {"msg": "An exception occurred. Error: "+str(e)}
        
        try:
            model = SetFitModel.from_pretrained("StatsGary/setfit-ft-sentinent-eval")
            preds = model(["i loved the spiderman movie!"])

            print('***************')
            print(preds)
            sentiment=preds
        except Exception as e:
            print("An exception occurred. Error: "+str(e))
            return {"msg": "An exception occurred. Error: "+str(e)}


        return {"sentiment": sentiment}



api.add_resource(SentimentAnalysis, '/analyze')



if __name__ == '__main__':
    app.run(debug=True)