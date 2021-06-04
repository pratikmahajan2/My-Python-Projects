from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C:\\Users\\Pratik Mahajan\\Documents\\GitHub\\My_Python_Projects\\Complex Projects\\Webdriver\\chromedriver.exe")
driver.get("https://web.whatsapp.com/")

print("Please scan the code to login")
action=input("Please press enter once done")

contact = "Priya Gupta"
operators = ['+','-','X','*','/']
operands=[]
play = 'Yes'
#msg = input("Enter the text you want to send: ")

searchBox = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]")
searchBox.send_keys(contact)
searchBox.send_keys(Keys.ENTER)

#msgBox = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
#msgBox.send_keys(msg)
#msgBox.send_keys(Keys.ENTER)
receivedMsg = driver.find_elements_by_css_selector("span._3Whw5.selectable-text.invisible-space.copyable-text")
msgs=[temp.text for temp in receivedMsg]
print(msgs[-1])
operation=str(msgs[-1])

for items in operation:
    print(items)
    if items in operators:
        print(items)
        oper = items
        break

oper1 = operation.split(oper)

if (items in operators) == True:
   if items == '+':
      result = int(oper1[0]) + int(oper1[1])
   if items == '-':
      result = int(oper1[0]) - int(oper1[1])
   if items == '*' or items.lower() == 'x':
      result = int(oper1[0]) * int(oper1[1])
   if items == '/':
      result = float(int(oper1[0]) / int(oper1[1]))

answer = "result is: "+str(result)

msgBox = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
msgBox.send_keys(answer)
msgBox.send_keys(Keys.ENTER)

time.sleep(5)

driver.quit()