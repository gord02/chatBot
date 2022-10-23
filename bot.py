from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

from cleaner import remove_chat_metadata

chatBot = ChatBot("chatPot")
trainer = ListTrainer(chatBot)

file = "chat.txt"

chatData = remove_chat_metadata(file)
trainer.train(chatData)

exit_condition = ['exit', ":q", "exit"]

while True:
    query = input("> ")
    if query in exit_condition:
        break
    else:
        print( f"🪴 {chatBot.get_response(query)}")