# pikachu_form
Title: Automate test plan for Registration page.

Description: this script will enter into  website:https://audiostack-qa-test.netlify.app/ and run some testcases from testrail.
Testcases I have automated are from "Registration Form" test runs: https://nipa23pandya.testrail.io/index.php?/runs/overview/1
Testcase run from their Ids:

T6: https://nipa23pandya.testrail.io/index.php?/tests/view/6
T8: https://nipa23pandya.testrail.io/index.php?/tests/view/8
T9: https://nipa23pandya.testrail.io/index.php?/tests/view/9
T10: https://nipa23pandya.testrail.io/index.php?/tests/view/10
T17: https://nipa23pandya.testrail.io/index.php?/tests/view/17
T20: https://nipa23pandya.testrail.io/index.php?/tests/view/20

Driver code: "registration_main.py" is driver file where all library functions are mentioned and performed.

Driver function: perform_testcases() is the driver function where all testcases are performed.

Other functions are followed by that function.

self.perform_testrun_dropdown_mandatory_t6()

self.perform_testrun_pokemon_stats_t8()

self.perform_testrun_pokemon_stats_consistent_t9()

self.perform_testrun_registration_successful_t10()

self.perform_testrun_registration_not_successful_t17()

self.perform_testrun_dropdown_mandatory_delay_1s_t20()

above all testrun are performing testcases step by step and giving test result data and Test result status:Passed/failed.

Below mentioned modules/packages need to install before running this code:

selenium
webdriver_manager.chrome
