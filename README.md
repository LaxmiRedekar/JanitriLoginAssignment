This project contains Selenium automation test cases for the Janitri Dashboard Login Page.
The scripts are written in Python using Selenium WebDriver.

**Features Tested**:
1. Valid Login – Written with sample email/password (since no real credentials were given).
2. Missing Email – Only password entered.
3. Missing Password – Only email entered.
4. Missing Email & Password – Both fields empty.
5. Password Masking/Unmasking – Validate password toggle feature.
6. Invalid Email Pattern – Wrong email format check.
7. Case Sensitivity – Check login with uppercase email.
8. Password Toggle Value Check – Ensure password value doesn’t change when unmasked.

**Tools & Tech Stack**
Language: Python
Automation Tool: Selenium WebDriver
Browser: Chrome
IDE: PyCharm

**How to Run**
Clone this repository:
git clone https://github.com/LaxmiRedekar/JanitriLoginAssignment.git

Install dependencies (make sure you have Python 3 and pip):
pip install selenium

Run the script:
python LoginPage.py
