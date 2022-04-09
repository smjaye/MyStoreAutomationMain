import unittest
import mystore_locators as locators
import mystore_methods as methods

class MystoreautomationAppPositiveTestCases(unittest.TestCase):

    @staticmethod  # signal to Unittest that this is a function inside class (vs @classmethod)
    def test_main_my_store_automation():
        methods.setUp()
        methods.create_new_account()
        methods.sign_out()
        methods.sign_in()
        methods.my_shopping_cart()
        methods.check_out()
        methods.tearDown()
        