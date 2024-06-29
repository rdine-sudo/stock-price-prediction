from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime as nowdt
import sweetify
from .  import models
import nltk
nltk.download('vader_lexicon')
import requests
from bs4 import BeautifulSoup

CURRENCY = [
  {
    "Symbol": "BTC-USD",
    "Company Name": "Bitcoin"
  },
  {
    "Symbol": "ETH-USD",
    "Company Name": "Ethereum"
  },
  {
    "Symbol": "USDT-USD",
    "Company Name": "Tethert"
  },
  {
    "Symbol": "BNB-USD",
    "Company Name": "BNB"
  },
  {
    "Symbol": "XRP-USD",
    "Company Name": "XRP"
  },
  {
    "Symbol": "USDC-USD",
    "Company Name": "USD Coin"
  },
  {
    "Symbol": "STETH-USD",
    "Company Name": "Lido Staked ETH"
  },
  {
    "Symbol": "SOL-USD",
    "Company Name": "Solana"
  },
  {
    "Symbol": "ADA-USD",
    "Company Name": "Cardano"
  },
  {
    "Symbol": "WTRX-USD",
    "Company Name": "Wrapped TRON"
  },
  {
    "Symbol": "DOGE-USD",
    "Company Name": "Dogecoin"
  },
  {
    "Symbol": "TRX-USD",
    "Company Name": "TRON"
  },
  {
    "Symbol": "TON11419-USD",
    "Company Name": "Toncoin"
  },
  {
    "Symbol": "DAI-USD",
    "Company Name": "Dai"
  },
  {
    "Symbol": "MATIC-USD",
    "Company Name": "Polygon"
  },
  {
    "Symbol": "DOT-USD",
    "Company Name": "Polkadot"
  },
  {
    "Symbol": "LTC-USD",
    "Company Name": "Litecoin"
  },
  {
    "Symbol": "WBTC-USD",
    "Company Name": "Wrapped Bitcoin"
  },
  {
    "Symbol": "BCH-USD",
    "Company Name": "Bitcoin Cash"
  },
  {
    "Symbol": "LINK-USD",
    "Company Name": "Chainlink"
  },
  {
    "Symbol": "SHIB-USD",
    "Company Name": "Shiba Inu"
  },
  {
    "Symbol": "AVAX-USD",
    "Company Name": "Avalanche"
  },
  {
    "Symbol": "LEO-USD",
    "Company Name": "UNUS SED LEO"
  },
  {
    "Symbol": "TUSD-USD",
    "Company Name": "TrueUSD"
  },
  {
    "Symbol": "WKAVA-USD",
    "Company Name": "Wrapped Kava"
  },
  {
    "Symbol": "XLM-USD",
    "Company Name": "Stellar"
  },
  {
    "Symbol": "XMR-USD",
    "Company Name": "Monero"
  },
  {
    "Symbol": "OKB-USD",
    "Company Name": "OKB"
  },
  {
    "Symbol": "ATOM-USD",
    "Company Name": "Cosmos"
  },
  {
    "Symbol": "UNI7083-USD",
    "Company Name": "Uniswap"
  }
]
# Create your views here.
def index(request):
    errorMessage = ''
    if request.method == 'POST':
        username = request.POST['email']  # username
        password = request.POST['password']  # password
        user = authenticate(username=username, password=password)  # Authendicating user
        if user is not None:
            login(request, user)  # if user availlable login
            return redirect('/home')
        else:
            sweetify.error(request, 'Invalid user')
            print("error2")
            errorMessage = 'True'
    context = {'errorMessage': "Invalid User"}
    return render(request, 'index.html', context)

    
def registration(request):
    if request.method == "POST":
        firstName = request.POST["firstName"]
        lastName = request.POST["lastName"]
        email = request.POST["email"]
        password = request.POST["password"]

        user = User.objects.create_user(email, email, password)
        user.first_name = firstName
        user.last_name = lastName
        user.save()
        return redirect('/')

    return render(request, 'registration.html')

def home(request):
    return render(request, 'home.html')

def prediction(request):
    data = None
    if request.method == "POST":
        currency = request.POST["currency"]
        data = loadData(currency)
    return render(request, 'prediction.html', data)

def sentiment(request):
    data = None
    if request.method == "POST":
        currency = request.POST["currency"]
        data = loadSentimentData(currency)
    return render(request, 'sentiment.html', data)

def logout_view(request):
    logout(request)
    return redirect('/')

def loadData(name):
    date  = []
    close  = []
    data = models.ForecastedTrend.objects.filter(name=name)
    for i in data:
      date.append(i.Date.strftime("%m/%d/%Y"))
      close.append(i.Forecast)
    return {'date': date, "close": close}


def loadSentimentData(name):
    import nltk
    from nltk.sentiment.vader import SentimentIntensityAnalyzer

    # Initialize the VADER sentiment analyzer
    sia = SentimentIntensityAnalyzer()
    # Define the cryptocurrency coin name you want to search for
    coin_name = 'bitcoin'

    # URL of the CoinDesk Bitcoin news search page
    url = f'https://www.cnbc.com/{coin_name}/'

    # Send an HTTP GET request to the search page
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find and print search results
        search_results = soup.find_all('a', class_='Card-title')
        search_data  = ''
        for idx, result in enumerate(search_results, start=1):
            search_data += result.text.strip()
            print(f"Search Result {idx}: {result.text.strip()}")
        print(search_data)
        if not search_results:
            print(f"No search results found for '{coin_name}' on the page.")
    else:
        print("Error: Unable to retrieve search results.")
    # Text to analyze
    text = str(search_data)

    # Perform sentiment analysis
    sentiment_scores = sia.polarity_scores(text)

    # Interpret the sentiment scores
    if sentiment_scores['compound'] >= 0.05:
        sentiment = "Positive"
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    # Print the sentiment and sentiment scores
    print(f"Sentiment: {sentiment}")
    print(f"Positive Score: {sentiment_scores['pos']:.2f}")
    print(f"Negative Score: {sentiment_scores['neg']:.2f}")
    print(f"Neutral Score: {sentiment_scores['neu']:.2f}")
    print(f"Compound Score: {sentiment_scores['compound']:.2f}")
    return {'Sentiment': sentiment}

