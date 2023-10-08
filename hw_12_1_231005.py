from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.implicitly_wait(1)
browser.get("https://rozetka.com.ua/ua") # Заходимо на сайт Розетка
chat = browser.find_element(By.XPATH, '//span[@class="exponea-close-cross"]').click() # Закриваємо віконце що спливає
slider_4 = WebDriverWait(browser, 6).until(
    EC.visibility_of_element_located((By.XPATH, '//ul[@class="simple-slider__list ng-star-inserted"]/li[4]'))
) # Чекаємо 6 секунд доки не з'явиться четвертий елемент в каруселі реклами. Стає видимим.
browser.quit()




