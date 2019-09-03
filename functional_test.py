from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class HomePageTest(unittest.TestCase): # unittest.TestCase means we are inhering from TestCase class
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    # test methods are recognized by any method that starts with 'test'
    def test_home_page(self):
        # Nikkivisits a great to-do app site:
        self.browser.get('http://localhost:8000')

        # She sees the title and it matches with what she expected
        self.assertIn('To-Do', self.browser.title)

        # There is also a heading on the page where she can add here to-do items
        heading_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('My To Do List', heading_text)

        # she finds a spot to add a to-do items
        input_box = self.browser.find_element_by_id('id_new_item')

        # she sees grayed out text guiding her to enter text in that spot
        self.assertEqual(input_box.get_attribute('placeholder'),
            'Enter a to-do item')

        # she types in 'Stain deck stairs'
        input_box.send_keys('Stain deck stairs')
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        self.fail('Finish this test! - forcing to failing on purpose')

if __name__ == '__main__':
  unittest.main()
