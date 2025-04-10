from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# ChromeDriver yolu
service = Service("C:/Users/user/Desktop/chromedriver.exe")  
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.get("https://www.trendyol.com/")
driver.maximize_window()

driver.find_element(By.ID,"Combined-Shape").click()
driver.find_element(By.ID,"onetrust-reject-all-handler").click()
# driver.find_element(By.XPATH,"//*[@id='navigation-wrapper']/nav/div/div[2]/div/span").click()
# time.sleep(10)
driver.find_element(By.XPATH,"//*[@id='navigation-wrapper']/nav/ul/li[2]").click()
driver.find_element(By.XPATH,"//*[@id='browsing-gw-homepage']/div/div[1]/div[1]/div/article[3]/div/div/div[1]/div/div/a").click()
time.sleep(10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.execute_script("window.scrollTo(0, 0);")
#driver.execute_script("window.scrollTo(0, 0);")

uruns_list=driver.find_elements(By.CLASS_NAME,"p-card-content-wrapper")
urun_titles = []

for urun in uruns_list:
    urun_titles.append(urun.text)

# İş ilanlarını dosyaya kaydet
with open("urun.txt", "w", encoding="UTF-8") as file:
    for urun in urun_titles:
        file.write(urun + "\n\n")

driver.quit()
