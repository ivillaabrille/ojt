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

	def greeting(self):
		greeting_resp = ['Hello I am the Support Bot ready to answer your inquiries!', 'Hello there! I am here to answer your questions!']
		print(random.choice(greeting_resp))


#main
bot = ChatBot()
ui = ''
bot.startup()

greeting_kw = ('hi', 'hello', 'greeting', 'whats up', 'good morning', 'good evening', 'good afternoon', 'good noon')


while True:
	ui = bot.conversation()
	for greeting in greeting_kw:
		if greeting in ui:
			bot.greeting()

	if 'thank you' in ui:
		print('Your Welcome!')
		sys.exit()

	# else:
	# 	print('I dont get it.')
