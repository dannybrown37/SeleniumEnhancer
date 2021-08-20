# Installation

```
pip install selenium-enhancer
```

# Setting Up a Driver

[ChromeDriver](https://chromedriver.chromium.org/) is recommended as it has more options, but Firefox and IE drivers are compatible as well. Set the path to your chosen driver as a system environment variable named CHROME_DRIVER FIREFOX_DRIVER, or IE_DRIVER.

# Examples

See/run `examples.py` for usage examples.

# Miscellaneous

[PyPi](https://pypi.org/project/selenium-enhancer/)


# Updating PyPi (notes to self)

0. Commit to Git
1. Update version number in setup.py
2. `python setup.py sdist`
3. `twine upload --skip-existing dist/*`