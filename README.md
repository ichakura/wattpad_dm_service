# wattpad_dm_service
# Uses web scraping in order to fix many problems with Wattpad DM's

So the current Wattpad DM Service is pretty much hot garbage. I'll go ahead and line out a few problems now: 
  
  * Messages cannot be sent with the enter key, you have to click the button to send a message
  * You MUST refresh the entire page in order to see new messages you were sent. (WTF)


BUG FIXES TO ADD:
- [ ] (MAIN) Messages you send will be buried in requests, and as such will take too long to actually send
- [ ] Cannot currently select from all available DM's.
- [ ] Creating a user login file at first launch. Currently, you must do the following:
        ```python
        
          import pickle
          import selenium.webdriver 

          driver = selenium.webdriver.Chrome("chromedriver.exe")
          driver.get("http://www.wattpad.com/")
          #YOU MUST LOG IN WITH YOUR CREDNETIALS, THEN RUN:
          pickle.dump( driver.get_cookies() , open("login.pkl","wb"))
        
   
