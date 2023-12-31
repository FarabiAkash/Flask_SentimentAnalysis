# Flask_SentimentAnalysis

The project is a sentiment analysis service done using Flask

## Description

The service takes a text as a POST request and returns a detailed analysis of the text.

### POST request [http://127.0.0.1:5000/analyze]
```
{
    "text": "Pineapple on pizza is the worst. I like cheese on Pizza. Pizza is not difficult to eat. I love pizza. I also love chocolate, especially the dark chocolates. But the orange-flavored cholates disgust me"
}
```
### Request response
```
{
    "sentiment": "Positive",
    "detailed_analysis": {
        "Pineapple on pizza is the worst": "Negative",
        " I like cheese on Pizza": "Positive",
        " Pizza is not difficult to eat": "Positive",
        " I love pizza": "Positive",
        " I also love chocolate, especially the dark chocolates": "Positive",
        " But the orange flavored cholates disgust me": "Negative"
    }
}

```

## Getting Started

### Installing

Install and update using pip:
```
$   python -m venv vEnv_name
$   pip install flask
$   pip install flask-restful
$   pip install setfit
```
Or Install the 'requirements.txt' file 

## Application Structure 
```
.
|──────Flask_SentimentAnalysis/
| |────analysis.py/
| |────app.py/
```


### Executing program

* How to run the program
* Go to the directory 'Flask_SentimentAnalysis'
* run the command
```
python -m flask --app .\app.py run
```
## Reference

Offical Website

- [Flask](http://flask.pocoo.org/)
- [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)
- [Hugging Face- Setfit](https://huggingface.co/StatsGary/setfit-ft-sentinent-eval)




## Authors

Al-Farabi Akash
alfa.farabi@gmail.com
