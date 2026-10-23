import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

portfolio_dir = r"c:\Users\harih\Downloads\portfolio"
index_url = f"file:///{portfolio_dir.replace('\\', '/')}/index.html"

options = Options()
options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1280,1050")

driver = webdriver.Chrome(options=options)

try:
    # 1. Capture functionality.png
    driver.get(index_url)
    time.sleep(1)
    func_path = os.path.join(portfolio_dir, "functionality.png")
    driver.save_screenshot(func_path)
    print(f"Captured functionality.png to {func_path}")

    # 2. Scroll to recommendation section and add a recommendation
    # Type new recommendation into #new_recommendation
    rec_input = driver.find_element(By.ID, "new_recommendation")
    rec_text = "John is an outstanding developer with exceptional AI and full-stack capabilities. His problem solving and dedication are world-class!"
    rec_input.send_keys(rec_text)
    time.sleep(0.5)

    # Click submit
    submit_btn = driver.find_element(By.ID, "recommend_btn")
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", submit_btn)
    time.sleep(0.5)
    submit_btn.click()
    time.sleep(1)

    # Now screenshot showing new recommendation + popup
    new_rec_path = os.path.join(portfolio_dir, "new_recommendation.png")
    driver.save_screenshot(new_rec_path)
    print(f"Captured new_recommendation.png to {new_rec_path}")

finally:
    driver.quit()
