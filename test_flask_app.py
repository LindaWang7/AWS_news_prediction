import requests
import pickle

# BASE_URL = "http://your-app-url.us-east-1.elasticbeanstalk.com/predict"
BASE_URL = "http://127.0.0.1:5000/predict"

TEST_TEXTS = [
    {"text": "This is fake news"},
    {"text": "Another fake news example"},
    {"text": "This is real news"},
    {"text": "Legitimate news example"}
]
def unit_test(news):
    response = requests.get(BASE_URL, params={'news': news})
    print(response, response.text)


if __name__ == "__main__":

    news_real_1 = "Some Liberal MPs issued a deadline to Prime Minister Justin Trudeau"
    news_real_2 = "Canada will lower the number of permanent immigrants it allows into the country"
    news_fake_1 = "This is a fake news"
    news_fake_2 = "This is another fake news"

    unit_test(news_real_1)
    unit_test(news_real_2)
    unit_test(news_fake_1)
    unit_test(news_fake_2)
    
