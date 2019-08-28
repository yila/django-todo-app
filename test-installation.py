import django
from selenium import webdriver

print('django version ' + django.get_version())
browser = webdriver.Chrome()
browser.get("http://www.google.com")
assert 'Google' in browser.title
browser.quit()
