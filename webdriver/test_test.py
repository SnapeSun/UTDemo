import requests,time
from selenium import webdriver

#coding=utf-8
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://login.sina.com.cn/signup/signin.php?entry=sso')
driver.implicitly_wait(10)
# write=driver.find_element_by_id("kw")
# write.send_keys('hello')
# driver.find_element_by_id("su").click()
cookies = driver.get_cookies()
print(cookies)

write_username = driver.find_element_by_id("username")
write_username.send_keys('1171541089@qq.com')
write_pwd = driver.find_element_by_id("password")
write_pwd.send_keys("snape.12")
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/form/div[2]/div/ul/li[7]/div[1]/input").click()
driver.implicitly_wait(30)
driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/ul/li[1]/a/span[1]").click()
driver.implicitly_wait(2)
editinput  = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div[2]/div[1]/div[1]/div/div[2]/textarea")
editinput.clear()
editinput.send_keys('auto_send_message！')
send_word = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div[2]/div[1]/div[1]/div/div[3]/div[1]/a")
send_word.click()
