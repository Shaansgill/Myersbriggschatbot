from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot 

bot=ChatBot('Test')

conv = open('ENTJ.txt', 'r').readlines()

bot.set_trainer(ListTrainer)
bot.train(conv)

while True:
	request = input('You: ')
	response = bot.get_response(request)

	print('Bot: ', response)