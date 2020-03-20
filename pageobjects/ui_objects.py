
class ui_objects(object):

    """
    Class of objects for Android devices

    Work in progress
    """

    def __init__(self, driver):
        self.driver = driver
    """
    Navigation bar on the bottom for Contacts, History, Dial, PurpleMail, Settings
    """

    def go_to_dialpad(self):
        self.driver.find_element_by_accessibility_id("Dial").click()

    def go_to_contacts(self):
        self.driver.find_element_by_accessibility_id("Contacts").click()

    def go_to_history(self):
        self.driver.find_element_by_accessibility_id("History").click()

    def go_to_settings(self):
        self.driver.find_element_by_accessibility_id("Settings").click()

    """
    Incoming calls decline or answer
    """

    def answer_incoming_call(self):
        self.driver.implicitly_wait(5000)
        self.driver.find_element_by_id(":id/accept_call_iv").click()

    def decline_incoming_call(self):
        self.driver.implicitly_wait(5000)
        self.driver.find_element_by_id(":id/reject_call_iv").click()

    """
    The buttons available on the Dial pad
    
    """

    def call_button(self):
        self.driver.find_element_by_id(":id/call_iv").click()

    def press_button_one(self):
        self.driver.find_element_by_id(":id/key_1").click()

    def press_button_two(self):
        self.driver.find_element_by_id(":id/key_2").click()

    def press_button_three(self):
        self.driver.find_element_by_id(":id/key_3").click()

    def press_button_four(self):
        self.driver.find_element_by_id(":id/key_4").click()

    def press_button_five(self):
        self.driver.find_element_by_id("id/key_5").click()

    def press_button_six(self):
        self.driver.find_element_by_id("id/key_6").click()

    def press_button_seven(self):
        self.driver.find_element_by_id("id/key_7").click()

    def press_button_eight(self):
        self.driver.find_element_by_id("id/key_8").click()

    def press_button_nine(self):
        self.driver.find_element_by_id("id/key_9").click()

    def press_button_zero(self):
        self.driver.find_element_by_id("id/key_0").click()

    def press_search_on_diapad(self):
        self.driver.find_element_by_id("id/key_search").click()

    def press_add_on_dialpad(self):
        self.driver.find_element_by_id("id/add_iv").click()

    def press_delete_on_dialpad(self):
        self.driver.find_element_by_id(":id/clear_input_iv").click()


