How To Run Tests

1)Install all requirements in terminal:
$  pip3 install -r requirements.txt

2)Download Selenium WebDriver from https://chromedriver.chromium.org/downloads (choose version which is compatible with your browser)

3)Run tests:
$ python3 -m pytest -v --driver Chrome --driver-path "xpath to your chromedriver"
