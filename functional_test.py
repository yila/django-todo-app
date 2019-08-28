from selenium import webdriver
import unittest

class HomePageTest(unittest.TestCase): # unittest.TestCase means we are inhering from TestCase class
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()
        
    # test methods are recognized by any method that starts with 'test'
    def test_home_page(self):
        browser.get('http://localhost:8000')
        self.assertIn('To-Do', browser.title)

if __name__ == '__main__':
  unittest.main()
