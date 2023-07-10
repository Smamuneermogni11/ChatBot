from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot instance
chatbot = ChatBot('My Chatbot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot using the English corpus
trainer.train('chatterbot.corpus.english')

# Run the chatbot
while True:
    user_input = input('User: ')

    if user_input.lower() == 'quit':
        break

    response = chatbot.get_response(user_input)
    print('ChatBot:', response)
