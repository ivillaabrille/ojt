import sys
import random

class ChatBot():

	def __init__(self, user_name='', age = 0):
		self.user_name = ''
		self.age = 0

	def startup(self):
		print('Hello I am the Support Bot ready to answer your inquiries! What is your name?')
		self.user_name = str(input('You> '))
		print('And your age?')
		self.age = str(input('You> '))
		print("So you're {}, {} right? Welcome! I am going to answer your inquiries starting now. Hit me up with your questions.".format(self.user_name, self.age))

	def conversation(self):
		return str(input("You> "))

	def check_greeting(self, user_input):
		greeting_kw = ('hi', 'hello', 'greeting', 'whats up', 'morning', 'evening', 'afternoon', 'noon')
		greeting_resp = ['Hello I am the Support Bot ready to answer your inquiries!', 'Hello there! I am here to answer your questions!']

		words = user_input.split()
		for word in words:
			if word.lower() in greeting_kw:
				print(random.choice(greeting_resp))
				break


#main
bot = ChatBot()
ui = ''
bot.startup()
while True:
	ui = bot.conversation()
	if 'thank you' in ui:
		print('Your Welcome!')
		sys.exit()

	else:
		bot.check_greeting(ui)
