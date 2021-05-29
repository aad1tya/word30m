import pandas as pd
from PyDictionary import PyDictionary
import random
from pushbullet import Pushbullet
import time
from datetime import datetime

word_data = pd.read_excel('lemmas.xlsx')
word_data = word_data['lemma']
word_data = word_data[1000:]
file = 'new_word.txt'

def greetings(current_time):
    if hour_time == '08':
        lists = ["Have a great day ahead"]
        with open(file, mode = 'w') as f:
            f.write(lists[random.randint(0,3)])
        
        with open(file, mode = 'r') as f:
            text = f.read()
        
        push = pb.push_note("Good Morning".title(), text)
    
    if hour_time == '13':
        lists = ["What's for Lunch?", "Let's achieve some great wonders today!!", "Time for a Lunch Break!"]
        with open(file, mode = 'w') as f:
            f.write(lists[random.randint(0,3)])
        
        with open(file, mode = 'r') as f:
            text = f.read()
        
        push = pb.push_note("Good Afternoon!".title(), text)
    
    if hour_time == '22':
        with open(file, mode = 'w') as f:
            f.write("How was your day?")
        with open(file, mode = 'r') as f:
            text = f.read()
        
        push = pb.push_note("Good Night".title(), text)
    
            
while True:        
    now = datetime.now()
    current_time = now.strftime('%H:%M')
    hour_time = now.strftime('%H')
    if '09:00' < current_time < '21:00': 

        API_KEY = config.api_key
        pb = Pushbullet(API_KEY)

        dictionary = PyDictionary()
        with open(file, mode = 'w') as f:
            word = word_data.iloc[random.randint(0, 4000)]
            try:
                f.write("1st definition: " + dictionary.meaning(word)['Noun'][0:2][0].title())
                f.write('\n')
                if len(dictionary.meaning(word)['Noun']) > 1:
                    f.write("2nd Defintion: " + dictionary.meaning(word)['Noun'][0:2][1].title())
            except:
                f.write("Google the definition, we kind of messed up in the code!")

        with open(file, mode = 'r') as f:
            text = f.read()

        push = pb.push_note(word.title(), text)

    greetings(hour_time)
    time.sleep(1800)

    
