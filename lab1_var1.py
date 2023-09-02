


from selenium import webdriver
import webbrowser
from selenium.webdriver.common.by import By
import time
from urllib.parse import urlparse



driver = webdriver.Chrome()
url = "https://mcd.mosmetro.ru/"
driver.get(url)

time.sleep(0.5)

links1 = []
links2 = []

elems = driver.find_elements(By.XPATH, "//a[@href]")
for elem in elems:
    link = elem.get_attribute("href")
    parsed = urlparse(link)
    if parsed.netloc != "":
        links2.append(link)

if url in links2:
    links2.remove(url)

links2 = list(set(links2))

print('Первоначальный список:')
for i, link in enumerate(links2):
    print(str(i) + ' - ' + link)

links1 = links2[:]
links2.sort()

print('\t\t***')
print("Открытие сайтов в сортированном порядке:")
i = 0
for open_url in links2:
    time.sleep(2)
    driver.execute_script("window.open('" + str(open_url) + "');")
    print(str(i) + ' - ' + open_url)
    i += 1

print('\t\t***')
print('Закрытие сайтов в первоначальном порядке:')
driver.switch_to.window(driver.window_handles[0])
link = driver.current_url
driver.close()
print(0, ' - ', link)

#количество  открытых окон
n = len(links2)
for kk in range(0, len(links1)):
    for mm in range(0, n):
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[mm])
        link = driver.current_url
        # есть ли слэш в ссылке
        if link == links1[kk] \
            or (link[-1] == '/' and link[:-1] == links1[kk]):
            driver.close()
            n -= 1
            print(kk + 1, ' - ', link)
            break

driver.quit()
