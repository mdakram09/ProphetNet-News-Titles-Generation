import flask
from flask import Flask, request, render_template,url_for,redirect
#from transformers import XLMProphetNetTokenizer, XLMProphetNetForConditionalGeneration, ProphetNetConfig
import json
import requests

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





@app.route('/')
def index():
    return render_template('index.html',articles=articles)



@app.route("/aboutus")
def aboutus():
    return render_template('aboutus.html')


@app.route("/contactus")
def contactus():
    return render_template('contactus.html')



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



@app.route('/news', methods=['POST','GET'])
def news():
    articles = get_data(url)
    return render_template('news.html',articles=articles)


@app.route('/invalid')
def invalid():
    return "<center><h2 style='color:green;'>something went wrong..!</h2></center>"

@app.route('/search', methods=['POST','GET'])
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