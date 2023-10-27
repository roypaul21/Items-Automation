from selenium import webdriver
browser = webdriver.Chrome()


class Automation:
    
    def autoItems(item_list):
        print(item_list)
        browser.get("https://shopee.ph/")
        """for item in item_list:
            print(f"Start Automate {item}")"""