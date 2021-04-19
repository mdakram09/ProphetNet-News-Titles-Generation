import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
import pickle

def runPrediction():
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
    ## To check accuracy
    # matrix=confusion_matrix(test['Label'],predictions)
    # print(matrix)
    # score=accuracy_score(test['Label'],predictions)
    # print(score)
    # report=classification_report(test['Label'],predictions)
    # print(report)
    pickle.dump(randomclassifier, open('model.pkl', 'wb'))

runPrediction()