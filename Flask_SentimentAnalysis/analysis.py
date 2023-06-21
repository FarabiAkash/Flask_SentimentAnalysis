from setfit import SetFitModel
from statistics import mean 


def sentAnalysis(text):
            
    # Split the test intu multiple line for line wise analysis.
    text = text.split('.')
    # Remove the last item in the list if it is empty
    if(text[-1] == ''):
        text.pop()
    # Load the pretrained model
    model = SetFitModel.from_pretrained("StatsGary/setfit-ft-sentinent-eval")
    # Run inference for all teh items
    preds = model(text)
    preds=preds.tolist()
    # conver the score to Negative or Positive
    temp_preds=[]
    for i in range(len(preds)):
        if preds[i] == 1:
            temp_preds.append('Positive')
        if preds[i] == 0:
            temp_preds.append('Negative')
    # create a statement wise analysis dictionary
    res = {}
    for key in text:
        for value in temp_preds:
            res[key] = value
            temp_preds.remove(value)
            break
    # Generate an overall analysis of the statement
    preds_avg = mean(preds)
    if (preds_avg<0.4):
        sentiment = 'Negative'
    elif (preds_avg>.6):
        sentiment = 'Positive'
    else:
        sentiment = 'Neutral'

    # Return the analysis result in a dictionary
    result = {"sentiment": sentiment,
            "detailed_analysis" : res
            }
    return result