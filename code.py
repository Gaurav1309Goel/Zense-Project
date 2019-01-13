from datetime import datetime
from time import gmtime, strftime

import schedule
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

try:
    import autoit
except:
    pass

import time
import datetime
import os

Contact = []
unsaved_Contact = []
message = []
Choice1 = None
Choice2 = None
document_filename = None

# for taking time into refrence
showtime = strftime("%Y %m %d %H %M %S", gmtime())
var2 = []
showtime += " "
s2 = ""
for j in range(len(showtime)):
    if showtime[j] != " ":
        s2 += showtime[j]
    else:
        var2.append(s2)
        s2 = ""

if (int(var2[3]) >= 18):
    if int(var2[3]) == 18:
        if int(var2[4]) >= 30:
            date1 = int(var2[2]) + 1
        else:
            date1 = int(var2[2])
    else:
        date1 = int(var2[2]) + 1
else:
    date1 = int(var2[2])

year1 = int(var2[0])
month1 = int(var2[1])
hour1 = int(var2[3])
minute1 = int(var2[4])
second1 = int(var2[5])


# taking input of contacts
def input_contacts():
    # list of Contacts
    while True:
        # Enter the choice a or b
        print("Please Choose One of the Options:\n")
        print("a.Message to Saved Contact Number\n")
        print("b.Message to Unsaved Contact Number\n")
        x = input("Enter choice a or b:\n")
        print()
        if x == "a":
            n = int(input('Enter the number of Contacts '))
            print()
            for i in range(0, n):
                name = input("Enter contact name ")
                Contact.append(name)
        elif x == "b":
            n = int(input('Enter the number of unsaved contacts '))
            print()
            for i in range(0, n):
                name = input("Enter the contact number")
                unsaved_Contact.append(name)

        more_choice = input("Do you want to add more contacts(yes/no)->")
        if more_choice == "no":
            break
        else:
            if x == "a":
                n = int(input('Enter the number of Contacts'))
                print()
                for i in range(0, n):
                    name = input("Enter contact name ")
                    Contact.append(name)
            elif x == "b":
                n = int(input('Enter the number of unsaved contacts '))
                print()
                for i in range(0, n):
                    name = input("Enter the contact number")
                    unsaved_Contact.append(name)

        # printing saved contacts or unsaved contacts added
        if len(Contact) != 0:
            print("\nSaved contacts enetered ", Contact)
        if len(unsaved_Contact) != 0:
            print("\nUnsaved contacts entered ", unsaved_Contact)
        input("\nPress Enter to start...")


# taking input for message
def input_message():
    print()
    print("Enter the message and use the symbol '#' to end the message:\n")
    message_to_be_send = ""
    completed = False

    while not completed:
        message_to_be_send = input()
        if len(message_to_be_send) != 0 and message_to_be_send[-1] == "#":
            completed = True
            message.append(message_to_be_send[:-1])
        else:
            print("Type again: \n")
            message_to_be_send = ""
            message_to_be_send = input()
            message.append(message_to_be_send[:-1])
            completed = True

    print()
    print(message)


# loging in to whatsapp
def whatsapp():
    global driver, wait
    driver = webdriver.Chrome("..\drivers\chromedriver.exe")
    time.sleep(3)
    driver.get("https://web.whatsapp.com/")
    driver.maximize_window()
    time.sleep(3)
    print("Qr scanned")


# mechanism to send message
def sending_message(i):
    try:
        # searching name of that person
        search = driver.find_element_by_css_selector('label._2MSJr')
        search.send_keys(Contact[i])
        search.send_keys(Keys.ENTER)

        # sending message
        search1 = driver.find_element_by_class_name('_1Plpp')
        search1.send_keys(message)
        driver.find_element_by_xpath("//span[@data-icon='send']").click()

        # sending emoji
        if sending_emoji == "yes":
            searchx = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[1]")
            searchx.click()
            time.sleep(2)

            searchy = driver.find_element_by_xpath(
                "//*[@id='main']/footer/div[2]/div/div[3]/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/span")
            searchy.click()
            time.sleep(2)

            searchz = driver.find_element_by_class_name('_35EW6')
            searchz.click()
            time.sleep(2)

        # sending GIF related to message
        if sending_gif == "yes":
            searchn = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[1]")
            searchn.click()
            time.sleep(2)

            searchf = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[1]/div/div[3]/button/span")
            searchf.click()
            time.sleep(3)

            searche = driver.find_element_by_xpath(
                "//*[@id='main']/footer/div[2]/div/div[3]/div/div[2]/div/span/div/label/div/input")
            searche.send_keys(topic)
            time.sleep(3)

            searcht = driver.find_element_by_xpath(
                "//*[@id='main']/footer/div[2]/div/div[3]/div/div[2]/div/div/div/div/div[1]/div[1]/div/div/video")
            searcht.click()
            time.sleep(3)

            searchu = driver.find_element_by_xpath(
                "//*[@id='app']/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span[2]/div/div")
            searchu.click()
            time.sleep(2)

        print("Message sent successfuly")
    except NoSuchElementException:
        print("Message not sent")


# mechanism to send messages to unsaved contacts
def sending_message_to_unsaved_contacts(i):
    try:
        # searching the unsaved number
        inputing = driver.find_element_by_css_selector('label._2MSJr')
        inputing.send_keys(unsaved_Contact[i])
        inputing.send_keys(Keys.ENTER)

        # sending message
        search1 = driver.find_element_by_class_name('_1Plpp')
        search1.send_keys(message)
        driver.find_element_by_xpath("//span[@data-icon='send']").click()

        # sending emoji
        if sending_emoji == "yes":
            searchx = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[1]")
            searchx.click()
            time.sleep(2)

            searchy = driver.find_element_by_xpath(
                "//*[@id='main']/footer/div[2]/div/div[3]/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/span")
            searchy.click()
            time.sleep(2)

            searchz = driver.find_element_by_class_name('_35EW6')
            searchz.click()
            time.sleep(2)

        # sending GIF related to message
        if sending_gif == "yes":
            searchn = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[1]")
            searchn.click()
            time.sleep(2)

            searchf = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[1]/div/div[3]/button/span")
            searchf.click()
            time.sleep(3)

            searche = driver.find_element_by_xpath(
                "//*[@id='main']/footer/div[2]/div/div[3]/div/div[2]/div/span/div/label/div/input")
            searche.send_keys(topic)
            time.sleep(3)

            searcht = driver.find_element_by_xpath(
                "//*[@id='main']/footer/div[2]/div/div[3]/div/div[2]/div/div/div/div/div[1]/div[1]/div/div/video")
            searcht.click()
            time.sleep(3)

            searchu = driver.find_element_by_xpath(
                "//*[@id='app']/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span[2]/div/div")
            searchu.click()
            time.sleep(2)

        print("Message sent successfuly")
    except NoSuchElementException:
        print("Failed to send message")


def sending_attachments():
    # Attachment Drop Down Menu
    clipart = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div/span')
    clipart.click()
    time.sleep(4)

    # To send Videos and Images.
    media = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button')
    media.click()
    time.sleep(4)

    hour1 = datetime.datetime.now().hour

    # After 6am and before 11am scheduled this.
    if (hour1 >= 6 and hour1 <= 11):
        image = os.getcwd() + "\\Downloads\\" + 'goodmorning.jpg'

    # After 9pm and before 10pm schedule this
    elif (hour1 >= 21 and hour1 <= 23):
        image = os.getcwd() + "\\Downloads\\" + 'goodnight.jpg'

    else:
        image = os.getcwd() + "\\Downloads\\" + 'howareyou.jpg'
        print("a")
        print(image)

    autoit.control_focus("Open", "Edit1")  # seen from github
    print("a")
    autoit.control_set_text("Open", "Edit1", (image))  # seen from github of an user from US
    print("a")
    autoit.control_click("Open", "Button1")  # seen from github of an user from US
    print("a")
    time.sleep(3)
    send_button = driver.find_element_by_xpath(
        '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span[2]/div/div/span')
    send_button.click()


# Function to send Documents(PDF, Word file, PPT, etc.)
def sending_files():
    # Attachment Drop Down Menu
    clip = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div/span')
    clip.button()
    time.sleep(1)
    print("a")

    # To send a Document(PDF, Word file, PPT)
    doc = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/ul/li[3]/button')
    doc.click()
    time.sleep(2)
    print("a")

    doc_path = os.getcwd() + "\\Documents\\" + document_filename  # seen from github
    autoit.control.focus("Open", "Edit1")  # seen from github
    autoit.control_set_text("Open", "Edit1", (doc_path))  # seen from github
    autoit.control_click("Open", "Button1")  # seen from github

    time.sleep(3)
    whatsapp_sending_button = driver.find_element_by_xpath(
        '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span[2]/div/div/span')
    whatsapp_sending_button.click()


# sending through messenger
def sending_via_messenger():
    # opening facebook so it can reach upto that person profile and message can be sent by clicking on message button
    driver = webdriver.Chrome("..\drivers\chromedriver.exe")
    driver.maximize_window()
    time.sleep(3)
    driver.get("https://facebook.com")

    # loging in and password details
    search2 = driver.find_element_by_id('email')
    search2.send_keys(your_mail)
    search3 = driver.find_element_by_id('pass')
    search3.send_keys(your_password)
    driver.find_element_by_id('loginbutton').click()
    time.sleep(3)
    driver.find_element_by_class_name('_3ixn').click()
    time.sleep(3)

    # searching name of the person I am unable to reach upto last step in messenger as it is blocked by facebook so last step of messaging only be done by user.
    search4 = driver.find_element_by_class_name('_1frb')
    search4.send_keys(username)
    time.sleep(2)
    search4.send_keys(Keys.ENTER)
    time.sleep(2)
    driver.find_element_by_id('u_0_k').click()
    time.sleep(3)
    search5 = driver.find_element_by_xpath("//a[text()='{0}']".format(username))
    search5.click()
    time.sleep(4)


# sending through mail
def sending_mail():
    # yahoo opening
    driver = webdriver.Chrome("..\drivers\chromedriver.exe")
    time.sleep(3)
    driver.maximize_window()
    time.sleep(3)
    driver.get("https://login.yahoo.com")

    # loging in and password filling
    search7 = driver.find_element_by_id('login-username')
    search7.send_keys(your_mail)
    driver.find_element_by_id('login-signin').click()
    time.sleep(2)
    search8 = driver.find_element_by_id('login-passwd')
    search8.send_keys(your_password)
    driver.find_element_by_id('login-signin').click()
    driver.find_element_by_id('mega-bottombar-mail').click()

    # composing mail
    driver.find_element_by_xpath("//a[text()='Compose']").click()
    search9 = driver.find_element_by_xpath("//*[@id='message-to-field']")
    search9.send_keys(mail)
    search10 = driver.find_element_by_xpath("//*[@id='mail-app-component']/div[1]/div/div[1]/div[3]/div/div/input")

    # subject for mail
    search10.send_keys(subject)

    # writing mail
    search11 = driver.find_element_by_class_name('rte')
    search11.send_keys(message)

    # mail sent
    driver.find_element_by_xpath("//span[text()='Send']").click()
    driver.quit()


def sending():
    for i in range(0, len(Contact)):
        sending_message(i)
        print("Message sent to ", Contact[i])
        if (Choice1 == "yes"):
            try:
                sending_attachments()
            except:
                print('Attachment not sent.')
        if (Choice2 == "yes"):
            try:
                sending_files()
            except:
                print('Files not sent')
    time.sleep(5)
    if len(unsaved_Contact) > 0:
        for i in unsaved_Contact:
            link = "https://wa.me/" + i
            sending_message_to_unsaved_contacts(i)

            # driver  = webdriver.Chrome()
            driver.get(link)
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="action-button"]').click()
            time.sleep(4)
            print("Sending message to", i)

            sending_message_to_unsaved_contact()
            if (Choice1 == "yes"):
                try:
                    sending_attachments()
                except:
                    print('Attachment not sent.')
            if (Choice2 == "yes"):
                try:
                    sending_files()
                except:
                    print('Files not sent')
            time.sleep(7)

    driver.quit()


# For GoodMorning Image and Message
schedule.every().day.at("06:00").do(sending)
# For How are you message
schedule.every().day.at("14:00").do(sending)
# For GoodNight Image and Message
schedule.every().day.at("23:00").do(sending)
# Example Schedule for a particular day of week Monday
schedule.every().monday.at("06:00").do(sending)


def scheduler():  # seen from github as an refrence
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    print(
        "                                                                                 WELCOME                    \n")
    print(
        "                                                SELECT AS PER REQUIREMENT TO SEND MESSAGE OR IMAGE OR VIDEOS OR GIFs...     \n")
    print(
        "                                                                    VIA FACEBOOK, WHATSAPP, YAHOO MAIL...        \n ")
    print(
        "                                                                          TO COMPLETE YOUR TASK             \n ")
    print()

    # to send via whatsapp
    to_send_whatsapp_message = input('Do you want to send whatsapp message(Yes/No)->\n')
    if (to_send_whatsapp_message == "Yes"):
        input_contacts()
        input_message()
        print("SCAN YOUR QR FOR WHATSAPP WEB")
        whatsapp()
    Choice1 = input("Would you like to send attachment(yes/no): ")
    Choice2 = input("Would you like to send a Document file(yes/no): ")
    sending_gif = input("Would you like to send any gif(yes/no): ")
    sending_emoji = input("Would you like to send any emoji(yes/no): ")
    if Choice2 == "yes":
        document_filename = input("Enter the Document file name you want to send: ")
    if sending_gif == "yes":
        topic = input("Your motive of message so I can search for GIF: ")
    to_schedule = input('Do you want use schedule for messaging(Yes/No): \n')
    if (to_schedule == "Yes"):
        time_to_send_message = input('input time in 24 hour (HH:MM) format: \n')
        schedule.every().day.at(time_to_send_message).do(sending)
    else:
        sending()
    if (to_schedule == "Yes"):
        scheduler()

# to send via mail
to_send_mail = input('Do you want to send mail(Yes/No)->\n')
if (to_send_mail == "Yes"):
    your_mail = input('Please enter your mail: ')
    your_password = input('Enter your password: ')
    mail = input('Enter email of person: ')
    subject = input('Subject for your content: ')
    sending_mail()

# to send via facebook messenger
to_send_facebook = input('Do you want to send message through messenger(yes/no): ')
if (to_send_facebook == "yes"):
    your_mail = input('Please enter your mail: ')
    your_password = input('Please enter your Password for Facebook: ')
    username = input('Please enter the Username of the other Person: ')
    sending_via_messenger()

print("Task Completed")
