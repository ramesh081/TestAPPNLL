from django.shortcuts import render
from django.db import connection
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


# Create your views here.
@api_view(['POST'])
def getanalytics(request):
    if request.method == 'POST':
      try:
        url = request.data['url']
        req = Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urlopen(req).read()
        soup = BeautifulSoup(html)
        text = soup.get_text()
        analyser = SentimentIntensityAnalyzer()
        scores = analyser.polarity_scores(text)
        return Response(scores)
      except Exception as e:
        return Response("The error is : " + str(e))

      
