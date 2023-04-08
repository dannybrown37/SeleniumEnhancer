# Installation

```
pip install selenium-enhancer
```

# Setting Up a Driver

After installing or whenver you need to update to the latest version of
ChromeDriver, run:

```
python -m selenium_enhancer.get_latest_chrome_driver
```

[ChromeDriver](https://chromedriver.chromium.org/) is recommended as it has 
more options, but Firefox and IE drivers are in theory compatible as well.
Please feel free to contribute if you need additional functionality.

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

# Examples

If you're cloning the repo to contribute, you can run/view/add to the tests
with at ``pytest tests -s -vv``.

# Miscellaneous

[PyPi](https://pypi.org/project/selenium-enhancer/)


# Updating PyPi (notes to self)

1. Update version number in setup.py
2. Commit to Git
3. `python setup.py sdist`
4. `twine upload --skip-existing dist/*`