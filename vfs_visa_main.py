
import sys
import logging
import subprocess
from sys import argv

from logging.config import fileConfig
import random
from ReadConfig import _ConfigReader

from cmath import exp
import email
import time
import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import smtplib
from email.mime.text import MIMEText

import pyautogui

mail_host = 'xxxx.xx.xx'
mail_user = 'XXXXXXXXX@email'
mail_pass = "password"
sender = 'XXXXXXXXX@email'
receivers = ['XXXXXXXXX@email','XXXXXXXXX@email']

global web_driver
global email_count
global WiFi_count
email_count, WiFi_count = 0, 0
global WiFi_List

def _check_load():
    try:
        WebDriverWait(web_driver,60,0.5).until_not(EC.visibility_of_element_located(("xpath", "//*[@id='loader']")))
        WebDriverWait(web_driver,60,0.5).until_not(EC.visibility_of_element_located(("xpath", "//ngx-ui-loader/div[1]/div[2]")))
        time.sleep(1)
        WebDriverWait(web_driver,90,0.5).until_not(EC.visibility_of_element_located(("xpath", "//*[@id='loader']")))
        WebDriverWait(web_driver,90,0.5).until_not(EC.visibility_of_element_located(("xpath", "//ngx-ui-loader/div[1]/div[2]")))
        return True
    except:
        logging.debug("Time out")
        raise Exception("Time out")

def _chech_login(dtimes = "Second"):
    try:
        WebDriverWait(web_driver,1,0.1).until_not(EC.element_to_be_clickable(("xpath", "/html/body/app-root/div/app-login/section/div/div/mat-card/form/button/span[1]")))
        return True
    except:
        logging.info("Logging {}".format(dtimes))
        return False
        # raise Exception("Time out")


def _check_config():
    if len(visa_centre) != len(visa_centre_num):
        logging.info("the number of visa_centre is {}, while the number of visa_centre_num is {}".format(len(_VFSemail),len(_VFSpassword)))
        exit()
    if len(category) != len(category_num):
        logging.info("the number of category is {}, while the number of category_num is {}".format(len(_VFSemail),len(_VFSpassword)))
        exit()
    if len(sub_category) != len(sub_category_num):
        logging.info("the number of sub_category is {}, while the number of sub_category_num is {}".format(len(_VFSemail),len(_VFSpassword)))
        exit()
    Num_visa_centre, Num_category, Num_sub_category = len(visa_centre),len(category),len(sub_category)
    if Num_visa_centre != Num_category:
        logging.info("the number of visa_centre is {}, while the number of category is {}".format(len(_VFSemail),len(_VFSpassword)))
        exit()
    if Num_visa_centre != Num_sub_category:
        logging.info("the number of visa_centre is {}, while the number of sub_category is {}".format(len(_VFSemail),len(_VFSpassword)))
        exit()
    if len(_VFSemail) != len(_VFSpassword):
        logging.info("the number of _VFSemail is {}, while the number of _VFSpassword is {}".format(len(_VFSemail),len(_VFSpassword)))
        exit()


def countdown(t):
    while t > -1:
        timer = 'Retry after {:02d} seconds'.format(t)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

def _init_web_driver():
        global web_driver
        firefox_options = Options()

        web_driver = webdriver.Chrome()

        web_driver.maximize_window()
        # time.sleep(0.1)
        # print(agent)
        
def _open_web(country):
    global web_driver
    global vpn_state
    open_web = False
    count_web = 90
    if country == "GERMANY":
        web_site = "https://visa.vfsglobal.com/chn/en/deu/login"
    elif country == "ITALY":
        web_site = "https://visa.vfsglobal.com/chn/en/ita/login"

    try:
        if (vpn_state == 0):
            vpn_state = 1
            time.sleep(2)
        web_driver.get(web_site)
    except:
        logging.debug("Can not get {}".format(country))
        raise Exception("Can not get {}".format(country))
    # try:
    #     WebDriverWait(web_driver,300,1).until(EC.element_to_be_clickable(("xpath", "//button/span")))
    #     time.sleep(5)
    # except:
    #     logging.debug("Can not load {}".format(country))
    #     raise Exception("Can not load")

def _start_newbooking():
    try:
        WebDriverWait(web_driver,1,0.2).until(EC.element_to_be_clickable(("xpath", "//section/div/div[2]/button/span")))
        # time.sleep(5)
        if _check_load():
            _new_booking_button = web_driver.find_element(
                        "xpath", "//section/div/div[2]/button/span"
                    )
            _new_booking_button.click()
    except:
        logging.debug("Start Fail")
        raise Exception("Start Fail")

def _login():
    global web_driver
    global email_count
    global vpn_state
    if _check_load():
        try:
            if vpn_state == 1:
                vpn_state = 0
            _email_input = web_driver.find_element("xpath", "//input[@id='mat-input-0']")
            _email_input.send_keys(_VFSemail[email_count])
            _password_input = web_driver.find_element("xpath", "//input[@id='mat-input-1']")
            _password_input.send_keys(_VFSpassword[email_count])
            # _accept_button = web_driver.find_element("xpath", "//*[@id='onetrust-accept-btn-handler']")
            # _accept_button.click()
            _login_button = web_driver.find_element("xpath", "//button/span")
            _login_button.click()
        except:
            logging.debug("Can not load")
            raise Exception("Can not load")
    if _check_load():
        login_times = 1
        while not _chech_login("{}".format(login_times)) and login_times <= 6:
            # time.sleep(1)
            try:
                _login_button = web_driver.find_element("xpath", "//button/span")
                _login_button.click()
            except:
                logging.debug("Can not load")
                raise Exception("Can not load")
            login_times = login_times + 1
            if _check_load():
                continue
        if _check_load():
            _start_newbooking()

    


# def _change_WiFi_email():
#     global email_count
#     global WiFi_count
#     global WiFi_List
#     email_count = (email_count + 1) % len(_VFSemail)

def _get_appointment_date_new(index):
    global web_driver
    logging.info(
            "Getting appointment date: Visa Centre: {}, Category: {}, Sub-Category: {}".format(
                visa_centre[index], category[index], sub_category[index]
            )
        )
    #--- centre ---#
    if visa_centre_num[index] != '0':
        if _check_load():
            try:
                WebDriverWait(web_driver,2,1).until(EC.element_to_be_clickable(("xpath", "//mat-form-field/div/div/div[3]")))
                # time.sleep(5)
                _visa_centre_dropdown = web_driver.find_element(
                    "xpath", "//mat-form-field/div/div/div[3]"
                )
                _visa_centre_dropdown.click()
            except:
                logging.debug("Centre Fail")
                raise Exception("Centre Fail")
            
            time.sleep(0.5)
            try:
                xpath_centre = '//mat-option['+visa_centre_num[index] + ']/span'
                _visa_centre = web_driver.find_element(
                            "xpath",
                            xpath_centre)
                web_driver.execute_script("arguments[0].click();", _visa_centre)
            except:
                logging.debug("Centre Fail")
                raise Exception("Centre Fail")
    # time.sleep(1.5)
    
    if category_num[index] != '0':
        if _check_load():
            try:
                WebDriverWait(web_driver,2,1).until(EC.element_to_be_clickable(("xpath", "//mat-form-field/div/div/div[3]")))
                # time.sleep(5)
                _category_dropdown = web_driver.find_element(
                    "xpath", "/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[1]/form/div[2]/mat-form-field/div/div[1]/div[3]"
                )
                _category_dropdown.click()
            except:
                logging.debug("Category Fail")
                raise Exception("Category Fail")
            
            time.sleep(0.5)
            try:
                xpath_category = '//mat-option['+category_num[index] + ']/span'
                _category = web_driver.find_element(
                            "xpath",
                            xpath_category)
                web_driver.execute_script("arguments[0].click();", _category)
            except:
                logging.debug("Category Fail")
                raise Exception("Category Fail")
    # time.sleep(1.5)
    
    if sub_category_num[index] != '0':
        if _check_load():
            try:
                WebDriverWait(web_driver,2,1).until(EC.element_to_be_clickable(("xpath", "//mat-form-field/div/div/div[3]")))
                _sub_category_dropdown = web_driver.find_element(
                    "xpath", "/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[1]/form/div[3]/mat-form-field/div/div[1]/div[3]"
                )
                _sub_category_dropdown.click()
            except:
                logging.debug("Sub_category Fail")
                raise Exception("Sub_category Fail")
            
            time.sleep(0.5)
            try:
                xpath_sub_category = '//mat-option['+sub_category_num[index] + ']/span'
                _sub_category = web_driver.find_element(
                            "xpath",
                            xpath_sub_category)
                web_driver.execute_script("arguments[0].click();", _sub_category
                                          )
            except:
                logging.debug("Sub_category Fail")
                raise Exception("Sub_category Fail")
    # if sub_category_num[index] != '0':
    #     time.sleep(7)
    # elif category_num[index] != '0':
    #     time.sleep(14)
    # else:
    #     time.sleep(21)
    if _check_load():
        try:
            return web_driver.find_element("xpath", "//div[4]/div")
        except:
            logging.debug("Slot Fail")
            raise Exception("Slot Fail")

def string_time(sssstime):
    sss = sssstime
    value1 = sss.split()
    valuetime = value1[4].split('-')
    day = int(valuetime[0])
    month = int(valuetime[1])
    if month < 5:
        return True
    if month == 5:
        return True
    if month == 6:
        if day <= 30:
            return True
    return False

def _get_appointment_date_init():
    global web_driver
    logging.info(
            "Getting appointment date: Visa Centre: {}, Category: {}, Sub-Category: {}".format(
                "Init", "Init", "Init"
            )
        )
    #--- centre ---#
    if _check_load():
        web_driver.execute_script("window.scrollBy(0,-1000)")
        if '1' != '0':
            try:
                WebDriverWait(web_driver,1,0.2).until(EC.element_to_be_clickable(("xpath", "//mat-form-field/div/div/div[3]")))
                # time.sleep(5)
                _visa_centre_dropdown = web_driver.find_element(
                    "xpath", "//mat-form-field/div/div/div[3]"
                )
                _visa_centre_dropdown.click()
            except:
                logging.debug("Centre Fail")
                raise Exception("Centre Fail")
            
            time.sleep(1)
            xpath_centre = '//mat-option['+ '1' + ']/span'
            _visa_centre = web_driver.find_element(
                        "xpath",
                        xpath_centre)
            web_driver.execute_script("arguments[0].click();", _visa_centre)
    # time.sleep(1.5)
    if _check_load():
        web_driver.execute_script("window.scrollBy(0,2000)")
        return web_driver.find_element("xpath", "//div[4]/div")        
    
def send_mail(sss):
    message = MIMEText(sss,'plain','utf-8')
    message['Subject'] = 'VISA!!!'
    message['From'] = sender
    message['To'] = receivers[0]
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host,25)
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender,receivers,message.as_string())
        smtpObj.quit()
        print('success')
    except smtplib.SMTPException as e:
        print('error',e)
    message = MIMEText(sss,'plain','utf-8')
    message['Subject'] = 'VISA!!!'
    message['From'] = sender

def _send_message(_message,sub="DEFAULT"):
    if (
        len(_message.text) != 0
        and _message.text != "No appointment slots are currently available"
        and _message.text
        != "Currently No slots are available for selected category, please confirm waitlist\nTerms and Conditions"
        and _message.text
        != "No appointment slots are currently available. Please try another application centre if applicable"
        and _message.text
        != "We are sorry, but no appointment slots are currently available. Please try again later"
        and _message.text
        != "We are sorry but no appointment slots are currently available. New slots open at regular intervals, please try again later"
        ): 
        logging.info("Appointment slots available at {} : {}".format(visa_centre[i],_message.text))
        if (string_time(_message.text)):
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
            message = "{} at {}".format(_message.text, st)
            send_mail(message + "_" + sub)
            #send message by qcloud
            value1 = st.split()
            value2 = value1[1].split(":")
            time_now = value2[0] + value2[1] + value2[2]
            time_now.encode("utf-8")
            sss = _message.text
            value1 = sss.split()
            valuetime = value1[4].split('-')
            time_slot = valuetime[2] + valuetime[1] + valuetime[0]
            time_slot.encode("utf-8")
            # QSMS.send_sms_multi(1,1,[time_now,time_slot])
            # QSMS.send_sms_single(1,1,[time_now,time_slot])
            return True
        else:
            logging.info("No slots available")
            return False
    else:
        logging.info("No slots available")
        return False


def input_info():
    global web_driver
    logging.info(
                "Current Email {}".format(_VFSemail[email_count])
                    )
    index_people = 0

    #---Continue---#
    if _check_load():
        web_driver.execute_script("window.scrollBy(0,1000)")
        time.sleep(2)
        _continue_button = web_driver.find_element("xpath","/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[2]/button/span[1]")
        _continue_button.click()
    
    time.sleep(5)
    #---first_name---#
    if _check_load():
        logging.info(
                "Input First Name {}".format(first_name[index_people])
                    )
        _input_firstname = web_driver.find_element("xpath", "//*[@id='mat-input-2']")
        _input_firstname.send_keys(first_name[index_people])

    #---last_name---#
    logging.info(
            "Input Last Name {}".format(last_name[index_people])
                )
    _input_last_name = web_driver.find_element("xpath", "//*[@id='mat-input-3']")
    _input_last_name.send_keys(last_name[index_people])

    #---gender---#
    logging.info(
            "Input Gender {}".format(gender[index_people])
                )
    _gender_dropdown = web_driver.find_element("xpath", "/html/body/app-root/div/app-applicant-details/section/mat-card[1]/form/app-dynamic-form/div/div/app-dynamic-control[7]/div/div[1]/div/app-dropdown/div/mat-form-field/div/div[1]/div[3]")
    _gender_dropdown.click()
    time.sleep(0.5)
    if gender[index_people] == "FEMALE":
        _gender_select = web_driver.find_element(
                    "xpath",
                    "//mat-option[1]/span")
    else:
        _gender_select = web_driver.find_element(
                    "xpath",
                    "//mat-option[2]/span")
    logging.debug("Gender Select: " + _gender_select.text)
    web_driver.execute_script("arguments[0].click();", _gender_select)

    #---date_birth---#
    logging.info(
            "Input Date Birth {}".format(date_birth[index_people])
                )
    _input_date_birth = web_driver.find_element("xpath", "//*[@id='dateOfBirth']")
    _input_date_birth.send_keys(date_birth[index_people])

    #---country---#
    logging.info(
            "Input Country {}".format("CHINA")
                )
    _country_dropdown = web_driver.find_element("xpath", "/html/body/app-root/div/app-applicant-details/section/mat-card[1]/form/app-dynamic-form/div/div/app-dynamic-control[8]/div/div/div/app-dropdown/div/mat-form-field/div/div[1]/div[3]")
    _country_dropdown.click()
    time.sleep(0.5)
    _country_select = web_driver.find_element(
                "xpath",
                "//mat-option[43]/span")
    logging.debug("Gender Select: " + _country_select.text)
    web_driver.execute_script("arguments[0].click();", _country_select)

    #---passport---#
    logging.info(
            "Input Passport {}".format(passport[index_people])
                )
    _input_passport = web_driver.find_element("xpath", "//*[@id='mat-input-4']")
    _input_passport.send_keys(passport[index_people])

    #---passport_date---#
    logging.info(
            "Input Passport Date {}".format(passport_date[index_people])
                )
    _input_passport_date = web_driver.find_element("xpath", "//*[@id='passportExpirtyDate']")
    _input_passport_date.send_keys(passport_date[index_people])
    
    #---contact_number---#
    web_driver.execute_script("window.scrollBy(0,1000)")
    logging.info(
            "Input Contact Number {}".format(contact_number[index_people])
                )
    _input_contact_number = web_driver.find_element("xpath", "//*[@id='mat-input-6']")
    _input_contact_number.send_keys(contact_number[index_people])
    _input_contact_number = web_driver.find_element("xpath", "//*[@id='mat-input-5']")
    _input_contact_number.send_keys('86')

    #---email---#
    logging.info(
            "Input Email {}".format(contact_email[index_people])
                )
    _input_email = web_driver.find_element("xpath", "//*[@id='mat-input-7']")
    _input_email.send_keys(contact_email[index_people])

    #---Save---#
    _save_button = web_driver.find_element("xpath","/html/body/app-root/div/app-applicant-details/section/mat-card[2]/app-dynamic-form/div/div/app-dynamic-control/div/div/div[2]/button/span[1]")
    _save_button.click()

    time.sleep(180)
   

if __name__ == "__main__":
    count = 1
    vpn_state = 0
    #read log file setting
    logging_path = r"config\logging.ini"
    config_path = r"config\config.ini"
    print(logging_path)
    fileConfig(logging_path)
    logging = logging.getLogger()
    #read vfs setting
    logging.info("Read Config")
    _ReadConfig = _ConfigReader(config_path)
    _interval_raw = _ReadConfig.read_prop("DEFAULT", "interval")
    _interval_raw = int(_interval_raw)
    _VFSemail = _ReadConfig.read_prop_list("VFS","vfs_email")
    _VFSpassword = _ReadConfig.read_prop_list("VFS","vfs_password")
    
    _VFS_country = _ReadConfig.read_prop("VFS","vfs_country")

    visa_centre =  _ReadConfig.read_prop_list("VFS","visa_centre")
    visa_centre_num =  _ReadConfig.read_prop_list("VFS","visa_centre_num")
    category =  _ReadConfig.read_prop_list("VFS","category")
    category_num =  _ReadConfig.read_prop_list("VFS","category_num")
    sub_category = _ReadConfig.read_prop_list("VFS","sub_category")
    sub_category_num = _ReadConfig.read_prop_list("VFS","sub_category_num")
    _check_config()
    #read infomation
    info_state = _ReadConfig.read_prop("INFO", "STATE")
    first_name = _ReadConfig.read_prop_list("INFO", "first_name")
    last_name = _ReadConfig.read_prop_list("INFO", "last_name")
    gender = _ReadConfig.read_prop_list("INFO","gender")
    date_birth = _ReadConfig.read_prop_list("INFO","date_birth")
    passport = _ReadConfig.read_prop_list("INFO","passport")
    passport_date = _ReadConfig.read_prop_list("INFO","passport_date")
    contact_number = _ReadConfig.read_prop_list("INFO","contact_number")
    contact_email = _ReadConfig.read_prop_list("INFO","contact_email")

    _interval = random.randrange(_interval_raw,_interval_raw + 10,1)
    logging.info("Starting VFS Appointment Bot")
    # _send_message_test()
    #send_mail("Test")

    while True:
        try:
            _ReadConfig = _ConfigReader(config_path)
            _interval_raw = _ReadConfig.read_prop("DEFAULT", "interval")
            _interval_raw = int(_interval_raw)
            _VFSemail = _ReadConfig.read_prop_list("VFS","vfs_email")
            _VFSpassword = _ReadConfig.read_prop_list("VFS","vfs_password")
            
            _VFS_country = _ReadConfig.read_prop("VFS","vfs_country")

            visa_centre =  _ReadConfig.read_prop_list("VFS","visa_centre")
            visa_centre_num =  _ReadConfig.read_prop_list("VFS","visa_centre_num")
            category =  _ReadConfig.read_prop_list("VFS","category")
            category_num =  _ReadConfig.read_prop_list("VFS","category_num")
            sub_category = _ReadConfig.read_prop_list("VFS","sub_category")
            sub_category_num = _ReadConfig.read_prop_list("VFS","sub_category_num")
            _check_config()
            #read infomation
            info_state = _ReadConfig.read_prop("INFO", "STATE")
            first_name = _ReadConfig.read_prop_list("INFO", "first_name")
            last_name = _ReadConfig.read_prop_list("INFO", "last_name")
            gender = _ReadConfig.read_prop_list("INFO","gender")
            date_birth = _ReadConfig.read_prop_list("INFO","date_birth")
            passport = _ReadConfig.read_prop_list("INFO","passport")
            passport_date = _ReadConfig.read_prop_list("INFO","passport_date")
            contact_number = _ReadConfig.read_prop_list("INFO","contact_number")
            contact_email = _ReadConfig.read_prop_list("INFO","contact_email")
            logging.info("Running VFS Appointment Bot: Attempt#{}".format(count))
            _init_web_driver()
            _open_web(_VFS_country)
            _login()
            for i in range(len(visa_centre)):
                _message = _get_appointment_date_new(i)
                get_appointment_times = 0
                if len(_message.text) == 0:
                    logging.info("BLANK")
                while (len(_message.text) == 0 and get_appointment_times < 0):
                    _get_appointment_date_init()
                    _message = _get_appointment_date_new(i)
                    get_appointment_times = get_appointment_times + 1
                if (_send_message(_message,sub_category[i]) and info_state == "ON"):
                    input_info()
                    break
            web_driver.close()
            web_driver.quit()
            countdown(int(_interval))
            _interval = random.randrange(_interval_raw,_interval_raw + 10,1)
        except Exception as e:
            logging.info(e.args[0] + ". Please check the logs for more details")
            logging.debug(e, exc_info=True, stack_info=True)
            web_driver.close()
            web_driver.quit()
            countdown(int(120))
            _interval = random.randrange(_interval_raw,_interval_raw + 10,1)
            pass
        
        print("\n")
        count += 1
