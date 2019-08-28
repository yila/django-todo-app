# Required Installation

* Python 3.6
* Git
* A headless browser driver: Chrome - chromedriver, Firefox - firefoxdriver, etc.
* geckodriver (firefox only)
* Django - <code>pip install "django<2"</code>
* Selenium - <code>pip install selenium</code>

# Sanity Check
## Python and Django Installation
* Activate your virtual env:
<code>source [virtualEnvFolder]/bin/activate</code>

<code>
(project location)$python

Python 3.6.0 (default, Aug 27 2019, 11:43:14)<br/>
[GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.10.44.4)] on darwin<br/>
Type "help", "copyright", "credits" or "license" for more information.<br/>
\>>> import django<br/>
\>>> print(django.get_version())<br/>
1.11.x
</code>

## Selenium and Browser Driver Installation
Create a python file called **test-installation.py**.  Add following to it:

<code>
from selenium import webdriver<br/>
browser = webdriver.Chrome() #you need to have chromedriver installed<br/>
browser.get('http://www.google.com')<br/>
print(browser.title) # this should print "Google" in console (terminal)<br/>
browser.quit()<br/>
</code>

Run the **test-installation.py** file.  If everything is installed correctly you should see 'Google' print in the terminal.
<code>python test-installation.py</code>
