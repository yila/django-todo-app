from selenium import webdriver
import unittest

class HomePageTest(unittest.TestCase): # unittest.TestCase means we are inhering from TestCase class

  # test methods are recognized by any method that starts with 'test'
  def test_home_page(self):
    browser = webdriver.Chrome()
    browser.get('http://localhost:8000')
    self.assertIn('To-Do', browser.title)
    browser.quit()

if __name__ == '__main__':
  unittest.main()
