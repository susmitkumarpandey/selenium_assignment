
## Overview
This project demonstrates how to use Selenium WebDriver to automate the process of filling out a Google Form. The script opens a specified Google Form URL, enters data into various fields, and submits the form. If successful, it takes a screenshot of the submission confirmation page. Then it sends a mail to the recipent after getting some inputs from the user using a form. 

## Requirements
+ Python 3.10.1
+ Google Chrome browser
+ ChromeDriver
+ selenium
+ webdriver-manager
+ smtp
+ flask
+ bootstrap5

## Notes
The script uses implicitly_wait to wait for elements to load. Adjust the wait times as necessary for your internet speed and form complexity.
Ensure the XPath values in the script match the structure of the target Google Form. XPath values may need updating if the form structure changes.
The script captures a screenshot of the submission confirmation page. Review this screenshot to verify the form submission's success.
Then it takes some information from the users using a flaskform anda sends them a mail of the user details.

## Troubleshooting
If you encounter NoSuchElementException, check the XPath values to ensure they match the current form structure.
For WebDriverException, verify that ChromeDriver is correctly installed and matches the version of your Chrome browser.
