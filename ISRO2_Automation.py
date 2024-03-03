from selenium import webdriver 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def scroll():
 for i in range(15):
            driver.execute_script(" window.scrollBy(0, 200);")
            time.sleep(0.5)
            #print("scrolling time: " + str(i))
 for i in range(15):
            driver.execute_script(" window.scrollBy(0, -200);")
            time.sleep(0.5)
            print("scrolling time: " + str(i)) 
            
 driver.back()
 driver.back()
 time.sleep(1)
 #abc()

           
#driver = webdriver.Chrome('C:\Users\This PC\AppData\Local\Programs\Python\Python311\Scripts')

Options = Options()
Options.add_experimental_option("detach", True)




driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=Options)
driver.maximize_window()
def initialize_browswe():
 driver.get("https://www.isro.gov.in/")
 
driver.execute_script("window.scrollBy(0,2000)","")

initialize_browswe() 


#driver.find_element(by=By.NAME, value='search_query').send_keys("Technical Gurji")
#driver.find_elements(by=By.XPATH, value='//*[@id="menu"]/li[3]/a/span')[0].click()
#links = driver.find_elements("xpath",'//*[@id="search-icon-legacy"]')
#for link in links:
        #link.click()
        #break

#subscription = driver.find_element(by=By.CLASS_NAME, value='')
#subscription.click()
time.sleep(1)
driver.back()
driver.back()
time.sleep(1)
driver.forward()
driver.forward()
time.sleep(1)
driver.refresh()
#driver.find_elements(by=By.XPATH, value='//*[@id="menu"]/li[3]/a/span')[0].click()
def abc():
 for i in range(2):
  driver.find_element(by=By.LINK_TEXT, value='About').click()
  time.sleep(1)
  driver.find_element(by=By.LINK_TEXT, value='Activities').click()
  time.sleep(1)
  driver.find_element(by=By.LINK_TEXT, value='Services').click()
  time.sleep(1)
  driver.find_element(by=By.LINK_TEXT, value='Programmes').click()
  time.sleep(1)
  driver.find_element(by=By.LINK_TEXT, value='Resources').click()
  time.sleep(1)

  driver.find_element(by=By.LINK_TEXT, value='Engage with Us').click()
  time.sleep(1)
  driver.find_element(by=By.LINK_TEXT, value='Activities').click()
  time.sleep(2)
  driver.find_element(by=By.LINK_TEXT, value='Launchers').click()

  driver.execute_script("window.scrollBy(0,1000)","")
  time.sleep(2)
  driver.find_element(by=By.LINK_TEXT, value='Geosynchronous Satellite Launch Vehicle (GSLV)').click()

  scroll()
 #abc() 
abc()


    
#driver.find_elements(by=By.CLASS_NAME, value='style-scope ytd-channel-name')[0].click()    



