import spacy
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from transformers import pipeline
import nltk

nltk.download('vader_lexicon')
nlp = spacy.load("en_core_web_sm")
sia = SentimentIntensityAnalyzer()
summarizer = pipeline("summarization", model="sshleifer/distilbar
