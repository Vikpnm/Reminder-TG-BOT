import telebot
import datetime
import time
import schedule

# Bot Token
bot = telebot.TeleBot("YOUR_BOT_TOKEN_HERE")
UserID = "Your_USER_ID" #Your User Id,you can have it @chatIDrobot

# Messages
Mesenge1 = "Yourmsg1"
Mesenge2 = "Msg2"
Mesenge3 = "Msg3"

# Get current time
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("current time:", current_time)  # print current time


# Function to send message 1
def send_msg_1():
    bot.send_message(UserID, Mesenge1)
    print("Message №1 has been sent")


# Function to send message 2
def send_msg_2():
    bot.send_message(UserID, Mesenge2)
    print("Message №2 has been sent")


# Function to send message 3
def send_msg_3():
    bot.send_message(UserID, Mesenge3)
    print("Message №3 has been sent")


# Function to check time AND START tasks
def check_time():
    # Schedule message 1 to be sent every day at 10:10
    schedule.every().day.at("10:10").do(send_msg_1)

    # Schedule message 3 to be sent every Monday at 10:10
    schedule.every().monday.at("10:10").do(send_msg_3)

    # Schedule message 2 to be sent every 1 minute
    schedule.every(1).minutes.do(send_msg_2)


check_time()  # call function

# Keep the program running
while True:
    schedule.run_pending()
    time.sleep(1)
