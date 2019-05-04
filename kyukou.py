#encoding:utf-8
import database
import time
import datetime
from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from discord_webhook import DiscordWebhook
import gosh

def youbi():
    d = datetime.datetime.now()
    return (d.weekday())

def main(id, password):
    # Headless Firefoxを起動させて休講情報のページへ移動
    options = Options()
    options.add_argument('-headless')
    browser = Firefox(executable_path='geckodriver', options=options)
    browser.set_window_size(1080, 2160)         # ウィンドウサイズを調整
    # wait = WebDriverWait(browser, timeout=10)
    print(id, password)

    browser.get('https://jjh.tmu.ac.jp/campusweb/campusportal.do')
    browser.find_element_by_id("userNameInput").send_keys(id)               # ID
    browser.find_element_by_id("passwordInput").send_keys(password)      # Password
    browser.find_element_by_css_selector('button[type="submit"]').click()

    # 休憩
    time.sleep(1)

    # 休講情報のページに飛ぶ
    browser.find_element_by_id("tab-kh").click()

    # 休憩
    time.sleep(0.5)

    # スマホ版サイトに飛ぶ
    browser.find_element_by_id("portalsmart").click()

    # 休憩
    time.sleep(0.5)

    # 休講情報一覧に飛ぶ
    browser.find_element_by_class_name("button").click()

    # 曜日判定してそのページに飛ぶ
    day = youbi()
    print(day)
    if(day == 0):
        pass
    elif(day == 1):
        browser.find_element_by_css_selector('ol[class="flex-control-nav flex-control-paging"] > li:nth-of-type(2)').click()
    elif(day == 2):
        browser.find_element_by_css_selector('ol[class="flex-control-nav flex-control-paging"] > li:nth-of-type(3)').click()
    elif(day == 3):
        browser.find_element_by_css_selector('ol[class="flex-control-nav flex-control-paging"] > li:nth-of-type(4)').click()
    elif (day == 4):
        browser.find_element_by_css_selector('ol[class="flex-control-nav flex-control-paging"] > li:nth-of-type(5)').click()
    elif(day == 5):
        browser.find_element_by_css_selector('ol[class="flex-control-nav flex-control-paging"] > li:nth-of-type(6)').click()
    elif(day == 6):
        print("oho")

    # スクレイピングしたページデータを整形する
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")

    # 休講情報を取ってくる
    if(day == 0):
        info = soup.select("li[class='slide-first flex-active-slide'] > ul[class=campussmart-list] > li[class='first'] > table > tbody")
    elif(day >= 1 and day < 5):
        info = soup.select("li[class='flex-active-slide'] > ul[class=campussmart-list] > li[class='first'] > table > tbody")
    else:
        info = soup.select("ul[class=campussmart-list] > li[class='first'] > table > tbody")

    time.sleep(0.5)

    # スクリーンショットを撮る
    browser.save_screenshot("paper.png")

    print(info)

    URL = gosh.requestsURL()
    webhook = DiscordWebhook(url = URL, username = 'astpy')

    # 写真を送る
    with open("./paper.png", "rb") as f:
        webhook.add_file(file=f.read(), filename='example.jpg')

    webhook.execute()

