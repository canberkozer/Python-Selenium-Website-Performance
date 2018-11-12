#New Tab Example
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
driver = webdriver.Chrome(chrome_options=options)
driver.get("http://www.google.com")
print("Initial Page Title is : %s" %driver.title)
windows_before  = driver.current_window_handle
print("First Window Handle is : %s" %windows_before)
driver.execute_script("window.open('https://www.yahoo.com')")
time.sleep(10)
windows_after = driver.window_handles
new_window = [x for x in windows_after if x != windows_before][0]
driver.switch_to_window(new_window)
print("Page Title after Tab Switching is : %s" %driver.title)
print("Second Window Handle is : %s" %new_window)
driver.switch_to_window(windows_before)
