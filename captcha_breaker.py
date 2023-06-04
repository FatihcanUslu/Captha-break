from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

#google lens adresi
website='https://www.google.com.tr/imghp?hl=tr&tab=ri&authuser=0&ogbl'
#kodun çalışması için selenium uyumlu chromedriver.exe indirilmeli
path='webdriver/chromedriver.exe'
#denenecek olan fotoğrafın yolu
captcha_path=os.path.abspath("deneme.png")

def driver_create():
    service=Service(path)
    chrome_options = Options()#açılan web sitede iş bittikten sonra kapanmama hatası olduğu için kullanıldı
    chrome_options.add_experimental_option("detach", True)
    driver=webdriver.Chrome(service=service,options=chrome_options)
    return driver


driver=driver_create()
driver.get(website)#istenilen web site adresine git
driver.find_element(By.XPATH, '//div[@jscontroller="lpsUAf"]').click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.DV7the[jsname="tAPGc"]')))
file_element = driver.find_element(By.XPATH, '//input[@type="file"]')
file_element.send_keys(captcha_path)


#Resim yüklenene kadar bekler
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[jsaction="contextmenu:ha96zc;O70qEb:r2DH1b;GIdK5c:HpaDwf;"]')))
#Metin butonuna bas
driver.find_element(By.CSS_SELECTOR, 'button#ucj-4.VfPpkd-rOvkhd-jPmIDe.VfPpkd-rOvkhd-jPmIDe-OWXEXe-ssJRIf').click()
#Tüm metni seç butonuna bas
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[@class="VfPpkd-vQzf8d" and text()="Tüm metni seç"]')))
driver.find_element(By.XPATH, '//span[@class="VfPpkd-vQzf8d" and text()="Tüm metni seç"]').click()
#Sonucu elde et
captha_answer=driver.find_element(By.XPATH, '//div[@class="wCgoWb"]').text
print(captha_answer)
driver.quit()





