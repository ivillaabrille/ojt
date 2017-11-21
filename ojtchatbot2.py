import sys

class ChatBot():

	def __init__(self, user_input='', greeting_kw=(), greeting_resp=[]):
		self.user_input = ''
	
	def startup(self):
		print('Hello! I am the Support Bot ready to take your requests! Please choose from the list below to get Started:')
		print('[1] Request \n [2] Update on your Request \n [3] Technical Support \n [4] Exit')
		return str(input("You> "))

	def request(self):
		print('Welcome to the Request Menu! Here we provide the following services so you are able to choose which you would like:')
		print('[1] Application \n [2] Design \n [3] Logo \n [4] Back to Main Menu')
		return str(input("You> "))

	def requestapp(self):
		print('You are requesting an Application from us, please fill up the fields below.')
		self.appname = str(input('Application Name: '))
		self.apptype = str(input('Application Type(Web-Based or Desktop-Based): '))
		self.description = str(input('Description and or functionalities you want in your app: '))
		self.timeframe = str(input('When do you want it done?: '))
		self.budget = str(input('Budget: '))
		self.email = str(input('Enter your email so we are able to contact you when we approve your request: '))
		self.phone = str(input('Enter your Mobile or Telephone Number: '))

		#database query to insert into app table
		print('Your request has been sent to us. Please wait awhile to check if your request was accepted.')

	def requestdesign(self):
		print('You are requesting an Design from us, please fill up the fields below.')
		self.designname = str(input('Design Name: '))
		self.description = str(input('Description such as shape, colors, and etc. for your design: '))
		self.timeframe = str(input('When do you want it done?: '))
		self.budget = str(input('Budget: '))
		self.email = str(input('Enter your email so we are able to contact you when we approve your request: '))
		self.phone = str(input('Enter your Mobile or Telephone Number: '))

		#database query to insert into design table
		print('Your request has been sent to us. Please wait awhile to check if your request was accepted.')

	def requestlogo(self):
		print('You are requesting an Logo from us, please fill up the fields below.')
		self.logoname = str(input('Logo Name: '))
		self.description = str(input('Description such as shape, colors, and etc. for your Logo: '))
		self.timeframe = str(input('When do you want it done?: '))
		self.budget = str(input('Budget: '))
		self.email = str(input('Enter your email so we are able to contact you when we approve your request: '))
		self.phone = str(input('Enter your Mobile or Telephone Number: '))

		#database query to insert into logo table
		print('Your request has been sent to us. Please wait awhile to check if your request was accepted.')

	def update(self, user_input):
		update_keywords = ('progress', 'going', 'time', 'how')
		#database query to get approved apps
		#database query to get approved designs
		#database query to get approved logos

		#for app name in app query
		#if app name in user_input:

		#for design name in design query
		#if design name in user_input:

		#for logo name in logo query
		#if logo name in user_input:
		words = user_input.split()
		for word in words:
			if word.lower() in update_keywords:
				print('Response')




#main
bot = ChatBot()
userinput = ''
while True:
	ui = bot.startup()
	if ui == '1':
		ui2 = bot.request()
		if ui2 == '1':
			bot.requestapp()
		elif ui2 == '2':
			bot.requestdesign()
		elif ui2 == '3':
			bot.requestlogo()
		elif ui2 == '4':
			bot.startup()
		else:
			print('Invalid Choice! Please Try Again.')

	elif ui == '2':
		print('Hello there! Ask me anything regarding updates of your request!')
		userinput = str(input('You> '))
		bot.update(userinput)

	elif ui == '3':
		pass
		#response
		#insert question and answer in a table

	elif ui == '4':
		sys.exit()

	else:
		print('Invalid Choice! Please Try Again.')
