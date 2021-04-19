
from flask import Flask, request, render_template
from sklearn.metrics import accuracy_score
import pickle
import nltk
import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))
# cv = pickle.load(open('transform.pkl','rb'))
nltk.download('stopwords')
set(stopwords.words('english'))

@app.route('/')
def my_form():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    df=pd.read_csv('Data.csv', encoding = "ISO-8859-1")
    #train = df[df['Date'] < '20150101']
    # Removing punctuations
    data = df.iloc[:,2:27]
    data.replace("[^a-zA-Z]"," ",regex=True, inplace=True)
    # Renaming column names for ease of access
    list1 = [i for i in range(25)]
    new_Index = [str(i) for i in list1]
    data.columns = new_Index
    # Convertng headlines to lower case
    for index in new_Index:
        data[index] = data[index].str.lower()
    ' '.join(str(x) for x in data.iloc[1,0:25])
    headlines = []
    for row in range(0,len(data.index)):
        headlines.append(' '.join(str(x) for x in data.iloc[row,0:25]))
    # implemet bag of words
    countvector = CountVectorizer(ngram_range=(2,2))
    dataset = countvector.fit_transform(headlines)
    # implement RandomForest Classifier
    randomclassifier = RandomForestClassifier(n_estimators=200,criterion='entropy')
    randomclassifier.fit(dataset,df['Label'])

    test_data = request.form['text1'].lower()
    processed_data = [test_data]
    transformed_data = countvector.fit_transform(processed_data).toarray()



    # countvector = CountVectorizer(ngram_range=(2,2))
    # test_dataset = countvector.transform(test_data)
    # processed_data = ' '.join([word for word in test_data.split() if word not in stop_words]) 
    prediction = model.predict(transformed_data)

    #accuracy = accuracy_score(test_data,prediction)
    return render_template('form.html', final=prediction, test_data=test_data)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5002, threaded=True)
