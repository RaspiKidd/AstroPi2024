from textblob import TextBlob
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('brown')

def setimentAnylsis(sentance):
    anaylsis = TextBlob(sentance)
    polarity = analysis.sentiment.polarity
    
    if polarity > 0:
        return "positive :)"
    if polarity == 0:
        return "neutral :|"
    else:
        return "negative:("
def main():
    print("Welcome to the Sentiment Analysis Tool!")
    
    sentance = input("Enter a sentence to analyse its sentiment: ")
    
    sentiment = sentimentAnalysis(sentance)
    
    print(f"The sentiment of this sentance is: {sentiment}")
    
    if __name__== "__main__":
        main()