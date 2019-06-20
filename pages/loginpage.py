from selenium import webdriver

class Login:

        def login_facebook(self):
            # Launch the browser and get the uRL>>S1
            driver = webdriver.Chrome(executable_path="C:/Users/Admin/Downloads/chromedriver.exe")
            driver.get("https://www.facebook.com/")
            # login to the application>>s2
            driver.find_element_by_name("email").send_keys("9535468206")
            driver.find_element_by_id("pass").send_keys("preethiaunty")
            driver.find_element_by_xpath("//input[@type='submit']").click()

