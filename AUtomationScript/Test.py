from selenium import webdriver

drv = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
drv.maximize_window()
drv.get("http://localhost:3000/#/sign_in?last_page=/")

# Login page

drv.find_element_by_id("normal_login_username").send_keys("testuser")
drv.find_element_by_id("normal_login_password").send_keys("pl123")
drv.find_element_by_class_name("ant-btn.login-form-button.ant-btn-primary").click()
page_name = drv.title
assert page_name =="Test Automation Template"
print("Login is successful")
# assert drv.title == "Test Automation Template"
# print("Page 1 accessed successfully")

#Page 1
page1= drv.find_element_by_link_text("Page 1")
page1.click()
page1_name = drv.title
print(f"Page1 {page1_name}")

#Page 2
drv.find_element_by_link_text("Page 2").click()
page2_name = drv.title
print(f"Page 2 {page2_name}")

#Page 3
drv.find_element_by_link_text("Page 3").click()
page3_name = drv.title
print(f"Page 3 {page3_name}")


# logout
# drv.find_element_by_xpath("//li[text()='Logout'").click()
# drv.find_elements_by_css_selector("ul.ant-dropdown-menu.ant-dropdown-menu-light.ant-dropdown-menu-root.ant-dropdown-menu-vertical")
drv.close()