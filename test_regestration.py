
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

mail = "anjanajju027@gmail.com"
password = "Govindha1@"
onetimepass = "264200"

driver = webdriver.Chrome()
driver.implicitly_wait(3)

driver.get("https://proschool.ai/")
#print(driver.title)
driver.find_element(By.XPATH,"//a[contains(text(),'Login / Sign Up')]").click()
#print("sign up button")
wait = WebDriverWait(driver, 3)
driver.find_element(By.XPATH,"//*[@id='root']/div[1]/div/div/form/div/div[6]/span/a").click()
#print("sign up")
driver.find_element(By.XPATH,"//button[contains(text(),'Teacher')]").click()
#print("teacher")
driver.find_element(By.XPATH,"//input[@name='email']").send_keys(mail)
driver.find_element(By.XPATH,"//input[@name='password']").send_keys(password)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
#print("REGISTER")
modal = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@role='dialog']")))

#print("visible")
driver.find_element(By.XPATH, "//button[contains(text(),'Confirm')]").click()
#print("confirm registration")

#//input[@autocomplete='one-time-code']

otp = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@autocomplete='one-time-code']")))
#print("otp seen")
otp_inputs = wait.until(EC.presence_of_all_elements_located(
    (By.CSS_SELECTOR, 'input[autocomplete="one-time-code"]')
))
assert len(otp_inputs) >= 6

for i, digit in enumerate(onetimepass):
    otp_inputs[i].send_keys(digit)

print("enterd otp")
driver.find_element(By.XPATH, "//button[contains(text(),'Confirm code')]").click()



#note: Onetime password are changed for every we need to take care for further steps
