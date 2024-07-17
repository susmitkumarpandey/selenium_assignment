
## Overview
This project demonstrates how to use Selenium WebDriver to automate the process of filling out a Google Form. The script opens a specified Google Form URL, enters data into various fields, and submits the form. If successful, it takes a screenshot of the submission confirmation page.

## Requirements
+ Python 3.10.1
+ Google Chrome browser
+ ChromeDriver
+ selenium
+ webdriver-manager

## Notes
The script uses implicitly_wait to wait for elements to load. Adjust the wait times as necessary for your internet speed and form complexity.
Ensure the XPath values in the script match the structure of the target Google Form. XPath values may need updating if the form structure changes.
The script captures a screenshot of the submission confirmation page. Review this screenshot to verify the form submission's success.

## Troubleshooting
If you encounter NoSuchElementException, check the XPath values to ensure they match the current form structure.
For WebDriverException, verify that ChromeDriver is correctly installed and matches the version of your Chrome browser.
