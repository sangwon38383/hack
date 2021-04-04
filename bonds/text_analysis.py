from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import requests

def do_search(text):
    subscription_key = "cb86145a200f40b891825d40f2d70ad8"
    search_url = 'https://api.bing.microsoft.com/v7.0/search'
    search_term = text
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    params = {"q": search_term, "textDecorations": True, "textFormat": "HTML"}
    response = requests.get(search_url, headers=headers, params=params)
    search_results = response.json()
    text = search_results['webPages']['value'][0]['snippet']
    return text

def authenticate_client():
    key = "4d81d266fa544d14b61307f781f73411"
    endpoint = "https://sangwon38383.cognitiveservices.azure.com/"
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client


def sentiment_analysis_example(documents):
    client = authenticate_client()
    documents = [documents]
    response = client.analyze_sentiment(documents=documents)[0]
    rate = response.confidence_scores.negative
    return rate
   
        

def do_anal(text):
    tex = do_search(text)
    texx = sentiment_analysis_example(tex)
    return texx
