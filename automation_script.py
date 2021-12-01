from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import clipboard

driver = webdriver.Chrome(r"C:\Users\Hritik Dev\selenium_testing\Browsers\chromedriver.exe")
actions = ActionChains(driver)

driver.maximize_window()
#print(time.time())
start_time=time.time()
for i in range(60):
    #print(time.time())
    print("--- %s seconds ---" % (time.time() - start_time))
    time.sleep(1)
driver.implicitly_wait(60)


driver.get("http://ec2-54-226-47-239.compute-1.amazonaws.com/lab/lab")
print("checkpoint1    Entered the website-------------------------------------------------")
time.sleep(3)

driver.find_element_by_name("password").send_keys("fc9978327b83b906b8bb5ef5ec579adf")
print("checkpoint2    Entered the token---------------------------------------------------")

#time.sleep(10)
#driver.find_element_by_class_name("btn btn-default").send_keys(Keys.ENTER)
driver.find_element(By.ID,"login_submit").send_keys(Keys.ENTER)
print("checkpoint3    Done the login -----------------------------------------------------")
time.sleep(7)#10

#h= driver.find_element_by_class_name(r"jp-DirListing-itemIcon fm5u5yq")
#ele= driver.find_element_by_xpath('//*[@id="Layer_1"]')
ele=driver.find_element(By.ID,"Layer_1")
#print(ele)
##print(h)
#for aa in ele:
#    print(aa.text)
#time.sleep(2)
#yo=actions.context_click(ele).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.RETURN).perform()


hehe=actions.context_click(ele)
hehe.perform()
time.sleep(.7)

hehe.send_keys(Keys.ARROW_UP).perform()
time.sleep(.7)

hehe.send_keys(Keys.ARROW_UP).perform()
time.sleep(.7)

hehe.send_keys(Keys.ARROW_UP).perform()
time.sleep(.7)
hehe.send_keys(Keys.RETURN).perform()

var_text=clipboard.paste()


#driver.execute_script("window.open('https://facebook.com', 'new_window')") # TO CHANGE TAB
#driver.title



p = driver.current_window_handle
chwd = driver.window_handles
for w in chwd:
    if(w!=p):
        driver.switch_to.window(w)
    break
driver.get(var_text)
# we can download check


time.sleep(180) # this time , we need to be careful
driver.close()