# -*- coding: utf-8 -*-
import requests
import re
import slack
from bs4 import BeautifulSoup
from time import sleep


# 対象のprime video url
# 例) { 'url' : 'https://www.amazon.co.jp/gp/video/detail/XXXXXXXX/' },
#     { 'url' : 'https://www.amazon.co.jp/gp/video/detail/YYYYYYYY/' }
scrape_datas = [
    { 'url' : 'https://www.amazon.co.jp/gp/video/detail/XXXXX/'}
]


# slack config
slack_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
client = slack.WebClient(slack_token)


# send slack
def send_message(message):
    channel_id = "#primevideo"
    client.chat_postMessage(
        channel=channel_id,
        as_user='false',
        username='PrimeVideoChan',
        icon_emoji=':seedling:',
        text=message
    )


# スクレイピングの実行
def scrape_primevideo(scrape_data):

    # custom user-agent
    ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)" \
        "AppleWebKit/537.36 (KHTML, like Gecko)" \
        "Chrome/60.0.3112.113"

    # custom header
    headers = {
        "User-Agent": ua,
        "Accept-Encoding": "deflate",
        "Accept-Language": "ja,en-US;q=0.9,en;q=0.8"
    }

    # アクセス先url
    url = scrape_data['url']

    # スクレイピングを実行
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html5lib')
    title = soup.select("h1[data-automation-id='title']")[0].text.strip()
    item = soup.find("div", class_="av-playback-messages")
    img = item.find('img')
    src = ""

    # imgがあればsrcを取得
    if img is not None:
        src = img['src']

    # primelogoが含まれていればprime videoと判断して通知する
    if re.search('primelogo', src, flags=re.IGNORECASE):
        message =  "「" + title + "」が無料になったようです\n" + url
        slack = send_message(message)


# main
for scrape_data in scrape_datas:
    scrape_primevideo(scrape_data)
    sleep(1)
