import datetime

from faker import Faker
fake = Faker(locale='en_US')




#----------------------- My Store Automation  App Data parameters-------------------------

app = 'My Store Automation'
mystore_url = 'http://automationpractice.com/index.php'
mystore_home_page_title = 'My Store'
page_heading = 'Authentication'
sub_heading = 'Create an account'

email = fake.email()
password = fake.password()[0:7]
first_name = fake.first_name_female()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'
company = fake.company()
address1 = fake.street_address()
address2 = fake.secondary_address()
city = fake.city()
postalcode = fake.postcode()
home_phone = fake.phone_number()[0:10]
mobile_phone = fake.phone_number()[0:10]
address_alias = f'927 Tyson Cove'
additional_information = f'For product related update, call on my mobile phone number '
