import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from selenium import webdriver
import time
import csv
import tkinter as tk
from tkinter import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

url = ['https://www.firesprinkler.org/WWW/About/Find_a_Contractor_Member/WWW/About/findacontractor.aspx?hkey=0cae56e6-505a-4141-93d5-5ceee45b7195']

start_time = time.time()
file_name = 'firesprinkler.csv'

def csv_make():
    try:
        header = ['no','company_name', 'address', 'phone', 'email', 'website']
        
        # data save into CSV file
        with open(file_name, "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(header)  # write the header
        f.close()
    except:
        pass
    

def data_scrap():
    csv_make()
    driver = runFirefox()
    driver.get(url[0])
    driver.maximize_window()
    time.sleep(4)
    count = 1
    driver.find_element_by_xpath("//select[@name='ctl01$TemplateBody$WebPartManager1$gwpciNewContentCollectionOrganizerCommon$ciNewContentCollectionOrganizerCommon$NewQueryMenuCommon$ResultsGrid$Sheet0$Input4$DropDown1']/option[text()='United States']").click()
    sel = driver.find_element_by_xpath("//select[@name='ctl01$TemplateBody$WebPartManager1$gwpciNewContentCollectionOrganizerCommon$ciNewContentCollectionOrganizerCommon$NewQueryMenuCommon$ResultsGrid$Sheet0$Input3$DropDown1']")
    states = []
    for option in sel.find_elements_by_tag_name('option'):
        if option.text=='(Any)':
            continue
        states.append(option.text) 
    for state in states:
        driver.find_element_by_xpath("//select[@name='ctl01$TemplateBody$WebPartManager1$gwpciNewContentCollectionOrganizerCommon$ciNewContentCollectionOrganizerCommon$NewQueryMenuCommon$ResultsGrid$Sheet0$Input3$DropDown1']/option[text()='%s']"%state).click()  
        
        try:
            driver.find_element_by_xpath(".//input[@name='ctl01$TemplateBody$WebPartManager1$gwpciNewContentCollectionOrganizerCommon$ciNewContentCollectionOrganizerCommon$NewQueryMenuCommon$ResultsGrid$Sheet0$SubmitButton']").click()
        except:
            pass
        time.sleep(5)
        try:
            input = driver.find_element_by_id("ctl01_TemplateBody_WebPartManager1_gwpciNewContentCollectionOrganizerCommon_ciNewContentCollectionOrganizerCommon_NewQueryMenuCommon_ResultsGrid_Grid1_ctl00_ctl02_ctl00_ChangePageSizeTextBox")
            input.send_keys(700)
    
            driver.find_element_by_xpath(".//input[@name='ctl01$TemplateBody$WebPartManager1$gwpciNewContentCollectionOrganizerCommon$ciNewContentCollectionOrganizerCommon$NewQueryMenuCommon$ResultsGrid$Grid1$ctl00$ctl02$ctl00$ChangePageSizeLinkButton']").click()
            time.sleep(4)
        except:
            pass
        rowData0 = driver.find_elements_by_class_name('rgRow')
        rowData1 = driver.find_elements_by_class_name('rgAltRow')
        # for i in range(len(rowData0)):
        while True:
            if len(rowData0) != 0:
                break
            else:
                time.sleep(1)
                rowData0 = driver.find_elements_by_class_name('rgRow')
        print(len(rowData0))
        row = rowData0[0]
        script = row.find_element_by_xpath(".//a[1]").get_attribute('href')
        driver.execute_script(script)
        
        while True:
            try:
                companyname = driver.find_elements_by_xpath(".//span[@id='ctl00_TemplateBody_WebPartManager1_gwpciMiniProfile_ciMiniProfile_contactName_institute']")
                if(len(companyname) != 0):
                    break
            except:
                print("getting",len(companyname))
                time.sleep(1)
        
        print(companyname[0].get_attribute('innerHTML'))
            # address = divdetails[i].find_element_by_xpath(".//span[@id='ctl00_TemplateBody_WebPartManager1_gwpciMiniProfile_ciMiniProfile_contactAddress__address']").text
            # phonenum = divdetails[i].find_element_by_xpath(".//span[@id='ctl00_TemplateBody_WebPartManager1_gwpciMiniProfile_ciMiniProfile_contactAddress__phoneNumber']").text
            # email = ''
            # try:
            #     email = divdetails[i].find_element_by_xpath(".//a[@id='ctl00_TemplateBody_WebPartManager1_gwpciMiniProfile_ciMiniProfile_contactAddress__email']").text
            # except:
            #     pass
            # site = ''
            # try:
            #     site = divdetails[i].find_element_by_xpath(".//a[@id='ctl00_TemplateBody_WebPartManager1_gwpciProfileSection_ciProfileSection_CsContact.Website']").text
            # except:
            #     pass
            
            # closebuttons = driver.find_element_by_class_name("rwCloseButton")
            # closebuttons.click()
            
            # line_data = [str(count), companyname, address, phonenum, email, site]
            # with open(file_name, 'a', newline='', encoding="utf-8") as f:
            #     writer = csv.writer(f, delimiter=',')
            #     writer.writerow(line_data)
            #     f.close()
            # line_data.clear()
            # count+=1
        
        # for  i in range(len(rowData1)):
        #     row = rowData1[i]
        #     script = row.find_element_by_xpath(".//a[1]").get_attribute('href')
        #     driver.execute_script(script)
        #     time.sleep(5)
            
        #     # divdetail = driver.find_element_by_xpath("/html/body/form/div["+str(i+1)+"]")
        #     # companyname = driver.find_element_by_class_name("SectionLabel").text
        #     # print(companyname)
        #     # address = divdetails[i].find_element_by_xpath(".//span[@id='ctl00_TemplateBody_WebPartManager1_gwpciMiniProfile_ciMiniProfile_contactAddress__address']").text
        #     # phonenum = divdetails[i].find_element_by_xpath(".//span[@id='ctl00_TemplateBody_WebPartManager1_gwpciMiniProfile_ciMiniProfile_contactAddress__phoneNumber']").text
        #     # email = ''
        #     # try:
        #     #     email = divdetails[i].find_element_by_xpath(".//a[@id='ctl00_TemplateBody_WebPartManager1_gwpciMiniProfile_ciMiniProfile_contactAddress__email']").text
        #     # except:
        #     #     pass
        #     # site = ''
        #     # try:
        #     #     site = divdetails[i].find_element_by_xpath(".//a[@id='ctl00_TemplateBody_WebPartManager1_gwpciProfileSection_ciProfileSection_CsContact.Website']").text
        #     # except:
        #     #     pass
            
        #     closebuttons = driver.find_element_by_class_name("rwCloseButton")
        #     closebuttons.click()
        #     time.sleep(3)
        #     # line_data = [str(count), companyname, address, phonenum, email, site]
        #     # with open(file_name, 'a', newline='', encoding="utf-8") as f:
        #     #     writer = csv.writer(f, delimiter=',')
        #     #     writer.writerow(line_data)
        #     #     f.close()
        #     # line_data.clear()
        #     count+=1
    return
    
    
    
    # driver.execute_script('alert("Hello");')
    
    #driver.quit()
    
    
def runFirefox():

    option = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options =option)
    driver.implicitly_wait(3)
    return driver
 
if __name__ == '__main__':
    data_scrap()
    '''
    master = Tk()
    master.title("Python Data Scraper")  # scraping interface title
    master.geometry("500x180")  # interface size
    Label = Label(master)
    Label["text"] = "URL:"
    Label.pack(padx=10, pady=10)
    variable = StringVar(master)
    variable.set(url[0])  # default value
    w = OptionMenu(master, variable, *url)
    w.pack()
    button_start = Button(master, command=data_scrap)
    button_start["text"] = "Start"
    button_start.pack(padx=30, pady=30, fill=X)
    master.mainloop()
'''