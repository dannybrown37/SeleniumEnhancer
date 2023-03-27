from selenium_enhancer.selenium_enhancer import SeleniumEnhancer


class ExampleCases(SeleniumEnhancer):

    def __init__(self):

        self.example_google_search()
        self.example_web_form_text_input_manipulation()


    def example_google_search(self):
        """ An example of a simple Google search. 
        
            Note the use of XPath selectors, as these elements don't 
            have id attributes. 
        """

        self.start_chrome_driver(detach=True)
        # detach=True keeps the browser open after program ends

        # built-in Selenium method to go to web page
        self.driver.get("https://www.google.com")

        # Enter search term, click "I'm Feeling Lucky button"
        self.set_input_elements({"//input[@name='q']" : "Selenium Enhancer"})
        self.click_button("//input[@name='btnI']") # I'm Feeling Lucky
        
        # Close the driver when you're finished. 
        self.driver.close()

    
    def example_web_form_text_input_manipulation(self):
        """
            An example of completing a webform. 

            Note how multiple input boxes can be completed with one
            method call.
        """

        self.start_chrome_driver(detach=True)
        self.driver.get("https://www.w3schools.com/html/html_forms.asp")

        # Clear default text from name boxes        
        self.clear_input_element("fname")   # fname = id of input element
        self.clear_input_element("lname")
        
        # Enter text into form
        self.set_input_elements({
            "fname" : "Robert Nesta",
            "lname" : "Marley"
        })
        
        # Submit the form
        self.click_button("//input[@value='Submit']")
        
        self.driver.close()


def test_basic_usage():
    ExampleCases()