# Importing TextBlob
from textblob import TextBlob
import nltk

# Downloading necessary data for TextBlob
nltk.download('punkt')
nltk.download('average_perceptron_tagger')
nltk.download('brown')

def sentimentAnalysis(sentance):
#     Creating a TextBlob object
      analysis = TextBlob object
      
#     Getting sentiment polarity
      polarity = analysis.sentiment.polarity
      
      if polarity > 0:
          return "Positive"
      if polarity == 0:
          return "Neutral"
      else:
          return "Negative"
        
# main function
def main():
    print("Welcome to the Sentiment Analysis Tool!")
    
        
        
        
      
      
      
      
      



