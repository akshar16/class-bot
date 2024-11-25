
#import timeTable
import time
import info
from main import driver


def joinFirst():
    driver.get(info.firstClassLink)
    time.sleep(60) #seconds
    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(1800)
    driver.quit()

def joinSecond():
    driver.get(info.secondClassLink)
    time.sleep(60) #seconds
    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(1800)
    driver.quit()

def joinThird():
    driver.get(info.thirdClassLink)
    time.sleep(60) #seconds
    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(1800)
    driver.quit()

def joinFourth():
    driver.get(info.fourthClassLink)
    time.sleep(60) #seconds
    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(1800)
    driver.quit()

def joinFifth():
    driver.get(info.fifthClassLink)
    time.sleep(60) #seconds
    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(1800)
    driver.quit()

def joinSixth():
    driver.get(info.sixthClassLink)
    time.sleep(60) #seconds
    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(1800)
    driver.quit()

def joinSeventh():
    driver.get(info.seventhClassLink)
    time.sleep(60) #seconds
    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(1800)
    driver.quit()

def joinEighth():
    driver.get(info.eighthClassLink)
    time.sleep(60) #seconds
    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(1800)
    driver.quit()

def joinNineth():
    driver.get(info.ninthClassLink)
    time.sleep(60) #seconds
    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(1800)
    driver.quit()
