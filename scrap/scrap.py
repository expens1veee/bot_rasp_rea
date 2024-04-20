import selenium.webdriver
from selenium.webdriver.common.by import By
from rasp_rea_bot.scrap.linked_list import LinkedList
driver = selenium.webdriver.Chrome() # Firefox()

driver.get('https://rasp.rea.ru/?q=15.27д-мо02%2F23б#today')
driver.maximize_window()

all_cards = driver.find_elements(By.XPATH, '//*[@id="zoneTimetable"]/div')

str1 = ''
for row in all_cards:
    str1+=row.text

f = open ('rasp.txt','w')

f.write(str1)
f.close()

f = open ('rasp.txt','r')
rasp = f.read()
f.close()
# print(rasp)


lst = LinkedList()
# cf = ['1','2','3','4','5','6']
pn = ''
a = 0
for i in range (a,len(rasp)):
    if rasp[i] != 'В' and rasp[i+1] != 'Т':
            pn+=rasp[i]
    else:
        a = i
        break
# print(strr)
lst.InsertAtEnd(pn)
# lst.printLL()

vt =''
for i in range(a, len(rasp)):
    if rasp[i] != 'С' and rasp[i+2] != 'Е':
        vt+=rasp[i]
    else:
        a = i
        break

lst.InsertAtEnd(vt)
# lst.printLL()

sr =''
for i in range(a, len(rasp)):
    if rasp[i] != ' Ч' and rasp[i+2] != 'Т':
        sr+=rasp[i]
    else:
        a = i
        break

lst.InsertAtEnd(sr)
# lst.printLL()


ch =''
for i in range(a, len(rasp)):
    if rasp[i] != ' П' and rasp[i+1] != 'Я':
        ch+=rasp[i]
    else:
        a = i
        break
lst.InsertAtEnd(ch)


pt =''
for i in range(a, len(rasp)):
    if rasp[i] != ' С' and rasp[i+2] != 'У':
        pt+=rasp[i]
    else:
        a = i
        break
lst.InsertAtEnd(pt)


sub = ''
for i in range(a, len(rasp)):
        sub+=rasp[i]
lst.InsertAtEnd(sub)











