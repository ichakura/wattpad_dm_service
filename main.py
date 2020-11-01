from flask import Flask, request, jsonify, render_template
from selenium import webdriver
from datetime import datetime
from multiprocessing import Process, Value
import time
import itertools
import sys
import threading
import os
import pickle
import webbrowser #for opening the 127.0.0.1 webpage, feature to be implemented :)

app = Flask(__name__)






#creating variables 
message_extract_list = []
from_them = []
from_me = []
splitlines = ""

@app.route('/')
def index():
    return render_template('main.html')
@app.route('/parse_data/', methods=['POST'])
def parse_data():
    if request.method == 'POST':
        names = request.get_json()
        print(names)
        messagedriver.find_element_by_xpath("//textarea[@placeholder='Write a message...']").send_keys(names)
        time.sleep(1)
        messagedriver.find_element_by_class_name('btn-orange').click()

@app.route('/messages/')
def record_loop():
    while True:
        try:
            #parsing logic----------------
            conversation = readdriver.find_elements_by_xpath('//div[@class="conversations"]')
            fromthem = readdriver.find_elements_by_class_name('from-other')
            fromme = readdriver.find_elements_by_class_name('from-me')

            for thing in conversation:
                splitlines = thing.text.splitlines()
            for thing in fromthem:
                from_them.append(thing.text)
            for thing in fromme:
                from_me.append(thing.text)
            
            similar_them = set(from_them) & set(splitlines)
            similar_me = set(from_me) & set(splitlines)

            for item in list(similar_them):
                temp_num = splitlines.index(item)
                splitlines[temp_num] = "Them: " + splitlines[temp_num]
            for item in list(similar_me):
                temp_num = splitlines.index(item)
                splitlines[temp_num] = "Me: " + splitlines[temp_num]
            #parsing logic----------------



            readdriver.refresh() #refreshes page for new parse

            return render_template('messages.html', messages=splitlines) #updates messages list by sending split lines, and is read from by index.html
        except:
            continue #this is horrible practice. you should never do this. as to why i'm doing it? because that's the only way it works...
    
if __name__ == '__main__':
    readdriver = webdriver.Chrome("chromedriver.exe")
    messagedriver = webdriver.Chrome("chromedriver.exe")
    done = False 
    def animate(): #for animation
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break                                                    
            sys.stdout.write('\rBooting ' + c)
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write('\rBegin!     ')
    t = threading.Thread(target=animate)
    t.start() #begins thread for animation

    readdriver.get("https://www.wattpad.com") #get to website
    messagedriver.get("https://www.wattpad.com") 

    login = pickle.load(open("login.pkl", "rb"))

    for cookie in login: #add cookies to instance
        readdriver.add_cookie(cookie) 
        messagedriver.add_cookie(cookie)

    readdriver.get("https://www.wattpad.com") #you have to do this to overcome the captcha check
    messagedriver.get("https://www.wattpad.com") 

    readdriver.get("URL TO DM HERE")
    messagedriver.get("URL TO DM HERE")

    done = True #ends animation




    p = Process(target=record_loop)
    p.start()  
    app.run(debug=True, host='0.0.0.0', use_reloader=False)
    p.join()
