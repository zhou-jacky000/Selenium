from selenium import *
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options as ChromeOptions
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
    driver.get("https://www.chatbot.com/chatbot-demo/")
    print("已打開網頁")
    time.sleep(5)

def click_ChatBot_button():
    try:
        # 切換至最外層的 iframe，如果有嵌套 iframe，需逐層切換
        iframe1 = WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.ID, 'chat-widget-minimized'))
        )
        print("已切換至聊天機器人 iframe")

        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button'))
        )
        button.click()

        # 切換回主頁面，避免嵌套問題
        driver.switch_to.default_content()
    except TimeoutException:
        print("未能找到聊天機器人 iframe")

def click_ChatBot_contact():
    try:
        # 先切回主頁面，然後再進入目標 iframe
        driver.switch_to.default_content()

        iframe2 = WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.ID, 'chat-widget'))
        )
        print("已切換至 chat-widget iframe")

        contact_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="homescreen-wrapper"]/div[2]/div[1]/div/div/button'))
        )
        contact_button.click()
        print("已點擊 Contact 按鈕")
    except TimeoutException:
        print("未能找到 chat-widget iframe 或 Contact 按鈕")
    

def input_Text():
    try:
        # 確保還在 chat-widget iframe 中，不切回主頁
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//textarea[@aria-label="Write a message…"]'))
        )
        input_field.send_keys('Hi')
        print("已輸入文字到對話框")

        # 點擊傳送按鈕
        send_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Send a message"]'))
        )
        send_button.click()
        print("已點擊 傳送 按鈕")
    except TimeoutException:
        print("未能找到輸入框")


def click_ChatBot_clearchat():
    try:
        # 點擊Option按鈕
        option_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Open menu"]'))
        )
        option_button.click()
        print("已點擊 Option 按鈕")
        time.sleep(3.5)
        # 點擊Clear按鈕
        clear_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//li[@role="menuitem" and contains(text(), "Clear chat")]'))
        )
        clear_button.click()
        print("已點擊 Clear 按鈕")
    except TimeoutException:
        print("未能找到Clear按鈕")

def click_ChatBot_questions():
    try:
        questions = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "I have questions")]'))
        )
        questions.click()
        print("已點擊問題按鈕")
    except TimeoutException:
        print("未能找到問題按鈕")


def click_ChatBot_priceing():
    try:
        priceing = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div/div/div[4]/div[2]/div/div[4]/div/div/button[3]'))
        )
        priceing.click()
        print("已點擊價錢按鈕")
    except TimeoutException:
        print("未能找到價錢按鈕")
def click_CahtBot_compareplans():
    try:
        link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div/div/div[4]/div[2]/div/div[6]/div/div/div/div/div[2]/div/div[1]/div/div/div/div/ul/li[1]'))
        )
        link.click()
        print("已點擊比較方案按鈕")
    except TimeoutException:
        print("未能找到比較方案按鈕")

# 主程式流程
try:
    open_page()
    click_ChatBot_button()
    time.sleep(5)
    click_ChatBot_contact()
    time.sleep(5)
    input_Text()
    time.sleep(5)
    click_ChatBot_clearchat()
    time.sleep(5)
    click_ChatBot_questions()
    time.sleep(5)
    click_ChatBot_priceing()
    time.sleep(5)
    click_CahtBot_compareplans()
    time.sleep(500)   
except Exception as e:
    print(f"流程中斷：{e}")