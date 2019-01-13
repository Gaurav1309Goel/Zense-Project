# Zense-Project
## Python Automation using Selenium & Scheduling of messages and media

**Objective:**

> This project can be used to Automate Whatsapp through Whatsapp through Whatsapp Web, Facebook messenger and Yahoo mail. We can add number of contacts whom we want to send messages or media attachments(like Video or Images or GIFs). Selenium, AutoIt and Schedule have been used one from Automation and other for Scheduling messages.

**Uses:**
 
> We can schedule Good Morning or Good Night messages with a nice Picture at a particular time to our loved ones. We can set timings. Suppose at 12 o'clock you want to wish your friend Happy Birthday so schedule your messages and sleep.

## Installation Required:
    If you are using Python 2.7.13 use pip instead of pip3
    
    $ pip3 install -r requirements.txt
            OR
    $ pip3 install selenium
    $ pip3 install schedule
    $ pip3 install PyAutoIt
**Platform for Windows:**

> ChromeDriver used: If this version becomes outdated or gives problem download latest version from [Download Link](http://chromedriver.chromium.org/downloads).
      
**Platform for MacOs:**
 
 ###### Remove ChromeDriverused in repository and install Mac ChromeDriver.
>Set ChromeDriver path in function whatsapp() [Set ChromeDriver Path](https://stackoverflow.com/questions/44870294/selenium-chromedriver-in-relative-path-for-mac-and-python/44870398#44870398)

**For Sending Attachments you need to Install AutoIt (If you only what to send messages not to install AutoIt) | (Only FOR WINDOWS USERS):**

###### Installation is pretty Simple no changes in setting are required keep everything default. Few clicks on Next and you are done.
>[To download AutoIt](https://www.autoitscript.com/site/autoit/downloads/)

**NOTE: For Unsaved Contacts:**

Do enter your country code then contact number.
>Use: 919899123456

>Don't Use: +919899123456

**input_message()**

In this function we take input of message to send to all the Contacts list from user.
>Example: Good Morning

**Your choice to schedule to message or not:**

do you want to schedule your message(Yes/No):Yes

>input time in 24 hour (HH:MM) format - 13:13

**Your choice to send attachment or not:**

Would you like to send attachment(yes/no):yes

>Answer the input with yes or no

**sending_attachments():**
 
NOTE: Add Photos & Videos in the Media Folder.

>image_path = os.getcwd() +"\Media\" + 'goodmorning.jpg'

Example path to send goodmorning image to your listed Contacts.

"hour1" variable is used to check current Hour on the clock and according image is sent to the Contact.

- If time is after 6 and before 11am schedule goodmorning.jpg image.
- If time is after 9pm schedule goodnight image.
- If time is anyother send howareyou image.
- You can set your own photos at a particular time feel free to do that.

**sending_files():**

NOTE: Add the document in the documents folder.

- Would you file to send a Document file(yes/no): yes

>Enter the Document file name you want to send: attendance
>If the document file names are same then write the document name with extension attendance.txt or attendance.pdf

**Schedule Message and Attachments:**

schedule.every().Monday.at("06:00").do(sender)

schedule.every().Tuesday.at("07:00").do(sender)

schedule.every().Friday.at("07:30").do(sender)

schedule.every().day.at("08:30").do(sender)

- You can make change these schedule days and time according to you. 
