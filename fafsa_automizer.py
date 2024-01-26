import time
import webbrowser

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# download chromedriver and update the path
driver_path = '/path/to/chromedriver'
options = webdriver.ChromeOptions()
options.binary_location = driver_path

driver = webdriver.Chrome(options=options)

url = 'https://studentaid.gov/h/apply-for-aid/fafsa'

xpath = '//*[@id="fsa_Button_FAFSA_EditForm"]'

driver.get(url)

# function to check if button is available
def is_button_available():
    try:
        button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        return button.is_displayed() and button.is_enabled()
    except:
        return False

# number of attempts below
attempts = 100000
for attempt in range(attempts):
    print(f"Refresh attempt {attempt + 1}")
    
    # Refresh the page
    driver.refresh()

    # add a delay to see the page being refreshed
    time.sleep(2)  # adjust the sleep duration as needed
    
    # check if the button is available
    if is_button_available():
        print("FAFSA is available!")
        
        # youtube link for celebration
        yt_url = 'https://www.youtube.com/watch?v=0E4haJHYUJw&ab_channel=SlowTVRelax%26Background'
        webbrowser.open(yt_url)
        
        break

driver.quit()
