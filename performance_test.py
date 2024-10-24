import requests
import time
import csv

# BASE_URL = "http://127.0.0.1:5000/predict"
BASE_URL = "http://ECE444PRA5CA-env.eba-mggkj3tg.ca-central-1.elasticbeanstalk.com"
# BASE_URL = "http://your-app-url.us-east-1.elasticbeanstalk.com/predict"


def test_latency():
    with open('latency_results.csv', 'w', newline='') as csvfile:
        fieldnames = ['test_case', 'response_time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for i in range(100):
            for idx, test_text in enumerate(TEST_TEXTS):
                start_time = time.time()
                response = requests.get(BASE_URL, params=test_text)
                end_time = time.time()
                response_time = end_time - start_time
                
                writer.writerow({
                    'test_case': f"test_case_{idx+1}",
                    'response_time': response_time
                })
                print(f"Test {idx+1}, Request {i+1}: {response_time} seconds")

if __name__ == "__main__":
    news_real_1 = "Some Liberal MPs issued a deadline to Prime Minister Justin Trudeau"
    news_real_2 = "Canada will lower the number of permanent immigrants it allows into the country"
    news_fake_1 = "This is a fake news"
    news_fake_2 = "This is another fake news"


    TEST_TEXTS = [
        {"text": news_real_1},
        {"text": news_real_2},
        {"text": news_fake_1},
        {"text": news_fake_2}
]
    test_latency()
