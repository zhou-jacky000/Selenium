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

# 通用函式
def wait_and_click(by, value, description, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )
        element.click()
        print(f"已點擊 {description}")
    except TimeoutException:
        print(f"未能找到 {description}")

def switch_to_iframe(iframe_id):
    """切換到指定的 iframe"""
    try:
        driver.switch_to.default_content()
        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.ID, iframe_id))
        )
        print(f"已切換至 {iframe_id} iframe")
    except TimeoutException:
        print(f"未能找到 {iframe_id} iframe")


# 功能函式
def open_page():
    """打開網頁"""
    driver.get("https://www.chatbot.com/chatbot-demo/")
    print("已打開網頁")
    time.sleep(5)

def click_ChatBot_button():
    try:
        switch_to_iframe('chat-widget-minimized')
        wait_and_click(By.XPATH, '//button', '聊天機器人按鈕')
        driver.switch_to.default_content()
        time.sleep(5)
    except TimeoutException:
        print("未能找到聊天機器人 iframe")

def click_ChatBot_contact():
    try:
        # 先切回主頁面，然後再進入目標 iframe
        switch_to_iframe('chat-widget')
        wait_and_click(By.XPATH, '//*[@id="homescreen-wrapper"]/div[2]/div[1]/div/div/button', 'Contact 按鈕')
        time.sleep(5)
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
        wait_and_click(By.XPATH, '//button[@aria-label="Send a message"]', '傳送按鈕')
        time.sleep(5)
    except TimeoutException:
        print("未能找到輸入框")


def click_ChatBot_clearchat():
    try:
        wait_and_click(By.XPATH, '//button[@aria-label="Open menu"]', 'Option 按鈕')
        wait_and_click(By.XPATH, '//li[@role="menuitem" and contains(text(), "Clear chat")]', 'Clear 按鈕')
        time.sleep(5)
    except TimeoutException:
        print("未能找到Clear按鈕")

def click_ChatBot_questions():
    try:
        wait_and_click(By.XPATH, '//button[contains(text(), "I have questions")]', 'Questions 按鈕')
        time.sleep(5)
    except TimeoutException:
        print("未能找到Questions按鈕")


def click_ChatBot_priceing():
    try:
        wait_and_click(By.XPATH, '/html/body/div/div[1]/div/div/div[4]/div[2]/div/div[4]/div/div/button[3]', 'Price 按鈕')
        time.sleep(5)
    except TimeoutException:
        print("未能找到Price按鈕")
def click_CahtBot_compareplans():
    try:
        wait_and_click(By.XPATH, '/html/body/div/div[1]/div/div/div[4]/div[2]/div/div[6]/div/div/div/div/div[2]/div/div[1]/div/div/div/div/ul/li[1]', '比較方案按鈕')
    except TimeoutException:
        print("未能找到Compare Plans按鈕")

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
    print("已導入至 Compare plans")
    time.sleep(500)   
except Exception as e:
    print(f"流程中斷：{e}")