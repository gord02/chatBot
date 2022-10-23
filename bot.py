from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatBot = ChatBot("chatPot")

trainer = ListTrainer(chatBot)

# training data, statement and its accepted response
trainer.train([
    "Hi",
    "Welcome, friend 👀",
])
trainer.train([
    "Are you a plant?",
    "No, I'm the pot below the plant!",
])

exit_condition = ['exit', ":q", "exit"]

while True:
    query = input("> ")
    if query in exit_condition:
        break
    else:
        print( f"🪴 {chatBot.get_response(query)}")