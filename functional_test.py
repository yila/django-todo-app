from selenium import webdriver
import unittest

class HomePageTest(unittest.TestCase): # unittest.TestCase means we are inhering from TestCase class
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    # test methods are recognized by any method that starts with 'test'
    def test_home_page(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish this test! - forcing to failing on purpose')

if __name__ == '__main__':
  unittest.main()
