from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Set up Chrome for headless browsing
options = Options()
options.headless = True  # Make Chrome run in the background (without opening a window)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.imdb.com/chart/top")  # URL of IMDb Top 250

# Example: Scrape the top movie titles
movie_titles = driver.find_elements(By.XPATH, '//td[@class="titleColumn"]/a')

for title in movie_titles:
    print(title.text)

driver.quit()  # Close the browser
