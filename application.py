from flask import Flask, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle



application = Flask(__name__)
@application.route('/', methods=['GET', 'POST'])
def index():
    return "Your Flask App Works! V1.0"

def load_model(news_text):
    print("in load_model")
    print("the news text is:", news_text)
    # model loading
    with open('basic_classifier.pkl', 'rb') as fid:
        loaded_model = pickle.load(fid)
    with open('count_vectorizer.pkl', 'rb') as vd:
        vectorizer = pickle.load(vd)
    
    # how to use model to predict
    prediction = loaded_model.predict(vectorizer.transform([news_text]))[0]
    # output will be 'FAKE’ if fake, 'REAL' if real
    return prediction

@application.route("/predict")
def predict():
    news_text = request.args.get('news')
    result = load_model(news_text)
    return f"Model Prediction: {result}"


if __name__ == "__main__":
    application.run()