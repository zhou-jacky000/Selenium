from selenium import *
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options as ChromeOptions
from datetime import datetime, timedelta
import time
import os
import sys

# 找到解壓後的資料夾路徑 (打包後使用)
BASE_DIR = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
chromedriver_path = os.path.join(BASE_DIR, "chromedriver.exe")
service = Service(executable_path=chromedriver_path)

# 建立瀏覽器選項
options = uc.ChromeOptions()
options.headless = False  # 設為 True 以啟用非可視化模式

# 初始化 undetected_chromedriver
driver = uc.Chrome(service=service, options=options)

def open_page():
    """打開網頁"""
    pass

def click_ChatBot_button():
    pass

def click_ChatBot_contact():
    pass




def input_Text():
    pass

def click_ChatBot_clearchat():
    pass

def click_ChatBot_questions():
    pass


def click_ChatBot_priceing():
    pass
def click_CahtBot_compareplans():
    pass

# 主程式流程
try:
    open_page()
    click_ChatBot_button()
    click_ChatBot_contact()
    input_Text()
    click_ChatBot_clearchat()
    click_ChatBot_questions()
    click_ChatBot_priceing()
    click_CahtBot_compareplans()
except Exception as e:
    print(f"流程中斷：{e}")