import requests

from telebot import TeleBot

TOKEN = "BOT_TOKEN"
api_key = "NtA1EtQ68zB7gPAXBXIOkUAT5t3xZZvo"
mybot = TeleBot(TOKEN)

@mybot.message_handler(commands=['start'])
def start(message):
    mybot.send_message(message.chat.id, "Welcome to NY Times")

@mybot.message_handler(commands=['news'])
def news(message):
      api_url = f"https://api.nytimes.com/svc/mostpopular/v2/emailed/7.json?api-key={api_key}"
      response = requests.get(api_url)
      if response.status_code == 200:
          data = response.json()
          text = ""
          for i, news_item in enumerate(data["results"]):
            text += f"{i+1}. {news_item['title']}\n{news_item['url']}\n\n"
      mybot.send_message(message.chat.id, text)
mybot.polling()