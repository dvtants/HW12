"""
д/з #12 від 05.10.2023 р.:
1. Знайти будь-який сайт, де є елементи, які потрібно очікувати (або з’являються з затримкою, або неактивні кнопки,
які згодом стають активними, або якісь повідомлення, які зникають, тощо), та написати автотест,
де використати методи явного очікування.
2. Створити новий репо, в якому буде скрипт із задачи №1. Вимоги до репо:
посилання на репо коректне, репо публічний, при переході за посиланням, відкриваєтсья сторінка з репо.
в репо є опис у файлі readme
є хоча б один коміт (а краще два), який грамотно описує те, що було змінено.
УВАГА! Відповідь на дане д/з має бути лише у вигляді посилання на репо в github.
Жодних файлів скриптів та архівів надсилати НЕ потрібно.
"""

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




