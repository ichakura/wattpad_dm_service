import pickle
import selenium.webdriver 

driver = selenium.webdriver.Firefox()
driver.get("http://www.google.com")
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
  * Messages cannot be sent with the enter key, you have to click the button to send a message
  * You MUST refresh the entire page in order to see new messages you were sent. (WTF)

And it was mainly to fix these two annoying problems that I created this program.
It was also mainly for me to learn web-scraping and Flask, and I like to think I achieved that. 

BUG FIXES TO ADD:
- [ ] (MAIN) Messages you send will be buried in requests, and as such will take too long to actually send
- [ ] Cannot currently select from all available DM's.
- [ ] Creating a user login file at first launch 
         * Currently, you must do the following:
        ```python
        
          import pickle
          import selenium.webdriver 

          driver = selenium.webdriver.Chrome("chromedriver.exe")
          driver.get("http://www.wattpad.com/")
          #YOU MUST LOG IN WITH YOUR CREDNETIALS, THEN RUN:
          pickle.dump( driver.get_cookies() , open("login.pkl","wb"))
        ```
   
