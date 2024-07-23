from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

url = 'https://www.pdffiller.com/jsfiller-desk12/?mode=ref&lang=en&ref=https%3A%2F%2Fwww.pdffiller.com%2Fen%2Fforms%2Fdashboard&projectId=1341383752&loader=tips&MEDIUM_PDFJS=true&PAGE_REARRANGE_V2_MVP=true&richTextFormatting=true&isPageRearrangeV2MVP=true&jsf-page-rearrange-v2=true&jsf-new-header=false&routeId=01e4b4bc6e38052ce472779d65e49acf#340eb4730c8342cf9d5e20a072e34f77'
driver.get(url)
# Wait for the iframe to load
wait = WebDriverWait(driver, 10)
iframe = wait.until(EC.presence_of_element_located((By.ID, 'jsf-pdf-viewer')))

# Switch to the iframe context
driver.switch_to.frame(iframe)

# Get the PDF URL from the iframe's source
pdf_url = driver.current_url

response = requests.get(pdf_url)
if response.status_code == 200:
    with open('test.pdf', 'wb') as f:
        f.write(response.content)
    print("Downloaded test.pdf successfully.")
else:
    print("Failed to download test.pdf.")

# Switch back to the main context
driver.switch_to.default_content()

driver.quit()
