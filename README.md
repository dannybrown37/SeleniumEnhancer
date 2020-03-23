Install using:

```
pip install SeleniumEnhancer
```

Help on module selenium_helper:

NAME
    selenium_helper

CLASSES
    builtins.object
        SeleniumHelper
    
    class SeleniumHelper(builtins.object)
     |  A parent class that assists with Selenium testing and automation.
     |  
     |  This class is built to be inherited by more specialized tasks that
     |  will benefit from the Selenium web driver functionality within.
     |  
     |  Methods are arranged alphabetically for value.
     |  
     |  Methods defined here:
     |  
     |  accept_simple_alert(self)
     |      Method method clicks the OK button in a pop-up alert.
     |  
     |  attach_image_file_to_input(self, input_id, img_path)
     |      Method to attach an image file to input with type="file".
     |      
     |      Requires two strings: a partial/unique id of an input element
     |      and the path of an image file (relative to working directory).
     |  
     |  check_box(self, checkbox_id, uncheck=False, return_status=False)
     |      Method's default behavior is to check unchecked boxes.
     |      
     |      Requires a string equal to a partial/unique id or XPath.
     |      
     |      * Optional arguments/behavior *
     |      uncheck=True -- will instead uncheck a checked box.
     |      return_status=True -- instead returns checked status
     |  
     |  check_for_presence_of_element(self, element_id)
     |      Method returns True if element exists or False if not.
     |      
     |      Takes partial but unique ID, XPath, or CSS selector.
     |  
     |  clear_input_element(self, element_id)
     |      Method to clear an input element.
     |      
     |      Requires a string equal to a partial/unique id or XPath.
     |  
     |  click_button(self, identifier, dbl_click=False, no_js=False)
     |      Method to click an element (with JavaScript by default).
     |      
     |      Requires a string identifier that can be a partial/unique
     |      id, CSS selector, or XPath.
     |      
     |      * Optional arguments/behavior *
     |      dbl_click=True --  double clicks the element.
     |      no_js=True -- mimic user click rather than click with JS
     |  
     |  get_text_from_element(self, element_id, input=False)
     |      Method returns text from an element.
     |      
     |      Requires a string identifier that can be a partial/unique
     |      id, CSS selector, or XPath.
     |      
     |      If trying to get the current text/value from an input
     |      element, include `input=True` to do so.
     |  
     |  get_text_of_current_selection(self, element_id)
     |      Method returns selected text from a select element.
     |      
     |      Takes an id only (for now).
     |  
     |  set_input_elements(self, data)
     |      Method to set any number of text input elements on a page.
     |      
     |      Requires a dictionary with at least one key-value pair but
     |      can be any size. Keys must be an identifier that can be a
     |      partial/unique id or XPath. Values should be the desired
     |      text corresponding to each identifier.
     |  
     |  set_select_elements(self, data)
     |      Method to choose any number of select elements on a page.
     |      
     |      Requires a dictionary with at least one key-value pair but
     |      can be any size. Keys must be an identifier that can be a
     |      partial/unique ~name~. Values should be the text of the
     |      desired option to select.
     |  
     |  start_chrome_driver(self, detach=False, headless=False, ga_debug=False)
     |      Method to start the Chrome driver with specified options. 
     |      
     |      This is where I do most of my work and thus has the most
     |      extensive option list.
     |  
     |  start_firefox_driver(self)
     |      Method to start the Firefox driver with specified optons.
     |  
     |  start_ie_driver(self)
     |      Method to start the Internet Explorer driver.
     |  
     |  switch_to_iframe(self, iframe_id)
     |      Method to switch to an iframe on a page.
     |      
     |      Requires a string identifier that can be a partial/unique
     |      id or Xpath.
     |  
     |  wait_for_page_load(self, timeout=10)
     |      Method to wait for page to load before continuing.
     |      
     |      This method checks for the staleness of the old page
     |      (i.e., that the new page has loaded) prior to moving
     |      forward with further actions. Therefore, it only
     |      works in situations where the URL changes between
     |      page loads. 
     |      
     |      Usage:
     |      
     |      with self.wait_for_page_load():
     |          # click a button or do whatever
     |      # do the next thing that was failing before using this
     |      
     |      Thanks to ObeyTheTestingGoat for this delightfully
     |      borrowed method!
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)




