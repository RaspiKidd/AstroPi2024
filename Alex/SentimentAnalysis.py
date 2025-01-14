# Importing TextBlob
from textblob import TextBlob
import nltk

# Downloading necessary data for TextBlob
nltk.download('punkt')
nltk.download('average_perceptron_tagger')
nltk.download('brown')

def sentimentAnalysis(sentance):
#     Creating a TextBlob object
      analysis = TextBlob(sentance)
      
#     Getting sentiment polarity
      polarity = analysis.sentiment.polarity
      
      if polarity > 0:
          return "Positive"
      elif polarity == 0:
          return "Neutral"
      else:
          return "Negative"
        
# main function
def main():
    print("Welcome to the Sentiment Analysis Tool!")
    
# user input
sentance = input("Enter a sentance to analyse its sentiment: ")

# Analysing Sentiment
sentiment = sentimentAnalysis(sentance)

# Printing Sentiment
print(f"The sentiment of the sentance is: {sentiment}")

# Calling main function
if __name__ == "__main__":
    main()
    
        
        
        
      
      
      
      
      



