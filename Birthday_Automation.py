from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.options import Options 
from selenium.common.exceptions import TimeoutException 
from selenium.webdriver.common.keys import Keys 
import time 
  
chrome_options = webdriver.ChromeOptions() 
  
prefs = {"profile.default_content_setting_values.notifications": 2} 
chrome_options.add_experimental_option("prefs", prefs) 
browser = webdriver.Chrome("chromedriver.exe") 
  
browser.get('https://www.facebook.com/') 
  
username = "navanshu004@gmail.com"

password = "XXXXXXXXXXX"
    
element = browser.find_elements_by_xpath('//*[@id ="email"]') 
element[0].send_keys(username) 
  
print("Username Entered") 
  
element = browser.find_element_by_xpath('//*[@id ="pass"]') 
element.send_keys(password) 
  
print("Password Entered") 
  
log_in = browser.find_elements_by_id('loginbutton') 
log_in[0].click() 
  
print("Login Successfull") 
browser.get('https://www.facebook.com/events/birthdays/')  
feed = 'Happy Birthday ! Wish you a great Year ahead'
  
element = browser.find_elements_by_xpath("//*[@class ='enter_submit\ 
       uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea\ 
                  inlineReplyTextArea mentionsTextarea textInput']") 
  
cnt = 0
  
for el in element: 
    cnt += 1
    element_id = str(el.get_attribute('id')) 
    XPATH = '//*[@id ="' + element_id + '"]'
    post_field = browser.find_element_by_xpath(XPATH) 
    post_field.send_keys(feed) 
    post_field.send_keys(Keys.RETURN) 
    print("Birthday Wish posted for friend" + str(cnt))  
browser.close()