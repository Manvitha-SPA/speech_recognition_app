import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

st.title("CHATBOT")
input_text=st.text_input("Search the topic you want")

with st.chat_message(name="assistant"):
    st.write(input_text)




# # Set the path to your WebDriver executable
# #webdriver_path = 'chromedriver-win64'  # Change this to your WebDriver path
# driver = webdriver.Chrome()

# # Open the Streamlit app URL
# app_url = 'https://www.wikipedia.org/'
# driver.get(app_url)

# search=driver.find_element(By.ID,"searchInput")
# search.click()

# search.send_keys(st.write(input_text))



# Wait for the results to load (you might need to customize the wait time)
# time.sleep(5)

# # Extract data from the web page
# # Use driver.find_element_by_* methods to locate and extract data

# # Close the browser
# driver.quit()
