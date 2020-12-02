from selenium import webdriver
import time
driver = webdriver.Chrome()  # Inicia o browser


url =  "https://msn.com"
driver.get(url)
                                              
escolhe_opcao = driver.find_element_by_xpath('//*[@id="main"]/div[6]/ul/li[3]/a/div/span[1]')
escolhe_opcao.click()
verificar_noticia = driver.find_elements_by_id('header-common')
time.sleep(10)
driver.quit()

