How To Run Tests

Install all requirements:

pip3 install -r requirements.txt

Download Selenium WebDriver from https://chromedriver.chromium.org/downloads (choose version which is compatible with your browser)

Run tests:

python3 -m pytest -v --driver Chrome --driver-path "xpath to your chromedriver"
