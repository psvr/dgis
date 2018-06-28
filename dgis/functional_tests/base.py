from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Firefox()
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', chrome_options=chrome_options)
        self.driver = webdriver.Chrome('/usr/bin/chromedriver')

    def tearDown(self):
        self.driver.quit()

    def test_can_get_title(self):
        self.driver.get('http://127.0.0.1:8000')
        self.assertIn('DGIS', self.driver.title)
        self.fail('Finish the test')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
