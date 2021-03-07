from datetime import datetime
import telegram_send as ts
import random
import time


def send(message):
    ts.send(messages=[str(message)])


def read_messages(path):
    with open(path, 'r') as f:
        return f.readlines()


morning_greetings = read_messages('greetings/morning.txt')
night_greetings = read_messages('greetings/night.txt')
food_greetings = read_messages('greetings/food.txt')
walk_greetings = read_messages('greetings/walk.txt')


def mainloop():

    for _ in range(1200):

        now = datetime.now()
        current_time = str(now.strftime('%H:%M'))

        if current_time == '07:00':
            send(random.choice(morning_greetings))

        elif current_time == '08:05':
            send(random.choice(food_greetings))

        elif current_time == '13:05':
            send(random.choice(walk_greetings))

        elif current_time == '18:00':
            send(random.choice(food_greetings))

        elif current_time == '18:05':
            send(random.choice(food_greetings))

        elif current_time == '21:00':
            send(random.choice(night_greetings))

        elif current_time == '21:01':
            exit()

        print('sleeping...')
        time.sleep(60)


mainloop()
