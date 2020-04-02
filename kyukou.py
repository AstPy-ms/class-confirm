# 今回は動的サイトのためsleep関数を多用する

#encoding:utf-8
import database
import time
import datetime
from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from discord_webhook import DiscordWebhook
import subprocess
import gosh
import cryptography

# 曜日を取得する
def youbi():
    d = datetime.datetime.now()
    return (d.weekday())

# main関数
# ここで実際にスクリーンショットを取ってWebhookでdiscordに送信
def main(id, password, disname):
    # Headless Firefoxを起動させて休講情報のページへ移動
    options = Options()
    #options.add_argument('-headless')
    browser = Firefox(executable_path='geckodriver', options=options)       # Firefoxを起動
    browser.set_window_size(1080, 2160)                                     # ウィンドウサイズを調整
    # wait = WebDriverWait(browser, timeout=10)
    print(id, password)

    # 学生ポータルにログインする
    browser.get('https://portal.tmu.ac.jp/uniprove_pt/UnLoginControlSP')
    time.sleep(0.5)
    browser.find_element_by_id("username").send_keys(id)               # ID
    browser.find_element_by_id("password").send_keys(password)      # Password
    browser.find_element_by_name('_eventId_proceed').click()

    # 休憩
    time.sleep(1.2)

    # PC版をクリック
    browser.find_element_by_css_selector('p[class="pc_link"] > a[class="ui-link"]').click()

    # 休講情報のページに飛ぶ
    browser.find_element_by_css_selector('ul[class="link_item"] > li:nth-of-type(4) > span > a[href="javascript:void(0);"]').click()

    # 休憩
    time.sleep(0.5)

    # 検索条件を絞る
    browser.find_element_by_id("chapter").click()
    browser.find_element_by_id("chkEtrdFlg_1").click()
    browser.find_element_by_name("ESearch").click()

    # 休講情報一覧に飛ぶ
    # browser.find_element_by_class_name("button").click()

    """
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
    """

    '''
    # 休講情報を取ってくる(HTML)
    if(day == 0):
        info = soup.select("li[class='slide-first flex-active-slide'] > ul[class=campussmart-list] > li[class='first'] > table > tbody")
    elif(day >= 1 and day < 5):
        info = soup.select("li[class='flex-active-slide'] > ul[class=campussmart-list] > li[class='first'] > table > tbody")
    else:
        info = soup.select("ul[class=campussmart-list] > li[class='first'] > table > tbody")

    # print(info)
    '''

    time.sleep(0.5)

    # スクリーンショットを撮る
    browser.save_screenshot("paper.png")

    """
    # WebhookのURLを取得しゴミを排除する
    URL = database.searchurl(disname)
    URL = URL[2:]
    URL = URL[:-3]
    print(URL)
    # URL = gosh.requestsURL()
    """
    URL = gosh.requestsURL()
    webhook = DiscordWebhook(url = URL, username = 'astpy')

    # 写真を送る
    with open("./paper.png", "rb") as f:
        webhook.add_file(file=f.read(), filename='example.jpg')

    webhook.execute()

    subprocess.check_call("rm -rf ./paper.png", shell=True)

