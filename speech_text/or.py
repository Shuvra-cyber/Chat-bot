from chatterbot import Chatbot

bot = Chatbot('Simple bot',trainer = 'chatterbot.trainers.ChatterBotCorpusTrainer')

bot.train('chatterbot.corpus.english')
while True:
    user_input = input('You')