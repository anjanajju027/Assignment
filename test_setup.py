import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

mail = "anjanajju027@gmail.com"
password = "Govindha1@"
onetimepass = "264200"

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("https://proschool.ai/")
#print(driver.title)
driver.find_element(By.XPATH,"//a[contains(text(),'Login / Sign Up')]").click()
wait = WebDriverWait(driver, 1)
#driver.find_element(By.XPATH,"//*[@id='root']/div[1]/div/div/form/div/div[6]/span/a").click()
driver.find_element(By.XPATH,"//button[contains(text(),'Teacher')]").click()
driver.find_element(By.XPATH,"//input[@name='email']").send_keys(mail)
driver.find_element(By.XPATH,"//input[@name='password']").send_keys(password)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
#print("login successfully")
setup = WebDriverWait(driver, 10).until(
    ec.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Setup Profile')]")))
#print("visible")
driver.find_element(By.XPATH,"//button[contains(text(),'Setup Profile')]").click()
#print("setup")
driver.find_element(By.XPATH,"(//input[@name='name'])[1]").send_keys("Anjan")
dropdown_element = driver.find_element(By.NAME, "title")
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("Mr.")
#time.sleep(1)
#driver.find_element(By.XPATH,"(//label[contains(text(),'Location')])[4]").send_keys("Hyderabad")
english_option = driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div/a[1]")
driver.execute_script("arguments[0].click();", english_option)
#print("english option")
#time.sleep(1)
gender_dropdown = driver.find_element(By.ID, "gendar-select-feild")
select = Select(gender_dropdown)
select.select_by_visible_text("Male")
#print("gender dropdown")
#########################################hyderbad
location_input = driver.find_element(By.CLASS_NAME, "pac-target-input")
location_input.clear()
location_input.send_keys("Hyderabad")

# Wait for the suggestion that contains "Telangana"
wait4 = WebDriverWait(driver, 10)
suggestion = wait4.until(ec.visibility_of_element_located(
    (By.XPATH, "//div[contains(@class, 'pac-item')][.//span[contains(text(), 'Telangana')]]")
))

# Scroll into view and click it via JS
driver.execute_script("arguments[0].scrollIntoView(true);", suggestion)
#time.sleep(1)
driver.execute_script("arguments[0].click();", suggestion)

print("Selected location: Hyderabad Telangana, India")


###calnedar

calendar_input = driver.find_element(By.XPATH, "(//input[@placeholder='MM:DD:YYYY'])[1]")
driver.execute_script("arguments[0].click();", calendar_input)
#time.sleep(3)
#print("calendar")

target_month = "September"
target_year = "1998"

while True:
    try:
        header_element = driver.find_element(By.CLASS_NAME, "rdtSwitch")
        header_text = header_element.text.strip()

        if not header_text or len(header_text.split()) != 2:
            print("Waiting for calendar header to load...")
            time.sleep(0.5)
            continue

        current_month, current_year = header_text.split()

        if current_month == target_month and current_year == target_year:
            break


        prev_btn = driver.find_element(By.CLASS_NAME, "rdtPrev")
        driver.execute_script("arguments[0].click();", prev_btn)
        time.sleep(0.3)
    except Exception as e:
        print(f"Error during calendar navigation: {e}")
        break


target_day = "3"
target_month_index = "8"
target_year_value = "1998"

all_days = driver.find_elements(By.CLASS_NAME, "rdtDay")
for day in all_days:
    day_value = day.get_attribute("data-value")
    day_month = day.get_attribute("data-month")
    day_year = day.get_attribute("data-year")
    day_class = day.get_attribute("class")

    if (
        day_value == target_day
        and day_month == target_month_index
        and day_year == target_year_value
        and "rdtDisabled" not in day_class
    ):
        driver.execute_script("arguments[0].click();", day)
        print("Date selected: September 3, 1998")
        break

time.sleep(2)
driver.find_element(By.XPATH, "(//button[contains(text(),'Next')])[4]").click()
#print("next")
wait = WebDriverWait(driver, 20)
visible_textareas = driver.find_elements(By.XPATH, "//textarea[@name='introduction' and not(ancestor::div[contains(@style,'display: none')])]")
# Filter for only visible ones (in case hidden by animation or position)
for textarea in visible_textareas:
    if textarea.is_displayed():
        textarea.clear()
        textarea.send_keys("hi")
        print("Text entered successfully")

else:
    print("No visible textarea found.")



#text = driver.find_element(By.XPATH, "(//textarea[@name='introduction'])[1]")
#text.send_keys("Python selenium")
#wait3 = WebDriverWait(driver, 10)
#wait3.until(ec.visibility_of_element_located((By.XPATH,"(//textarea[@name='introduction'])[1]")))
#print("text area")
