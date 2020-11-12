# Otus functional test challenge

# Requirements

* https://selenium-python.readthedocs.io/getting-started.html

* python version 3.8.5
* install selenium 'pip install selenium'
* install a webdriver for chrome
* move webdriver to C:\Windows
* possible issue running chromedriver with bluetooth settings

# Running

* **Update the credentials.py file with what will be used for testing.**
  * Default - new student with no classes
  * Enrolled - student enrolled in the interview class "QA Tech Challenge"
* Major caveat - the enrolled student must be assigned to the class given in the interview.
* There are two test files. Run tests with:
  * 'python -m unittest test_enrolled.py'
  * 'python -m unittest test_unenrolled.py'

# Resources

* https://sites.google.com/a/chromium.org/chromedriver/getting-started
* https://sites.google.com/a/chromium.org/chromedriver/home
* https://selenium-python.readthedocs.io/installation.html


# Notes

* I couldn't get the .env to work, so I created credentials.py and ignored it.
