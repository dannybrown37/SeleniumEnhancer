# Installation

```
pip install selenium-enhancer
```

# Setting Up a Driver

On Linux/WSL, you can download the latest version of Chrome Driver to
the default location with this script: 

```bash
LATEST_VERSION=$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE) && 
wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$LATEST_VERSION/chromedriver_linux64.zip && 
sudo unzip /tmp/chromedriver.zip chromedriver -d selenium_enhancer/data/;
```

[ChromeDriver](https://chromedriver.chromium.org/) is recommended as it has 
more options, but Firefox and IE drivers are compatible as well. Set the 
path to your chosen driver as a system environment variable named 
CHROME_DRIVER, FIREFOX_DRIVER, or IE_DRIVER.

# Examples

See/run `examples.py` for usage examples.

# Miscellaneous

[PyPi](https://pypi.org/project/selenium-enhancer/)


# Getting Started

```python
from selenium_enhancer import SeleniumEnhancer

class ClassName(SeleniumEnhancer):

    def complete_web_form(self):
        self.start_chrome_driver()
        self.driver.get("full-url-of-page-with-form.com")
        self.set_input_elements({
            "id or CSS selector or XPath" : "value I want to set",
            "second id or CSS selector or XPath" : "second value"
        })
        self.set_select_elements({
            "name or id of select element" : "partial/complete text of option"
        })
        self.click_button("submitButtonId")


driver = ClassName()
driver.complete_web_form()
```



# Updating PyPi (notes to self)

1. Update version number in setup.py
2. Commit to Git
3. `python setup.py sdist`
4. `twine upload --skip-existing dist/*`