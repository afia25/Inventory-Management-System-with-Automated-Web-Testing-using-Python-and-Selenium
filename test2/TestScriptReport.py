
# pip install pyhtmlreport
from pyhtmlreport import Report
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

report = Report()
driver = webdriver.Chrome(executable_path="D:\\software pycharm projects\\web driver\\chromedriver.exe")

report.setup(
	report_folder=r'D:\software pycharm projects\test2\Reports',
	module_name='Inventory Management System Report',
	release_name='Release 1',
	selenium_driver=driver
)
driver.get("http://localhost:8000/")
driver.maximize_window()
time.sleep(1)

try:
    report.write_step(
    	'Login to the system',
    	status=report.status.Start,
    	test_number=1
    )
    driver.find_element(By.ID, "id_username").send_keys("Nova")
    #time.sleep(1)
    driver.find_element(By.ID, "id_password").send_keys("uap123456")
    #time.sleep(1)
    driver.find_element_by_name("loginbutton").send_keys(Keys.ENTER)
    time.sleep(1)

    assert "home" in driver.current_url
    report.write_step(
    	'Google Search returned results',
    	status=report.status.Pass,
    	screenshot=True
    )
except AssertionError:
    report.write_step(
        'Google Search did not return any result',
	 status=report.status.Fail,
	 screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )



try:
    report.write_step(
    	'Go to food page',
    	status=report.status.Start,
    	test_number=2
    )
    driver.find_element(By.LINK_TEXT, "Customer").click()
    #time.sleep(2)
    driver.find_element_by_name("cat").send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[contains(text(),'Food')]").click()
    #time.sleep(2)

    assert "food" in driver.current_url
    report.write_step(
    	'Google Search returned results',
    	status=report.status.Pass,
    	screenshot=True
    )
except AssertionError:
    report.write_step(
        'Google Search did not return any result',
	 status=report.status.Fail,
	 screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )



try:
    report.write_step(
    	'Order food and add to cart',
    	status=report.status.Start,
    	test_number=3
    )
    driver.find_element_by_name("product_id").send_keys("7")
    #time.sleep(1)
    driver.find_element(By.XPATH, "//input[@name='user_id']").send_keys("208")
    #time.sleep(1)
    driver.find_element(By.XPATH, "//input[@name='quantity']").send_keys("3")
    #time.sleep(1)
    driver.find_element_by_name("foodbutton").send_keys(Keys.ENTER)
    time.sleep(1)

    assert "food" in driver.current_url
    report.write_step(
    	'Google Search returned results',
    	status=report.status.Pass,
    	screenshot=True
    )
except AssertionError:
    report.write_step(
        'Google Search did not return any result',
	 status=report.status.Fail,
	 screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )




try:
    report.write_step(
    	'View Cart',
    	status=report.status.Start,
    	test_number=4
    )
    driver.find_element_by_name("cartbutton").send_keys(Keys.ENTER)
    time.sleep(1)

    assert "userorder" in driver.current_url
    report.write_step(
    	'Google Search returned results',
    	status=report.status.Pass,
    	screenshot=True
    )
except AssertionError:
    report.write_step(
        'Google Search did not return any result',
	 status=report.status.Fail,
	 screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )




try:
    report.write_step(
    	'Confirm Order',
    	status=report.status.Start,
    	test_number=5
    )
    driver.find_element_by_name("buybutton").send_keys(Keys.ENTER)
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Logout").click()
    #time.sleep(15)
    driver.find_element(By.LINK_TEXT, "Login").click()
    driver.find_element(By.ID, "id_username").send_keys("Aria12")
    #time.sleep(1)
    driver.find_element(By.ID, "id_password").send_keys("uap123456")
    #time.sleep(1)
    driver.find_element_by_name("loginbutton").send_keys(Keys.ENTER)


    assert "home" in driver.current_url
    report.write_step(
    	'Google Search returned results',
    	status=report.status.Pass,
    	screenshot=True
    )
except AssertionError:
    report.write_step(
        'Google Search did not return any result',
	 status=report.status.Fail,
	 screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )



try:
    report.write_step(
    	'Go to stock report page and take a screenshot',
    	status=report.status.Start,
    	test_number=6
    )
    driver.find_element(By.LINK_TEXT,"Admin").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Stock").click()
    driver.save_screenshot("stock_report.png")
    driver.find_element(By.LINK_TEXT, "Logout").click()


    assert "logout" in driver.current_url
    report.write_step(
    	'Google Search returned results',
    	status=report.status.Pass,
    	screenshot=True
    )
except AssertionError:
    report.write_step(
        'Google Search did not return any result',
	 status=report.status.Fail,
	 screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )



try:
    report.write_step(
    	'Go to create an invoice page',
    	status=report.status.Start,
    	test_number=7
    )
    driver.find_element(By.LINK_TEXT, "Login").click()
    driver.find_element(By.ID, "id_username").send_keys("Tithi25")
    driver.find_element(By.ID, "id_password").send_keys("uap123456")
    driver.find_element_by_name("loginbutton").send_keys(Keys.ENTER)
    driver.find_element(By.LINK_TEXT, "Employee").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Create").click()


    assert "invoice" in driver.current_url
    report.write_step(
    	'Google Search returned results',
    	status=report.status.Pass,
    	screenshot=True
    )
except AssertionError:
    report.write_step(
        'Google Search did not return any result',
	 status=report.status.Fail,
	 screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )




try:
    report.write_step(
    	'Create a new invoice',
    	status=report.status.Start,
    	test_number=8
    )
    driver.find_element(By.XPATH, "//input[@name='name_of_customer']").send_keys("Nova Tasnuba")
    driver.find_element(By.XPATH, "//input[@name='customer_id']").send_keys("208")
    driver.find_element(By.XPATH, "//input[@name='name_of_product']").send_keys("Flour")
    driver.find_element(By.XPATH, "//input[@id='id_prod_id']").send_keys("7")
    driver.find_element(By.XPATH, "//input[@id='id_quantity']").send_keys("3")
    driver.find_element(By.XPATH, "//input[@id='id_total_price']").send_keys("180")
    driver.find_element(By.CSS_SELECTOR, "input[name='delivery_charge']").send_keys("20")
    driver.find_element(By.CSS_SELECTOR, "input[name='discount']").send_keys("0")
    driver.find_element(By.CSS_SELECTOR, "input[name='total']").send_keys("200")
    driver.find_element(By.CSS_SELECTOR, "input[id='id_payment']").send_keys("200")
    driver.find_element(By.CSS_SELECTOR, "input[id='id_due']").send_keys("0")
    driver.find_element_by_name("invoice_button").send_keys(Keys.ENTER)


    assert "invoice" in driver.current_url
    report.write_step(
    	'Google Search returned results',
    	status=report.status.Pass,
    	screenshot=True
    )
except AssertionError:
    report.write_step(
        'Google Search did not return any result',
	 status=report.status.Fail,
	 screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )



try:
    report.write_step(
    	'Go to all invoices page',
    	status=report.status.Start,
    	test_number=9
    )
    driver.get("http://localhost:8000/empHome/")
    driver.find_element(By.LINK_TEXT, "All Invoices").click()
    driver.back()
    time.sleep(1)


    assert "empHome" in driver.current_url
    report.write_step(
    	'Google Search returned results',
    	status=report.status.Pass,
    	screenshot=True
    )
except AssertionError:
    report.write_step(
        'Google Search did not return any result',
	 status=report.status.Fail,
	 screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )


try:
    report.write_step(
    	'Go to sales report page, increase sales amount and logout',
    	status=report.status.Start,
    	test_number=10
    )
    driver.find_element(By.PARTIAL_LINK_TEXT, "Sales").click()
    driver.find_element_by_name("pid").send_keys("7")
    driver.find_element(By.ID, "quan").send_keys("3")
    driver.find_element_by_name("sales_button").send_keys(Keys.ENTER)
    driver.find_element(By.LINK_TEXT, "Logout").click()
    time.sleep(2)


    assert "logout" in driver.current_url
    report.write_step(
    	'Google Search returned results',
    	status=report.status.Pass,
    	screenshot=True
    )
except AssertionError:
    report.write_step(
        'Google Search did not return any result',
	 status=report.status.Fail,
	 screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )



finally:
    report.generate_report()
    driver.quit()