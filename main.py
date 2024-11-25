import datetime
from selenium import webdriver
import schedule
import time
import join
import info

# Initialize the driver for Selenium
driver = webdriver.Chrome('add  your chromedriver here')

# Get the current date and time
e = datetime.datetime.now()

# Define the joinClass function to schedule Zoom classes
def joinClass():
    schedule.every().day.at(info.firstClass).do(join.joinFirst)
    schedule.every().day.at(info.secondClass).do(join.joinSecond)
    schedule.every().day.at(info.thirdClass).do(join.joinThird)
    schedule.every().day.at(info.fourthClass).do(join.joinFourth)
    schedule.every().day.at(info.fifthClass).do(join.joinFifth)
    schedule.every().day.at(info.sixthClass).do(join.joinSixth)
    schedule.every().day.at(info.seventhClass).do(join.joinSeventh)
    schedule.every().day.at(info.eighthClass).do(join.joinEighth)
    schedule.every().day.at(info.ninthClass).do(join.joinNineth)

    while True:
        schedule.run_pending()
        time.sleep(1)  # Sleep for 1 second before checking the schedule again

# Get the current day and print it
day = e.strftime("%a")
print(day)

# Start the class schedule
joinClass()
