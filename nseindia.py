from selenium import webdriver
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Запуск веб-драйвера
driver = webdriver.Chrome()

# Открытие веб-сайта
driver.get("https://www.nseindia.com")

# Наведение курсора на элемент "MARKET DATA"
market_data = driver.find_element(By.ID, "link_2")
webdriver.ActionChains(driver).move_to_element(market_data).perform()
# Клик по "Pre-Open Market"
pre_open_market = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.LINK_TEXT, "Pre-Open Market")))
pre_open_market.click()
# Ожидание загрузки страницы
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//table[@id='livePreTable']/tbody/tr")))

# Получение данных и запись в CSV файл
with open('final_prices.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Имя', 'Цена'])
    rows = driver.find_elements(By.XPATH, "//table[@id='livePreTable']/tbody/tr")
    for row in rows:
        name = row.find_element(By.XPATH, ".//td[2]").text
        price = row.find_element(By.XPATH, ".//td[3]").text
        writer.writerow([name, price])
with open('final_prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Имя', 'Цена'])
    rows = driver.find_elements(By.XPATH, "//table[@id='livePreTable']/tbody/tr")
    for row in rows:
        name = row.find_element(By.XPATH, ".//td[2]").text
        price = row.find_element(By.XPATH, ".//td[3]").text
        writer.writerow([name, price])
# Закрытие веб-драйвера
driver.quit()