import random
import sys

CONVERSING = True

memory = []
greetings = ['hola', 'hello', 'hi','hey!','hello','Hi']
questions = ['how are you','how are you doing']
responses = ['okay','i am fine']
validations = ['yes','yeah','yea','no','nah','not really']
verifications = ['are you sure','you sure','sure']
thanks = ['thanks', 'thank you', 'thank']
techsupport = ['sell', 'offer', 'offered', 'services', 'available', 'services offered', 'how long', 'how much']
requests = ['app', 'design', 'logo']

while CONVERSING:
	
	userInput= input(">>>Me: ")
	for greeting in greetings:
		if greeting in userInput.lower():
			random_greeting = random.choice(greetings)
			print(random_greeting)
			memory.append((userInput.lower(),random_greeting))
			break

	for question in questions:
		if question in userInput.lower():
			random_response = random.choice(responses)
			memory.append((userInput.lower(),random_response))
			print(random_response)
			break

	for verification in verifications:
		if verification in userInput.lower():
			random_response = random.choice(validations)
			memory.append((userInput.lower(),random_response))
			print(random_response)
			break

	for support in techsupport:
		if support in userInput.lower() and support is 'how long':
			random_response = 'Requests usually take up to x days depending on its scale.'
			memory.append((userInput.lower(), random_response))
			print(random_response)
			break

		elif support in userInput.lower() and support is 'how much':
			random_response = 'Requests usually cost at around x pesos depending on its scale.'
			memory.append((userInput.lower(), random_response))
			print(random_response)
			break

		elif support in userInput.lower():
			random_response = 'We take requests for an app, a design or a logo. What would you like?'
			memory.append((userInput.lower(), random_response))
			print(random_response)
			break

	for request in requests:
		if request in userInput.lower() and request is 'app':
			random_response = 'What kind of app? (Desktop-based or Web-based)'
			memory.append((userInput.lower(), random_response))
			print(random_response)
			userInput2= input(">>>Me: ")
			if 'desktop-based' in userInput2.lower():
				random_response = 'Alright. Request has been placed for a Desktop-based App. Please provide us with your email to confirm a few things.'
				memory.append((userInput2.lower(), random_response))
				print(random_response)
				userInput3 = input(">>>Me: ")
				if '@' in userInput3:
					random_response = 'We received the email "{}". Kindly wait awhile for details regarding your request.'.format(userInput3)
					memory.append((userInput3, random_response))
					print(random_response)
				else:
					print('Invalid Email!')

			elif 'web-based' in userInput2.lower():
				random_response = 'Alright. Request has been placed for a Web-based App. Please provide us with your email to confirm a few things.'
				memory.append((userInput.lower(), random_response))
				print(random_response)
				userInput3 = input(">>>Me: ")
				if '@' in userInput3:
					random_response = 'We received the email "{}". Kindly wait awhile for details regarding your request.'.format(userInput3)
					memory.append((userInput3, random_response))
					print(random_response)
				else:
					print('Invalid Email!')

			break


		elif request in userInput.lower() and request is 'design':
			random_response = 'What should the design look like?'
			memory.append((userInput.lower(), random_response))
			print(random_response)
			userInput2= input(">>>Me: ")
			random_response = 'Alright. Request has been placed for a Design. Please provide us with your email to confirm a few things.'
			memory.append((userInput2.lower(), random_response))
			print(random_response)
			userInput3 = input(">>>Me: ")
			if '@' in userInput3:
				random_response = 'We received the email "{}". Kindly wait awhile for details regarding your request.'.format(userInput3)
				memory.append((userInput3, random_response))
				print(random_response)
			else:
				print('Invalid Email!')

			break

		elif request in userInput.lower() and request is 'logo':
			random_response = 'What should the logo look like?'
			memory.append((userInput.lower(), random_response))
			print(random_response)
			userInput2= input(">>>Me: ")
			random_response = 'Alright. Request has been placed for a Logo. Please provide us with your email to confirm a few things.'
			memory.append((userInput2.lower(), random_response))
			print(random_response)
			userInput3 = input(">>>Me: ")
			if '@' in userInput3:
				random_response = 'We received the email "{}". Kindly wait awhile for details regarding your request.'.format(userInput3)
				memory.append((userInput3, random_response))
				print(random_response)
			else:
				print('Invalid Email!')

			break


	for thank in thanks:
		if thank in userInput.lower():
			random_response = "You're Welcome!"
			memory.append((userInput.lower(), random_response))
			print(random_response)
			CONVERSING = False
			break
		
for conversations in memory:
	print(conversations)

	
'''This can be extended with elif statements and eventually you will eventually have your very own slightly clever AI. Just make sure that the else statement is always at the bottom of your code'''