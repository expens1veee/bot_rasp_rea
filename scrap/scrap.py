import selenium.webdriver
from selenium.webdriver.common.by import By
from rasp_rea_bot.scrap.linked_list import LinkedList
driver = selenium.webdriver.Chrome()  # Firefox()

driver.get('https://rasp.rea.ru/?q=15.27д-мо02%2F23б#today')
driver.maximize_window()

all_cards = driver.find_elements(By.XPATH, '//*[@id="zoneTimetable"]/div')

str_1 = ''.join(row.text for row in all_cards)

with open('rasp.txt', 'w') as f:
    f.write(str_1)
    f.close()

with open('rasp.txt', 'r') as f:
    rasp = f.read()
    f.close()


lst = LinkedList()
monday = ''
a = 0

for i in range(a, len(rasp)):
    if rasp[i] != 'В' and rasp[i+1] != 'Т':
        monday += rasp[i]
    else:
        a = i
        break

lst.InsertAtEnd(monday)


tuesday = ''
for i in range(a, len(rasp)):
    if rasp[i] != 'С' and rasp[i+2] != 'Е':
        tuesday += rasp[i]
    else:
        a = i
        break

lst.InsertAtEnd(tuesday)

wednesday = ''
for i in range(a, len(rasp)):
    if rasp[i] != ' Ч' and rasp[i+2] != 'Т':
        wednesday += rasp[i]
    else:
        a = i
        break

lst.InsertAtEnd(wednesday)


thursday = ''

for i in range(a, len(rasp)):
    if rasp[i] != ' П' and rasp[i+1] != 'Я':
        thursday += rasp[i]
    else:
        a = i
        break
lst.InsertAtEnd(thursday)


friday = ''

for i in range(a, len(rasp)):
    if rasp[i] != ' С' and rasp[i+2] != 'У':
        friday += rasp[i]
    else:
        a = i
        break
lst.InsertAtEnd(friday)


saturday = ''

for i in range(a, len(rasp)):
    saturday += rasp[i]
lst.InsertAtEnd(saturday)
