import time
import webbrowser

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# set the path to webdriver, in this case chro (e.g., chromedriver, geckodriver)
# Download the appropriate driver for your browser and update the path
driver_path = '/path/to/chromedriver'
options = webdriver.ChromeOptions()
options.binary_location = driver_path

driver = webdriver.Chrome(options=options)

url = 'https://studentaid.gov/h/apply-for-aid/fafsa'

xpath = '//*[@id="fsa_Button_FAFSA_EditForm"]'

driver.get(url)

# Function to check if the button is available
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

    # Add a delay to see the page being refreshed
    time.sleep(2)  # Adjust the sleep duration as needed
    
    # Check if the button is available
    if is_button_available():
        print("FAFSA is available!")
        
        # youtube link for celebration
        yt_url = 'https://www.youtube.com/watch?v=0E4haJHYUJw&ab_channel=SlowTVRelax%26Background'
        webbrowser.open(yt_url)
        
        break

driver.quit()
