from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tkinter import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


s = Service(ChromeDriverManager().install())

print("""\nPlease Enter date in DD-MMM-YYYY Format\n\nExample: 14-OCT-2022\n\nNOTE-----"DO NOT CLOSE BROWSER WINDOW BEFORE COPYING DATA"\n """)
uname1 = input("Enter userid: ")
pswd = input("Enter password: ")
fromDate = input('Enter From date: ')
ToDate = input('Enter To date: ')


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(service=s, options=options)
driver.set_window_size(1024, 600)
driver.maximize_window()
driver.get('https://www.shcilestamp.com/eStampIndia/useradmin/UserAdminLoginServlet?rDoAction=LoadLoginPage')
driver.implicitly_wait(12)
driver.find_element(By.CLASS_NAME, 'close-btn').click()
USERid = driver.find_element(
    By.XPATH, '/html/body/form/table/tbody/tr[1]/td/table[3]/tbody/tr/td/table/tbody/tr[3]/td[2]/input')
USERid.send_keys(uname1)
Password = driver.find_element(
    By.XPATH, '/html/body/form/table/tbody/tr[1]/td/table[3]/tbody/tr/td/table/tbody/tr[4]/td[2]/input')
Password.send_keys(pswd)
Capcha = driver.find_element(By.XPATH, '//*[@id="searchjcaptcha"]').click()
try:
    WebDriverWait(driver, 120).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/form/b/div/table/tbody/tr[2]/td[1]/input')))
    checkbtn = driver.find_element(
        By.XPATH, '/html/body/form/b/div/table/tbody/tr[2]/td[1]/input').click()
    remove = driver.find_element(
        By.XPATH, '/html/body/form/b/table/tbody/tr/td[1]/div/input').click()
except:
    print('Remove not found. Skipping...')

element = WebDriverWait(driver, 120).until(
    EC.presence_of_element_located((By.LINK_TEXT, "Create Submission")))
driver.find_element(By.LINK_TEXT, "Search Certificate").click()
try:
    driver.implicitly_wait(3)
    driver.switch_to.alert.accept()
except:
    print('Conquered Alert:)\n')

from_date = driver.find_element(
    By.XPATH, '/html/body/table/tbody/tr[1]/td/table[3]/tbody/tr[1]/td[2]/form/table/tbody/tr[3]/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/table/tbody/tr/td[1]/input')
from_date.send_keys(fromDate)

to_date = driver.find_element(
    By.XPATH, '/html/body/table/tbody/tr[1]/td/table[3]/tbody/tr[1]/td[2]/form/table/tbody/tr[3]/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td[5]/table/tbody/tr/td[1]/input')
to_date.send_keys(ToDate)

search_btn = driver.find_element(
    By.XPATH, '/html/body/table/tbody/tr[1]/td/table[3]/tbody/tr[1]/td[2]/form/table/tbody/tr[3]/td/table/tbody/tr[2]/td/table/tbody/tr/td[1]/input').click()


def NEXTSA():
    driver.execute_script('''
    ayu = document.getElementsByTagName('font')[02].childNodes
    four = ayu[ayu.length-4].click()
    ''')


def myloop_0():
    driver.execute_script(
        '''JAC = 1
    while (JAC <= document.getElementsByClassName('td-text').length-6){
        a = document.getElementsByClassName('td-text')[`${JAC}`].id = `b${JAC}`; float_n = parseFloat(a.replaceAll(", ", ""));
        JAC += 7
    }''')

    driver.execute_script(
        '''JAC1 = 0
    while (JAC1 <= document.getElementsByClassName('td-text').length-7){
        b = document.getElementsByClassName('td-text')[`${JAC1}`].id = `a${JAC1}`
        JAC1 += 7
    }''')


def my_loop_1():
    lastee = driver.execute_script(
        '''return newEle = document.getElementsByClassName('td-text').length-5
    
    ''')
    lastel = int(lastee)

    i = 1
    while i <= lastel:

        ayu = driver.find_element(By.ID, f"b{i}").get_attribute("innerText")
        a = driver.execute_script(
            "return Anu = parseInt(document.getElementsByTagName('b')[02].innerText)")
        ayu = float(ayu.replace(',', ''))
        if ayu > 500:
            nis = (driver.find_element(
                By.ID, f"a{i-1}").get_attribute("innerText")).replace('-', '')
            clickOnCert = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.ID, f"a{i-1}"))).click()
            panCopyId = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.ID, "panCopyCollected")))
            purBy = driver.execute_script(
                "return pBy = document.getElementsByTagName('div')[10].innerText")
            mydate = driver.execute_script(
                "return jdate = ((document.getElementsByTagName('div')[8].innerText).substr(0, 11)).replaceAll('-', '/')")
            fmN = driver.execute_script(
                "return fiMn = document.getElementsByClassName('txt-body')[35].innerText")
            SmN = driver.execute_script(
                "return SeMn = document.getElementsByClassName('txt-body')[37].innerText")
            driver.execute_script(
                "document.getElementsByClassName('button')[0].click()")
            for my_loop in range(a-1):
                NEXTSA()

            myloop_0()

            show_greater = print(
                f"{nis} -  - {mydate} - {ayu} - {purBy} - {SmN}{fmN}")
        i += 7


def my_loop_2():
    driver.execute_script(
        '''j = 1
    while (j <= 3){
        ayu = document.getElementsByTagName('font')[02].childNodes
        four = ayu[ayu.length-4].click()
        j += 1
    }
    ''')


ak = 1
while ak < 200:
    myloop_0()
    my_loop_1()
    my_loop_2()
    ak += 1