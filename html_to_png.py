# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os

# HTML路径
html_path = os.path.abspath("Perk_Overview_EN.html")
png_path = os.path.abspath("Perk_Overview_EN.png")

print(f"Converting HTML to PNG...")
print(f"Source: {html_path}")

try:
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1400,2200")
    options.add_argument("--hide-scrollbars")
    options.add_argument("--force-device-scale-factor=1")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(f"file:///{html_path}")

    # 获取页面实际高度
    height = driver.execute_script("return document.body.scrollHeight")
    print(f"Page height: {height}px")
    driver.set_window_size(1400, height + 100)

    driver.save_screenshot(png_path)
    driver.quit()

    print(f"[OK] PNG saved: {png_path}")
except Exception as e:
    print(f"[ERROR] {e}")
