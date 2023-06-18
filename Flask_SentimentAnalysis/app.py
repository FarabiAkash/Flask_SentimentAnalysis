from flask import Flask, request
from flask_restful import Resource, Api

from setfit import SetFitModel
from statistics import mean 

app = Flask(__name__)
api = Api(app)

temp_database={
    '1': 'Positive',
    '0': 'Negative'
}

class SentimentAnalysis(Resource):

    def post(self):
        sentiment = {}
        try:
            data = request.json
            text = data['text']
        except Exception as e:
            return {"msg": "An exception occurred. Error: "+str(e)}, 400
        
        try:
            data = ["i hate the spiderman movie!", "pineapple on pizza is the worst", "The new book pissed me of", "He ate lunch", "I love you", "Some days are harder than others; I'm doing my best today.", "I'm working on accepting myself just as I am.", "Feelings are not facts.", "I can ride this wave and get back to work."]
            text = text.split('.')
            if(text[-1] == ''):
                text.pop()
            model = SetFitModel.from_pretrained("StatsGary/setfit-ft-sentinent-eval")
            preds = model(text)
            preds=preds.tolist()
            temp_preds=[]
            for i in range(len(preds)):
                if preds[i] == 1:
                    temp_preds.append('Positive')
                if preds[i] == 0:
                    temp_preds.append('Negative')
            res = {}
            for key in text:
                for value in temp_preds:
                    res[key] = value
                    temp_preds.remove(value)
                    break
            preds_avg = mean(preds)
            if (preds_avg<0.4):
                sentiment = 'Negative'
            elif (preds_avg>.6):
                sentiment = 'Positive'
            else:
                sentiment = 'Neutral'
        except Exception as e:
            return {"msg": "An exception occurred. Error: "+str(e)}, 500
        result = {
            "sentiment": sentiment,
            "detailed_analysis" : res
        }
        return {"sentiment_analysis": result}, 200



api.add_resource(SentimentAnalysis, '/analyze')



if __name__ == '__main__':
    app.run(debug=True)


