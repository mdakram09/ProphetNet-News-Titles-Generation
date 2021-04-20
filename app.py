import flask
from flask import Flask, request, render_template,url_for,redirect,jsonify
#from transformers import XLMProphetNetTokenizer, XLMProphetNetForConditionalGeneration, ProphetNetConfig
import json
import requests
import tweepy
from textblob import TextBlob


# for stock sentiment analysis
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')

set(stopwords.words('english'))

#PROPHETNET_PATH = 'model/prophetnet'

app = Flask(__name__)

#model = XLMProphetNetForConditionalGeneration.from_pretrained(PROPHETNET_PATH)
#tokenizer = XLMProphetNetTokenizer.from_pretrained(PROPHETNET_PATH)

# Custom Prediction Function
# def text_summarize(text):
#     inputs = tokenizer(text, padding=True, max_length=256, return_tensors='pt')
#     summary_ids = model.generate(inputs['input_ids'], num_beams=4, max_length=100, early_stopping=True)
#     result = tokenizer.batch_decode(summary_ids, skip_special_tokens=True)
#     return result[0]


url = ('https://newsapi.org/v2/top-headlines?'
       'country=in&'
       'apiKey=58f304ff540642adbe4816847fcefbc4')
def get_data(url):
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    return articles

articles = get_data(url)

#---------------- USE YOU API BY CREATING DEVELOPER ACCOUNT ON TWITTER -----------------------------------------------------------

consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#-------------------------------------------------------------------------


@app.route("/twitter")
def twitter():
    return render_template('twitter.html')



@app.route("/search",methods=["GET","POST"])
def searchtweet():
    search_tweet = request.form.get("search_query")
    
    t = []
    tweets = api.search(search_tweet, tweet_mode='extended')
    for tweet in tweets:
        polarity = TextBlob(tweet.full_text).sentiment.polarity
        subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
        t.append([tweet.full_text,polarity,subjectivity])
        # t.append(tweet.full_text)

    return jsonify({"success":True,"tweets":t})



@app.route('/')
def index():
    return render_template('index.html',articles=articles)



@app.route("/aboutus")
def aboutus():
    return render_template('aboutus.html')


@app.route("/contactus")
def contactus():
    return render_template('contactus.html')


@app.route("/stocksentiment")
def stocksentiment():
    return render_template('stocksentiment.html')



@app.route('/stocksentiment', methods=['POST'])
def stocksentimentlogic():
    stop_words = stopwords.words('english')
    test_data = request.form['test_data'].lower()

    processed_data = ' '.join([word for word in test_data.split() if word not in stop_words])

    sia = SentimentIntensityAnalyzer()
    dd = sia.polarity_scores(text=processed_data)
    compound = round((1 + dd['compound'])/2, 2)

    return render_template('stocksentiment.html', final=compound, test_data=test_data)




@app.route('/corona', methods=['POST','GET'])
def corona():
    data ='corona'
    if not data:
        return redirect(url_for('invalid'))
    else:
        url= ('https://newsapi.org/v2/everything?q='+data+'&apiKey=58f304ff540642adbe4816847fcefbc4')
        articles = get_data(url)
        return render_template('topics.html',articles=articles,data=data)



@app.route('/india', methods=['POST','GET'])
def india():
    data ='india'
    if not data:
        return redirect(url_for('invalid'))
    else:
        url= ('https://newsapi.org/v2/everything?q='+data+'&apiKey=58f304ff540642adbe4816847fcefbc4')
        articles = get_data(url)
        return render_template('topics.html',articles=articles,data=data)


@app.route('/sports', methods=['POST','GET'])
def sports():
    data ='sports'
    if not data:
        return redirect(url_for('invalid'))
    else:
        url= ('https://newsapi.org/v2/everything?q='+data+'&apiKey=58f304ff540642adbe4816847fcefbc4')
        articles = get_data(url)
        return render_template('topics.html',articles=articles,data=data)


@app.route('/entertainment', methods=['POST','GET'])
def entertainment():
    data ='entertainment'
    if not data:
        return redirect(url_for('invalid'))
    else:
        url= ('https://newsapi.org/v2/everything?q='+data+'&apiKey=58f304ff540642adbe4816847fcefbc4')
        articles = get_data(url)
        return render_template('topics.html',articles=articles,data=data)


@app.route('/technology', methods=['POST','GET'])
def technology():
    data ='technology'
    if not data:
        return redirect(url_for('invalid'))
    else:
        url= ('https://newsapi.org/v2/everything?q='+data+'&apiKey=58f304ff540642adbe4816847fcefbc4')
        articles = get_data(url)
        return render_template('topics.html',articles=articles,data=data)


@app.route('/education', methods=['POST','GET'])
def education():
    data ='education'
    if not data:
        return redirect(url_for('invalid'))
    else:
        url= ('https://newsapi.org/v2/everything?q='+data+'&apiKey=58f304ff540642adbe4816847fcefbc4')
        articles = get_data(url)
        return render_template('topics.html',articles=articles,data=data)


@app.route('/gaming', methods=['POST','GET'])
def gaming():
    data ='gaming'
    if not data:
        return redirect(url_for('invalid'))
    else:
        url= ('https://newsapi.org/v2/everything?q='+data+'&apiKey=58f304ff540642adbe4816847fcefbc4')
        articles = get_data(url)
        return render_template('topics.html',articles=articles,data=data)


@app.route('/jobs', methods=['POST','GET'])
def jobs():
    data ='jobs'
    if not data:
        return redirect(url_for('invalid'))
    else:
        url= ('https://newsapi.org/v2/everything?q='+data+'&apiKey=58f304ff540642adbe4816847fcefbc4')
        articles = get_data(url)
        return render_template('topics.html',articles=articles,data=data)


@app.route('/stockmarket', methods=['POST','GET'])
def stockmarket():
    data ='stock market'
    if not data:
        return redirect(url_for('invalid'))
    else:
        url= ('https://newsapi.org/v2/everything?q='+data+'&apiKey=58f304ff540642adbe4816847fcefbc4')
        articles = get_data(url)
        return render_template('topics.html',articles=articles,data=data)


@app.route('/weather', methods=['POST','GET'])
def weather():
    data ='weather'
    if not data:
        return redirect(url_for('invalid'))
    else:
        url= ('https://newsapi.org/v2/everything?q='+data+'&apiKey=58f304ff540642adbe4816847fcefbc4')
        articles = get_data(url)
        return render_template('topics.html',articles=articles,data=data)


@app.route('/trending', methods=['POST','GET'])
def trending():
    data ='trending'
    if not data:
        return redirect(url_for('invalid'))
    else:
        url= ('https://newsapi.org/v2/everything?q='+data+'&apiKey=58f304ff540642adbe4816847fcefbc4')
        articles = get_data(url)
        return render_template('topics.html',articles=articles,data=data)



@app.route('/invalid')
def invalid():
    return "<center><h2 style='color:green;'>something went wrong..!</h2></center>"

@app.route('/searchnews', methods=['POST','GET'])
def search():
    if request.method =='POST':
            data =request.form['search']
            if not data:
                return redirect(url_for('invalid'))
            else:
                url= ('https://newsapi.org/v2/everything?q='+data+'&apiKey=58f304ff540642adbe4816847fcefbc4')
                articles = get_data(url)
                return render_template('search.html',articles=articles,data=data)
        
    #print(get_data(url)) 
    #else:
      #  redirect(url_for('index.html'))

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         sentence = request.json['input_text']
#         model = request.json['model']
#         if sentence != '':
#             if model.lower() == 'prophetnet':
#                 output = text_summarize(sentence)
#             else:
#                 pass
#             response = {}
#             response['response'] = {
#                 'summary': str(output),
#                 'model': model.lower()
#             }
#             return flask.jsonify(response)
#         else:
#             res = dict({'message': 'Empty input'})
#             return app.response_class(response=json.dumps(res), status=500, mimetype='application/json')
#     except Exception as ex:
#         res = dict({'message': str(ex)})
#         print(res)
#         return app.response_class(response=json.dumps(res), status=500, mimetype='application/json')


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=8001)