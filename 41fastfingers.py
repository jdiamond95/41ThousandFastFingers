import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

url = "https://10fastfingers.com/advanced-typing-test/english"

def main():
	#Open browser and open 10 Fast Fingers
	driver = webdriver.Chrome()
	driver.get(url)
		
	try:
		# Wait until the words are available
		element = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.CSS_SELECTOR, "#row1 > span.highlight"))
		)
		# Grab the page source to extract all the words, html parse with beautiful soup
		html = driver.page_source
		soup = BeautifulSoup(html, features='html.parser')
		words = soup.find_all('span')
		textfield = driver.find_element_by_id('inputfield')
		# For all spans that have the attribute 'wordnr', send keystrokes for each word
		for word in words:
			if word.has_attr('wordnr'):
				textfield.send_keys(word.getText() + " ")
	except:
		print("Something went wrong :(")
	
	time.sleep(60)
	driver.close()

if __name__ == "__main__":
	main()