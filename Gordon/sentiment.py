from textblob import TextBlob
import nltk


nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('brown')

def sentimentAnalysis(sentance):
    analysis = TextBlob(sentance)
    polarity = analysis.sentiment.polarity
    
    if polarity> 0:
        return "Positive"
    if polarity == 0:
        return "Neutral"
    else:
        return "Negative"
    
def main():
    print("Welcome to the Sentiment Analysis Tool!")
    
    sentance = input ("Enter a sentance to analyse its sentiment: ")
    
    sentiment = sentimentAnalysis(sentance)
    
    print(f"The sentiment of the sentance is:{sentiment}")
    
    if __name__== "__main__":
        main()