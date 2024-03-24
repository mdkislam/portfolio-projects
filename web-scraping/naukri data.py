from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

driver= webdriver.Firefox()
url= "https://www.naukri.com/naukri-jobs?glbl_qcrc=1019%2C1020&functionAreaIdGid=3"
driver.get(url)

# get number of pages in the website:
time.sleep(2)
total_jobs = int(driver.find_element(By.XPATH,"//span[contains(@class,'count-string')]").text.split(' ')[-1])
jobs_per_page= int(driver.find_element(By.XPATH,"//span[contains(@class,'count-string')]").text.split(' ')[2])
total_pages= total_jobs//jobs_per_page

title= []
row2= []
row3 = []
job_desc = []
row5 = []
row6 =[]
web_link= []



current_page= 1
while current_page <=total_pages:
    time.sleep(3)
    job_detail_elments = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class,'sjw__tuple')]")))

    for element in job_detail_elments:
        title.append(WebDriverWait(element,10).until(EC.presence_of_element_located((By.XPATH,".//div[contains(@class,'row1')]"))).text)
        row2.append(WebDriverWait(element,10).until(EC.presence_of_element_located((By.XPATH, ".//div[contains(@class,'row2')]"))).text)
        job_desc.append(WebDriverWait(element,10).until(EC.presence_of_element_located((By.XPATH, ".//div[contains(@class,'row4')]"))).text)
        row3.append(WebDriverWait(element,10).until(EC.presence_of_element_located((By.XPATH, ".//div[contains(@class,'row3')]"))).text)
        row5.append(WebDriverWait(element,10).until(EC.presence_of_element_located((By.XPATH, ".//div[contains(@class,'row5')]"))).text)
        row6.append(WebDriverWait(element,10).until(EC.presence_of_element_located((By.XPATH, ".//div[contains(@class,'row6')]"))).text)
        web_link.append(WebDriverWait(element,10).until(EC.presence_of_element_located((By.XPATH,".//div[contains(@class,'row1')]//a"))).get_attribute('href'))
    current_page += 1
    next_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'styles_btn-secondary__2AsIP') and contains(span, 'Next')]"))
    )
    # Click the "Next" button using JavaScript
    driver.execute_script("arguments[0].click();", next_button)
    
driver.close()

df= pd.DataFrame({
    'title':title,
    'row2':row2,
    'row3':row3,
    'job_description':job_desc,
    'row5':row5,
    'row6':row6,
    'link':web_link
})

df.to_csv('naukri data (rogue).csv')
