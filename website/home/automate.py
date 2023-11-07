from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Automation:

    def autoItems(item_list):
        print(item_list)
        browser = webdriver.Chrome()
        browser.get("https://www.lazada.com.ph/")

        wait = WebDriverWait(browser, 20)

        search_input_selector = "search-box__input--O34g"
        search_btn_selector = "search-box__button--1oH7"

        prod_name_selector = "/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/a"
        prod_price_selector = "/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div/div/div[2]/div[3]/span"
        try:
            search_input = wait.until(
                        EC.presence_of_element_located((By.CLASS_NAME, search_input_selector)))
            search_input.send_keys("Mouse")
            print('--search input')
           
            search_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, search_btn_selector)))
            search_btn.click()
            print('--search button click\n')
            
            prod_name = wait.until(
                        EC.presence_of_element_located((By.XPATH, prod_name_selector)))
            print(prod_name.text)
            print('--product name\n')
            
            prod_price = wait.until(
                        EC.presence_of_element_located((By.XPATH, prod_price_selector)))
            print(prod_price.text)
            print('--product price')
       
        except Exception as e:
            print(f"Error: {e}")  

        finally:
            browser.quit

       
        #loop items to search
        """for item in item_list:
            print(f"Start Automate {item}")
    
            #search items

            #enumerate numbers of products per item and limit with condition

            #get product names and price  throught xpath

            #get previous product price in the database and current price to calculate price rate
            
            #store store it in the database 
            
            #return 
        """