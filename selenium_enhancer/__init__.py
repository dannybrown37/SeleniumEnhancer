__version__ = '0.2.22'

try:
    from .selenium_enhancer import SeleniumEnhancer
except ModuleNotFoundError:
    pass  # this will fail on `pip install .`, but allows for shorter import