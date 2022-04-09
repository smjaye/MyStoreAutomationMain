import datetime
from selenium import webdriver  # import selenium to the file
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import mystore_locators as locators
from selenium.webdriver.support.ui import Select # ----------add this import for drop down lists
from selenium.webdriver import Keys




s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)


def setUp():
    print(f'Launch {locators.app}  App')
    print(f'__________________________________________________________')
    # make browser full screen
    driver.maximize_window()
    # give browser up to 30 seconds to respond
    driver.implicitly_wait(30)
    # navigate to My Store Automation App website
    driver.get(locators.mystore_url)


    # check that My Store URL and the home page title are as expected
    if driver.current_url == locators.mystore_url and driver.title == locators.mystore_home_page_title:
        print(f'Wow! {locators.app} App website launched successfully!')
        print(f' {locators.app} Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        sleep(0.25)
    else:
        print(f'{locators.app} did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Page title: {driver.title}')
        tearDown()


def tearDown():
    if driver is not None:
        print(f'______________________________________________')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()


def create_new_account():
    print(f'_________________*****CREATE A NEW ACCOUNT*****________________________')
    if driver.current_url == locators.mystore_url:  # # check we are on the home page
        driver.find_element(By.XPATH, '//a[@title="Log in to your customer account"]').click()
        sleep(0.5)
        assert driver.find_element(By.XPATH, '//h1[contains(., "Authentication")]').is_displayed()
        sleep(0.5)
        assert driver.find_element(By.XPATH, '//h3[contains(., "Create an account")]').is_displayed()
        sleep(0.5)
        print(f'Page to create a new account is displayed with heading: {locators.page_heading}')
        print(f'Page to create a new account is displayed with sub-heading: {locators.sub_heading}')
        sleep(0.25)
        driver.find_element(By.XPATH, '//input[@id="email_create"]').send_keys(locators.email)
        sleep(0.25)
        driver.find_element(By.ID, 'SubmitCreate').click()
        sleep(0.25)
        driver.find_element(By.ID, 'id_gender2').is_displayed()
        sleep(0.25)
        driver.find_element(By.ID, 'id_gender2').is_enabled()
        sleep(0.25)
        driver.find_element(By.ID, 'id_gender2').is_selected()
        sleep(0.25)
        driver.find_element(By.ID, 'id_gender2').click()
        sleep(0.25)
        driver.find_element(By.XPATH, '//input[@id="customer_firstname"]').send_keys(locators.first_name)
        sleep(0.25)
        driver.find_element(By.XPATH, '//input[@id="customer_lastname"]').send_keys(locators.last_name)
        sleep(0.25)
        driver.find_element(By.ID, 'passwd').send_keys(locators.password)
        sleep(0.25)
        driver.find_element(By.XPATH, '//select[@id="days"]').click()
        sleep(0.25)
        Select(driver.find_element(By.XPATH, '//select[@id="days"]')).select_by_index('11')
        sleep(0.25)
        driver.find_element(By.XPATH, '//select[@id="months"]').click()
        sleep(0.25)
        Select(driver.find_element(By.XPATH, '//select[@id="months"]')).select_by_value('10')
        sleep(0.25)
        driver.find_element(By.XPATH, '//select[@id="years"]').click()
        sleep(0.25)
        Select(driver.find_element(By.XPATH, '//select[@id="years"]')).select_by_value('1998')
        sleep(0.25)
        driver.find_element(By.ID, 'company').send_keys(locators.company)
        sleep(0.25)
        driver.find_element(By.ID, 'address1').send_keys(locators.address1)
        sleep(0.25)
        driver.find_element(By.ID, 'address2').send_keys(locators.address2)
        sleep(0.25)
        driver.find_element(By.ID, 'city').send_keys(locators.city)
        sleep(0.25)
        driver.find_element(By.XPATH, '//select[@id="id_state"]').click()
        sleep(0.25)
        Select(driver.find_element(By.XPATH, '//select[@id="id_state"]')).select_by_value('16')
        sleep(0.25)
        driver.find_element(By.ID, 'postcode').send_keys(locators.postalcode)
        sleep(0.25)
        Select(driver.find_element(By.XPATH, '//select[@id="id_country"]')).select_by_visible_text('United States')
        sleep(0.25)
        driver.find_element(By.XPATH, '//textarea[@id="other"]').send_keys(locators.additional_information)
        sleep(0.25)
        driver.find_element(By.XPATH, '//input[@id="phone"]').send_keys(locators.home_phone)
        sleep(0.25)
        driver.find_element(By.XPATH, '//input[@id="phone_mobile"]').send_keys(locators.mobile_phone)
        sleep(0.25)
        driver.find_element(By.XPATH, '//input[@id="alias"]').send_keys(locators.address_alias)
        sleep(0.25)
        driver.find_element(By.CSS_SELECTOR, 'button[id="submitAccount"] span').click()
        sleep(0.25)
        if driver.find_element(By.XPATH, '//h1[contains(., "My account")]').is_displayed():
            print(f'________________******You are in your accounts page!******___________________________')
            print(f'____________******Welcome message is displayed: ******___________________________')
        else:
            print(f'___________***** oops! You are not in your accounts page. Check your code or website ')
        sleep(0.25)
        assert driver.find_element(By.XPATH, '//a[contains(., "account")]').is_displayed()
        print(f'The full_name is displayed: {locators.full_name}')


def sign_out():
    print(f'_______________*********** SIGN OUT OF ACCOUNT ************________________________')
    driver.find_element(By.XPATH, '//a[@title="Log me out"]').click()
    sleep(0.25)
    print(f'You have successfully signed out, feel free to sign in again!')


def sign_in():
    print(f'______________*********** SIGN IN AGAIN *************_____________________________')
    driver.find_element(By.XPATH, '//input[@id="email"]').send_keys(locators.email)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[@id="passwd"]').send_keys(locators.password)
    sleep(0.25)
    driver.find_element(By.XPATH, '//span[normalize-space()="Sign in"]').click()
    sleep(0.25)
    assert driver.find_element(By.XPATH, '//a[contains(., "account")]').is_displayed()
    print(f'The full_name is displayed: {locators.full_name}')
    print(f'Hello! You have signed in again')


def my_shopping_cart():
    print(f'______________******* START SHOPPING *******________________________________')
    driver.find_element(By.XPATH, '//a[@title="Women"]').click()
    sleep(0.5)
    driver.find_element(By.XPATH, '//a[@title="Printed Summer Dress"]').click()
    sleep(0.5)
    driver.find_element(By.XPATH, '//input[@id="quantity_wanted"]').clear()
    sleep(0.5)
    driver.find_element(By.XPATH, '//input[@id="quantity_wanted"]').send_keys('2')
    sleep(0.5)
    assert driver.find_element(By.XPATH, '//a[@id="color_16"]').is_displayed()
    sleep(0.25)
    driver.find_element(By.XPATH, '//a[@id="color_16"]').is_selected()
    sleep(0.25)
    driver.find_element(By.XPATH, '//a[@id="color_16"]').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//span[contains(., "Add to cart")]').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//span[contains(., "Continue shopping")]').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//a[@title="Women"]').click()
    sleep(0.25)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(0.5)
    driver.find_element(By.XPATH, '//img[@title="Printed Chiffon Dress"]').click()
    sleep(0.25)
    assert driver.find_element(By.XPATH, '//a[@id="color_16"]').is_displayed()
    sleep(0.25)
    driver.find_element(By.XPATH, '//a[@id="color_16"]').is_selected()
    sleep(0.25)
    driver.find_element(By.XPATH, '//a[@id="color_16"]').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//span[contains(., "Add to cart")]').click()
    sleep(0.25)
    assert driver.find_element(By.XPATH, '//span[contains(@class,"ajax_cart_product_txt_s")]').is_displayed()
    print(f'____________****You have selected your purchases. You are welcome to shop again!****______________________')
    print(f'Total items in cart is displayed!')


def check_out():
    print(f'_____________************* CHECKOUT PROCESS ***************_________________________________')
    driver.find_element(By.XPATH, '//a[contains(., "Proceed to checkout")]').click()
    sleep(0.5)
    assert driver.find_element(By.XPATH, '//h1[contains(., "Shopping-cart summary")]').is_displayed()
    sleep(0.5)
    print(f'______________*** Shopping cart summary with purchase details is displayed ***______________________')
    driver.find_element(By.XPATH, '//a[@class="button btn btn-default standard-checkout button-medium"]//span[contains(text(),"Proceed to checkout")]').click()
    sleep(0.5)
    assert driver.find_element(By.XPATH, '//ul[@id="address_delivery"]').is_displayed()
    sleep(0.5)
    print(f'________****** Address confirmation page is displayed ******___________________________________')
    driver.find_element(By.XPATH, '//button[@name="processAddress"]//span[contains(text(),"Proceed to checkout")]').click()
    sleep(0.5)
    assert driver.find_element(By.XPATH, '//span[contains(., " Shipping")]').is_displayed()
    sleep(0.5)
    print(f'___________******Shipping details page is displayed!******___________________')
    driver.find_element(By.XPATH, '//input[@id="cgv"]').click()
    sleep(0.5)
    driver.find_element(By.XPATH, '//button[@name="processCarrier"]//span[contains(text(),"Proceed to checkout")]').click()
    sleep(0.5)
    assert driver.find_element(By.XPATH, '//li[@class="step_current last"]//span[contains(text(), " Payment")]').is_displayed()
    sleep(0.5)
    print(f'___________******* Payment details page is displayed!*******_______________________________')
    driver.find_element(By.XPATH, '//a[@title="Pay by check."]//span[contains(text(), "(order processing will be longer)")]').click()
    sleep(0.5)
    assert driver.find_element(By.XPATH, '//h3[@class="page-subheading"]').is_displayed()
    sleep(0.5)
    print(f'_____________******* Order Summary page is displayed *******______________________')
    driver.find_element(By.XPATH, '//button[@class="button btn btn-default button-medium"]//span[contains(text(), "I confirm my order")]').click()
    sleep(0.5)
    assert driver.find_element(By.XPATH, '//p[@class="alert alert-success"]').is_displayed()
    print(f'Hey! This is the Order Confirmation Page.Your order is complete.')
    print(f'Order success message is displayed')
    sleep(0.5)
    driver.find_element(By.XPATH, '//img[@alt="My Store"]').click()
    sleep(0.5)






#
# setUp()
# create_new_account()
# sign_out()
# sign_in()
# my_shopping_cart()
# check_out()
# tearDown()

