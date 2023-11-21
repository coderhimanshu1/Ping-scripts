import time
import requests

# Define your app URLs
APP_URL_portfolio = 'https://himanshu.dev/'
Pathos = 'https://pathos-backend.onrender.com'
APP_URL_remplr_unified = 'https://remplr.com/'
APP_URL_remplr1 = 'https://remplr.onrender.com/'
APP_URL_404_remplr_backend = 'https://remplr-backend.onrender.com/'
APP_URL_404_jobly_backend = 'https://jobly-backend-x9gn.onrender.com'
APP_URL_jobly_fronend ='https://job-findr.onrender.com'
APP_URL_resume = "https://resume-69e0.onrender.com/"
# Time interval: 20 minutes in seconds
INTERVAL = 20 * 60

def ping_app(url):
    try:
        response = requests.get(url)
        print(f"Received {response.status_code} from {url} at {time.ctime()}")
    except requests.RequestException as e:
        print(f"Error pinging {url} at {time.ctime()}: {e}")

def keep_awake():
    while True:
        ping_app(APP_URL_portfolio)
        ping_app(Pathos)
        ping_app(APP_URL_404_remplr_backend)
        ping_app(APP_URL_404_jobly_backend)
        ping_app(APP_URL_jobly_fronend)
        ping_app(APP_URL_remplr1)
        ping_app(APP_URL_resume)
        ping_app(APP_URL_remplr_unified)
        
        time.sleep(INTERVAL)

if __name__ == "__main__":
    keep_awake()
