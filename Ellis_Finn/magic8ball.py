import random
import time
#from sense_hat import SenseHat
#sh = SenseHat()
#sh.show_message("
print("Ask a question")
question = input("what is your question")
replies = ['Signs point yes', 'Without a doubt', 'You may rely on it', 'Do not count on it',
           'Looking good', 'Cannot predict now', 'It is decidedly so','Outlook not so good'] 
print(random.choice(replies)) 