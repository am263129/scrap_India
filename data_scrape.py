from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from random import randint
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
from requests import get

def Create_Driver():
    
    options = Options()
    options.add_experimental_option("excludeSwitches",["ignore-certificate-errors", "safebrowsing-disable-download-protection", "safebrowing-disable-auto-update", "disable-client-side-phishing-detection"])
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-extensions')
    options.add_argument('--profile-directory=default')
    options.add_argument('--incognito')
    options.add_argument('--disable-plugin-discovery')
    options.add_argument('--start-maximized')
    options.add_argument("--enable-automation")
    options.add_argument("--test-type=browser")

    driver = webdriver.Chrome(executable_path="chromedriver", options = options)
    
    return driver


def Start():
    # driver = Create_Driver()
    # driver.get("https://www.racenet.com.au/racing-form-guide")
    page = requests.get("https://www.racenet.com.au/racing-form-guide")

    print(page.text)


if __name__ == '__main__':

    list_city = []
    list_agent = []
    list_proxy = []
    damaged_proxy_list = []
    Password =''
    print(len(list_proxy))
    city_limit = len(list_city)
    print(city_limit)
    root = Tk() 
    root.geometry("500x150")
    root.title("Sony account Creator")
    root.wm_attributes("-topmost", 1)

    v = IntVar()

    root.grid_columnconfigure(0, weight = 1)
    root.grid_columnconfigure(1, weight = 1)
    root.grid_columnconfigure(2, weight = 1)
    root.grid_columnconfigure(3, weight = 1)
    root.grid_columnconfigure(4, weight = 1)
    root.grid_columnconfigure(5, weight = 1)
    root.grid_columnconfigure(6, weight = 1)
    root.grid_columnconfigure(7, weight = 1)
    root.grid_columnconfigure(8, weight = 1)
    root.grid_columnconfigure(9, weight = 1)
    root.grid_columnconfigure(10, weight = 1)
    root.grid_columnconfigure(11, weight = 1)
    

    Label_number_account =  Label(root, text="From Date", )
    Label_number_account.grid(row = 1, column = 0 ,columnspan = 3 ,sticky = W+E)
    Start_date =  Entry(root, bd =2, )
    Start_date.grid(row = 1, column = 3,columnspan = 3,sticky = W+E,padx=5)
    Label_number_account =  Label(root, text="To Date", )
    Label_number_account.grid(row = 1, column =  6, columnspan = 3, sticky = W+E)
    End_date =  Entry(root, bd =2, )
    End_date.grid(row = 1, column = 9 ,columnspan = 3 ,sticky = W+E, padx=5)

    Option1 = Radiobutton(root, text="Australia", variable=v, value=1)
    Option1.grid(row = 2, column = 0 ,columnspan = 6,sticky = W+E)

    Option2 = Radiobutton(root, text="International", variable=v, value=2)
    Option2.grid(row= 2, column = 6,columnspan = 6, sticky = W+E)

    # Option3 = Radiobutton(root, text="Harness", variable=v, value=3)
    # Option3.grid(row= 2, column = 8,columnspan = 3, sticky = W+E)
    
    space =  Label(root, text="", height = 2)
    space.grid(row = 3, column =  6, columnspan = 3, sticky = W+E)

    Btn_start = Button(root, height = 2, text = "Start", command = lambda: Start() )
    Btn_start.grid( row = 4, column = 5,columnspan = 4, sticky = W + E)


    # Label_status =  Label(root, text="Current status")
    # Label_status.grid(row = 4, column = 1 , sticky = W+E)

    # output_status = Frame(root,height = 100, background = "pink")
    # output_status.grid(column = 0, columnspan = 20, row = 5 ,rowspan = 10,padx=20, pady=5,sticky = W+E)

    # S = Scrollbar(output_status)
    # T = Text(output_status, width=500)
    # S.pack(side=RIGHT, fill=Y)
    # T.pack(side=LEFT, fill = Y)
    # S.config(command=T.yview)
    # T.config(yscrollcommand=S.set)

    mainloop()