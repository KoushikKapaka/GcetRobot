import json
import random
import chatterbot
from chatterbot.trainers import ListTrainer
from chatterbot.comparisons import LevenshteinDistance
from chatterbot import ChatBot
data = json.loads (open('data.json', 'r').read())
intent=data['intents']
train=[]
for k, row in enumerate (intent) : 
    for q in row['patterns']:
        response = random.choice(row['responses'])
        train.append(q)
        train.append(response)
  
bot = ChatBot('GreetBot',preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ],logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": chatterbot.comparisons.LevenshteinDistance,
        }
    ],statement_comparison_function=LevenshteinDistance)
trainner= ListTrainer(bot)
trainner.train(train)
