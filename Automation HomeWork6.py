import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://shemsvcollege.github.io/Trivia/")
driver.maximize_window()

start = driver.find_element(By.XPATH,'//*[@id="startB"]')
start.click()
# q1------------------------------------------------------------
question1 = driver.find_element(By.XPATH,'//*[@id="myform1"]/div/div/div/input')
question1.send_keys("how old are u ?")

next1 = driver.find_element(By.XPATH,'//*[@id="nextquest"]')
next1.click()


q1a1= driver.find_element(By.XPATH,'//*[@id="answers"]/div[1]/div[2]/input')
q1a1.send_keys("10")

q1a2= driver.find_element(By.XPATH,'//*[@id="answers"]/div[2]/div[2]/input')
q1a2.send_keys("11")



q1a3= driver.find_element(By.XPATH,'//*[@id="answers"]/div[3]/div[2]/input')
q1a3.send_keys("12")



q1a4= driver.find_element(By.XPATH,'//*[@id="answers"]/div[4]/div[2]/input')
q1a4.send_keys("13")


q1_correct = driver.find_element(By.XPATH, '//*[@id="answers"]/div[1]/div[1]/input')
q1_correct.click()

next2 = driver.find_element(By.XPATH,'//*[@id="nextquest"]')
next2.click()
# q2------------------------------------------------------------

question2 = driver.find_element(By.XPATH,'//*[@id="myform1"]/div/div/div/input')
question2.send_keys("how old are u ?")


next3 = driver.find_element(By.XPATH,'//*[@id="nextquest"]')
next3.click()

q2a1= driver.find_element(By.XPATH,'//*[@id="answers"]/div[1]/div[2]/input')
q2a1.send_keys("10")

q2a2= driver.find_element(By.XPATH,'//*[@id="answers"]/div[2]/div[2]/input')
q2a2.send_keys("11")



q2a3= driver.find_element(By.XPATH,'//*[@id="answers"]/div[3]/div[2]/input')
q2a3.send_keys("12")



q2a4= driver.find_element(By.XPATH,'//*[@id="answers"]/div[4]/div[2]/input')
q2a4.send_keys("13")


q2_correct = driver.find_element(By.XPATH, '//*[@id="answers"]/div[1]/div[1]/input')
q2_correct.click()

next4 = driver.find_element(By.XPATH,'//*[@id="nextquest"]')
next4.click()
# q3------------------------------------------------------------

question3 = driver.find_element(By.XPATH,'//*[@id="myform1"]/div/div/div/input')
question3.send_keys("how old are u ?")


next5 = driver.find_element(By.XPATH,'//*[@id="nextquest"]')
next5.click()

q3a1= driver.find_element(By.XPATH,'//*[@id="answers"]/div[1]/div[2]/input')
q3a1.send_keys("10")

q3a2= driver.find_element(By.XPATH,'//*[@id="answers"]/div[2]/div[2]/input')
q3a2.send_keys("11")



q3a3= driver.find_element(By.XPATH,'//*[@id="answers"]/div[3]/div[2]/input')
q3a3.send_keys("12")



q3a4= driver.find_element(By.XPATH,'//*[@id="answers"]/div[4]/div[2]/input')
q3a4.send_keys("13")


q3_correct = driver.find_element(By.XPATH, '//*[@id="answers"]/div[1]/div[1]/input')
q3_correct.click()

next6 = driver.find_element(By.XPATH,'//*[@id="nextquest"]')
next6.click()

# -------------------play---------------------------------------


play = driver.find_element(By.XPATH,'//*[@id="secondepage"]/center/button[1]')
play.click()



# q1

q1= driver.find_element(By.XPATH,'//*[@id="2"]/input[1]')
q1.click()


next9 = driver.find_element(By.XPATH,'//*[@id="btnnext"]')
next9.click()

# q2

q2= driver.find_element(By.XPATH,'//*[@id="1"]/input[1]')
q2.click()


next10 = driver.find_element(By.XPATH,'//*[@id="btnnext"]')
next10.click()

# q3

q3= driver.find_element(By.XPATH,'//*[@id="0"]/input[1]')
q3.click()


next11 = driver.find_element(By.XPATH,'//*[@id="btnnext"]')
next11.click()

time.sleep(100)