
from appium import webdriver
import time
import unittest

from pageobjects.ui_objects import ui_objects


class TestOne(unittest.TestCase):

    def setUp(self):
        desired_caps = {
            "platformName": "android",
            "deviceName": "SM-G950U",
            "udid": "R58M43CHYBJ",
            "appPackage": "blank",
            "appActivity": "blank",
            "noReset": "True",
            "automationName": "uiautomator2"
        }

        self.android_one = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_caps)

    def test_purple_to_iOS_decline_call(self):
        # Assign UI objects to phone
        android_phone = ui_objects(self.android_one)

        android_phone.go_to_dialpad()
        # dial 212 444 1000
        android_phone.press_button_eight()
        android_phone.press_button_zero()
        android_phone.press_button_one()
        android_phone.press_button_two()
        android_phone.press_button_zero()
        android_phone.press_button_seven()
        android_phone.press_button_nine()
        android_phone.press_button_zero()
        android_phone.press_button_six()
        android_phone.press_button_zero()

        android_phone.call_button()
        time.sleep(5)

    def tearDown(self):
        self.android_one.quit()


if __name__ == '__main__':
    unittest.main()
