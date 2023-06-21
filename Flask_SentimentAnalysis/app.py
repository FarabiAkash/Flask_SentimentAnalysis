from flask import Flask, request
from flask_restful import Resource, Api
from analysis import sentAnalysis

app = Flask(__name__)
api = Api(app)

class SentimentAnalysis(Resource):

    def post(self):
        #take the test input. It can be single line or a paragraph
        try:
            data = request.json
            text = data['text']
        except Exception as e:
            return {"msg": "An exception occurred. Error: "+str(e)}, 400
        try:
            result = sentAnalysis(text)
        except Exception as e:
            result={"msg": "An exception occurred. Error: "+str(e)}
            return {"msg": "An exception occurred. Error: "+str(e)}, 500
        return result, 200


api.add_resource(SentimentAnalysis, '/analyze')

if __name__ == '__main__':
    app.run(debug=True)


