"""Title: Automate test plan for Registration page.

    Author - Neepa Pandya

Description: this script will enter into  website:https://audiostack-qa-test.netlify.app/ and run some testcases from testrail.
Testcases I have automated are from "Registration Form" test runs: https://nipa23pandya.testrail.io/index.php?/runs/overview/1
Testcase run from their Ids:

T6: https://nipa23pandya.testrail.io/index.php?/tests/view/6
T8: https://nipa23pandya.testrail.io/index.php?/tests/view/8
T9: https://nipa23pandya.testrail.io/index.php?/tests/view/9
T10: https://nipa23pandya.testrail.io/index.php?/tests/view/10
T17: https://nipa23pandya.testrail.io/index.php?/tests/view/17
T20: https://nipa23pandya.testrail.io/index.php?/tests/view/20

"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time

class RegUi:
    """Class for handling all the web interface and other functions related activities.
    param:
        browser: str('edge'/'chrome')
    return:
        object: web driver object
    """

    def __init__(self, browser="chrome"):
        """Initialise the web driver."""
        self.driver = RegUi.driver_init(browser)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.url = "https://audiostack-qa-test.netlify.app/"
        self.name ="Neepa"
        self.random_pokemon ="bulbasaur"

    def perform_testcases(self):
        """Load the main web page and perform testcases."""
        try:
            print("Performing testcases by their testrun number from testrail :")
            self.perform_testrun_dropdown_mandatory_t6()
            self.perform_testrun_pokemon_stats_t8()
            self.perform_testrun_pokemon_stats_consistent_t9()
            self.perform_testrun_registration_successful_t10()
            self.perform_testrun_registration_not_successful_t17()
            self.perform_testrun_dropdown_mandatory_delay_1s_t20()
        except Exception as exc:
            print("Error while performing testrun.")
            raise exc

    def perform_testrun_registration_successful_t10(self):
        """Verify "Registration Successful" pop up alert message notification with successful registration."""
        print("---------------------Performing testrun no T10------------------------")
        print("STEP 1: Enter into https://audiostack-qa-test.netlify.app/")
        self.driver.get(self.url)
        print("STEP 2: Write input text in Name input field.")
        self.selecting_input_textbox()
        print("STEP 3: selecting random_pokemon")
        self.selecting_random_pokemon()
        self.click_on_submit_button()
        print("STEP 4:Verify pop up registration notification.")
        result = self.verify_pop_up_registration_notification()
        if result:
            print("Test Result: Passed")
        else:
            print("Test Result: Failed")
        print("---------------------End of testrun no T10------------------------")
        print("------------------------------------------------------------------")

    def perform_testrun_dropdown_mandatory_t6(self):
        """Verify that  display of  a red “*” asterisk mark as the Pokemon Starter dropdown is a mandatory field."""
        print("---------------------Performing testrun no T6------------------------")
        print("STEP 1: Enter into https://audiostack-qa-test.netlify.app/")
        self.driver.get(self.url)
        print("STEP 2: Verify Starter pokemon dropdown box is highlighting with red colour.")
        result = self.verify_starter_pokemon_dropdown_mandatory_field()
        if result:
            print("Test Result: Passed")
        else:
            print("Test Result: Failed")
        print("---------------------End of testrun no T6------------------------")
        print("------------------------------------------------------------------")

    def perform_testrun_dropdown_mandatory_delay_1s_t20(self):
        """Verify that  display of  a red “*” asterisk mark as the Pokemon Starter dropdown is a mandatory field."""
        print("---------------------Performing testrun no T20------------------------")
        print("STEP 1: Enter into https://audiostack-qa-test.netlify.app/")
        self.driver.get(self.url)
        print("STEP 2: Verify Starter pokemon dropdown box is highlighting with red colour.")
        result = self.verify_starter_pokemon_dropdown_mandatory_field_with_1_seconds_delay()
        if result:
            print("Test Result: Passed")
        else:
            print("Test Result: Failed")
        print("---------------------End of testrun no T20------------------------")
        print("------------------------------------------------------------------")

    def perform_testrun_pokemon_stats_t8(self):
        """Verify that user should able to see  the selected Pokemon stats on form."""
        print("---------------------Performing testrun no T8------------------------")
        print("STEP 1: Get list of starter pokemon from dropdown box.")
        starter_pokemon, options = self.get_list_of_starter_pokemon_from_dropdown()
        print("STEP 2: selecting each starter pokemon from list.")
        for pokemon in options:
            print("selecting Starter Pokemon " + pokemon)
            starter_pokemon.send_keys(pokemon)
            time.sleep(1)
            print("STEP 3: Verifying stats are available or not.")
            stats = self.driver.find_element(By.XPATH, '//div[@class="css-1nkdwiq"]')
            if stats:
                print(" Test_step Result: Selected " + pokemon + " stats detail!")
                stats_text = stats.text
                print(stats_text)
                print("Test_step Result: Passed")
            else:
                print(" Test_step Result: selected pokemon " + pokemon + " stats are not available")
                print(" Test_step Result: failed")
        print("---------------------End of testrun no T8------------------------")
        print("------------------------------------------------------------------")

    def perform_testrun_pokemon_stats_consistent_t9(self):
        """Verify stats are consistent with selected pokemon."""
        print("---------------------Performing testrun no T9------------------------")
        print("STEP 1: Get list of starter pokemon from dropdown box.")
        starter_pokemon, options = self.get_list_of_starter_pokemon_from_dropdown()
        print("STEP 2: selecting each starter pokemon from list.")
        for pokemon in options:
            print("selecting Starter Pokemon " + pokemon)
            starter_pokemon.send_keys(pokemon)
            time.sleep(1)
            print("STEP 3: Verifying stats are consistent with selected pokemon.")
            stats = self.driver.find_element(By.XPATH, '//div[@class="css-1nkdwiq"]')
            if stats:
                stats_pokemon_detail = self.driver.find_element(By.XPATH, '//p[@class="css-19tvwk3"]')
                stats_pokemon = stats_pokemon_detail.text
                if stats_pokemon == pokemon:
                    print("Test_step Result: selected pokemon " + pokemon + " and their stats are consistent with each other.")
                    print("Test_step Result: Passed")
                else:
                    print("Test_step Result: selected pokemon " + pokemon + " and their stats are not consistent with each other.")
                    print(" Test_step Result: failed")
            else:
                print(" Test_step Result: selected pokemon" + pokemon + " stats are not available")
                print(" Test_step Result: failed")
        print("---------------------End of testrun no T9------------------------")
        print("------------------------------------------------------------------")

    def perform_testrun_registration_not_successful_t17(self):
        """ Verifying registration not successful plus mandatory field."""
        print("---------------------Performing testrun no T17------------------------")
        print("STEP 1: Enter into https://audiostack-qa-test.netlify.app/")
        self.driver.get(self.url)
        print("STEP 2: Write input text in Name input field.")
        self.selecting_input_textbox()
        print("STEP 3: Verify Starter pokemon dropdown box is highlighting with red colour.")
        step_result_1 = self.verify_starter_pokemon_dropdown_mandatory_field()
        print("STEP 4:Verify pop up registration notification.")
        step_result_2 = self.verify_pop_up_registration_notification()
        if (step_result_2== True) and (step_result_1== True):
            print("Test Result: Passed")
        else:
            print("Test Result: Failed")
        print("---------------------End of testrun no T17------------------------")
        print("------------------------------------------------------------------")

    def verify_pop_up_registration_notification(self):
        """Verifying pop up registration notification"""
        div_element_1 = self.driver.find_element(By.XPATH, '//div[@class="chakra-toast__title css-1nhm9ic"]')
        result =False
        if div_element_1:
            registration_pop_up = div_element_1.text
            div_element_2 = self.driver.find_element(By.XPATH, '//div[@class="chakra-toast__description css-1tl80zq"]')
            pop_up_description = div_element_2.text
            result = registration_pop_up == "Registration Successful"
            print("Test_step Result: User gets notification :\n" + registration_pop_up + "\n" + pop_up_description)
        else:
            print("Test_step Result: User does not get notification about registration successful.")
        return result

    def selecting_input_textbox(self):
        # print("Write input text in Name input field.")
        pokemon_name = self.driver.find_element(By.NAME, "name")
        pokemon_name.send_keys(self.name)
        print(self.name + " is writing in name input text field.")

    def selecting_random_pokemon(self):
        # print("selecting random_pokemon")
        starter_pokemon = self.driver.find_element(By.NAME, "starter_pokemon")
        starter_pokemon.send_keys(self.random_pokemon)
        time.sleep(1)

    def click_on_submit_button(self):
        """click on submit button"""
        print("Test_step:Click on submit button.")
        submit_button = self.driver.find_element(By.XPATH, '//button[@class="chakra-button css-5kjf22"]')
        submit_button.click()

    def get_list_of_starter_pokemon_from_dropdown(self):
        """ get_list_of_starter_pokemon_from_dropdown"""
        self.driver.get(self.url)
        time.sleep(1)
        starter_pokemon = self.driver.find_element(By.NAME, "starter_pokemon")
        options = [x.text for x in starter_pokemon.find_elements(By.TAG_NAME, "option")]
        print("list of starter_pokemon: \n", options)
        # removing first value" Select your starter" as not needed.
        options.pop(0)
        return starter_pokemon, options

    def verify_starter_pokemon_dropdown_mandatory_field(self):
        """Verifying Starter pokemon dropdown box is highlighting with red colour."""
        print("Test_step: User leave unselected any Pokemon from Pokemon Starter dropdown box")
        starter_pokemon = self.driver.find_element(By.NAME, "starter_pokemon")
        starter_pokemon.send_keys("Select your starter")
        self.click_on_submit_button()
        val = starter_pokemon.get_attribute("aria-invalid")
        if val:
            print("Test_step Result: Starter Pokemon dropdown box is highlighting in red as mandatory field.")
            return True
        else:
            print("Test_step Result: Starter Pokemon dropdown box is not highlighting in red as mandatory field.")

    def verify_starter_pokemon_dropdown_mandatory_field_with_1_seconds_delay(self):
        """Verifying Starter pokemon dropdown box is highlighting with red colour."""
        starter_pokemon = self.driver.find_element(By.NAME, "starter_pokemon")
        starter_pokemon.send_keys("Select your starter")
        time.sleep(1)
        submit_button = self.driver.find_element(By.XPATH, '//button[@class="chakra-button css-5kjf22"]')
        submit_button.click()
        val = starter_pokemon.get_attribute("aria-invalid")
        if val:
            print("Test_step Result: Starter Pokemon dropdown box is highlighting in red as mandatory field.")
            return True
        else:
            print("Test_step Result: Starter Pokemon dropdown box is not highlighting in red as mandatory field.")

    @staticmethod
    def driver_init(browser):
        """Initialize the web driver with the given name, currently working with Chrome web driver.
        Param:
            browser: str(edge/chrome)
        return:
            obj: web driver object.
        """
        if browser == "edge":
            # edge_options.add_argument('start-maximized')
            driver = webdriver.Edge()
        elif browser == "chrome":
            options = Options()
            options.add_argument("start-maximized")
            driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()), options=options
            )
        else:
            raise AttributeError(f"Web driver {browser} not found")
        return driver

    def close_session(self):
        """Close the web driver session, when script is terminating, or function is called."""
        try:
            print("CLosing the web driver session.")
            self.driver.quit()
        except EnvironmentError as exc:
            print(f"Exception while closing the browser. {exc}")

    def __del__(self):
        self.close_session()

if __name__ == "__main__":
    reg_page = RegUi()
    reg_page.perform_testcases()