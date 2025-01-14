# 專案說明

此專案使用 Python 與 `undetected_chromedriver` 及 `selenium` 來自動化操作 ChatBot 網頁。通過該腳本，您可以自動完成點擊聊天按鈕、輸入訊息、清除對話、點擊問題按鈕、檢視定價等功能。

## 需求環境

- Python 3.x
- `selenium`
- `undetected_chromedriver`
- 瀏覽器驅動程式（`chromedriver.exe`）

## 安裝方式

1. 安裝 Python 3.x
2. 透過 pip 安裝必要的套件：
   ```bash
   pip install selenium
   pip install undetected-chromedriver
   ```
3. 確認 `chromedriver.exe` 與執行檔位於相同的目錄中。

## 使用方法

1. 在專案目錄中，執行 `main.py`（以上述程式碼檔名為例）：
   ```bash
   python main.py
   ```
2. 程式將自動打開 ChatBot 示範頁面，並執行以下操作：
   - 點擊聊天機器人按鈕
   - 點擊 Contact 按鈕
   - 輸入訊息 "Hi"
   - 點擊傳送按鈕
   - 清除聊天紀錄
   - 點擊 "I have questions" 問題按鈕
   - 點擊 "Pricing"按鈕
   - 點擊 "Compare plans" 方案比較按鈕

## 主要函式說明

- `open_page()`: 開啟 ChatBot 頁面。
- `click_ChatBot_button()`: 點擊聊天機器人按鈕。
- `click_ChatBot_contact()`: 點擊 Contact 按鈕並切換至對話框 iframe。
- `input_Text()`: 輸入訊息並點擊傳送按鈕。
- `click_ChatBot_clearchat()`: 點擊清除聊天按鈕。
- `click_ChatBot_questions()`: 點擊 "I have questions" 問題按鈕。
- `click_ChatBot_priceing()`: 點擊定價按鈕。
- `click_CahtBot_compareplans()`: 點擊 "Compare plans" 方案比較按鈕。

## 錯誤處理

每個函式都使用 `try-except` 區塊來捕捉超時例外。若未找到目標元素，程式將顯示相應的錯誤訊息。

## 注意事項

- 使用 `switch_to_iframe(iframe_id)` 來切換 iframe，確保能夠操作內嵌的按鈕。
- 部分 XPath 為絕對路徑，可能需要根據網頁更新進行調整。


