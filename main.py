import time
from re import T

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

import random


class Boot:
    def __init__(self, doc):

        self.cnpj = doc
        options = Options()
        # options.add_argument("headless")
        self.browser = webdriver.Chrome(
            options=options, executable_path='./chromedriver')
        self.browser.maximize_window()

    def login(self):
        print('entrando no site')
        browser = self.browser
        browser.get("http://www8.receita.fazenda.gov.br/SimplesNacional/Aplicacoes/ATSPO/pgmei.app/Identificacao")
        # try:
        #     time.sleep(10)
        #     login_button = browser.find_element_by_xpath(
        #         "//a[@href='/accounts/login/?source=auth_switcher']"
        #     )
        #     login_button.click()
        # except:
        #     print('já estamos na página de login')
        #     pass
        # time.sleep(10)
        # user_element = browser.find_element(By.CSS_SELECTOR,
        #     "input[name='username']")
        # user_element.clear()
        # time.sleep(random.randint(4, 6))
        # user_element.send_keys(self.username)
        # time.sleep(random.randint(4, 6))
        # password_element = browser.find_element(By.XPATH,
        #     "//input[@name='password']")
        # password_element.clear()
        # password_element.send_keys(self.password)
        # time.sleep(random.randint(4, 6))
        # password_element.send_keys(Keys.RETURN)
        # try:
        #     time.sleep(random.randint(4, 6))
        #     ativar_notificacao = browser.find_element(By.XPATH,
        #                                               "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]")
        #     ativar_notificacao.click()
        #     time.sleep(5)
        # except Exception as e:
        #     print(e)
        #     pass



cnpj = '31249348000140'

executar = Boot(cnpj)
executar.login()


